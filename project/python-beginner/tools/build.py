#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ตัวช่วยสร้างไฟล์โจทย์ + เฉลย

ผู้เขียนกำหนด spec ของแต่ละข้อ แล้วสคริปต์นี้จะ
  1) เขียนไฟล์เฉลย .py
  2) รันเฉลยด้วย sample input
  3) เอา output จริงไปใส่ใน block ตัวอย่างของไฟล์โจทย์

ทำให้ตัวอย่างในโจทย์ตรงกับเฉลยเสมอ ไม่มีทางคำนวณผิด
"""
import os, subprocess, sys

DIFF = {"e": "🟢 Easy", "m": "🟡 Medium", "c": "🔴 Challenge"}


def build(chapter_dir, chapter_title, problems):
    """problems = list of dict:
        file    : "02_test"            ชื่อไฟล์โจทย์ (ไม่ต้องใส่ .md)
        answer  : "02_turn_on_ac"      ชื่อไฟล์เฉลย (ไม่ต้องใส่ .py)
        emoji   : "🌡️"
        name    : "เปิดแอร์หรือยัง"
        diff    : "e" | "m" | "c"
        body    : ส่วน "## โจทย์" (markdown)
        io      : ส่วน Input/Output อธิบายเป็นข้อความ (markdown, ไม่มีหัวข้อ)
        stdin   : ข้อความ input สำหรับตัวอย่าง ("" ถ้าไม่รับ input)
        hint    : ข้อความ hint (None ถ้าไม่มี)
        starter : โค้ดตั้งต้น
        code    : โค้ดเฉลย
    """
    adir = os.path.join(chapter_dir, "answer")
    os.makedirs(adir, exist_ok=True)
    made = []

    for i, p in enumerate(problems, 1):
        apath = os.path.join(adir, p["answer"] + ".py")
        with open(apath, "w", encoding="utf-8", newline="\n") as f:
            f.write(p["code"].strip("\n") + "\n")

        r = subprocess.run([sys.executable, apath], input=p.get("stdin", ""),
                           capture_output=True, text=True, timeout=10)
        if r.returncode != 0:
            raise SystemExit(f"เฉลย {p['answer']} รันไม่ผ่าน:\n{r.stderr}")
        out = r.stdout.rstrip("\n")

        parts = [f"# {p['emoji']} {chapter_title} — ข้อ {i}: {p['name']}", "",
                 f"**Difficulty:** {DIFF[p['diff']]}", "", "---", "",
                 "## โจทย์", "", p["body"].strip(), "", "---", "",
                 p["io"].strip(), "", "---", "", "## ตัวอย่าง", ""]

        if p.get("stdin", ""):
            parts += ["**Input:**", "", "```text", p["stdin"].rstrip("\n"), "```", ""]
        parts += ["**Output:**", "", "```text", out, "```", "", "---", ""]

        if p.get("hint"):
            parts += ["## 💡 Hint", "", p["hint"].strip(), "", "---", ""]

        parts += ["## Starter Code", "", "```python", p["starter"].strip("\n"), "```"]

        mpath = os.path.join(chapter_dir, p["file"] + ".md")
        with open(mpath, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(parts) + "\n")
        made.append((i, p))

    return made


def write_index(chapter_dir, chapter_no, chapter_title, scope_line, forbid_line,
                made, notes):
    rows = []
    for i, p in made:
        rows.append(f"| {i} | `{p['file']}.md` | {DIFF[p['diff']][0]} | {p['name']} | {p['axis']} |")
    n_e = sum(1 for _, p in made if p["diff"] == "e")
    n_m = sum(1 for _, p in made if p["diff"] == "m")
    n_c = sum(1 for _, p in made if p["diff"] == "c")
    txt = f"""# 📋 สารบัญโจทย์ — บท {chapter_no} {chapter_title}

**ขอบเขตของบทนี้:** {scope_line}

> ❌ {forbid_line}

---

## ลำดับที่แนะนำ

| # | ไฟล์ | ระดับ | โจทย์ | แกนการคิด |
|---|------|-------|-------|-----------|
""" + "\n".join(rows) + f"""

**สรุป:** 🟢 Easy {n_e} ข้อ · 🟡 Medium {n_m} ข้อ · 🔴 Challenge {n_c} ข้อ = **{len(made)} ข้อ**

---

## หมายเหตุสำหรับครู

{notes.strip()}
"""
    with open(os.path.join(chapter_dir, "00_index.md"), "w",
              encoding="utf-8", newline="\n") as f:
        f.write(txt)
