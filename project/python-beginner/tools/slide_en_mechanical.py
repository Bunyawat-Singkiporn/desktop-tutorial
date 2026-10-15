"""Mechanical TH->EN for slide markdown (no external API). Used when API rate-limited."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TH = ROOT / "slide"
EN = ROOT / "slide-en"
THAI = re.compile(r"[\u0E00-\u0E7F]")
FENCE = re.compile(r"(```[\s\S]*?```)")

# Longest-first phrase replacements (prose outside code fences)
PHRASES: list[tuple[str, str]] = [
    ("## โจทย์", "## Task"),
    ("## ตัวอย่าง", "## Example"),
    ("## คำใบ้", "## Hint"),
    ("## หมายเหตุสำหรับครู", "## Notes for teachers"),
    ("## ลำดับที่แนะนำ", "## Recommended order"),
    ("**เงื่อนไข:**", "**Requirements:**"),
    ("**ขอบเขตของบทนี้:**", "**Chapter scope:**"),
    ("**สรุป:**", "**Summary:**"),
    (
        "ไม่มี (กำหนดค่าในโปรแกรม / เรียกฟังก์ชันในโค้ด)",
        "None (values are set in the program / call functions in code)",
    ),
    ("ไม่มี (กำหนดค่าในโปรแกรม)", "None (values are set in the program)"),
    ("ดูตัวอย่าง", "See example"),
    ("# เขียนโค้ดตรงนี้", "# Write your code here"),
    ("# เขียนโค้ดที่นี่", "# Write your code here"),
    ("สารบัญโจทย์", "Exercise index"),
    ("| ระดับ |", "| Level |"),
    ("| โจทย์ |", "| Problem |"),
    ("| แกนการคิด |", "| Core idea |"),
    ("| ไฟล์ |", "| File |"),
    ("> ❌ ห้าม parameter · ห้าม `return` · ห้าม default argument", "> ❌ No parameters · no `return` · no default arguments"),
    ("> ❌ ห้าม `return` · ห้าม default / keyword argument", "> ❌ No `return` · no default / keyword arguments"),
    (" ข้อ · ", " problems · "),
    (" ข้อ = ", " problems = "),
    ("1 บรรทัด", "1 line"),
    ("2 บรรทัด", "2 lines"),
    ("3 บรรทัด", "3 lines"),
    ("4 บรรทัด", "4 lines"),
    ("ใบเสร็จ", "receipt"),
    ("กล่อง", "box layout"),
]

# Line-level translations (exact match after strip)
LINES: dict[str, str] = {}


def apply_phrases(text: str) -> str:
    text = re.sub(r"—\s*ข้อ\s*(\d+)\s*:", r"— Q\1:", text)
    for a, b in sorted(PHRASES, key=lambda x: -len(x[0])):
        text = text.replace(a, b)
    return text


def process_file(raw: str) -> str:
    raw = apply_phrases(raw)
    parts = FENCE.split(raw)
    out: list[str] = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            part = part.replace("# เขียนโค้ดตรงนี้", "# Write your code here")
            out.append(part)
            continue
        lines = part.split("\n")
        new_lines = []
        for line in lines:
            s = line.strip()
            if s in LINES:
                new_lines.append(line.replace(s, LINES[s]))
            else:
                new_lines.append(line)
        out.append("\n".join(new_lines))
    return apply_phrases("".join(out))


def sync_lessons(start: str, end: str) -> None:
    lessons = sorted(d for d in TH.iterdir() if d.is_dir() and d.name[:3].isdigit())
    lessons = [d for d in lessons if d.name >= start and d.name <= end]
    for lesson in lessons:
        for th_md in sorted(lesson.rglob("*.md")):
            if "answer" in th_md.parts:
                continue
            rel = th_md.relative_to(TH)
            en_path = EN / rel
            en_path.parent.mkdir(parents=True, exist_ok=True)
            en_path.write_text(process_file(th_md.read_text(encoding="utf-8")), encoding="utf-8")


if __name__ == "__main__":
    import sys
    sync_lessons(sys.argv[1] if len(sys.argv) > 1 else "039-return-values", sys.argv[2] if len(sys.argv) > 2 else "048-transition-prep")
