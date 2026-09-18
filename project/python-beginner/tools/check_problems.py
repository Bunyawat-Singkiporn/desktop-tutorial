#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ตรวจโจทย์ในโฟลเดอร์ slide/ ของ python-beginner

ตรวจ 3 อย่าง
  1) FORMAT  - โจทย์มีส่วนประกอบครบตาม _PROBLEM_STANDARD.md
  2) RUN     - เฉลยรันได้ และ output ตรงกับตัวอย่างในโจทย์เป๊ะ
  3) SCOPE   - โจทย์/เฉลยไม่ใช้ syntax ที่ยังไม่เคยสอนในบทนั้น

วิธีใช้
  python check_problems.py <path/to/slide>              # ตรวจทุกบท
  python check_problems.py <path/to/slide> 013          # ตรวจบทเดียว
"""
import os, re, sys, subprocess

# ── ขอบเขต: feature -> บทแรกที่สอน ────────────────────────────────
# ถ้า feature โผล่ในบทที่เล็กกว่าเลขนี้ = เกินขอบเขต
FIRST_TAUGHT = {
    "print":        5,
    "variable":     5,
    "type()":       7,
    "bool":         7,
    "int()":        8,
    "float()":      8,
    "str()":        8,
    "input()":      8,
    "concat+":      8,
    "f-string":    10,
    ":.2f":        10,
    "sep=":        10,
    "end=":        10,
    "arith":       11,
    "//":          11,
    "%":           11,
    "**":          11,
    "compare":     11,
    "if":          13,
    "else":        13,
    "elif":        15,
    "and":         16,
    "or":          16,
    "not":         16,
    "for-range":   17,
    "list":        18,
    "for-in-list": 18,
    "len()":       18,
    "while":       19,
    "break":       20,
    "continue":    20,
    "index[]":     25,
    ".append()":   26,
    ".remove()":   26,
    ".sort()":     26,
    ".insert()":   26,
    ".pop()":      26,
    "tuple":       29,
    "set":         30,
    "dict":        33,
    ".values()":   34,
    ".items()":    34,
    ".keys()":     34,
    "del":         34,
    "def":         37,
    "return":      39,
    "global":      41,
    "sum()":       40,
}

# feature -> regex ที่ใช้จับในโค้ด python
PATTERNS = [
    ("elif",        r"^\s*elif\b"),
    ("else",        r"^\s*else\s*:"),
    ("if",          r"^\s*if\b"),
    ("and",         r"\band\b"),
    ("or",          r"\bor\b"),
    ("not",         r"\bnot\b"),
    ("for-range",   r"\bfor\s+\w+\s+in\s+range\("),
    ("for-in-list", r"\bfor\s+\w+\s+in\s+(?!range\()"),
    ("while",       r"^\s*while\b"),
    ("break",       r"^\s*break\b"),
    ("continue",    r"^\s*continue\b"),
    ("def",         r"^\s*def\b"),
    ("return",      r"^\s*return\b"),
    ("global",      r"^\s*global\b"),
    ("list",        r"=\s*\[|\[\s*\]"),
    ("dict",        r"=\s*\{.*:.*\}|\{\s*\}"),
    ("set",         r"\bset\("),
    ("tuple",       r"=\s*\([^)]*,[^)]*\)"),
    (".append()",   r"\.append\("),
    (".remove()",   r"\.remove\("),
    (".sort()",     r"\.sort\("),
    (".insert()",   r"\.insert\("),
    (".pop()",      r"\.pop\("),
    (".keys()",     r"\.keys\("),
    (".values()",   r"\.values\("),
    (".items()",    r"\.items\("),
    ("del",         r"^\s*del\b"),
    ("len()",       r"\blen\("),
    ("sum()",       r"\bsum\("),
    ("index[]",     r"\w\[\s*-?\d"),
    ("f-string",    r'f"|f\''),
    (":.2f",        r":\.\d+f"),
    ("sep=",        r"\bsep\s*="),
    ("end=",        r"\bend\s*="),
    ("input()",     r"\binput\("),
    ("int()",       r"\bint\("),
    ("float()",     r"\bfloat\("),
    ("str()",       r"\bstr\("),
    ("type()",      r"\btype\("),
    ("//",          r"//"),
    ("%",           r"%"),
    ("**",          r"\*\*"),
    ("compare",     r"==|!=|>=|<=|>|<"),
]

# สิ่งที่ไม่เคยสอนเลยในหลักสูตรนี้ -> ห้ามใช้ทุกบท
NEVER_TAUGHT = [
    (r"\btry\b|\bexcept\b",      "try/except"),
    (r"\.upper\(|\.lower\(",     ".upper()/.lower()"),
    (r"\.split\(|\.join\(",      ".split()/.join()"),
    (r"\.strip\(",               ".strip()"),
    (r"\bsorted\(",              "sorted()"),
    (r"\benumerate\(",           "enumerate()"),
    (r"\bzip\(",                 "zip()"),
    (r"\bround\(",               "round()"),
    (r"\bmin\(|\bmax\(",         "min()/max()"),
    (r"\babs\(",                 "abs()"),
    (r"\bimport\b",              "import"),
    (r"\blambda\b",              "lambda"),
    (r"for .* in .* if |\[.* for .* in .*\]", "list comprehension"),
    (r"\bf?\".*\{.*\bif\b.*\belse\b.*\}", "ternary in f-string"),
    (r"^\s*\w+\s*=.*\bif\b.*\belse\b", "ternary expression"),
    (r"\bTrue\s*:|\bwhile\s+True\b(?!.*#)", None),  # while True ok from 020, handled below
]

CODE_FENCE = re.compile(r"```(?:python)?\n(.*?)```", re.S)
TEXT_BLOCK = re.compile(r"```text\n(.*?)```", re.S)


def chapter_num(folder):
    m = re.match(r"(\d+)", folder)
    return int(m.group(1)) if m else 999


def scope_violations(code, chnum):
    bad = []
    for feat, pat in PATTERNS:
        if re.search(pat, code, re.M):
            need = FIRST_TAUGHT.get(feat)
            if need and chnum < need:
                bad.append(f"{feat} (สอนบท {need:03d})")
    for pat, name in NEVER_TAUGHT:
        if name and re.search(pat, code, re.M):
            bad.append(f"{name} (ไม่เคยสอนในหลักสูตร)")
    if re.search(r"\bwhile\s+True\b", code) and chnum < 20:
        bad.append("while True (สอนบท 020)")
    return bad


def parse_problem(path):
    src = open(path, encoding="utf-8").read()
    out = {"difficulty": None, "input": None, "output": None,
           "starter": None, "hint": "💡 Hint" in src, "title": None}
    m = re.search(r"^#\s+(.+)$", src, re.M)
    if m:
        out["title"] = m.group(1).strip()
    m = re.search(r"\*\*Difficulty:\*\*\s*(\S+)", src)
    if m:
        out["difficulty"] = m.group(1)

    # ตัวอย่างชุดแรก: **Input:** ... ```text ... ``` แล้วตามด้วย **Output:** ... ```text ... ```
    m = re.search(r"\*\*Input:\*\*\s*\n+```text\n(.*?)```", src, re.S)
    if m:
        out["input"] = m.group(1)
    m = re.search(r"\*\*Output:\*\*\s*\n+```text\n(.*?)```", src, re.S)
    if m:
        out["output"] = m.group(1)
    blocks = CODE_FENCE.findall(src)
    if blocks:
        out["starter"] = blocks[-1]
    out["raw"] = src
    return out


def check_chapter(slide_dir, folder):
    chnum = chapter_num(folder)
    d = os.path.join(slide_dir, folder)
    adir = os.path.join(d, "answer")
    probs = sorted(f for f in os.listdir(d)
                   if f.endswith(".md") and re.match(r"\d\d_", f)
                   and not re.match(r"01_", f)
                   and f != "00_index.md"
                   and "_range" not in f and "_readiness" not in f)
    # ตัดไฟล์บทเรียนที่เป็น 02_ ออก (เช่น 017/02_range.md) จัดการด้วย _range แล้ว
    answers = sorted(os.listdir(adir)) if os.path.isdir(adir) else []
    errs, warns = [], []

    if len(probs) < 15:
        errs.append(f"มีโจทย์ {len(probs)} ข้อ (ต้อง >= 15)")

    diffs = {"🟢": 0, "🟡": 0, "🔴": 0}
    seen_titles = []

    for p in probs:
        pp = os.path.join(d, p)
        info = parse_problem(pp)
        tag = f"{folder}/{p}"

        if not info["difficulty"]:
            errs.append(f"{tag}: ไม่มีบรรทัด **Difficulty:**")
        else:
            for k in diffs:
                if k in info["difficulty"]:
                    diffs[k] += 1
        if info["output"] is None:
            errs.append(f"{tag}: ไม่มีตัวอย่าง Output แบบ ```text block")
        if info["title"]:
            seen_titles.append(info["title"])

        # scope ของ starter code
        if info["starter"]:
            for v in scope_violations(info["starter"], chnum):
                errs.append(f"{tag}: starter ใช้ {v}")

        # hint ต้องไม่ใช่โค้ดเฉลย
        mh = re.search(r"##\s*💡 Hint\n(.*?)(?=\n---|\n##|\Z)", info["raw"], re.S)
        if mh:
            hint = mh.group(1)
            if re.search(r"^\s*(if|else|for|while)\b.*:", hint, re.M):
                warns.append(f"{tag}: Hint มีโครงโค้ดเต็มบรรทัด อาจกลายเป็นเฉลย")

        # หาไฟล์เฉลยที่ขึ้นต้นด้วยเลขเดียวกัน
        num = p[:2]
        cand = [a for a in answers if a.startswith(num) and a.endswith(".py")]
        if not cand:
            errs.append(f"{tag}: ไม่มีไฟล์เฉลยขึ้นต้นด้วย {num} ใน answer/")
            continue
        if len(cand) > 1:
            errs.append(f"{tag}: มีไฟล์เฉลยขึ้นต้นด้วย {num} มากกว่า 1 ไฟล์ {cand} "
                        f"— น่าจะเป็นไฟล์เก่าค้าง ให้ลบทิ้ง")
            continue
        apath = os.path.join(adir, cand[0])
        code = open(apath, encoding="utf-8").read()
        for v in scope_violations(code, chnum):
            errs.append(f"{folder}/answer/{cand[0]}: ใช้ {v}")

        if info["output"] is not None:
            stdin = info["input"] if info["input"] is not None else ""
            try:
                r = subprocess.run([sys.executable, apath], input=stdin,
                                   capture_output=True, text=True, timeout=10)
            except subprocess.TimeoutExpired:
                errs.append(f"{folder}/answer/{cand[0]}: รันไม่จบ (timeout)")
                continue
            if r.returncode != 0:
                errs.append(f"{folder}/answer/{cand[0]}: รันแล้ว error -> "
                            f"{r.stderr.strip().splitlines()[-1] if r.stderr.strip() else '?'}")
                continue
            got = r.stdout.rstrip("\n")
            want = info["output"].rstrip("\n")
            if got != want:
                errs.append(f"{folder}/answer/{cand[0]}: output ไม่ตรงตัวอย่าง\n"
                            f"      ได้  : {got!r}\n      ควรได้: {want!r}")

    if diffs["🟢"] < 4 or diffs["🟡"] < 5 or diffs["🔴"] < 3:
        warns.append(f"{folder}: สัดส่วนความยาก 🟢{diffs['🟢']} 🟡{diffs['🟡']} 🔴{diffs['🔴']} "
                     f"(แนะนำ 5 / 6 / 4)")
    dup = {t for t in seen_titles if seen_titles.count(t) > 1}
    if dup:
        errs.append(f"{folder}: ชื่อโจทย์ซ้ำ {dup}")

    return len(probs), errs, warns


def main():
    slide_dir = sys.argv[1]
    only = sys.argv[2] if len(sys.argv) > 2 else None
    folders = sorted(f for f in os.listdir(slide_dir)
                     if os.path.isdir(os.path.join(slide_dir, f)) and re.match(r"\d\d\d-", f))
    if only:
        folders = [f for f in folders if f.startswith(only)]

    total_err = 0
    for f in folders:
        n, errs, warns = check_chapter(slide_dir, f)
        status = "OK  " if not errs else "FAIL"
        print(f"[{status}] {f}  ({n} ข้อ)")
        for e in errs:
            print(f"    ✗ {e}")
        for w in warns:
            print(f"    ! {w}")
        total_err += len(errs)

    print()
    print(f"สรุป: {len(folders)} บท, ข้อผิดพลาด {total_err} รายการ")
    return 1 if total_err else 0


if __name__ == "__main__":
    sys.exit(main())
