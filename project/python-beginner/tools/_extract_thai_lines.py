import re
from pathlib import Path

THAI = re.compile(r"[\u0E00-\u0E7F]")
ROOT = Path(__file__).resolve().parents[1]
lines: set[str] = set()
for d in sorted(ROOT.joinpath("slide").iterdir()):
    if not (d.is_dir() and d.name[:3].isdigit() and "013" <= d.name <= "024-"):
        continue
    for f in d.rglob("*.md"):
        if "answer" in f.parts:
            continue
        in_fence = False
        for line in f.read_text(encoding="utf-8").splitlines():
            s = line.strip()
            if s.startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            if THAI.search(line):
                lines.add(line.rstrip())
print(len(lines))
for x in sorted(lines):
    print(x)
