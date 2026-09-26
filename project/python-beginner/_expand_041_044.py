# -*- coding: utf-8 -*-
"""Expand weeks 041-044 to 15-problem standard."""
from __future__ import annotations

from _expand_helpers import write_week

NO_IN = "ไม่มี (กำหนดค่าในโปรแกรม)"
HAS_IN = "ดูตัวอย่าง"


def p(n, title, slug, body, out_desc, sample_out, starter, answer, hint=None, sample_in=None, in_desc=None):
    return {
        "n": n, "title": title, "slug": slug, "body": body,
        "input_desc": in_desc if in_desc is not None else (HAS_IN if sample_in is not None else NO_IN),
        "output_desc": out_desc,
        "sample_input": sample_in,
        "sample_output": sample_out,
        "hint": hint, "starter": starter, "answer": answer,
    }


def idx(title, scope, bans, rows, notes=""):
    table = "\n".join(
        f"| {i} | `{f}` | {lv} | {t} | {ax} |"
        for i, (f, lv, t, ax) in enumerate(rows, 1)
    )
    return f"""# 📋 สารบัญโจทย์ — {title}

**ขอบเขตของบทนี้:** {scope}

> ❌ {bans}

---

## ลำดับที่แนะนำ

| # | ไฟล์ | ระดับ | โจทย์ | แกนการคิด |
|---|------|-------|-------|-----------|
{table}

**สรุป:** 🟢 Easy 5 ข้อ · 🟡 Medium 6 ข้อ · 🔴 Challenge 4 ข้อ = **15 ข้อ**

---

## หมายเหตุสำหรับครู

{notes}
"""


FILES = [
    ("02_test.md", "🟢"), ("03_test.md", "🟢"), ("04_test.md", "🟢"),
    ("08_easy.md", "🟢"), ("09_easy.md", "🟢"),
    ("06_medium.md", "🟡"), ("07_medium.md", "🟡"), ("10_medium.md", "🟡"),
    ("11_medium.md", "🟡"), ("12_medium.md", "🟡"), ("13_medium.md", "🟡"),
    ("05_challenge.md", "🔴"), ("14_challenge.md", "🔴"),
    ("15_challenge.md", "🔴"), ("16_challenge.md", "🔴"),
]


def rows(items):
    return [(f, lv, t, ax) for (f, lv), (t, ax) in zip(FILES, items)]


# ───────── 041 scope / global ─────────
def week_041():
    items = [
        ("อ่านชื่อ global", "อ่านตัวแปรนอกฟังก์ชัน"),
        ("local ทับชื่อ", "shadowing"),
        ("คืนค่าจาก local", "return ค่าในฟังก์ชัน"),
        ("นับด้วย global", "global + แก้ค่า"),
        ("อ่านราคาเมนู", "global อ่านอย่างเดียว"),
        ("ภาษีจากเรทนอก", "อ่าน global ในคำนวณ"),
        ("เพิ่มคะแนนทีม", "global สะสม"),
        ("สวิตช์ไฟ", "global bool"),
        ("เติมเงินกระเป๋า", "global ตัวเลข"),
        ("ตั้งชื่อเล่น", "global สตริง"),
        ("นับรอบเกม", "เรียกซ้ำกับ global"),
        ("ยอดขายร้าน", "global + หลายฟังก์ชัน"),
        ("โหมดเงียบ", "global flag"),
        ("คลังไอเทม", "global list"),
        ("รีเซ็ตคะแนน", "global ตั้งค่าใหม่"),
    ]
    index = idx(
        "บท 041 Scope",
        "local vs global · อ่านตัวแปรนอกฟังก์ชัน · keyword `global` · ความรู้ถึง 040",
        "ห้าม `nonlocal` · ห้ามใช้ global โดยไม่จำเป็นในทุกข้อ",
        rows(items),
        "ข้อ 02 ห้าม copy ตัวอย่าง Alice ในบทเรียนเป๊ะ — เปลี่ยนชื่อ/สถานการณ์",
    )
    probs = [
        p(2, "อ่านชื่อ global", "read_global_name",
          "มีชื่อร้านเป็นตัวแปรนอกฟังก์ชัน\n\n**เงื่อนไข:**\n\n- มี `shop = \"Bean House\"` นอกฟังก์ชัน\n- สร้าง `show_shop()` พิมพ์ `Shop: <shop>` โดยอ่านค่า global\n- เรียก 1 ครั้ง",
          "1 บรรทัด", "Shop: Bean House",
          'shop = "Bean House"\n\ndef show_shop():\n    # พิมพ์ Shop: ...\n    ...\n\nshow_shop()',
          'shop = "Bean House"\n\ndef show_shop():\n    print(f"Shop: {shop}")\n\nshow_shop()'),
        p(3, "local ทับชื่อ", "shadow_x",
          "ตัวแปรชื่อเดียวกันคนละที่\n\n**เงื่อนไข:**\n\n- นอกฟังก์ชัน `x = 100`\n- ใน `demo()` ตั้ง `x = 50` แล้วพิมพ์ `Inside: 50`\n- หลังเรียกฟังก์ชันพิมพ์ `Outside: 100`",
          "2 บรรทัด", "Inside: 50\nOutside: 100",
          "x = 100\n\ndef demo():\n    # local x\n    ...\n\ndemo()\nprint(f\"Outside: {x}\")",
          'x = 100\n\ndef demo():\n    x = 50\n    print(f"Inside: {x}")\n\ndemo()\nprint(f"Outside: {x}")'),
        p(4, "คืนค่าจาก local", "return_local",
          "คำนวณในฟังก์ชันแล้วส่งค่าออก\n\n**เงื่อนไข:**\n\n- สร้าง `calc()` มี `result = 42` แล้ว return result\n- เก็บค่าใน `value` แล้วพิมพ์",
          "1 บรรทัด", "42",
          "def calc():\n    # return ค่าในฟังก์ชัน\n    ...\n\nvalue = calc()\nprint(value)",
          "def calc():\n    result = 42\n    return result\n\nvalue = calc()\nprint(value)"),
        p(8, "นับด้วย global", "global_count",
          "นับครั้งที่กดปุ่ม\n\n**เงื่อนไข:**\n\n- มี `count = 0` นอกฟังก์ชัน\n- `add_one()` ใช้ `global count` แล้ว `count += 1`\n- เรียก 2 ครั้ง แล้วพิมพ์ count",
          "1 บรรทัด", "2",
          "count = 0\n\ndef add_one():\n    # ใช้ global\n    ...\n\nadd_one()\nadd_one()\nprint(count)",
          "count = 0\n\ndef add_one():\n    global count\n    count += 1\n\nadd_one()\nadd_one()\nprint(count)"),
        p(9, "อ่านราคาเมนู", "menu_price",
          "ราคาเมนูอยู่ข้างนอกฟังก์ชัน\n\n**เงื่อนไข:**\n\n- `price = 45`\n- `show_price()` พิมพ์ `Price: 45`\n- เรียก 1 ครั้ง",
          "1 บรรทัด", "Price: 45",
          "price = 45\n\ndef show_price():\n    # อ่าน price\n    ...\n\nshow_price()",
          'price = 45\n\ndef show_price():\n    print(f"Price: {price}")\n\nshow_price()'),
        p(6, "ภาษีจากเรทนอก", "tax_rate_global",
          "อัตราภาษีเก็บเป็น global\n\n**เงื่อนไข:**\n\n- `TAX = 0.07`\n- `with_tax(amount)` คืน amount * (1 + TAX)\n- พิมพ์ผลของ `100` ทศนิยม 2 ตำแหน่ง",
          "1 บรรทัด", "107.00",
          "TAX = 0.07\n\ndef with_tax(amount):\n    # ใช้ TAX\n    ...\n\nprint(f\"{with_tax(100):.2f}\")",
          "TAX = 0.07\n\ndef with_tax(amount):\n    return amount * (1 + TAX)\n\nprint(f\"{with_tax(100):.2f}\")",
          "อ่าน TAX ได้โดยไม่ต้อง global ถ้าไม่แก้ค่า"),
        p(7, "เพิ่มคะแนนทีม", "team_score",
          "คะแนนทีมสะสมนอกฟังก์ชัน\n\n**เงื่อนไข:**\n\n- `score = 0`\n- `add_points(n)` ใช้ global เพิ่มคะแนน\n- เรียก `add_points(3)` แล้ว `add_points(5)` พิมพ์ score",
          "1 บรรทัด", "8",
          "score = 0\n\ndef add_points(n):\n    # global score\n    ...\n\nadd_points(3)\nadd_points(5)\nprint(score)",
          "score = 0\n\ndef add_points(n):\n    global score\n    score += n\n\nadd_points(3)\nadd_points(5)\nprint(score)",
          "ต้องมีบรรทัด global score"),
        p(10, "สวิตช์ไฟ", "light_switch",
          "สถานะไฟเป็น global bool\n\n**เงื่อนไข:**\n\n- `is_on = False`\n- `turn_on()` ตั้ง is_on เป็น True ด้วย global\n- เรียก turn_on แล้วพิมพ์ is_on",
          "1 บรรทัด", "True",
          "is_on = False\n\ndef turn_on():\n    # global\n    ...\n\nturn_on()\nprint(is_on)",
          "is_on = False\n\ndef turn_on():\n    global is_on\n    is_on = True\n\nturn_on()\nprint(is_on)",
          "แก้ bool ด้วย global"),
        p(11, "เติมเงินกระเป๋า", "wallet_global",
          "เงินในกระเป๋าเป็น global\n\n**เงื่อนไข:**\n\n- `money = 100`\n- `deposit(n)` เพิ่มเงินด้วย global\n- เติม 50 แล้วพิมพ์ money",
          "1 บรรทัด", "150",
          "money = 100\n\ndef deposit(n):\n    # global\n    ...\n\ndeposit(50)\nprint(money)",
          "money = 100\n\ndef deposit(n):\n    global money\n    money += n\n\ndeposit(50)\nprint(money)",
          "global ก่อนแก้ค่า"),
        p(12, "ตั้งชื่อเล่น", "nickname_global",
          "เปลี่ยนชื่อเล่นในโปรไฟล์\n\n**เงื่อนไข:**\n\n- `nickname = \"Guest\"`\n- `set_nick(name)` ตั้งค่าใหม่ด้วย global\n- ตั้งเป็น `\"Ace\"` แล้วพิมพ์ nickname",
          "1 บรรทัด", "Ace",
          'nickname = "Guest"\n\ndef set_nick(name):\n    # global\n    ...\n\nset_nick("Ace")\nprint(nickname)',
          'nickname = "Guest"\n\ndef set_nick(name):\n    global nickname\n    nickname = name\n\nset_nick("Ace")\nprint(nickname)',
          "กำหนดค่าใหม่ทั้งก้อน"),
        p(13, "นับรอบเกม", "round_counter",
          "นับรอบที่เล่น\n\n**เงื่อนไข:**\n\n- `rounds = 0`\n- `next_round()` เพิ่ม 1 ด้วย global และพิมพ์ `Round: <rounds>`\n- เรียก 3 ครั้ง",
          "3 บรรทัด", "Round: 1\nRound: 2\nRound: 3",
          "rounds = 0\n\ndef next_round():\n    # global + print\n    ...\n\nnext_round()\nnext_round()\nnext_round()",
          'rounds = 0\n\ndef next_round():\n    global rounds\n    rounds += 1\n    print(f"Round: {rounds}")\n\nnext_round()\nnext_round()\nnext_round()',
          "เพิ่มก่อนพิมพ์"),
        p(5, "ยอดขายร้าน", "sales_total",
          "ยอดขายสะสมของร้าน\n\n**เงื่อนไข:**\n\n- `total = 0`\n- `sell(price)` เพิ่มยอดด้วย global\n- `show_total()` พิมพ์ `Total: ...`\n- ขาย 30 กับ 45 แล้ว show",
          "1 บรรทัด", "Total: 75",
          "total = 0\n\ndef sell(price):\n    # global\n    ...\n\ndef show_total():\n    # พิมพ์ยอด\n    ...\n\nsell(30)\nsell(45)\nshow_total()",
          'total = 0\n\ndef sell(price):\n    global total\n    total += price\n\ndef show_total():\n    print(f"Total: {total}")\n\nsell(30)\nsell(45)\nshow_total()',
          "show อ่านอย่างเดียว ไม่ต้อง global"),
        p(14, "โหมดเงียบ", "quiet_mode",
          "สลับโหมดเงียบ\n\n**เงื่อนไข:**\n\n- `quiet = False`\n- `toggle()` สลับค่า quiet ด้วย global (True↔False)\n- เรียก toggle แล้วพิมพ์ quiet แล้ว toggle อีกครั้งแล้วพิมพ์อีก",
          "2 บรรทัด", "True\nFalse",
          "quiet = False\n\ndef toggle():\n    # สลับค่า\n    ...\n\ntoggle()\nprint(quiet)\ntoggle()\nprint(quiet)",
          "quiet = False\n\ndef toggle():\n    global quiet\n    if quiet:\n        quiet = False\n    else:\n        quiet = True\n\ntoggle()\nprint(quiet)\ntoggle()\nprint(quiet)",
          "สลับด้วย if หรือ not"),
        p(15, "คลังไอเทม", "inventory_global",
          "คลังไอเทมเป็น list global\n\n**เงื่อนไข:**\n\n- `items = []`\n- `add_item(name)` append ด้วย global\n- เพิ่ม Potion กับ Sword แล้วพิมพ์ items",
          "1 บรรทัด", "['Potion', 'Sword']",
          "items = []\n\ndef add_item(name):\n    # global\n    ...\n\nadd_item(\"Potion\")\nadd_item(\"Sword\")\nprint(items)",
          'items = []\n\ndef add_item(name):\n    global items\n    items.append(name)\n\nadd_item("Potion")\nadd_item("Sword")\nprint(items)',
          "append บน list global"),
        p(16, "รีเซ็ตคะแนน", "reset_score",
          "รีเซ็ตคะแนนเกม\n\n**เงื่อนไข:**\n\n- `score = 50`\n- `bonus()` เพิ่ม 10 ด้วย global\n- `reset()` ตั้ง score เป็น 0 ด้วย global\n- เรียก bonus แล้ว reset แล้วพิมพ์ score",
          "1 บรรทัด", "0",
          "score = 50\n\ndef bonus():\n    # +10\n    ...\n\ndef reset():\n    # ตั้ง 0\n    ...\n\nbonus()\nreset()\nprint(score)",
          "score = 50\n\ndef bonus():\n    global score\n    score += 10\n\ndef reset():\n    global score\n    score = 0\n\nbonus()\nreset()\nprint(score)",
          "reset ทับค่าทั้งก้อน"),
    ]
    for i, pr in enumerate(probs):
        probs[i] = dict(pr)
        probs[i]["starter"] = pr["starter"].replace("    ...\n", "")
    write_week("041-scope", chapter="Scope", emoji="🔭", index_md=index, problems=probs)


# ───────── 042 debugging — no try/except ─────────
def week_042():
    items = [
        ("เติม colon ที่หาย", "SyntaxError"),
        ("กันหารศูนย์", "ป้องกัน Runtime"),
        ("แก้ index เกิน", "IndexError"),
        ("แปลงก่อนบวก", "TypeError"),
        ("แก้ยอดรวมในลูป", "LogicError"),
        ("ใส่ print ดีบัก", "debug print"),
        ("ตรวจความยาว list", "กัน IndexError"),
        ("ตรวจตัวหารก่อน", "กัน ZeroDivision"),
        ("แก้เงื่อนไขกลับด้าน", "Logic"),
        ("แก้ชื่อตัวแปรผิด", "NameError แนวคิด"),
        ("หาผลรวมช่วงถูก", "Logic สะสม"),
        ("รายงานบั๊กสามชนิด", "แยกประเภท"),
        ("ซ่อมฟังก์ชันคูณ", "ใส่ขั้นตอน"),
        ("กัน list ว่าง", "ป้องกันก่อนใช้"),
        ("ดีบักใบเสร็จผิดยอด", "หาจุดผิด"),
    ]
    index = idx(
        "บท 042 Debugging",
        "แยก Syntax / Runtime / Logic · ป้องกัน error ด้วยเงื่อนไข · ใส่ print ตรวจค่า · ความรู้ถึง 041",
        "ห้าม `try` / `except` เด็ดขาด",
        rows(items),
        "โจทย์คือแก้หรือป้องกันบั๊ก ไม่ใช่จับ error",
    )
    probs = [
        p(2, "เติม colon ที่หาย", "fix_colon",
          "โค้ดเช็กคะแนนขาดเครื่องหมาย `:`\n\n**เงื่อนไข:**\n\n- รับคะแนนหนึ่งค่า\n- ถ้า >= 50 พิมพ์ `Pass` ไม่งั้น `Fail`\n- เขียน if ให้ถูกต้อง",
          "1 บรรทัด", "Pass",
          "score = int(input())\n\n# เขียน if/else ให้ถูก",
          'score = int(input())\nif score >= 50:\n    print("Pass")\nelse:\n    print("Fail")',
          sample_in="60"),
        p(3, "กันหารศูนย์", "safe_div",
          "หารตัวเลขสองค่า แต่ห้ามให้โปรแกรมพังเมื่อตัวหารเป็น 0\n\n**เงื่อนไข:**\n\n- รับ a และ b\n- ถ้า b == 0 พิมพ์ `Cannot divide`\n- ไม่งั้นพิมพ์ผล `a / b` ทศนิยม 1 ตำแหน่ง",
          "1 บรรทัด", "Cannot divide",
          "a = int(input())\nb = int(input())\n\n# กันหารศูนย์",
          'a = int(input())\nb = int(input())\nif b == 0:\n    print("Cannot divide")\nelse:\n    print(f"{a / b:.1f}")',
          sample_in="10\n0", hint="เช็ก b ก่อนหาร"),
        p(4, "แก้ index เกิน", "safe_index",
          "อ่านสมาชิกใน list แต่ต้องไม่เกินขอบ\n\n**เงื่อนไข:**\n\n- มี `nums = [10, 20, 30]`\n- รับ index เป็นจำนวนเต็ม\n- ถ้า index อยู่ระหว่าง 0 ถึง len-1 พิมพ์ค่า ไม่งั้นพิมพ์ `Out of range`",
          "1 บรรทัด", "Out of range",
          "nums = [10, 20, 30]\nindex = int(input())\n\n# เช็กขอบเขตก่อน",
          'nums = [10, 20, 30]\nindex = int(input())\nif index >= 0 and index < len(nums):\n    print(nums[index])\nelse:\n    print("Out of range")',
          sample_in="5", hint="เทียบกับ len(nums)"),
        p(8, "แปลงก่อนบวก", "fix_type",
          "ผู้ใช้พิมพ์ตัวเลขเป็นข้อความ ต้องแปลงก่อนบวก\n\n**เงื่อนไข:**\n\n- รับสองบรรทัดเป็นข้อความตัวเลข\n- แปลงเป็น int แล้วพิมพ์ผลบวก",
          "1 บรรทัด", "8",
          "a = input()\nb = input()\n\n# แปลงแล้วบวก",
          "a = input()\nb = input()\nprint(int(a) + int(b))",
          sample_in="3\n5"),
        p(9, "แก้ยอดรวมในลูป", "fix_total_loop",
          "โค้ดเดิมใช้ `total = i` ทำให้ได้ผลผิด ต้องเป็นสะสม\n\n**เงื่อนไข:**\n\n- รวมเลข 1 ถึง 4 ด้วยลูป\n- พิมพ์ผลรวมที่ถูกต้อง (10)",
          "1 บรรทัด", "10",
          "total = 0\nfor i in range(1, 5):\n    # แก้ให้สะสมถูก\n    ...\nprint(total)",
          "total = 0\nfor i in range(1, 5):\n    total += i\nprint(total)"),
        p(6, "ใส่ print ดีบัก", "debug_prints",
          "ฟังก์ชันคูณสองค่า ให้พิมพ์ค่าก่อนคูณเพื่อตรวจ\n\n**เงื่อนไข:**\n\n- สร้าง `calc(x, y)` พิมพ์ `x=<x>` และ `y=<y>` แล้วพิมพ์ `result=<x*y>`\n- เรียก `calc(3, 4)`",
          "3 บรรทัด", "x=3\ny=4\nresult=12",
          "def calc(x, y):\n    # พิมพ์ debug แล้วผล\n    ...\n\ncalc(3, 4)",
          'def calc(x, y):\n    print(f"x={x}")\n    print(f"y={y}")\n    print(f"result={x * y}")\n\ncalc(3, 4)',
          "พิมพ์ค่าก่อนคำนวณ"),
        p(7, "ตรวจความยาว list", "check_len_first",
          "จะอ่านสมาชิกตัวสุดท้าย ต้องมีข้อมูลก่อน\n\n**เงื่อนไข:**\n\n- รับ n แล้วอ่าน n จำนวนเต็มเก็บใน list\n- ถ้า list ว่างพิมพ์ `Empty` ไม่งั้นพิมพ์ตัวสุดท้าย",
          "1 บรรทัด", "Empty",
          "n = int(input())\nnums = []\nfor i in range(n):\n    nums.append(int(input()))\n\n# เช็กว่าง",
          'n = int(input())\nnums = []\nfor i in range(n):\n    nums.append(int(input()))\nif len(nums) == 0:\n    print("Empty")\nelse:\n    print(nums[-1])',
          sample_in="0", hint="ดู len ก่อนใช้ index"),
        p(10, "ตรวจตัวหารก่อน", "safe_avg",
          "หาค่าเฉลี่ยจากจำนวนชิ้น\n\n**เงื่อนไข:**\n\n- รับ total และ count\n- ถ้า count == 0 พิมพ์ `No data`\n- ไม่งั้นพิมพ์ average ทศนิยม 1 ตำแหน่ง",
          "1 บรรทัด", "No data",
          "total = int(input())\ncount = int(input())\n\n# กันหารศูนย์",
          'total = int(input())\ncount = int(input())\nif count == 0:\n    print("No data")\nelse:\n    print(f"{total / count:.1f}")',
          sample_in="100\n0", hint="เช็ก count ก่อน"),
        p(11, "แก้เงื่อนไขกลับด้าน", "fix_condition",
          "ประตูเปิดเมื่ออายุ >= 12 แต่โค้ดเคยเขียนกลับ\n\n**เงื่อนไข:**\n\n- รับอายุ\n- ถ้า >= 12 พิมพ์ `Enter` ไม่งั้น `Wait`",
          "1 บรรทัด", "Enter",
          "age = int(input())\n\n# เงื่อนไขให้ถูก",
          'age = int(input())\nif age >= 12:\n    print("Enter")\nelse:\n    print("Wait")',
          sample_in="15", hint="อย่าสลับ Enter/Wait"),
        p(12, "แก้ชื่อตัวแปรผิด", "fix_nameerror",
          "พิมพ์ราคาสุทธิจากตัวแปรที่ตั้งชื่อไว้\n\n**เงื่อนไข:**\n\n- มี `price = 120` และ `discount = 20`\n- คำนวณ `final_price` แล้วพิมพ์ `Pay: <final_price>`\n- อย่าพิมพ์ชื่อตัวแปรผิด",
          "1 บรรทัด", "Pay: 100",
          "price = 120\ndiscount = 20\n\n# คำนวณแล้วพิมพ์",
          'price = 120\ndiscount = 20\nfinal_price = price - discount\nprint(f"Pay: {final_price}")',
          "ใช้ชื่อให้ตรงกับที่ประกาศ"),
        p(13, "หาผลรวมช่วงถูก", "sum_range_fix",
          "ต้องการผลรวม 2+3+4\n\n**เงื่อนไข:**\n\n- ใช้ลูป range ให้ได้ผลรวม 9\n- พิมพ์ผลรวม",
          "1 บรรทัด", "9",
          "total = 0\n# ลูปให้ได้ 2+3+4\nprint(total)",
          "total = 0\nfor i in range(2, 5):\n    total += i\nprint(total)",
          "ระวัง stop ของ range"),
        p(5, "รายงานบั๊กสามชนิด", "bug_labels",
          "จำแนกประเภทบั๊กจากคำอธิบายสั้นๆ ที่กำหนดในโค้ด\n\n**เงื่อนไข:**\n\n- มี list `labels = [\"Syntax\", \"Runtime\", \"Logic\"]`\n- รับหมายเลข 0/1/2 แล้วพิมพ์ป้ายนั้น\n- ถ้าไม่อยู่ในช่วงพิมพ์ `Unknown`",
          "1 บรรทัด", "Runtime",
          'labels = ["Syntax", "Runtime", "Logic"]\ncode = int(input())\n\n# เลือกป้าย',
          'labels = ["Syntax", "Runtime", "Logic"]\ncode = int(input())\nif code >= 0 and code < len(labels):\n    print(labels[code])\nelse:\n    print("Unknown")',
          sample_in="1", hint="เช็กช่วงก่อน index"),
        p(14, "ซ่อมฟังก์ชันคูณ", "fix_mul_fn",
          "ฟังก์ชันควรคืนผลคูณ แต่เดิมพิมพ์อย่างเดียว\n\n**เงื่อนไข:**\n\n- สร้าง `mul(a, b)` ที่ return a*b\n- พิมพ์ผลของ `mul(6, 7)`",
          "1 บรรทัด", "42",
          "def mul(a, b):\n    # ต้อง return\n    ...\n\nprint(mul(6, 7))",
          "def mul(a, b):\n    return a * b\n\nprint(mul(6, 7))",
          "ใช้ return ไม่ใช่แค่ print"),
        p(15, "กัน list ว่าง", "guard_empty_avg",
          "หาค่าเฉลี่ยคะแนน ต้องกัน list ว่าง\n\n**เงื่อนไข:**\n\n- สร้าง `safe_avg(scores)` ถ้า len เป็น 0 คืน 0 ไม่งั้นคืน sum/len\n- พิมพ์ผลของ `[]` และ `[10, 20]`",
          "2 บรรทัด", "0\n15.0",
          "def safe_avg(scores):\n    # กันว่าง\n    ...\n\nprint(safe_avg([]))\nprint(safe_avg([10, 20]))",
          "def safe_avg(scores):\n    if len(scores) == 0:\n        return 0\n    else:\n        return sum(scores) / len(scores)\n\nprint(safe_avg([]))\nprint(safe_avg([10, 20]))",
          "เช็ก len ก่อนหาร"),
        p(16, "ดีบักใบเสร็จผิดยอด", "debug_receipt",
          "ใบเสร็จมียอดผิดเพราะลืมบวกตัวสุดท้ายในลูป — ให้รวมให้ถูก\n\n**เงื่อนไข:**\n\n- มี `prices = [40, 60, 25]`\n- สร้าง `total_of(prices)` คืนผลรวม\n- พิมพ์ผลรวม",
          "1 บรรทัด", "125",
          "def total_of(prices):\n    # รวมให้ครบ\n    ...\n\nprint(total_of([40, 60, 25]))",
          "def total_of(prices):\n    total = 0\n    for p in prices:\n        total += p\n    return total\n\nprint(total_of([40, 60, 25]))",
          "วนทุกตัวแล้วบวก"),
    ]
    for i, pr in enumerate(probs):
        probs[i] = dict(pr)
        probs[i]["starter"] = pr["starter"].replace("    ...\n", "")
    write_week("042-debugging", chapter="Debugging", emoji="🐛", index_md=index, problems=probs)


# ───────── 043 readability ─────────
def week_043():
    items = [
        ("ตั้งชื่อคะแนนให้ชัด", "meaningful names"),
        ("ใช้ค่าคงที่ ALL_CAPS", "DISCOUNT_RATE"),
        ("เก็บผลเปรียบเทียบ", "is_x = ..."),
        ("เปลี่ยนเป็น f-string", "เลิก + concat"),
        ("แยกเป็นฟังก์ชัน", "แยกงาน"),
        ("ใบเสร็จชื่อดี", "ชื่อตัวแปร"),
        ("เกณฑ์ผ่านชัดเจน", "is_passed"),
        ("ค่าคงที่ค่าส่ง", "SHIPPING_FEE"),
        ("คอมเมนต์เท่าที่จำเป็น", "ไม่คอมเมนต์ซ้ำ"),
        ("ฟังก์ชันคำนวณยอด", "get_total"),
        ("ป้ายสถานะอ่านง่าย", "ชื่อสื่อความ"),
        ("รีแฟกเตอร์บิลยาว", "แยกฟังก์ชัน"),
        ("ค่าคงที่หลายตัว", "หลาย ALL_CAPS"),
        ("โปรไฟล์สั้นชัด", "ชื่อ+ f-string"),
        ("รายงานสะอาด", "ประกอบแนวทาง"),
    ]
    index = idx(
        "บท 043 Code Readability",
        "ชื่อสื่อความ · ALL_CAPS ค่าคงที่ · `is_x = เปรียบเทียบ` · f-string · แยกฟังก์ชัน · ความรู้ถึง 042",
        "ห้ามเพิ่ม syntax ใหม่นอกขอบเขต",
        rows(items),
        "เน้นอ่านง่าย ไม่ใช่โจทย์อัลกอริทึมหนัก",
    )
    probs = [
        p(2, "ตั้งชื่อคะแนนให้ชัด", "rename_score",
          "มีคะแนน 75 ตรวจผ่านเกณฑ์ 50\n\n**เงื่อนไข:**\n\n- ใช้ชื่อ `score` และ `is_passed`\n- พิมพ์ `Passed` หรือ `Not passed`",
          "1 บรรทัด", "Passed",
          "score = 75\nis_passed = score >= 50\n\n# พิมพ์ตาม is_passed",
          'score = 75\nis_passed = score >= 50\nif is_passed:\n    print("Passed")\nelse:\n    print("Not passed")'),
        p(3, "ใช้ค่าคงที่ ALL_CAPS", "discount_const",
          "คำนวณราคาหลังลดด้วยอัตราคงที่\n\n**เงื่อนไข:**\n\n- ตั้ง `DISCOUNT_RATE = 0.1`\n- `price = 200`\n- พิมพ์ `Final: <price * (1 - DISCOUNT_RATE)>` ทศนิยม 1 ตำแหน่ง",
          "1 บรรทัด", "Final: 180.0",
          "DISCOUNT_RATE = 0.1\nprice = 200\n\n# คำนวณแล้วพิมพ์",
          'DISCOUNT_RATE = 0.1\nprice = 200\nfinal_price = price * (1 - DISCOUNT_RATE)\nprint(f"Final: {final_price:.1f}")'),
        p(4, "เก็บผลเปรียบเทียบ", "is_adult",
          "ตรวจอายุผู้ใหญ่\n\n**เงื่อนไข:**\n\n- รับอายุ\n- เก็บ `is_adult = age >= 18`\n- ถ้า True พิมพ์ `Adult` ไม่งั้น `Minor`",
          "1 บรรทัด", "Adult",
          "age = int(input())\nis_adult = age >= 18\n\n# ใช้ is_adult",
          'age = int(input())\nis_adult = age >= 18\nif is_adult:\n    print("Adult")\nelse:\n    print("Minor")',
          sample_in="20"),
        p(8, "เปลี่ยนเป็น f-string", "to_fstring",
          "มี name และ age ให้พิมพ์ด้วย f-string\n\n**เงื่อนไข:**\n\n- `name = \"Rin\"` `age = 14`\n- พิมพ์ `Name: Rin, Age: 14` ด้วย f-string",
          "1 บรรทัด", "Name: Rin, Age: 14",
          'name = "Rin"\nage = 14\n\n# ใช้ f-string',
          'name = "Rin"\nage = 14\nprint(f"Name: {name}, Age: {age}")'),
        p(9, "แยกเป็นฟังก์ชัน", "split_sum_fn",
          "รวมเลข 1 ถึง n ในฟังก์ชัน\n\n**เงื่อนไข:**\n\n- สร้าง `get_sum(n)` คืนผลรวม 1..n\n- พิมพ์ผลของ `5`",
          "1 บรรทัด", "15",
          "def get_sum(n):\n    # รวม 1..n\n    ...\n\nprint(get_sum(5))",
          "def get_sum(n):\n    total = 0\n    for i in range(1, n + 1):\n        total += i\n    return total\n\nprint(get_sum(5))"),
        p(6, "ใบเสร็จชื่อดี", "receipt_names",
          "ใบเสร็จใช้ชื่อตัวแปรสื่อความ\n\n**เงื่อนไข:**\n\n- `item_name = \"Notebook\"` `unit_price = 45` `quantity = 2`\n- พิมพ์ `Notebook x2 = 90`",
          "1 บรรทัด", "Notebook x2 = 90",
          'item_name = "Notebook"\nunit_price = 45\nquantity = 2\n\n# พิมพ์ใบเสร็จสั้น',
          'item_name = "Notebook"\nunit_price = 45\nquantity = 2\nprint(f"{item_name} x{quantity} = {unit_price * quantity}")',
          "คูณราคาต่อชิ้นกับจำนวน"),
        p(7, "เกณฑ์ผ่านชัดเจน", "is_passed_print",
          "รับคะแนนแล้วใช้ตัวแปร boolean\n\n**เงื่อนไข:**\n\n- `is_passed = score >= 60`\n- พิมพ์ `True` หรือ `False` ของ is_passed",
          "1 บรรทัด", "True",
          "score = int(input())\nis_passed = score >= 60\nprint(is_passed)",
          "score = int(input())\nis_passed = score >= 60\nprint(is_passed)",
          sample_in="72", hint="พิมพ์ค่า boolean โดยตรงได้"),
        p(10, "ค่าคงที่ค่าส่ง", "shipping_const",
          "ค่าส่งคงที่หักเมื่อยอดถึงเกณฑ์\n\n**เงื่อนไข:**\n\n- `SHIPPING_FEE = 40` `FREE_MIN = 300`\n- รับยอดซื้อ\n- ถ้า >= FREE_MIN พิมพ์ `Shipping: 0` ไม่งั้น `Shipping: 40`",
          "1 บรรทัด", "Shipping: 0",
          "SHIPPING_FEE = 40\nFREE_MIN = 300\ntotal = int(input())\n\n# ตัดสินใจค่าส่ง",
          'SHIPPING_FEE = 40\nFREE_MIN = 300\ntotal = int(input())\nif total >= FREE_MIN:\n    print("Shipping: 0")\nelse:\n    print(f"Shipping: {SHIPPING_FEE}")',
          sample_in="320", hint="เทียบกับ FREE_MIN"),
        p(11, "คอมเมนต์เท่าที่จำเป็น", "light_comment",
          "คำนวณเงินทอน พร้อมคอมเมนต์หนึ่งบรรทัดอธิบายทำไม\n\n**เงื่อนไข:**\n\n- รับ price และ paid\n- พิมพ์ `Change: <paid-price>`",
          "1 บรรทัด", "Change: 30",
          "price = int(input())\npaid = int(input())\n# คำนวณเงินทอนให้ลูกค้า\nchange = paid - price\nprint(f\"Change: {change}\")",
          'price = int(input())\npaid = int(input())\n# คำนวณเงินทอนให้ลูกค้า\nchange = paid - price\nprint(f"Change: {change}")',
          sample_in="70\n100", hint="คอมเมนต์อธิบายเหตุผล ไม่ใช่พูดซ้ำโค้ด"),
        p(12, "ฟังก์ชันคำนวณยอด", "get_total_fn",
          "แยกการรวมราคาสินค้าเป็นฟังก์ชัน\n\n**เงื่อนไข:**\n\n- `get_total(prices)` คืนผลรวม\n- พิมพ์ผลของ `[15, 25, 10]`",
          "1 บรรทัด", "50",
          "def get_total(prices):\n    # รวมราคา\n    ...\n\nprint(get_total([15, 25, 10]))",
          "def get_total(prices):\n    total = 0\n    for p in prices:\n        total += p\n    return total\n\nprint(get_total([15, 25, 10]))",
          "ชื่อฟังก์ชันบอกหน้าที่"),
        p(13, "ป้ายสถานะอ่านง่าย", "status_label",
          "แบตเตอรี่ต่ำเมื่อ < 20\n\n**เงื่อนไข:**\n\n- รับเปอร์เซ็นต์แบต\n- `is_low = battery < 20`\n- พิมพ์ `Low` หรือ `OK`",
          "1 บรรทัด", "Low",
          "battery = int(input())\nis_low = battery < 20\n\n# พิมพ์สถานะ",
          'battery = int(input())\nis_low = battery < 20\nif is_low:\n    print("Low")\nelse:\n    print("OK")',
          sample_in="15", hint="ใช้ is_low ใน if"),
        p(5, "รีแฟกเตอร์บิลยาว", "refactor_bill",
          "แยกการคิดส่วนลดและการพิมพ์\n\n**เงื่อนไข:**\n\n- `DISCOUNT = 20`\n- `final_price(price)` คืน price - DISCOUNT\n- `show(price)` พิมพ์ `Pay: <final>`\n- เรียก show(150)",
          "1 บรรทัด", "Pay: 130",
          "DISCOUNT = 20\n\ndef final_price(price):\n    # คืนราคาสุทธิ\n    ...\n\ndef show(price):\n    # พิมพ์ Pay\n    ...\n\nshow(150)",
          'DISCOUNT = 20\n\ndef final_price(price):\n    return price - DISCOUNT\n\ndef show(price):\n    print(f"Pay: {final_price(price)}")\n\nshow(150)',
          "แยกคำนวณกับแสดงผล"),
        p(14, "ค่าคงที่หลายตัว", "multi_const",
          "คิดค่าเข้าชมสวน\n\n**เงื่อนไข:**\n\n- `CHILD_PRICE = 80` `ADULT_PRICE = 150`\n- รับจำนวนเด็กและผู้ใหญ่\n- พิมพ์ `Total: <ยอด>`",
          "1 บรรทัด", "Total: 460",
          "CHILD_PRICE = 80\nADULT_PRICE = 150\nchildren = int(input())\nadults = int(input())\n\n# คำนวณยอด",
          'CHILD_PRICE = 80\nADULT_PRICE = 150\nchildren = int(input())\nadults = int(input())\ntotal = children * CHILD_PRICE + adults * ADULT_PRICE\nprint(f"Total: {total}")',
          sample_in="2\n2", hint="คูณแต่ละกลุ่มแล้วบวก"),
        p(15, "โปรไฟล์สั้นชัด", "clean_profile",
          "แสดงโปรไฟล์สั้นๆ\n\n**เงื่อนไข:**\n\n- รับชื่อและเมือง\n- พิมพ์ `Profile: <name> / <city>` ด้วย f-string",
          "1 บรรทัด", "Profile: Mina / Chiang Mai",
          "name = input()\ncity = input()\n\n# f-string",
          'name = input()\ncity = input()\nprint(f"Profile: {name} / {city}")',
          sample_in="Mina\nChiang Mai", hint="ใช้ f-string คู่เดียว"),
        p(16, "รายงานสะอาด", "clean_report",
          "สร้างรายงานคะแนนให้อ่านง่าย\n\n**เงื่อนไข:**\n\n- `PASS_SCORE = 50`\n- สร้าง `is_pass(score)` คืน True/False\n- สร้าง `report(name, score)` พิมพ์ `name: Pass` หรือ `name: Fail`\n- เรียกกับ `(\"Yam\", 66)` และ `(\"Bee\", 40)`",
          "2 บรรทัด", "Yam: Pass\nBee: Fail",
          "PASS_SCORE = 50\n\ndef is_pass(score):\n    # return เปรียบเทียบ\n    ...\n\ndef report(name, score):\n    # พิมพ์ผล\n    ...\n\nreport(\"Yam\", 66)\nreport(\"Bee\", 40)",
          'PASS_SCORE = 50\n\ndef is_pass(score):\n    return score >= PASS_SCORE\n\ndef report(name, score):\n    if is_pass(score):\n        print(f"{name}: Pass")\n    else:\n        print(f"{name}: Fail")\n\nreport("Yam", 66)\nreport("Bee", 40)',
          "ใช้ค่าคงที่และฟังก์ชันช่วยอ่าน"),
    ]
    for i, pr in enumerate(probs):
        probs[i] = dict(pr)
        probs[i]["starter"] = pr["starter"].replace("    ...\n", "")
    write_week("043-code-readability", chapter="Code Readability", emoji="✨", index_md=index, problems=probs)


# ───────── 044 practice-review integration; no startswith; no grade clone as main ─────────
def week_044():
    items = [
        ("ผลรวมคะแนน list", "ฟังก์ชัน+list"),
        ("dict วน .items()", "แสดงคู่คีย์"),
        ("ค่าเฉลี่ยกันว่าง", "guard + sum"),
        ("set จาก list", "ตัดซ้ำ"),
        ("tuple พิกัด", "อ่าน index"),
        ("dict ของ list คะแนน", "dict→list"),
        ("กรองคะแนนผ่าน", "list ใหม่"),
        ("รวมยอดตะกร้า", "list+ฟังก์ชัน"),
        ("นับความถี่คำสั้น", "dict นับ"),
        ("อัปเดตโปรไฟล์", "แก้ dict"),
        ("สมาชิกใน set", "in"),
        ("สรุปนักเรียนหลายคน", "dict of lists"),
        ("คลังสินค้า", "dict+ฟังก์ชัน"),
        ("จัดทีมไม่ซ้ำ", "set+list"),
        ("เมนูสั่งอาหาร", "ประกอบหลายอย่าง"),
    ]
    index = idx(
        "บท 044 Practice Review",
        "รวม list/tuple/set/dict/ฟังก์ชัน/scope เท่าที่เรียนแล้ว · dict ของ list ได้ · `sum()` ได้",
        "ห้าม `.startswith()` · ห้าม docstring บังคับ · ห้าม clone เกรด 80/70/60 เป็นแกนหลัก",
        rows(items),
        "เน้นผสมเครื่องมือ ไม่สอนของใหม่",
    )
    probs = [
        p(2, "ผลรวมคะแนน list", "sum_scores_fn",
          "รวมคะแนนใน list\n\n**เงื่อนไข:**\n\n- `total_of(scores)` คืนผลรวม\n- พิมพ์ผลของ `[70, 80, 90]`",
          "1 บรรทัด", "240",
          "def total_of(scores):\n    # รวม\n    ...\n\nprint(total_of([70, 80, 90]))",
          "def total_of(scores):\n    return sum(scores)\n\nprint(total_of([70, 80, 90]))"),
        p(3, "dict วน .items()", "items_loop",
          "แสดงสต็อกสินค้า\n\n**เงื่อนไข:**\n\n- มี `stock = {\"pen\": 10, \"eraser\": 5}`\n- วน `.items()` พิมพ์ `pen: 10` รูปแบบเดียวกัน",
          "2 บรรทัด", "pen: 10\neraser: 5",
          'stock = {"pen": 10, "eraser": 5}\n\n# วน items',
          'stock = {"pen": 10, "eraser": 5}\nfor k, v in stock.items():\n    print(f"{k}: {v}")'),
        p(4, "ค่าเฉลี่ยกันว่าง", "avg_guard",
          "ค่าเฉลี่ยที่กัน list ว่าง\n\n**เงื่อนไข:**\n\n- `average(scores)` ถ้าว่างคืน 0 ไม่งั้น sum/len\n- พิมพ์ผล `[]` และ `[8, 10]`",
          "2 บรรทัด", "0\n9.0",
          "def average(scores):\n    # กันว่าง\n    ...\n\nprint(average([]))\nprint(average([8, 10]))",
          "def average(scores):\n    if len(scores) == 0:\n        return 0\n    else:\n        return sum(scores) / len(scores)\n\nprint(average([]))\nprint(average([8, 10]))"),
        p(8, "set จาก list", "unique_names",
          "ตัดชื่อซ้ำในคิว\n\n**เงื่อนไข:**\n\n- จาก `names = [\"Ann\", \"Ben\", \"Ann\"]` สร้าง set แล้วพิมพ์ความยาว",
          "1 บรรทัด", "2",
          'names = ["Ann", "Ben", "Ann"]\nunique = set(names)\nprint(len(unique))',
          'names = ["Ann", "Ben", "Ann"]\nunique = set(names)\nprint(len(unique))'),
        p(9, "tuple พิกัด", "coord_tuple",
          "อ่านพิกัดจาก tuple\n\n**เงื่อนไข:**\n\n- `point = (3, 5)`\n- พิมพ์ `x=3` และ `y=5`",
          "2 บรรทัด", "x=3\ny=5",
          "point = (3, 5)\n\n# พิมพ์ x และ y",
          'point = (3, 5)\nprint(f"x={point[0]}")\nprint(f"y={point[1]}")'),
        p(6, "dict ของ list คะแนน", "dict_of_lists",
          "นักเรียนมีคะแนนหลายวิชา\n\n**เงื่อนไข:**\n\n- `data = {\"Ada\": [80, 90], \"Ben\": [70, 75]}`\n- วน `.items()` พิมพ์ `Ada: 170` โดยรวม list ด้วย sum",
          "2 บรรทัด", "Ada: 170\nBen: 145",
          'data = {"Ada": [80, 90], "Ben": [70, 75]}\n\n# วนแล้วรวม',
          'data = {"Ada": [80, 90], "Ben": [70, 75]}\nfor name, scores in data.items():\n    print(f"{name}: {sum(scores)}")',
          "ค่าใน dict เป็น list"),
        p(7, "กรองคะแนนผ่าน", "filter_60",
          "เก็บคะแนน >= 60\n\n**เงื่อนไข:**\n\n- `passed(scores)` คืน list ใหม่\n- พิมพ์ผล `[55, 60, 88, 40]`",
          "1 บรรทัด", "[60, 88]",
          "def passed(scores):\n    # กรอง\n    ...\n\nprint(passed([55, 60, 88, 40]))",
          "def passed(scores):\n    result = []\n    for s in scores:\n        if s >= 60:\n            result.append(s)\n    return result\n\nprint(passed([55, 60, 88, 40]))",
          "append เฉพาะที่ผ่าน"),
        p(10, "รวมยอดตะกร้า", "cart_total_fn",
          "ยอดตะกร้าจากราคา\n\n**เงื่อนไข:**\n\n- `cart_total(prices)` คืนผลรวม\n- พิมพ์ผล `[12, 18, 20]`",
          "1 บรรทัด", "50",
          "def cart_total(prices):\n    # รวม\n    ...\n\nprint(cart_total([12, 18, 20]))",
          "def cart_total(prices):\n    total = 0\n    for p in prices:\n        total += p\n    return total\n\nprint(cart_total([12, 18, 20]))",
          "ลูปรวมหรือใช้ sum"),
        p(11, "นับความถี่คำสั้น", "freq_count",
          "นับคำใน list\n\n**เงื่อนไข:**\n\n- จาก `words = [\"hi\", \"ok\", \"hi\", \"hi\"]` สร้าง dict นับความถี่\n- พิมพ์ค่าของคีย์ `\"hi\"`",
          "1 บรรทัด", "3",
          'words = ["hi", "ok", "hi", "hi"]\nfreq = {}\nfor w in words:\n    # นับใน dict\n    ...\nprint(freq["hi"])',
          'words = ["hi", "ok", "hi", "hi"]\nfreq = {}\nfor w in words:\n    if w in freq:\n        freq[w] = freq[w] + 1\n    else:\n        freq[w] = 1\nprint(freq["hi"])',
          "แบบนับความถี่ด้วย dict"),
        p(12, "อัปเดตโปรไฟล์", "update_profile",
          "อัปเดตคะแนนในโปรไฟล์\n\n**เงื่อนไข:**\n\n- `profile = {\"name\": \"Joy\", \"score\": 70}`\n- ตั้ง score เป็น 85 แล้วพิมพ์ทั้ง dict",
          "1 บรรทัด", "{'name': 'Joy', 'score': 85}",
          'profile = {"name": "Joy", "score": 70}\n\n# อัปเดต score\nprint(profile)',
          'profile = {"name": "Joy", "score": 70}\nprofile["score"] = 85\nprint(profile)',
          "กำหนดค่าคีย์ใหม่"),
        p(13, "สมาชิกใน set", "set_membership",
          "ตรวจว่ามีโค้ดส่วนลดในชุดหรือไม่\n\n**เงื่อนไข:**\n\n- `codes = {\"SAVE10\", \"FREE\", \"VIP\"}`\n- รับโค้ดหนึ่งคำ\n- ถ้ามีใน set พิมพ์ `Valid` ไม่งั้น `Invalid`",
          "1 บรรทัด", "Valid",
          'codes = {"SAVE10", "FREE", "VIP"}\ncode = input()\n\n# ใช้ in',
          'codes = {"SAVE10", "FREE", "VIP"}\ncode = input()\nif code in codes:\n    print("Valid")\nelse:\n    print("Invalid")',
          sample_in="FREE", hint="ใช้ in กับ set"),
        p(5, "สรุปนักเรียนหลายคน", "multi_student",
          "สรุปค่าเฉลี่ยแบบหยาบของแต่ละคน\n\n**เงื่อนไข:**\n\n- `student_scores = {\"Alice\": [85, 90, 80], \"Bob\": [70, 75, 65]}`\n- วนพิมพ์ `Alice: 85.0` โดยใช้ sum/len ทศนิยม 1 ตำแหน่ง\n- ไม่ต้องแปลงเป็นเกรดตัวอักษร",
          "2 บรรทัด", "Alice: 85.0\nBob: 70.0",
          'student_scores = {"Alice": [85, 90, 80], "Bob": [70, 75, 65]}\n\n# วนสรุป',
          'student_scores = {"Alice": [85, 90, 80], "Bob": [70, 75, 65]}\nfor name, scores in student_scores.items():\n    avg = sum(scores) / len(scores)\n    print(f"{name}: {avg:.1f}")',
          "อย่าทำเกรด A/B/C/F ในข้อนี้"),
        p(14, "คลังสินค้า", "inventory_fn",
          "จัดการจำนวนสินค้าใน dict\n\n**เงื่อนไข:**\n\n- `add_stock(inv, item, n)` เพิ่มจำนวน (ถ้ายังไม่มีให้เริ่ม 0)\n- เริ่ม `{}` เพิ่ม apple 3 สองครั้ง แล้วพิมพ์ inv",
          "1 บรรทัด", "{'apple': 6}",
          "def add_stock(inv, item, n):\n    # เพิ่มสต็อก\n    ...\n\ninv = {}\nadd_stock(inv, \"apple\", 3)\nadd_stock(inv, \"apple\", 3)\nprint(inv)",
          'def add_stock(inv, item, n):\n    if item in inv:\n        inv[item] = inv[item] + n\n    else:\n        inv[item] = n\n\ninv = {}\nadd_stock(inv, "apple", 3)\nadd_stock(inv, "apple", 3)\nprint(inv)',
          "เช็ก key ก่อนบวก"),
        p(15, "จัดทีมไม่ซ้ำ", "team_unique",
          "รายชื่อสมัครอาจซ้ำ ให้เหลือชื่อไม่ซ้ำแล้วเรียงด้วย .sort()\n\n**เงื่อนไข:**\n\n- จาก `raw = [\"C\", \"A\", \"B\", \"A\"]`\n- สร้าง list ใหม่โดยเพิ่มเฉพาะชื่อที่ยังไม่มี แล้ว sort\n- พิมพ์ list ผลลัพธ์",
          "1 บรรทัด", "['A', 'B', 'C']",
          'raw = ["C", "A", "B", "A"]\nteam = []\nfor name in raw:\n    # เพิ่มถ้ายังไม่มี\n    ...\nteam.sort()\nprint(team)',
          'raw = ["C", "A", "B", "A"]\nteam = []\nfor name in raw:\n    if name not in team:\n        team.append(name)\nteam.sort()\nprint(team)',
          "ใช้ in กับ list แล้ว sort"),
        p(16, "เมนูสั่งอาหาร", "food_menu_order",
          "เมนูเป็น dict ราคา และรายการสั่งเป็น list\n\n**เงื่อนไข:**\n\n- `menu = {\"rice\": 40, \"soup\": 30, \"tea\": 20}`\n- `order = [\"rice\", \"tea\", \"soup\"]`\n- สร้าง `bill(menu, order)` คืนยอดรวม\n- พิมพ์ยอด",
          "1 บรรทัด", "90",
          'menu = {"rice": 40, "soup": 30, "tea": 20}\norder = ["rice", "tea", "soup"]\n\ndef bill(menu, order):\n    # รวมราคา\n    ...\n\nprint(bill(menu, order))',
          'menu = {"rice": 40, "soup": 30, "tea": 20}\norder = ["rice", "tea", "soup"]\n\ndef bill(menu, order):\n    total = 0\n    for item in order:\n        total += menu[item]\n    return total\n\nprint(bill(menu, order))',
          "วน order แล้วบวกจาก menu"),
    ]
    for i, pr in enumerate(probs):
        probs[i] = dict(pr)
        probs[i]["starter"] = pr["starter"].replace("    ...\n", "")
    write_week("044-practice-review", chapter="Practice Review", emoji="🔁", index_md=index, problems=probs)


if __name__ == "__main__":
    week_041()
    week_042()
    week_043()
    week_044()
