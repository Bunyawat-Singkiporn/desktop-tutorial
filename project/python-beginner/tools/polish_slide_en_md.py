"""Fix common EN slide markdown issues and re-translate remaining Thai lines."""
from __future__ import annotations

import argparse
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN = ROOT / "slide-en"
THAI_RE = re.compile(r"[\u0E00-\u0E7F]")

FIXES = [
    (re.compile(r"^# # ", re.M), "## "),
    (re.compile(r"\* \* Difficulty: \* \*", re.I), "**Difficulty:**"),
    (re.compile(r"\* \* Output: \* \*", re.I), "**Output:**"),
    (re.compile(r"\* \* Input: \* \*", re.I), "**Input:**"),
    (re.compile(r"^# # (Input|Output|Sample|Problems|Problem|Task)\s*$", re.M), r"## \1"),
    (re.compile(r"— Number (\d+):", re.I), r"— Q\1:"),
    (re.compile(r"^## Problems\s*$", re.M), "## Task"),
    (re.compile(r"^## Sample\s*$", re.M), "## Example"),
    (re.compile(r"^## Problem\s*$", re.M), "## Task"),
    (re.compile(r"^## 💡 Hint\s*$", re.M), "## Hint"),
]


def mymemory(text: str) -> str:
    q = urllib.parse.quote(text[:450])
    url = f"https://api.mymemory.translated.net/get?q={q}&langpair=th|en"
    with urllib.request.urlopen(url, timeout=30) as resp:
        data = json.loads(resp.read().decode())
    return data.get("responseData", {}).get("translatedText", text)


def polish_text(text: str, retranslate: bool) -> str:
    for pat, repl in FIXES:
        text = pat.sub(repl, text)
    if not retranslate or not THAI_RE.search(text):
        return text
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    in_fence = False
    for line in lines:
        if line.strip().startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence or not THAI_RE.search(line):
            out.append(line)
            continue
        if line.lstrip().startswith("#") or line.lstrip().startswith("|"):
            out.append(line)
            continue
        try:
            out.append(mymemory(line.strip()) + ("\n" if line.endswith("\n") else ""))
            time.sleep(0.4)
        except Exception:
            out.append(line)
    return "".join(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", default="004-")
    ap.add_argument("--end", default="012-review")
    ap.add_argument("--retranslate", action="store_true")
    args = ap.parse_args()
    n = 0
    for lesson in sorted(p for p in EN.iterdir() if p.is_dir() and p.name[:3].isdigit()):
        if lesson.name < args.start or lesson.name > args.end:
            continue
        for md in sorted(lesson.glob("*.md")):
            text = md.read_text(encoding="utf-8")
            new = polish_text(text, args.retranslate)
            if new != text:
                md.write_text(new, encoding="utf-8")
            n += 1
    print(f"Polished {n} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
