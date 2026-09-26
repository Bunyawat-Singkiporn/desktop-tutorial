# -*- coding: utf-8 -*-
"""Expand weeks 007-012 to 15-problem standard (compact batch)."""
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


def index(title, scope, bans, rows, notes=""):
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


ROWS = [
    ("02_test.md", "🟢", None, None),
    ("03_test.md", "🟢", None, None),
    ("04_test.md", "🟢", None, None),
    ("08_easy.md", "🟢", None, None),
    ("09_easy.md", "🟢", None, None),
    ("06_medium.md", "🟡", None, None),
    ("07_medium.md", "🟡", None, None),
    ("10_medium.md", "🟡", None, None),
    ("11_medium.md", "🟡", None, None),
    ("12_medium.md", "🟡", None, None),
    ("13_medium.md", "🟡", None, None),
    ("05_challenge.md", "🔴", None, None),
    ("14_challenge.md", "🔴", None, None),
    ("15_challenge.md", "🔴", None, None),
    ("16_challenge.md", "🔴", None, None),
]


def fill_rows(items):
    # items: list of (title, axis) length 15 in teaching order matching ROWS files
    out = []
    for (f, lv, _, _), (t, ax) in zip(ROWS, items):
        out.append((f, lv, t, ax))
    return out


# ───────── 007 data types ─────────
def week_007():
    items = [
        ("ชนิดของอายุ", "type() กับ int"),
        ("ชนิดของราคา", "type() กับ float"),
        ("ชนิดของชื่อ", "type() กับ str"),
        ("ธงสถานะร้าน", "bool True/False"),
        ("เทียบ 5 กับ \"5\"", "พิมพ์ค่าบวกของ int vs concat str"),
        ("การ์ดข้อมูลผสม", "เก็บครบ 4 ชนิดแล้วพิมพ์"),
        ("ตรวจชนิดคะแนน", "type() หลายค่า"),
        ("ค่าความจริงสองอัน", "True/False แยกสถานการณ์"),
        ("ข้อความต่อกัน", "str + str"),
        ("โปรไฟล์สั้น", "ผสมชนิดในป้ายกำกับ"),
        ("อุณหภูมิติดลบ", "int ติดลบ + type"),
        ("ใบเสร็จชนิดข้อมูล", "หลาย type() ในใบเสร็จ"),
        ("สลับความหมายเลข", "int บวก vs str ต่อ"),
        ("สถานะเกมครบชุด", "bool หลายตัว"),
        ("รายงานชนิดครบ", "type() ทั้งสี่ชนิด"),
    ]
    idx = index(
        "บท 007 Data Types",
        "`int` `float` `str` `bool` / `True` `False` / `type()` / การต่อ str ด้วย `+`",
        "ไม่มี `input()` · ไม่มี f-string · ไม่มี `if`",
        fill_rows(items),
        "ข้อ 02 ไม่ซ้ำตารางตัวอย่างในบทเรียนแบบลอกมาทั้งก้อน — ใช้สถานการณ์อายุนักเรียน",
    )
    probs = [
        p(2, "ชนิดของอายุ", "type_age",
          'เก็บ `age = 12` แล้วแสดงค่าและชนิด',
          "2 บรรทัด", "Age: 12\nType: <class 'int'>",
          "age = 12\n\n# แสดงค่าและชนิด",
          "age = 12\nprint(\"Age:\", age)\nprint(\"Type:\", type(age))"),
        p(3, "ชนิดของราคา", "type_price",
          'เก็บ `price = 29.99` แสดงค่าและชนิด',
          "2 บรรทัด", "Price: 29.99\nType: <class 'float'>",
          "price = 29.99\n\n# แสดงผล",
          "price = 29.99\nprint(\"Price:\", price)\nprint(\"Type:\", type(price))"),
        p(4, "ชนิดของชื่อ", "type_name",
          'เก็บ `name = "Mira"` แสดงค่าและชนิด',
          "2 บรรทัด", "Name: Mira\nType: <class 'str'>",
          'name = "Mira"\n\n# แสดงผล',
          'name = "Mira"\nprint("Name:", name)\nprint("Type:", type(name))'),
        p(8, "ธงสถานะร้าน", "shop_open_flag",
          '`is_open = True` แสดงสถานะ',
          "1 บรรทัด", "Open: True",
          "is_open = True\n\n# แสดงผล",
          'is_open = True\nprint("Open:", is_open)'),
        p(9, "เทียบ 5 กับ \"5\"", "five_vs_text",
          '`a = 5` และ `b = "5"` แสดง `a + a` และ `b + b`',
          "2 บรรทัด", "10\n55",
          'a = 5\nb = "5"\n\n# แสดง a+a และ b+b',
          'a = 5\nb = "5"\nprint(a + a)\nprint(b + b)'),
        p(6, "การ์ดข้อมูลผสม", "mixed_card",
          '`name = "Ben"`, `age = 11`, `height = 1.4`, `is_member = False` แสดงครบ',
          "4 บรรทัด", "Name: Ben\nAge: 11\nHeight: 1.4\nMember: False",
          'name = "Ben"\nage = 11\nheight = 1.4\nis_member = False\n\n# แสดงผล',
          'name = "Ben"\nage = 11\nheight = 1.4\nis_member = False\nprint("Name:", name)\nprint("Age:", age)\nprint("Height:", height)\nprint("Member:", is_member)',
          "ครบทั้งสี่ชนิด"),
        p(7, "ตรวจชนิดคะแนน", "types_of_scores",
          '`score = 90`, `ratio = 0.9` แสดง type ของทั้งคู่',
          "2 บรรทัด", "<class 'int'>\n<class 'float'>",
          "score = 90\nratio = 0.9\n\n# แสดง type",
          "score = 90\nratio = 0.9\nprint(type(score))\nprint(type(ratio))",
          "print(type(...)) ตรงๆ"),
        p(10, "ค่าความจริงสองอัน", "two_bools",
          '`has_homework = True`, `is_weekend = False` แสดงทั้งคู่',
          "2 บรรทัด", "Homework: True\nWeekend: False",
          "has_homework = True\nis_weekend = False\n\n# แสดงผล",
          'has_homework = True\nis_weekend = False\nprint("Homework:", has_homework)\nprint("Weekend:", is_weekend)',
          "bool ใช้ตัวพิมพ์ใหญ่ True/False"),
        p(11, "ข้อความต่อกัน", "concat_words",
          '`a = "Good"` และ `b = "Morning"` ต่อเป็นประโยคเดียวด้วย `+` และช่องว่าง',
          "1 บรรทัด", "Good Morning",
          'a = "Good"\nb = "Morning"\n\n# ต่อข้อความ',
          'a = "Good"\nb = "Morning"\nprint(a + " " + b)',
          "คั่นด้วยสตริงช่องว่าง"),
        p(12, "โปรไฟล์สั้น", "short_profile",
          '`user = "Kai"`, `level = 4`, `active = True` แสดงโปรไฟล์',
          "3 บรรทัด", "User: Kai\nLevel: 4\nActive: True",
          'user = "Kai"\nlevel = 4\nactive = True\n\n# แสดงผล',
          'user = "Kai"\nlevel = 4\nactive = True\nprint("User:", user)\nprint("Level:", level)\nprint("Active:", active)',
          "ผสม str/int/bool"),
        p(13, "อุณหภูมิติดลบ", "negative_temp",
          '`temperature = -3` แสดงค่าและชนิด',
          "2 บรรทัด", "Temp: -3\nType: <class 'int'>",
          "temperature = -3\n\n# แสดงผล",
          'temperature = -3\nprint("Temp:", temperature)\nprint("Type:", type(temperature))',
          "เลขติดลบก็เป็น int"),
        p(5, "ใบเสร็จชนิดข้อมูล", "typed_receipt",
          'เก็บ `item = "Juice"`, `price = 25.5`, `qty = 2`, `paid = True` แล้วแสดงค่าและ type ของ price กับ qty',
          "ใบเสร็จ", "Item: Juice\nPrice: 25.5\nPrice Type: <class 'float'>\nQty: 2\nQty Type: <class 'int'>\nPaid: True",
          'item = "Juice"\nprice = 25.5\nqty = 2\npaid = True\n\n# แสดงผล',
          'item = "Juice"\nprice = 25.5\nqty = 2\npaid = True\nprint("Item:", item)\nprint("Price:", price)\nprint("Price Type:", type(price))\nprint("Qty:", qty)\nprint("Qty Type:", type(qty))\nprint("Paid:", paid)',
          "แสดงทั้งค่าและชนิดของตัวเลข"),
        p(14, "สลับความหมายเลข", "number_meanings",
          '`n = 3`, `t = "3"` แสดงผล `n + n`, `t + t`, และ type ของ t',
          "3 บรรทัด", "6\n33\n<class 'str'>",
          'n = 3\nt = "3"\n\n# แสดงผล',
          'n = 3\nt = "3"\nprint(n + n)\nprint(t + t)\nprint(type(t))',
          "ชนิดต่างกัน ผลบวกต่างกัน"),
        p(15, "สถานะเกมครบชุด", "game_flags",
          '`is_alive = True`, `has_key = False`, `game_over = False` แสดงครบ',
          "3 บรรทัด", "Alive: True\nKey: False\nGame Over: False",
          "is_alive = True\nhas_key = False\ngame_over = False\n\n# แสดงผล",
          'is_alive = True\nhas_key = False\ngame_over = False\nprint("Alive:", is_alive)\nprint("Key:", has_key)\nprint("Game Over:", game_over)',
          "ตั้งชื่อขึ้นต้น is_/has_ ได้"),
        p(16, "รายงานชนิดครบ", "all_four_types",
          'สร้างตัวแปรครบ 4 ชนิด: `i = 1`, `f = 1.5`, `s = "hi"`, `b = True` แล้วพิมพ์ type ทั้งสี่',
          "4 บรรทัด", "<class 'int'>\n<class 'float'>\n<class 'str'>\n<class 'bool'>",
          'i = 1\nf = 1.5\ns = "hi"\nb = True\n\n# แสดง type ทั้งสี่',
          'i = 1\nf = 1.5\ns = "hi"\nb = True\nprint(type(i))\nprint(type(f))\nprint(type(s))\nprint(type(b))',
          "ลำดับ int float str bool"),
    ]
    write_week("007-data-types", chapter="Data Types", emoji="🧬", index_md=idx, problems=probs)


# ───────── 008 type conversion ─────────
def week_008():
    items = [
        ("อายุปีหน้า", "int(input) แล้ว +1"),
        ("แปลงข้อความเป็นจำนวน", "int() จากตัวแปร str"),
        ("ราคารวมทศนิยม", "float(input)"),
        ("คะแนนเป็นข้อความ", "str(score) ต่อประโยค"),
        ("ปีเกิดคร่าวๆ", "ปีปัจจุบันลบอายุแบบกำหนดค่า"),
        ("ใบเสร็จแปลงชนิด", "float + str ป้าย"),
        ("จำนวนชิ้นเป็นข้อความ", "str(qty)"),
        ("ส่วนสูงเมตร", "float จาก input"),
        ("รวมสองจำนวนเต็ม", "int สองครั้ง"),
        ("ราคาหลัง VAT คร่าวๆ", "float * 1.07"),
        ("ข้อความประกาศคะแนน", "concat ด้วย str()"),
        ("บิลสองบรรทัด", "input สองค่า"),
        ("แปลงแล้วบวกต่อ", "int แล้วคำนวณ"),
        ("ป้ายราคาทศนิยม", "float และพิมพ์"),
        ("สรุปคำสั่งซื้อ", "int+float+str ป้าย"),
    ]
    idx = index(
        "บท 008 Type Conversion",
        "`int()` `float()` `str()` / `input()` (ไม่มี prompt) / `int(input())` `float(input())` / ต่อสตริงด้วย `+`",
        "ไม่มี f-string · ไม่มี `if` · ไม่มี loop",
        fill_rows(items),
        "บทนี้ `input()` ปรากฏได้ก่อนบท 009 — ใช้แบบไม่มีข้อความในวงเล็บ",
    )
    probs = [
        p(2, "อายุปีหน้า", "next_year_age",
          "รับอายุจำนวนเต็ม แล้วแสดงอายุปีหน้า (บวก 1)",
          "1 บรรทัด", "Next year: 14",
          "age = int(input())\n\n# แสดงอายุปีหน้า",
          'age = int(input())\nprint("Next year:", age + 1)',
          sample_in="13"),
        p(3, "แปลงข้อความเป็นจำนวน", "text_to_int",
          'มี `text = "20"` แปลงเป็น int เก็บใน `n` แล้วแสดง `n + 5`',
          "1 บรรทัด", "25",
          'text = "20"\n\n# แปลงแล้วคำนวณ',
          'text = "20"\nn = int(text)\nprint(n + 5)'),
        p(4, "ราคารวมทศนิยม", "float_price",
          "รับราคาแบบทศนิยม แล้วแสดงราคา",
          "1 บรรทัด", "Price: 49.5",
          "price = float(input())\n\n# แสดงราคา",
          'price = float(input())\nprint("Price:", price)',
          sample_in="49.5"),
        p(8, "คะแนนเป็นข้อความ", "score_message",
          '`score = 95` สร้างข้อความ `"Your score is: " + str(score)` แล้วพิมพ์',
          "1 บรรทัด", "Your score is: 95",
          "score = 95\n\n# สร้างข้อความ",
          'score = 95\nmessage = "Your score is: " + str(score)\nprint(message)'),
        p(9, "ปีเกิดคร่าวๆ", "birth_year_simple",
          "รับอายุ แล้วคำนวณปีเกิดคร่าวๆ จาก `2026 - age` แสดงผล",
          "1 บรรทัด", "Birth year: 2014",
          "age = int(input())\n\n# คำนวณปีเกิด",
          'age = int(input())\nbirth = 2026 - age\nprint("Birth year:", birth)',
          sample_in="12", hint="ลบจากปีคงที่ 2026"),
        p(6, "ใบเสร็จแปลงชนิด", "convert_receipt",
          'รับราคา float แล้วแสดง `"Total: " + str(price)`',
          "1 บรรทัด", "Total: 35.0",
          "price = float(input())\n\n# แสดงผลแบบต่อสตริง",
          'price = float(input())\nprint("Total: " + str(price))',
          sample_in="35", hint="ใช้ str() ก่อนต่อข้อความ"),
        p(7, "จำนวนชิ้นเป็นข้อความ", "qty_to_text",
          '`qty = 4` แสดง `"Items: " + str(qty)`',
          "1 บรรทัด", "Items: 4",
          "qty = 4\n\n# แสดงผล",
          'qty = 4\nprint("Items: " + str(qty))',
          hint="ต้อง str() ก่อนต่อ"),
        p(10, "ส่วนสูงเมตร", "height_float",
          "รับส่วนสูง float แสดง Height",
          "1 บรรทัด", "Height: 1.55",
          "height = float(input())\n\n# แสดงผล",
          'height = float(input())\nprint("Height:", height)',
          sample_in="1.55"),
        p(11, "รวมสองจำนวนเต็ม", "sum_two_ints",
          "รับจำนวนเต็มสองบรรทัด แสดงผลรวม",
          "1 บรรทัด", "Sum: 15",
          "a = int(input())\nb = int(input())\n\n# รวม",
          'a = int(input())\nb = int(input())\nprint("Sum:", a + b)',
          sample_in="7\n8"),
        p(12, "ราคาหลัง VAT คร่าวๆ", "vat_price",
          "รับราคา float แล้วคูณ 1.07 แสดงผล (ยังไม่ต้องปัดทศนิยมพิเศษ)",
          "1 บรรทัด", "With VAT: 107.0",
          "price = float(input())\n\n# คิด VAT",
          'price = float(input())\nprint("With VAT:", price * 1.07)',
          sample_in="100", hint="ราคา * 1.07"),
        p(13, "ข้อความประกาศคะแนน", "announce_score",
          "รับคะแนน int แล้วพิมพ์ข้อความ Score = ตามด้วยคะแนน โดยต่อสตริงด้วย str()",
          "1 บรรทัด", "Score = 88",
          "score = int(input())\n\n# ประกาศคะแนน",
          'score = int(input())\nprint("Score = " + str(score))',
          sample_in="88"),
        p(5, "บิลสองบรรทัด", "two_line_bill",
          "รับชื่อสินค้า (str) และราคา float แสดงสองบรรทัด",
          "2 บรรทัด", "Item: Soap\nPrice: 29.0",
          "item = input()\nprice = float(input())\n\n# แสดงบิล",
          'item = input()\nprice = float(input())\nprint("Item:", item)\nprint("Price:", price)',
          sample_in="Soap\n29", hint="input แรกเป็นข้อความ ครั้งที่สองแปลง float"),
        p(14, "แปลงแล้วบวกต่อ", "convert_then_add",
          'มี `raw = "15"` แปลงเป็น int แล้วบวก 10 แสดงผล',
          "1 บรรทัด", "Result: 25",
          'raw = "15"\n\n# แปลงและบวก',
          'raw = "15"\nn = int(raw)\nprint("Result:", n + 10)',
          hint="int(raw) ก่อนบวก"),
        p(15, "ป้ายราคาทศนิยม", "float_label",
          "รับราคา float แสดงป้าย `Tag:` ตามด้วยราคา",
          "1 บรรทัด", "Tag: 12.5",
          "price = float(input())\n\n# แสดงป้าย",
          'price = float(input())\nprint("Tag:", price)',
          sample_in="12.5"),
        p(16, "สรุปคำสั่งซื้อ", "order_summary",
          "รับชื่อสินค้า, จำนวนชิ้น (int), ราคาต่อชิ้น (float) แล้วแสดงสรุปพร้อม Line Total = จำนวนคูณราคา",
          "4 บรรทัด", "Name: Pen\nQty: 3\nPrice: 10.0\nLine Total: 30.0",
          "name = input()\nqty = int(input())\nprice = float(input())\n\n# สรุปคำสั่งซื้อ",
          'name = input()\nqty = int(input())\nprice = float(input())\nline_total = qty * price\nprint("Name:", name)\nprint("Qty:", qty)\nprint("Price:", price)\nprint("Line Total:", line_total)',
          sample_in="Pen\n3\n10", hint="Line Total คือจำนวนคูณราคา"),
    ]
    write_week("008-type-conversion", chapter="Type Conversion", emoji="🔄", index_md=idx, problems=probs)


# ───────── 009 input ─────────
def week_009():
    items = [
        ("ทักทายจากชื่อ", "input แล้วทัก"),
        ("ชื่อเต็มสองบรรทัด", "input สองครั้ง"),
        ("อายุปีหน้า", "int(input)+1"),
        ("การ์ดชื่อ-อายุ", "input ผสม int"),
        ("เมืองที่ชอบ", "input ข้อความ"),
        ("ใบลงทะเบียน", "สาม input"),
        ("ราคาต่อจำนวน", "int คูณราคาคงที่"),
        ("เพื่อนสองคน", "สองชื่อ"),
        ("รหัสห้อง", "input แล้วพิมพ์ป้าย"),
        ("น้ำหนักตัว", "float(input)"),
        ("สรุปทริปสั้น", "ชื่อ+วัน"),
        ("ฟอร์มสมัครคลับ", "หลายช่อง"),
        ("คำนวณเงินทอนคร่าวๆ", "paid - price"),
        ("บัตรนักเรียน", "หลายบรรทัด"),
        ("ออเดอร์เครื่องดื่ม", "ชื่อ+ขนาด+ราคา"),
    ]
    idx = index(
        "บท 009 Input",
        "`input()` / `int(input())` / `float(input())` (ไม่มี prompt) / print คั่นด้วยจุลภาค",
        "ไม่มี f-string · ไม่มี `if` · ไม่มี loop",
        fill_rows(items),
        "input() เรียกโดยไม่มีข้อความในวงเล็บเสมอ",
    )
    probs = [
        p(2, "ทักทายจากชื่อ", "hello_name",
          "รับชื่อ แล้วแสดง Hello ตามด้วยชื่อ",
          "1 บรรทัด", "Hello, Nita",
          "name = input()\n\n# ทักทาย",
          'name = input()\nprint("Hello,", name)', sample_in="Nita"),
        p(3, "ชื่อเต็มสองบรรทัด", "full_name_inputs",
          "รับชื่อจริงและนามสกุลคนละบรรทัด แสดง Full name",
          "1 บรรทัด", "Full name: Ada Lovelace",
          "first = input()\nlast = input()\n\n# แสดงชื่อเต็ม",
          'first = input()\nlast = input()\nprint("Full name:", first, last)', sample_in="Ada\nLovelace"),
        p(4, "อายุปีหน้า", "age_next",
          "รับอายุ int แสดง Next year",
          "1 บรรทัด", "Next year: 11",
          "age = int(input())\n\n# ปีหน้า",
          'age = int(input())\nprint("Next year:", age + 1)', sample_in="10"),
        p(8, "การ์ดชื่อ-อายุ", "name_age_card",
          "รับชื่อและอายุ แสดงสองบรรทัด",
          "2 บรรทัด", "Name: Sam\nAge: 10",
          "name = input()\nage = int(input())\n\n# การ์ด",
          'name = input()\nage = int(input())\nprint("Name:", name)\nprint("Age:", age)', sample_in="Sam\n10"),
        p(9, "เมืองที่ชอบ", "favorite_city",
          "รับชื่อเมือง แสดง Favorite city",
          "1 บรรทัด", "Favorite city: Bangkok",
          "city = input()\n\n# แสดงผล",
          'city = input()\nprint("Favorite city:", city)', sample_in="Bangkok"),
        p(6, "ใบลงทะเบียน", "registration",
          "รับชื่อ, อายุ, เมือง แสดงสามบรรทัด",
          "3 บรรทัด", "Name: Lea\nAge: 12\nCity: Nan",
          "name = input()\nage = int(input())\ncity = input()\n\n# แสดงใบลงทะเบียน",
          'name = input()\nage = int(input())\ncity = input()\nprint("Name:", name)\nprint("Age:", age)\nprint("City:", city)',
          sample_in="Lea\n12\nNan", hint="เรียก input ตามลำดับช่อง"),
        p(7, "ราคาต่อจำนวน", "price_times_qty",
          "ราคาสินค้าชิ้นละ 25 บาท รับจำนวนชิ้น แล้วแสดงยอด `qty * 25`",
          "1 บรรทัด", "Total: 75",
          "qty = int(input())\n\n# คิดยอด",
          'qty = int(input())\nprint("Total:", qty * 25)',
          sample_in="3", hint="คูณกับราคาคงที่ 25"),
        p(10, "เพื่อนสองคน", "two_friends",
          "รับชื่อเพื่อนสองคน แสดง Friends: a and b",
          "1 บรรทัด", "Friends: Ann and Ben",
          "a = input()\nb = input()\n\n# แสดงผล",
          'a = input()\nb = input()\nprint("Friends:", a, "and", b)', sample_in="Ann\nBen"),
        p(11, "รหัสห้อง", "room_code",
          "รับรหัสห้อง แสดง Room",
          "1 บรรทัด", "Room: A-204",
          "code = input()\n\n# แสดงผล",
          'code = input()\nprint("Room:", code)', sample_in="A-204"),
        p(12, "น้ำหนักตัว", "weight_input",
          "รับน้ำหนัก float แสดง Weight",
          "1 บรรทัด", "Weight: 42.5",
          "w = float(input())\n\n# แสดงผล",
          'w = float(input())\nprint("Weight:", w)', sample_in="42.5"),
        p(13, "สรุปทริปสั้น", "trip_days",
          "รับชื่อสถานที่และจำนวนวัน แสดงสองบรรทัด",
          "2 บรรทัด", "Place: Zoo\nDays: 2",
          "place = input()\ndays = int(input())\n\n# สรุป",
          'place = input()\ndays = int(input())\nprint("Place:", place)\nprint("Days:", days)', sample_in="Zoo\n2"),
        p(5, "ฟอร์มสมัครคลับ", "club_form",
          "รับชื่อ, ชั้นปี int, ความสนใจ แสดงสามบรรทัด",
          "3 บรรทัด", "Name: Oat\nGrade: 6\nInterest: Robots",
          "name = input()\ngrade = int(input())\ninterest = input()\n\n# ฟอร์ม",
          'name = input()\ngrade = int(input())\ninterest = input()\nprint("Name:", name)\nprint("Grade:", grade)\nprint("Interest:", interest)',
          sample_in="Oat\n6\nRobots", hint="แปลงเฉพาะช่องที่เป็นตัวเลข"),
        p(14, "คำนวณเงินทอนคร่าวๆ", "change_calc",
          "รับราคาและเงินที่จ่าย เป็น int แสดงเงินทอน",
          "1 บรรทัด", "Change: 30",
          "price = int(input())\npaid = int(input())\n\n# เงินทอน",
          'price = int(input())\npaid = int(input())\nprint("Change:", paid - price)',
          sample_in="70\n100", hint="paid - price"),
        p(15, "บัตรนักเรียน", "student_pass",
          "รับชื่อ, เลขที่, ห้อง แสดงบัตรสามบรรทัด",
          "3 บรรทัด", "Name: Pin\nNo: 8\nClass: 5/2",
          "name = input()\nno = int(input())\nklass = input()\n\n# บัตร",
          'name = input()\nno = int(input())\nklass = input()\nprint("Name:", name)\nprint("No:", no)\nprint("Class:", klass)',
          sample_in="Pin\n8\n5/2"),
        p(16, "ออเดอร์เครื่องดื่ม", "drink_order",
          "รับชื่อเครื่องดื่ม, ขนาด, ราคา float แสดงสามบรรทัด",
          "3 บรรทัด", "Drink: Cocoa\nSize: M\nPrice: 45.0",
          "drink = input()\nsize = input()\nprice = float(input())\n\n# ออเดอร์",
          'drink = input()\nsize = input()\nprice = float(input())\nprint("Drink:", drink)\nprint("Size:", size)\nprint("Price:", price)',
          sample_in="Cocoa\nM\n45", hint="ราคาใช้ float"),
    ]
    write_week("009-input", chapter="Input", emoji="⌨️", index_md=idx, problems=probs)


if __name__ == "__main__":
    week_007()
    week_008()
    week_009()
    print("done 007-009")
