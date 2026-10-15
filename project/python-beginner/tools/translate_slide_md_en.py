"""Translate slide/*.md prose to slide-en/ preserving fenced blocks."""
from __future__ import annotations

import argparse
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TH = ROOT / "slide"
EN = ROOT / "slide-en"
THAI_RE = re.compile(r"[\u0E00-\u0E7F]")
FENCE_RE = re.compile(r"^```")

SECTION_REPLACEMENTS = [
    (re.compile(r"^## โจทย์\s*$", re.M), "## Task"),
    (re.compile(r"^## ตัวอย่าง\s*$", re.M), "## Example"),
    (re.compile(r"^## 💡 Hint\s*$", re.M), "## Hint"),
]

COMMENT_REPLACEMENTS = [
    ("# เขียนโค้ดตรงนี้", "# Write your code here"),
    ("# เขียนโค้ดที่นี่", "# Write your code here"),
    ("# เขียนโค้ดที่ถูกต้องตรงนี้", "# Write your corrected code here"),
]

TITLE_RE = re.compile(r"^(#+\s*)(.*?)\s*—\s*ข้อ\s*(\d+)\s*:\s*(.*)$", re.UNICODE)
INDEX_TITLE_RE = re.compile(r"^#\s*📋\s*สารบัญโจทย์\s*—\s*บท\s*(\d+)\s*(.*)$", re.UNICODE)


def split_fenced(text: str) -> list[tuple[str, bool]]:
    lines = text.splitlines(keepends=True)
    parts: list[tuple[str, bool]] = []
    buf: list[str] = []
    in_fence = False
    for line in lines:
        if FENCE_RE.match(line.strip()):
            if in_fence:
                buf.append(line)
                parts.append(("".join(buf), True))
                buf = []
                in_fence = False
            else:
                if buf:
                    parts.append(("".join(buf), False))
                    buf = []
                buf = [line]
                in_fence = True
        else:
            buf.append(line)
    if buf:
        parts.append(("".join(buf), in_fence))
    return parts


def _mymemory_once(text: str) -> str:
    for attempt in range(5):
        try:
            q = urllib.parse.quote(text)
            url = f"https://api.mymemory.translated.net/get?q={q}&langpair=th|en"
            with urllib.request.urlopen(url, timeout=30) as resp:
                data = json.loads(resp.read().decode())
            out = data.get("responseData", {}).get("translatedText", text)
            if out and out != text:
                return out
            time.sleep(2.0 * (attempt + 1))
        except Exception:
            time.sleep(2.0 * (attempt + 1))
    return text


def mymemory_translate(text: str) -> str:
    if not text or not THAI_RE.search(text):
        return text
    if len(text) <= 450:
        return _mymemory_once(text.strip()) if text.strip() else text
    lines = text.splitlines(keepends=True)
    buf = ""
    out: list[str] = []
    for line in lines:
        if len(buf) + len(line) > 400 and buf.strip():
            out.append(_mymemory_once(buf) if THAI_RE.search(buf) else buf)
            buf = line
        else:
            buf += line
    if buf:
        out.append(_mymemory_once(buf) if THAI_RE.search(buf) else buf)
    return "".join(out)


def postprocess(text: str) -> str:
    for pat, repl in SECTION_REPLACEMENTS:
        text = pat.sub(repl, text)
    for old, new in COMMENT_REPLACEMENTS:
        text = text.replace(old, new)

    def title_sub(m: re.Match[str]) -> str:
        hashes, prefix, num, rest = m.group(1), m.group(2), m.group(3), m.group(4)
        if THAI_RE.search(prefix):
            prefix = mymemory_translate(prefix)
        if THAI_RE.search(rest):
            rest = mymemory_translate(rest)
        return f"{hashes}{prefix} — Q{num}: {rest}"

    text = TITLE_RE.sub(title_sub, text)

    def index_sub(m: re.Match[str]) -> str:
        num, rest = m.group(1), m.group(2).strip()
        if THAI_RE.search(rest):
            rest = mymemory_translate(rest)
        return f"# 📋 Exercise index — Lesson {num} {rest}"

    text = INDEX_TITLE_RE.sub(index_sub, text)
    text = text.replace("## ลำดับที่แนะนำ", "## Recommended order")
    text = text.replace("## หมายเหตุสำหรับครู", "## Notes for teachers")
    text = text.replace("**ขอบเขตของบทนี้:**", "**Scope of this lesson:**")
    text = text.replace("**สรุป:**", "**Summary:**")
    text = text.replace("| # | ไฟล์ | ระดับ | โจทย์ | แกนการคิด |", "| # | File | Level | Exercise | Core idea |")
    text = re.sub(r"^## Input\s*$", "## Input", text, flags=re.M)
    text = re.sub(r"^## Output\s*$", "## Output", text, flags=re.M)
    text = re.sub(r"^## Starter Code\s*$", "## Starter Code", text, flags=re.M)
    # common Input/Output prose
    text = re.sub(r"^ไม่มี \(โปรแกรมนี้ไม่รับค่าจากผู้ใช้\)\s*$", "None (this program does not read user input)", text, flags=re.M)
    text = re.sub(r"^ไม่มี\s*$", "None", text, flags=re.M)
    return text


def translate_prose_line(line: str) -> str:
    """Translate one markdown line, preserving structure."""
    nl = "\n" if line.endswith("\n") else ""
    core = line.rstrip("\n")
    if not THAI_RE.search(core):
        return line
    if TITLE_RE.match(core):
        m = TITLE_RE.match(core)
        assert m
        hashes, prefix, num, rest = m.group(1), m.group(2), m.group(3), m.group(4)
        if THAI_RE.search(prefix):
            prefix = _mymemory_once(prefix)
        if THAI_RE.search(rest):
            rest = _mymemory_once(rest)
        return f"{hashes}{prefix} — Q{num}: {rest}{nl}"
    for pat, repl in SECTION_REPLACEMENTS:
        if pat.match(core):
            return repl + nl
    if core.strip() == "ไม่มี (โปรแกรมนี้ไม่รับค่าจากผู้ใช้)":
        return "None (this program does not read user input)" + nl
    if core.strip() == "ไม่มี":
        return "None" + nl
    if core.strip() == "ดูตัวอย่าง":
        return "See the example" + nl
    if core.lstrip().startswith("#") or core.lstrip().startswith("|"):
        return _mymemory_once(core) + nl
    return _mymemory_once(core) + nl


def translate_prose_segment(seg: str) -> str:
    if not THAI_RE.search(seg):
        return seg
    return "".join(translate_prose_line(line) for line in seg.splitlines(keepends=True))


def translate_file(th_path: Path, en_path: Path) -> None:
    raw = th_path.read_text(encoding="utf-8")
    for old, new in COMMENT_REPLACEMENTS:
        raw = raw.replace(old, new)
    out_parts: list[str] = []
    for seg, is_code in split_fenced(raw):
        if is_code:
            out_parts.append(seg)
        else:
            out_parts.append(translate_prose_segment(seg))
    result = postprocess("".join(out_parts))
    en_path.parent.mkdir(parents=True, exist_ok=True)
    en_path.write_text(result, encoding="utf-8")


def lesson_filter(start: str, end: str) -> list[Path]:
    lessons = sorted(p for p in TH.iterdir() if p.is_dir() and p.name[:3].isdigit())
    if start:
        lessons = [p for p in lessons if p.name >= start]
    if end:
        lessons = [p for p in lessons if p.name <= end]
    return lessons


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", default="004-")
    ap.add_argument("--end", default="012-review")
    ap.add_argument("--delay", type=float, default=1.2)
    args = ap.parse_args()
    count = 0
    for lesson in lesson_filter(args.start, args.end):
        for th_md in sorted(lesson.glob("*.md")):
            en_md = EN / lesson.name / th_md.name
            print(f"translate {lesson.name}/{th_md.name}", flush=True)
            translate_file(th_md, en_md)
            count += 1
            time.sleep(args.delay)
    print(f"Done: {count} files", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
