#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shared helpers for generating gold-standard slide practice."""
from __future__ import annotations
import os, re, shutil, subprocess, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "slide"))


def clean_chapter(folder: str) -> str:
    d = os.path.join(ROOT, folder)
    assert os.path.isdir(d), d
    for name in list(os.listdir(d)):
        path = os.path.join(d, name)
        if name.startswith("01_") and name.endswith(".md"):
            continue
        if name == "answer":
            shutil.rmtree(path)
            os.makedirs(path)
            continue
        if re.match(r"\d\d_.*\.md$", name) or name == "00_index.md":
            os.remove(path)
    adir = os.path.join(d, "answer")
    if not os.path.isdir(adir):
        os.makedirs(adir)
    return d


def run_code(code: str, stdin: str = "") -> str:
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False, encoding="utf-8") as f:
        f.write(code)
        path = f.name
    try:
        r = subprocess.run([sys.executable, path], input=stdin, capture_output=True,
                           text=True, timeout=10)
        if r.returncode != 0:
            raise RuntimeError(f"code failed:\n{code}\n\n{r.stderr}")
        return r.stdout
    finally:
        os.unlink(path)


def write_problem(folder: str, p: dict) -> None:
    d = os.path.join(ROOT, folder)
    out = run_code(p["code"], p.get("stdin", ""))
    # ensure trailing newline in text blocks for checker rstrip consistency
    example_in = p.get("stdin", "")
    if example_in and not example_in.endswith("\n"):
        example_in += "\n"
    example_out = out
    if example_out and not example_out.endswith("\n"):
        example_out += "\n"

    cond = ""
    if p.get("conditions"):
        cond = "\n**เงื่อนไข:**\n\n" + "\n".join(f"- {c}" for c in p["conditions"]) + "\n"

    hint_block = ""
    if p.get("hint"):
        hint_block = f"\n## 💡 Hint\n\n{p['hint']}\n\n---\n"

    body = f"""# {p['title']}

**Difficulty:** {p['diff']}

---

## โจทย์

{p['scenario']}
{cond}
---

## Input

{p['inp']}

## Output

{p['out']}

---

## ตัวอย่าง

**Input:**

```text
{example_in}```

**Output:**

```text
{example_out}```

---
{hint_block}
## Starter Code

```python
{p['starter']}
```
"""
    with open(os.path.join(d, p["file"]), "w", encoding="utf-8", newline="\n") as f:
        f.write(body)
    with open(os.path.join(d, "answer", p["answer"]), "w", encoding="utf-8", newline="\n") as f:
        f.write(p["code"].rstrip() + "\n")


def write_index(folder, chapter_title, scope_lines, forbid_lines, rows, notes):
    lines = [
        f"# 📋 สารบัญโจทย์ — {chapter_title}",
        "",
        "**ขอบเขตของบทนี้:**",
        "",
    ]
    for s in scope_lines:
        lines.append(f"- {s}")
    lines.append("")
    if forbid_lines:
        lines.append("> ❌ " + " · ".join(forbid_lines))
        lines.append("")
    lines += [
        "---", "", "## ลำดับที่แนะนำ", "",
        "| # | ไฟล์ | ระดับ | โจทย์ | แกนการคิด |",
        "|---|------|-------|-------|-----------|",
    ]
    for i, (fn, level, name, axis) in enumerate(rows, 1):
        lines.append(f"| {i} | `{fn}` | {level} | {name} | {axis} |")
    lines += [
        "",
        "**สรุป:** 🟢 Easy 5 ข้อ · 🟡 Medium 6 ข้อ · 🔴 Challenge 4 ข้อ = **15 ข้อ**",
        "", "---", "", "## หมายเหตุสำหรับครู", "",
    ]
    for n in notes:
        lines.append(f"- {n}")
    lines.append("- เฉลยทุกข้ออยู่ใน `answer/` และผ่านการรันเทียบกับตัวอย่างในโจทย์แล้ว")
    lines.append("")
    with open(os.path.join(ROOT, folder, "00_index.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))


def emit(folder, probs, chapter_title, scope, forbid, notes):
    clean_chapter(folder)
    rows = []
    for p in probs:
        write_problem(folder, p)
        rows.append((p["file"], p["diff"], p["name"], p["axis"]))
        print(f"  {folder}/{p['file']}")
    write_index(folder, chapter_title, scope, forbid, rows, notes)
