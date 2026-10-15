"""Filename parity checker / structural sync helpers for slide <-> slide-en."""
from __future__ import annotations

import argparse
import compileall
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TH = ROOT / "slide"
EN = ROOT / "slide-en"
SKIP_PARTS = {"__pycache__"}
THAI_RE = re.compile(r"[\u0E00-\u0E7F]")


def lesson_dirs() -> list[Path]:
    return sorted(
        [p for p in TH.iterdir() if p.is_dir() and p.name[:3].isdigit()],
        key=lambda p: p.name,
    )


def rel_files(lesson: Path) -> set[str]:
    out: set[str] = set()
    if not lesson.exists():
        return out
    for f in lesson.rglob("*"):
        if not f.is_file():
            continue
        if any(part in SKIP_PARTS for part in f.parts):
            continue
        out.add(f.relative_to(lesson).as_posix())
    return out


def filter_lessons(start: str | None, end: str | None) -> list[Path]:
    lessons = lesson_dirs()
    if start:
        lessons = [p for p in lessons if p.name >= start]
    if end:
        lessons = [p for p in lessons if p.name <= end]
    return lessons


def cmd_diff(start: str | None, end: str | None) -> int:
    missing = extra = 0
    for th_lesson in filter_lessons(start, end):
        en_lesson = EN / th_lesson.name
        th_files = rel_files(th_lesson)
        en_files = rel_files(en_lesson)
        only_th = sorted(th_files - en_files)
        only_en = sorted(en_files - th_files)
        if only_th or only_en:
            print(f"\n== {th_lesson.name} ==")
            for x in only_th:
                print(f"  MISSING_EN  {x}")
                missing += 1
            for x in only_en:
                print(f"  EXTRA_EN    {x}")
                extra += 1
    print(f"\nSummary: missing_en={missing} extra_en={extra}")
    return 0 if missing == 0 and extra == 0 else 1


def cmd_delete_orphans(start: str | None, end: str | None, apply: bool) -> int:
    removed = 0
    for th_lesson in filter_lessons(start, end):
        en_lesson = EN / th_lesson.name
        if not en_lesson.exists():
            continue
        only_en = rel_files(en_lesson) - rel_files(th_lesson)
        for rel in sorted(only_en):
            path = en_lesson / rel
            print(f"DELETE {path.relative_to(ROOT)}")
            removed += 1
            if apply and path.exists():
                path.unlink()
        if apply:
            # clean empty dirs
            for d in sorted(en_lesson.rglob("*"), reverse=True):
                if d.is_dir() and not any(d.iterdir()):
                    d.rmdir()
    print(f"Orphans: {removed} ({'deleted' if apply else 'dry-run'})")
    return 0


def cmd_copy_answers(start: str | None, end: str | None) -> int:
    copied = 0
    for th_lesson in filter_lessons(start, end):
        src = th_lesson / "answer"
        if not src.exists():
            continue
        dst = EN / th_lesson.name / "answer"
        dst.mkdir(parents=True, exist_ok=True)
        # remove EN answers not in TH
        th_names = {p.name for p in src.glob("*.py")}
        for old in list(dst.glob("*.py")):
            if old.name not in th_names:
                old.unlink()
                print(f"DELETE answer {th_lesson.name}/{old.name}")
        for py in src.glob("*.py"):
            text = py.read_text(encoding="utf-8")
            # light comment localization
            text = text.replace("# เขียนโค้ดตรงนี้", "# Write your code here")
            text = text.replace("# เขียนโค้ดที่นี่", "# Write your code here")
            shutil.copy2(py, dst / py.name) if not THAI_RE.search(text) else (dst / py.name).write_text(text, encoding="utf-8")
            # always write possibly-cleaned text
            (dst / py.name).write_text(text, encoding="utf-8")
            copied += 1
    print(f"Copied/updated answers: {copied}")
    return 0


def cmd_thai_md(start: str | None, end: str | None) -> int:
    n = 0
    for th_lesson in filter_lessons(start, end):
        en_lesson = EN / th_lesson.name
        for f in sorted(en_lesson.rglob("*.md")) if en_lesson.exists() else []:
            if any(part in SKIP_PARTS for part in f.parts):
                continue
            text = f.read_text(encoding="utf-8", errors="ignore")
            if THAI_RE.search(text):
                print(f.relative_to(EN))
                n += 1
    print(f"EN md still containing Thai: {n}")
    return 0 if n == 0 else 1


def cmd_compile(start: str | None, end: str | None) -> int:
    ok = True
    for th_lesson in filter_lessons(start, end):
        ans = EN / th_lesson.name / "answer"
        if not ans.exists():
            continue
        if not compileall.compile_dir(str(ans), quiet=1):
            print(f"COMPILE FAIL {th_lesson.name}")
            ok = False
    print("compile ok" if ok else "compile failed")
    return 0 if ok else 1


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("command", choices=["diff", "delete-orphans", "copy-answers", "thai-md", "compile"])
    p.add_argument("--start", default=None, help="lesson folder >= this name")
    p.add_argument("--end", default=None, help="lesson folder <= this name")
    p.add_argument("--apply", action="store_true")
    args = p.parse_args()
    if args.command == "diff":
        return cmd_diff(args.start, args.end)
    if args.command == "delete-orphans":
        return cmd_delete_orphans(args.start, args.end, args.apply)
    if args.command == "copy-answers":
        return cmd_copy_answers(args.start, args.end)
    if args.command == "thai-md":
        return cmd_thai_md(args.start, args.end)
    if args.command == "compile":
        return cmd_compile(args.start, args.end)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
