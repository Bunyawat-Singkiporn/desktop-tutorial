# -*- coding: utf-8 -*-
import os
import re
from pathlib import Path

root = Path(r"c:\Users\test\Documents\GitHub\desktop-tutorial\project\python-beginner\slide-en")
thai = re.compile(r"[\u0E00-\u0E7F]")
# Real glue: ## heading ends and ``` starts on same line (no newline between)
same_line_fence = re.compile(r"(?m)^(#{1,6} .+?)```")
label_glue = re.compile(r"(?m)\*\*(?:Input|Output|Required Output):\*\*```")
starter_glue = re.compile(r"(?m)## Starter Code```")
angle_glue = re.compile(r"```>")

still_thai = []
glue_hits = []
needles = {
    "โจทย์": [],
    "ผลลัพธ์": [],
    "บาท": [],
    "Proposition": [],
    "decimal / float": [],
    "text / string": [],
}

for path in sorted(root.rglob("*.md")):
    if path.name == "README.md" or path.name.startswith("_"):
        continue
    text = path.read_text(encoding="utf-8")
    rel = str(path.relative_to(root)).replace("\\", "/")
    if thai.search(text):
        still_thai.append(rel)
    for m in same_line_fence.finditer(text):
        glue_hits.append((rel, "heading", repr(m.group(0)[:100])))
    for m in label_glue.finditer(text):
        glue_hits.append((rel, "label", repr(m.group(0))))
    for m in starter_glue.finditer(text):
        glue_hits.append((rel, "starter", repr(m.group(0))))
    for m in angle_glue.finditer(text):
        glue_hits.append((rel, "angle", "```>"))
    for needle, bucket in needles.items():
        if needle in text:
            bucket.append(rel)

print("REMAINING THAI:", len(still_thai))
for rel in still_thai:
    print(" ", rel)
print("TRUE GLUE HITS:", len(glue_hits))
for item in glue_hits:
    print(" ", item)
for needle, bucket in needles.items():
    print(f"needle {needle!r}: {len(bucket)}")
    for rel in bucket[:8]:
        print("  ", rel)

p001 = root / "001-what-is-python" / "01_what_is_python.md"
t001 = p001.read_text(encoding="utf-8")
print("001 Hello demo:", 'print("Hello!")' in t001)
print("001 Thai greeting left:", "สวัสดี" in t001)
print("001 Thai chars:", len(thai.findall(t001)))

# count md
md_count = sum(
    1
    for p in root.rglob("*.md")
    if p.name != "README.md" and not p.name.startswith("_")
)
print("content md files:", md_count)
