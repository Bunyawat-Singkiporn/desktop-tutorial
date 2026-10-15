"""Batch translate slide/*.md -> slide-en/*.md (Thai prose only)."""
from __future__ import annotations

import argparse
import re
import sys
import time
from pathlib import Path

from deep_translator import MyMemoryTranslator

ROOT = Path(__file__).resolve().parents[1]
TH = ROOT / "slide"
EN = ROOT / "slide-en"

THAI_RE = re.compile(r"[\u0E00-\u0E7F]")
FENCE_RE = re.compile(r"(```[\s\S]*?```)")

_translator = MyMemoryTranslator(source="th-TH", target="en-US")

HEADER_MAP = {
    "## โจทย์": "## Task",
    "## ตัวอย่าง": "## Example",
    "## คำใบ้": "## Hint",
    "## หมายเหตุสำหรับครู": "## Notes for teachers",
    "## หมายเหตุ": "## Notes",
    "## ลำดับที่แนะนำ": "## Recommended order",
}

STATIC = [
    ("# เขียนโค้ดตรงนี้", "# Write your code here"),
    ("# เขียนโค้ดที่นี่", "# Write your code here"),
    ("**เงื่อนไข:**", "**Rules:**"),
    ("**ขอบเขตของบทนี้:**", "**Chapter scope:**"),
    ("**สรุป:**", "**Summary:**"),
    ("ไม่มี (กำหนดค่าในโปรแกรม)", "None (values are set in the program)"),
    (
        "ไม่มี (กำหนดค่าในโปรแกรม / เรียกฟังก์ชันในโค้ด)",
        "None (values are set in the program / call functions in code)",
    ),
    ("สารบัญโจทย์", "Exercise index"),
    ("| ระดับ |", "| Level |"),
    ("| โจทย์ |", "| Problem |"),
    ("| แกนการคิด |", "| Core idea |"),
    ("| ไฟล์ |", "| File |"),
    ("## 💡 Hint", "## Hint"),
    (" ข้อ · ", " problems · "),
    (" ข้อ = ", " problems = "),
]


def mechanical(text: str) -> str:
    for a, b in sorted(HEADER_MAP.items(), key=lambda x: -len(x[0])):
        text = text.replace(a, b)
    for a, b in STATIC:
        text = text.replace(a, b)
    text = re.sub(r"—\s*ข้อ\s*(\d+)\s*:", r"— Q\1:", text)
    text = re.sub(r"=\s*\*\*(\d+)\s*ข้อ\*\*", r"= **\1 problems**", text)
    text = text.replace("## Problem", "## Task")
    return text


def _translate_once(text: str, retries: int = 6) -> str:
    text = text.strip("\n")
    if not text or not THAI_RE.search(text):
        return text
    if len(text) > 480:
        return translate_prose(text)
    delay = 2.5
    for attempt in range(retries):
        try:
            time.sleep(2.2)
            return _translator.translate(text)
        except Exception as e:
            if attempt == retries - 1:
                print(f"    FAIL: {e}", file=sys.stderr)
                return text
            time.sleep(delay)
            delay = min(delay * 1.4, 30.0)
    return text


def translate_prose(text: str) -> str:
    if not text.strip() or not THAI_RE.search(text):
        return text
    out: list[str] = []
    chunk: list[str] = []
    size = 0
    for line in text.split("\n"):
        add = len(line) + (1 if chunk else 0)
        if chunk and size + add > 460:
            block = "\n".join(chunk)
            out.append(_translate_once(block) if THAI_RE.search(block) else block)
            chunk, size = [], 0
        chunk.append(line)
        size += add
    if chunk:
        block = "\n".join(chunk)
        out.append(_translate_once(block) if THAI_RE.search(block) else block)
    return "\n".join(out)


def translate_md(raw: str) -> str:
    raw = mechanical(raw)
    parts = FENCE_RE.split(raw)
    for i in range(len(parts)):
        if i % 2 == 1:
            parts[i] = parts[i].replace("# เขียนโค้ดตรงนี้", "# Write your code here")
            parts[i] = parts[i].replace("# เขียนโค้ดที่นี่", "# Write your code here")
        elif THAI_RE.search(parts[i]):
            parts[i] = translate_prose(parts[i])
    return mechanical("".join(parts))


def lesson_filter(start: str | None, end: str | None) -> list[Path]:
    lessons = sorted(
        [d for d in TH.iterdir() if d.is_dir() and d.name[:3].isdigit()],
        key=lambda x: x.name,
    )
    if start:
        lessons = [d for d in lessons if d.name >= start]
    if end:
        lessons = [d for d in lessons if d.name <= end]
    return lessons


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--start", default="025")
    p.add_argument("--end", default="036-")
    p.add_argument("--only-thai", action="store_true")
    args = p.parse_args()

    n = 0
    for lesson in lesson_filter(args.start, args.end):
        for th_md in sorted(lesson.rglob("*.md")):
            if "answer" in th_md.parts:
                continue
            rel = th_md.relative_to(TH)
            en_path = EN / rel
            if args.only_thai and en_path.exists():
                if not THAI_RE.search(en_path.read_text(encoding="utf-8", errors="ignore")):
                    continue
            en_path.parent.mkdir(parents=True, exist_ok=True)
            raw = th_md.read_text(encoding="utf-8")
            print(rel.as_posix(), flush=True)
            en_path.write_text(translate_md(raw), encoding="utf-8")
            n += 1
    print(f"Wrote {n} files", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
