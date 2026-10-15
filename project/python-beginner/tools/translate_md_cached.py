"""Translate slide -> slide-en .md with JSON line cache (MyMemory, <500 chars/line)."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from pathlib import Path

from deep_translator import MyMemoryTranslator

ROOT = Path(__file__).resolve().parents[1]
TH, EN = ROOT / "slide", ROOT / "slide-en"
CACHE = Path(__file__).with_name("th_en_line_cache.json")

THAI_RE = re.compile(r"[\u0E00-\u0E7F]")
FENCE_RE = re.compile(r"(```[\s\S]*?```)")
TR = MyMemoryTranslator(source="th-TH", target="en-US")

HEADER = {
    "## โจทย์": "## Task",
    "## ตัวอย่าง": "## Example",
    "## คำใบ้": "## Hint",
    "## หมายเหตุสำหรับครู": "## Notes for teachers",
    "## ลำดับที่แนะนำ": "## Recommended order",
    "## 💡 Hint": "## Hint",
}
STATIC = [
    ("# เขียนโค้ดตรงนี้", "# Write your code here"),
    ("**เงื่อนไข:**", "**Rules:**"),
    ("**ขอบเขตของบทนี้:**", "**Chapter scope:**"),
    ("**สรุป:**", "**Summary:**"),
    ("ไม่มี (กำหนดค่าในโปรแกรม)", "None (values are set in the program)"),
    (
        "ไม่มี (กำหนดค่าในโปรแกรม / เรียกฟังก์ชันในโค้ด)",
        "None (values are set in the program / call functions in code)",
    ),
    ("# 📋 สารบัญโจทย์", "# 📋 Exercise index"),
    ("| ไฟล์ |", "| File |"),
    ("| ระดับ |", "| Level |"),
    ("| โจทย์ |", "| Problem |"),
    ("| แกนการคิด |", "| Core idea |"),
    ("บรรทัดเดียว", "One line"),
    (" ข้อ · ", " · "),
    (" = **15 ข้อ**", " = **15 problems**"),
]


def mech(t: str) -> str:
    for a, b in sorted(HEADER.items(), key=lambda x: -len(x[0])):
        t = t.replace(a, b)
    for a, b in STATIC:
        t = t.replace(a, b)
    t = re.sub(r"—\s*ข้อ\s*(\d+)\s*:", r"— Q\1:", t)
    t = re.sub(r"—\s*บท\s*(\d+)", r"— Chapter \1", t)
    return t


def load_cache() -> dict[str, str]:
    if CACHE.exists():
        return json.loads(CACHE.read_text(encoding="utf-8"))
    return {}


def save_cache(c: dict[str, str]) -> None:
    CACHE.write_text(json.dumps(c, ensure_ascii=False, indent=0), encoding="utf-8")


def tr_line(line: str, cache: dict[str, str]) -> str:
    if not THAI_RE.search(line):
        return line
    key = hashlib.sha256(line.encode()).hexdigest()
    if key in cache:
        return cache[key]
    for _ in range(4):
        try:
            out = TR.translate(line[:490])
            cache[key] = out
            time.sleep(2.5)
            return out
        except Exception:
            time.sleep(8)
    return line


def translate_text(raw: str, cache: dict[str, str]) -> str:
    raw = mech(raw)
    parts = FENCE_RE.split(raw)
    for i in range(len(parts)):
        if i % 2 == 1:
            parts[i] = parts[i].replace("# เขียนโค้ดตรงนี้", "# Write your code here")
        else:
            lines = []
            for ln in parts[i].split("\n"):
                lines.append(tr_line(ln, cache) if THAI_RE.search(ln) else ln)
            parts[i] = "\n".join(lines)
    return mech("".join(parts))


def lessons(start: str, end: str) -> list[Path]:
    ls = sorted([d for d in TH.iterdir() if d.is_dir() and d.name[:3].isdigit()], key=lambda p: p.name)
    if start:
        ls = [d for d in ls if d.name >= start]
    if end:
        ls = [d for d in ls if d.name <= end]
    return ls


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", default="026")
    ap.add_argument("--end", default="036")
    ap.add_argument("--skip-existing-clean", action="store_true")
    args = ap.parse_args()
    cache = load_cache()
    n = 0
    for lesson in lessons(args.start, args.end):
        for th_md in sorted(lesson.rglob("*.md")):
            if "answer" in th_md.parts:
                continue
            rel = th_md.relative_to(TH)
            en_path = EN / rel
            if args.skip_existing_clean and en_path.exists():
                if not THAI_RE.search(en_path.read_text(encoding="utf-8")):
                    continue
            en_path.parent.mkdir(parents=True, exist_ok=True)
            print(rel.as_posix(), flush=True)
            en_path.write_text(translate_text(th_md.read_text(encoding="utf-8"), cache), encoding="utf-8")
            save_cache(cache)
            n += 1
    print(f"Done {n}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
