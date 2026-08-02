# -*- coding: utf-8 -*-
"""Rewrite homework Starter Code blocks to be scaffolds, not full answers."""
from __future__ import annotations

import re
from pathlib import Path

HW = Path(__file__).resolve().parent / "homework"


def scaffold(answer: str) -> str:
    """Build incomplete starter from a full answer."""
    lines = answer.replace("\r\n", "\n").strip().split("\n")
    if not lines:
        return "# เขียนโค้ดตรงนี้"

    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        indent = line[: len(line) - len(line.lstrip())]

        if not stripped:
            out.append("")
            i += 1
            continue

        if stripped.startswith("#"):
            out.append(line)
            i += 1
            continue

        # Control headers: keep header, blank body with pass placeholder comment
        if re.match(r"^(if|elif|else|for|while)\b", stripped):
            out.append(line)
            # peek following indented block — replace with comment
            i += 1
            block_indent = None
            while i < len(lines):
                nxt = lines[i]
                ns = nxt.strip()
                if not ns:
                    i += 1
                    continue
                ni = nxt[: len(nxt) - len(nxt.lstrip())]
                if block_indent is None:
                    if len(ni) <= len(indent):
                        break
                    block_indent = ni
                if len(ni) < len(block_indent):
                    break
                # skip body lines of this block
                i += 1
            out.append(indent + "    # เขียนโค้ดตรงนี้")
            continue

        # Given literals / simple setup assignments — keep left side hints
        if "=" in stripped and "input(" not in stripped and not stripped.startswith("print"):
            # Keep assignment of given constants as scaffolding
            # but blank out computed RHS that uses other vars heavily? Keep simple given values.
            left, _, right = stripped.partition("=")
            left, right = left.strip(), right.strip()
            # Keep True/False/numbers/strings/lists as given data
            if re.match(
                r'^(\d+\.?\d*|True|False|None|".*"|\'.*\'|\[.*\])$',
                right,
            ):
                out.append(line)
            else:
                out.append(f"{indent}{left} = ")  # blank computation
            i += 1
            continue

        if "input(" in stripped:
            # Keep input lines as partial scaffold (they're the prompt structure)
            out.append(line)
            i += 1
            continue

        if stripped.startswith("print(") or "print(" in stripped:
            out.append(f"{indent}# แสดงผลตรงนี้")
            i += 1
            continue

        # Fallback
        out.append(f"{indent}# เขียนโค้ดตรงนี้")
        i += 1

    text = "\n".join(out).strip()
    # If scaffold accidentally equals answer, force blank
    if text.replace(" ", "") == answer.strip().replace(" ", ""):
        return "# เขียนโค้ดตรงนี้"
    # If nothing useful left
    if not text or text.count("#") == len([L for L in text.splitlines() if L.strip()]):
        # all comments is ok
        pass
    return text + "\n"


def replace_starter(md_text: str, new_starter: str) -> str:
    pattern = re.compile(
        r"(## Starter Code\s*\n\s*\n```python\n)(.*?)(\n```)",
        re.DOTALL,
    )

    def repl(m: re.Match) -> str:
        body = new_starter.rstrip("\n")
        return f"{m.group(1)}{body}{m.group(3)}"

    new_text, n = pattern.subn(repl, md_text, count=1)
    if n != 1:
        raise RuntimeError("Starter Code block not found or multiple")
    return new_text


def main() -> None:
    fixed = 0
    identical = 0
    for week in sorted(p for p in HW.iterdir() if p.is_dir()):
        answer_dir = week / "answer"
        if not answer_dir.exists():
            continue
        for md in sorted(week.glob("*.md")):
            if md.name == "README.md":
                continue
            num = md.stem  # 01
            ans_path = answer_dir / f"{num}.py"
            if not ans_path.exists():
                print("missing answer", ans_path)
                continue
            answer = ans_path.read_text(encoding="utf-8")
            starter = scaffold(answer)
            # Ensure starter is not identical to answer
            if starter.strip() == answer.strip():
                starter = "# เขียนโค้ดตรงนี้\n"
                identical += 1
            md_text = md.read_text(encoding="utf-8")
            # Extract old starter for comparison
            m = re.search(r"```python\n(.*?)```", md_text, re.DOTALL)
            old = m.group(1) if m else ""
            if old.strip() == answer.strip():
                pass  # expected bad case
            new_md = replace_starter(md_text, starter)
            md.write_text(new_md, encoding="utf-8")
            fixed += 1
    print(f"fixed={fixed} forced_blank_identical={identical}")


if __name__ == "__main__":
    main()
