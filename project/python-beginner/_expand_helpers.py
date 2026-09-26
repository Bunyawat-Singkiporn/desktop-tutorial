# -*- coding: utf-8 -*-
"""Helpers to write standard-format slide problems."""
from __future__ import annotations

import re
from pathlib import Path

SLIDE = Path(__file__).resolve().parent / "slide"

NUM_FILES = {
    2: "02_test.md",
    3: "03_test.md",
    4: "04_test.md",
    5: "05_challenge.md",
    6: "06_medium.md",
    7: "07_medium.md",
    8: "08_easy.md",
    9: "09_easy.md",
    10: "10_medium.md",
    11: "11_medium.md",
    12: "12_medium.md",
    13: "13_medium.md",
    14: "14_challenge.md",
    15: "15_challenge.md",
    16: "16_challenge.md",
}

DIFF = {
    2: "🟢 Easy",
    3: "🟢 Easy",
    4: "🟢 Easy",
    8: "🟢 Easy",
    9: "🟢 Easy",
    6: "🟡 Medium",
    7: "🟡 Medium",
    10: "🟡 Medium",
    11: "🟡 Medium",
    12: "🟡 Medium",
    13: "🟡 Medium",
    5: "🔴 Challenge",
    14: "🔴 Challenge",
    15: "🔴 Challenge",
    16: "🔴 Challenge",
}


def clear_practice(week_dir: Path) -> None:
    for p in week_dir.glob("*.md"):
        if p.name == "00_index.md":
            p.unlink()
            continue
        if p.name.startswith("01_"):
            continue
        if "_range" in p.name or "_readiness" in p.name:
            continue
        if re.match(r"\d\d_", p.name):
            # keep lesson-like 02_range already skipped; drop practice
            if any(x in p.name for x in ("_test", "_easy", "_medium", "_challenge")):
                p.unlink()
    ans = week_dir / "answer"
    if ans.exists():
        for p in ans.glob("*.py"):
            p.unlink()
    else:
        ans.mkdir(parents=True)


def render_problem(
    *,
    emoji: str,
    chapter: str,
    n: int,
    title: str,
    body: str,
    input_desc: str,
    output_desc: str,
    sample_input: str | None,
    sample_output: str,
    hint: str | None,
    starter: str,
) -> str:
    diff = DIFF[n]
    sample = ""
    if sample_input is not None:
        sample += f"**Input:**\n\n```text\n{sample_input.rstrip()}\n```\n\n"
    sample += f"**Output:**\n\n```text\n{sample_output.rstrip(chr(10))}\n```\n"
    hint_block = ""
    if hint:
        hint_block = f"\n---\n\n## 💡 Hint\n\n{hint.strip()}\n"
    return f"""# {emoji} {chapter} — ข้อ {n}: {title}

**Difficulty:** {diff}

---

## โจทย์

{body.strip()}

---

## Input

{input_desc.strip()}

## Output

{output_desc.strip()}

---

## ตัวอย่าง

{sample}
{hint_block}
---

## Starter Code

```python
{starter.rstrip()}
```
"""


def write_week(
    folder: str,
    *,
    chapter: str,
    emoji: str,
    index_md: str,
    problems: list[dict],
) -> None:
    week = SLIDE / folder
    clear_practice(week)
    (week / "00_index.md").write_text(index_md.strip() + "\n", encoding="utf-8")
    assert len(problems) == 15, folder
    for spec in problems:
        n = spec["n"]
        md = render_problem(
            emoji=emoji,
            chapter=chapter,
            n=n,
            title=spec["title"],
            body=spec["body"],
            input_desc=spec.get("input_desc", "ไม่มี (โปรแกรมนี้ไม่รับค่าจากผู้ใช้)"),
            output_desc=spec["output_desc"],
            sample_input=spec.get("sample_input"),
            sample_output=spec["sample_output"],
            hint=spec.get("hint"),
            starter=spec["starter"],
        )
        (week / NUM_FILES[n]).write_text(md, encoding="utf-8")
        (week / "answer" / f"{n:02d}_{spec['slug']}.py").write_text(
            spec["answer"].rstrip() + "\n", encoding="utf-8"
        )
    print(f"wrote {folder}: 15 problems + index")
