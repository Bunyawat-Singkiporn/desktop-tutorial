"""Overwrite slide-en/*.md from slide/*.md when EN missing or contains Thai."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TH, EN = ROOT / "slide", ROOT / "slide-en"
THAI_RE = re.compile(r"[\u0E00-\u0E7F]")

# reuse translator
sys.path.insert(0, str(Path(__file__).parent))
from translate_md_cached import load_cache, save_cache, translate_text  # noqa: E402


def lessons(start: str, end: str) -> list[Path]:
    ls = sorted([d for d in TH.iterdir() if d.is_dir() and d.name[:3].isdigit()], key=lambda p: p.name)
    if start:
        ls = [d for d in ls if d.name >= start]
    if end:
        ls = [d for d in ls if d.name <= end]
    return ls


def main() -> int:
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--start", default="025")
    ap.add_argument("--end", default="036")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    cache = load_cache()
    n = 0
    for lesson in lessons(args.start, args.end):
        for th_md in sorted(lesson.rglob("*.md")):
            if "answer" in th_md.parts:
                continue
            rel = th_md.relative_to(TH)
            en_path = EN / rel
            if en_path.exists() and not args.force:
                try:
                    body = en_path.read_text(encoding="utf-8")
                except OSError:
                    body = ""
                if body and not THAI_RE.search(body):
                    continue
            en_path.parent.mkdir(parents=True, exist_ok=True)
            print(rel.as_posix(), flush=True)
            en_path.write_text(
                translate_text(th_md.read_text(encoding="utf-8"), cache),
                encoding="utf-8",
            )
            save_cache(cache)
            n += 1
    print(f"Synced {n}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
