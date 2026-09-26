# -*- coding: utf-8 -*-
"""Expand weeks 037-040 to 15-problem standard."""
from __future__ import annotations

from _expand_helpers import write_week

NO_IN = "ไม่มี (กำหนดค่าในโปรแกรม / เรียกฟังก์ชันในโค้ด)"
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


# ───────── 037 functions: def no params, print only, no return ─────────
def week_037():
    items = [
        ("ป้ายร้านกาแฟ", "def + print หลายบรรทัด"),
        ("เมนูว่าง 2 รอบ", "เรียกซ้ำ"),
        ("เส้นคั่นสั้น", "ฟังก์ชันเส้นคั่น"),
        ("ป้ายปิดร้าน", "ข้อความคงที่"),
        ("ทักทายจาก input", "input ในฟังก์ชัน"),
        ("ใบเสร็จสั้น", "หลาย print ใน def"),
        ("นับถอยหลัง 3", "ลูปในฟังก์ชัน"),
        ("เมนูของหวาน", "รายการคงที่"),
        ("สรุปยอดคงที่", "คำนวณใน def"),
        ("ตารางเวรสั้น", "ลูปพิมพ์รายการ"),
        ("กล่องประกาศ", "กรอบ ="),
        ("เครื่องคิดเลขเล็ก", "รับ 2 ค่าใน def"),
        ("ใบเสร็จหลายรายการ", "list + ลูปใน def"),
        ("รายงานอุณหภูมิ", "if ใน def"),
        ("สองหน้าจอ ATM", "เรียก 2 ฟังก์ชัน"),
    ]
    index = idx(
        "บท 037 Functions",
        "`def name():` ไม่มีพารามิเตอร์ · แสดงผลด้วย `print` · เรียกฟังก์ชัน · ความรู้บท 001–036",
        "ห้าม parameter · ห้าม `return` · ห้าม default argument",
        rows(items),
        "ข้อ 02 ห้าม clone `greet()` จากบทเรียน — ใช้สถานการณ์ร้าน/ป้ายแทน",
    )
    probs = [
        p(2, "ป้ายร้านกาแฟ", "shop_sign",
          "ร้านกาแฟต้องการป้ายเปิดร้าน\n\n**เงื่อนไข:**\n\n- สร้าง `show_sign()` ที่พิมพ์ 3 บรรทัดตามตัวอย่าง\n- เรียกฟังก์ชัน 1 ครั้ง",
          "3 บรรทัด", "==== COFFEE ====\nOpen 7:00 - 18:00\n================",
          "# สร้าง show_sign() แล้วเรียก",
          'def show_sign():\n    print("==== COFFEE ====")\n    print("Open 7:00 - 18:00")\n    print("================")\n\nshow_sign()'),
        p(3, "เมนูว่าง 2 รอบ", "empty_menu",
          "จอเมนูว่างยังไม่โหลดรายการ\n\n**เงื่อนไข:**\n\n- สร้าง `show_empty()` พิมพ์ `Menu loading...`\n- เรียก 2 ครั้ง",
          "2 บรรทัด", "Menu loading...\nMenu loading...",
          "# show_empty แล้วเรียก 2 ครั้ง",
          'def show_empty():\n    print("Menu loading...")\n\nshow_empty()\nshow_empty()'),
        p(4, "เส้นคั่นสั้น", "divider",
          "ต้องการเส้นคั่นก่อนหัวข้อ\n\n**เงื่อนไข:**\n\n- สร้าง `line()` พิมพ์ `----------`\n- เรียก `line()` แล้วพิมพ์ `REPORT` แล้วเรียก `line()` อีกครั้ง",
          "3 บรรทัด", "----------\nREPORT\n----------",
          "# line + REPORT",
          'def line():\n    print("----------")\n\nline()\nprint("REPORT")\nline()'),
        p(8, "ป้ายปิดร้าน", "closed_sign",
          "ตอนปิดร้านต้องแสดงป้าย\n\n**เงื่อนไข:**\n\n- สร้าง `closed()` พิมพ์ `Sorry, we are closed.`\n- เรียก 1 ครั้ง",
          "1 บรรทัด", "Sorry, we are closed.",
          "# closed()",
          'def closed():\n    print("Sorry, we are closed.")\n\nclosed()'),
        p(9, "ทักทายจาก input", "ask_greet",
          "แอปต้อนรับรับชื่อลูกค้าแล้วทักทาย\n\n**เงื่อนไข:**\n\n- สร้าง `greet_guest()` อ่านชื่อด้วย `input()` แล้วพิมพ์ `Welcome, <name>!`\n- เรียก 1 ครั้ง",
          "1 บรรทัด", "Welcome, Mira!",
          "# greet_guest()",
          'def greet_guest():\n    name = input()\n    print(f"Welcome, {name}!")\n\ngreet_guest()',
          sample_in="Mira"),
        p(6, "ใบเสร็จสั้น", "mini_receipt",
          "พิมพ์ใบเสร็จกาแฟหนึ่งรายการ\n\n**เงื่อนไข:**\n\n- สร้าง `print_receipt()` แสดงตามตัวอย่าง\n- เรียก 1 ครั้ง",
          "ใบเสร็จ", "Item : Latte\nPrice: 85\nThank you",
          "# print_receipt()",
          'def print_receipt():\n    print("Item : Latte")\n    print("Price: 85")\n    print("Thank you")\n\nprint_receipt()',
          "จัดข้อความให้ตรงตัวอย่าง"),
        p(7, "นับถอยหลัง 3", "countdown3",
          "จอเกมนับถอยหลังก่อนเริ่ม\n\n**เงื่อนไข:**\n\n- สร้าง `countdown()` พิมพ์ 3 2 1 ด้วยลูป `for` ในฟังก์ชัน\n- หลังลูปพิมพ์ `Go!`\n- เรียก 1 ครั้ง",
          "4 บรรทัด", "3\n2\n1\nGo!",
          "# countdown()",
          'def countdown():\n    for i in range(3, 0, -1):\n        print(i)\n    print("Go!")\n\ncountdown()',
          "ใช้ range นับถอยหลัง หรือพิมพ์ทีละค่า"),
        p(10, "เมนูของหวาน", "dessert_menu",
          "ร้านของหวานมีรายการคงที่\n\n**เงื่อนไข:**\n\n- สร้าง `show_desserts()` พิมพ์ 3 บรรทัดตามตัวอย่าง\n- เรียก 1 ครั้ง",
          "3 บรรทัด", "1. Cake\n2. Cookie\n3. Ice Cream",
          "# show_desserts()",
          'def show_desserts():\n    print("1. Cake")\n    print("2. Cookie")\n    print("3. Ice Cream")\n\nshow_desserts()',
          "พิมพ์ทีละบรรทัดในฟังก์ชัน"),
        p(11, "สรุปยอดคงที่", "fixed_total",
          "บิลมีราคาสินค้า 120 และ 80 รวมในฟังก์ชัน\n\n**เงื่อนไข:**\n\n- สร้าง `show_total()` คำนวณผลรวมแล้วพิมพ์ `Total: <ยอด>`\n- เรียก 1 ครั้ง",
          "1 บรรทัด", "Total: 200",
          "# show_total()",
          'def show_total():\n    a = 120\n    b = 80\n    print(f"Total: {a + b}")\n\nshow_total()',
          "เก็บตัวแปรในฟังก์ชันแล้วบวก"),
        p(12, "ตารางเวรสั้น", "duty_table",
          "พิมพ์ชื่อเวรจาก list ในฟังก์ชัน\n\n**เงื่อนไข:**\n\n- ใน `show_duty()` มี `names = [\"Ann\", \"Ben\", \"Cat\"]`\n- วนพิมพ์แต่ละชื่อ\n- เรียก 1 ครั้ง",
          "3 บรรทัด", "Ann\nBen\nCat",
          "# show_duty()",
          'def show_duty():\n    names = ["Ann", "Ben", "Cat"]\n    for name in names:\n        print(name)\n\nshow_duty()',
          "list อยู่ภายในฟังก์ชัน"),
        p(13, "กล่องประกาศ", "announce_box",
          "พิมพ์กล่องประกาศกิจกรรม\n\n**เงื่อนไข:**\n\n- สร้าง `announce()` แสดงตามตัวอย่าง\n- เรียก 1 ครั้ง",
          "กล่อง", "====================\n   CLUB FAIR DAY\n====================",
          "# announce()",
          'def announce():\n    print("====================")\n    print("   CLUB FAIR DAY")\n    print("====================")\n\nannounce()',
          "นับความยาว = ให้เท่ากัน"),
        p(5, "เครื่องคิดเลขเล็ก", "simple_calc",
          "เครื่องคิดเลขรับตัวเลข 2 ค่าแล้วแสดงผลบวก\n\n**เงื่อนไข:**\n\n- สร้าง `add_two()` อ่านจำนวนเต็ม 2 บรรทัด แล้วพิมพ์ `Sum: <ผลรวม>`\n- เรียก 1 ครั้ง",
          "1 บรรทัด", "Sum: 15",
          "# add_two()",
          'def add_two():\n    a = int(input())\n    b = int(input())\n    print(f"Sum: {a + b}")\n\nadd_two()',
          sample_in="7\n8", hint="รับ input ทั้งสองค่าในฟังก์ชัน"),
        p(14, "ใบเสร็จหลายรายการ", "multi_receipt",
          "พิมพ์รายการราคาจาก list แล้วสรุปยอด\n\n**เงื่อนไข:**\n\n- ใน `bill()` มี `prices = [45, 60, 30]`\n- พิมพ์แต่ละราคาในรูป `Item: <ราคา>`\n- สุดท้ายพิมพ์ `Total: <ผลรวม>`\n- เรียก 1 ครั้ง",
          "4 บรรทัด", "Item: 45\nItem: 60\nItem: 30\nTotal: 135",
          "# bill()",
          'def bill():\n    prices = [45, 60, 30]\n    total = 0\n    for price in prices:\n        print(f"Item: {price}")\n        total += price\n    print(f"Total: {total}")\n\nbill()',
          "สะสมยอดด้วยตัวแปรในลูป"),
        p(15, "รายงานอุณหภูมิ", "temp_report",
          "เซ็นเซอร์อ่านอุณหภูมิหนึ่งค่าแล้วจัดสถานะ\n\n**เงื่อนไข:**\n\n- สร้าง `check_temp()` อ่านจำนวนเต็ม\n- ถ้าอุณหภูมิ >= 30 พิมพ์ `Hot` ไม่งั้น `Cool`\n- เรียก 1 ครั้ง",
          "1 บรรทัด", "Hot",
          "# check_temp()",
          'def check_temp():\n    temp = int(input())\n    if temp >= 30:\n        print("Hot")\n    else:\n        print("Cool")\n\ncheck_temp()',
          sample_in="32", hint="ใช้ if/else ในฟังก์ชัน"),
        p(16, "สองหน้าจอ ATM", "atm_screens",
          "ตู้ ATM มีหน้าจอต้อนรับและหน้าจอยอดเงิน\n\n**เงื่อนไข:**\n\n- สร้าง `welcome()` พิมพ์ `ATM Ready`\n- สร้าง `balance()` พิมพ์ `Balance: 500`\n- เรียก `welcome()` แล้วตามด้วย `balance()`",
          "2 บรรทัด", "ATM Ready\nBalance: 500",
          "# welcome + balance",
          'def welcome():\n    print("ATM Ready")\n\ndef balance():\n    print("Balance: 500")\n\nwelcome()\nbalance()',
          "สองฟังก์ชันแยกงานกัน"),
    ]
    # Fix countdown - range with negative step is NEVER taught!
    # Need to rewrite countdown without negative step
    probs[6] = p(7, "นับถอยหลัง 3", "countdown3",
          "จอเกมนับถอยหลังก่อนเริ่ม\n\n**เงื่อนไข:**\n\n- สร้าง `countdown()` พิมพ์ 3 แล้ว 2 แล้ว 1 แล้ว `Go!`\n- ใช้ list `[3, 2, 1]` วนพิมพ์ได้\n- เรียก 1 ครั้ง",
          "4 บรรทัด", "3\n2\n1\nGo!",
          "# countdown()",
          'def countdown():\n    for n in [3, 2, 1]:\n        print(n)\n    print("Go!")\n\ncountdown()',
          "วน list ตัวเลขแล้วพิมพ์ Go!")
    write_week("037-functions", chapter="Functions", emoji="⚙️", index_md=index, problems=probs)


# ───────── 038 parameters: params, print, no return/defaults ─────────
def week_038():
    items = [
        ("ทักทายชื่อเพื่อน", "พารามิเตอร์ 1 ตัว"),
        ("แสดงราคาสินค้า", "พารามิเตอร์ตัวเลข"),
        ("บวกแล้วพิมพ์", "สองพารามิเตอร์"),
        ("ป้ายอายุ", "ชื่อ+อายุ"),
        ("ส่วนสูงซม.", "พารามิเตอร์เดียว"),
        ("ส่วนลดคงที่", "คำนวณแล้วพิมพ์"),
        ("ตรวจสิทธิ์โหวต", "if ในฟังก์ชัน"),
        ("พื้นที่สี่เหลี่ยม", "กว้าง×สูง"),
        ("BMI สั้น", "คำนวณแล้วพิมพ์"),
        ("หาค่ามากกว่า", "เปรียบเทียบสองค่า"),
        ("ใบเสร็จ 2 รายการ", "หลายพารามิเตอร์"),
        ("ตั๋วหนัง", "อายุ→ราคา"),
        ("เข้าสู่ระบบสั้น", "เทียบรหัส"),
        ("สรุปคะแนน 3 วิชา", "หลายพารามิเตอร์"),
        ("บิลส่วนลดเงื่อนไข", "คำนวณ+if"),
    ]
    index = idx(
        "บท 038 Parameters",
        "พารามิเตอร์ใน `def` · ส่งอาร์กิวเมนต์ตอนเรียก · `print` ในฟังก์ชัน · ความรู้ถึง 037",
        "ห้าม `return` · ห้าม default / keyword argument",
        rows(items),
        "ข้อ 02 ห้าม clone `greet(name)` พิมพ์ Hello name แบบบทเรียนเป๊ะ — เปลี่ยนสถานการณ์",
    )
    probs = [
        p(2, "ทักทายชื่อเพื่อน", "hi_friend",
          "แอปแชททักทายเพื่อน\n\n**เงื่อนไข:**\n\n- สร้าง `hi(name)` พิมพ์ `Hi, <name>!`\n- เรียกกับ `\"Kate\"` และ `\"Leo\"`",
          "2 บรรทัด", "Hi, Kate!\nHi, Leo!",
          "# hi(name)",
          'def hi(name):\n    print(f"Hi, {name}!")\n\nhi("Kate")\nhi("Leo")'),
        p(3, "แสดงราคาสินค้า", "show_price",
          "ชั้นวางแสดงราคา\n\n**เงื่อนไข:**\n\n- สร้าง `show_price(price)` พิมพ์ `Price: <price>`\n- เรียกกับ `99` และ `150`",
          "2 บรรทัด", "Price: 99\nPrice: 150",
          "# show_price",
          'def show_price(price):\n    print(f"Price: {price}")\n\nshow_price(99)\nshow_price(150)'),
        p(4, "บวกแล้วพิมพ์", "add_print",
          "เครื่องคิดเลขบวกสองจำนวนแล้วแสดงผลทันที\n\n**เงื่อนไข:**\n\n- สร้าง `add(a, b)` พิมพ์ผลบวกอย่างเดียว\n- เรียก `add(3, 5)` และ `add(10, 20)`",
          "2 บรรทัด", "8\n30",
          "# add(a, b)",
          "def add(a, b):\n    print(a + b)\n\nadd(3, 5)\nadd(10, 20)"),
        p(8, "ป้ายอายุ", "age_label",
          "ป้ายชื่อนักเรียนพร้อมอายุ\n\n**เงื่อนไข:**\n\n- สร้าง `label(name, age)` พิมพ์ `<name> (<age>)`\n- เรียกกับ `(\"Mew\", 12)` และ `(\"Oak\", 13)`",
          "2 บรรทัด", "Mew (12)\nOak (13)",
          "# label",
          'def label(name, age):\n    print(f"{name} ({age})")\n\nlabel("Mew", 12)\nlabel("Oak", 13)'),
        p(9, "ส่วนสูงซม.", "height_cm",
          "บันทึกส่วนสูงนักกีฬา\n\n**เงื่อนไข:**\n\n- สร้าง `show_height(cm)` พิมพ์ `Height: <cm> cm`\n- เรียกกับ `165` และ `172`",
          "2 บรรทัด", "Height: 165 cm\nHeight: 172 cm",
          "# show_height",
          'def show_height(cm):\n    print(f"Height: {cm} cm")\n\nshow_height(165)\nshow_height(172)'),
        p(6, "ส่วนลดคงที่", "discount20",
          "ร้านลดทันที 20 บาท\n\n**เงื่อนไข:**\n\n- สร้าง `after_discount(price)` พิมพ์ `Pay: <price-20>`\n- เรียกกับ `100` และ `85`",
          "2 บรรทัด", "Pay: 80\nPay: 65",
          "# after_discount",
          'def after_discount(price):\n    print(f"Pay: {price - 20}")\n\nafter_discount(100)\nafter_discount(85)',
          "หัก 20 แล้วพิมพ์"),
        p(7, "ตรวจสิทธิ์โหวต", "check_vote",
          "ตรวจอายุก่อนเข้าคูหา\n\n**เงื่อนไข:**\n\n- สร้าง `check_vote(age)` ถ้า age >= 18 พิมพ์ `Can vote` ไม่งั้น `Too young`\n- เรียกกับ `20` และ `15`",
          "2 บรรทัด", "Can vote\nToo young",
          "# check_vote",
          'def check_vote(age):\n    if age >= 18:\n        print("Can vote")\n    else:\n        print("Too young")\n\ncheck_vote(20)\ncheck_vote(15)',
          "เทียบกับ 18 ในฟังก์ชัน"),
        p(10, "พื้นที่สี่เหลี่ยม", "rect_area_print",
          "คำนวณพื้นที่โต๊ะ\n\n**เงื่อนไข:**\n\n- สร้าง `area(w, h)` พิมพ์ `Area: <w*h>`\n- เรียกกับ `(4, 5)` และ `(3, 7)`",
          "2 บรรทัด", "Area: 20\nArea: 21",
          "# area",
          'def area(w, h):\n    print(f"Area: {w * h}")\n\narea(4, 5)\narea(3, 7)',
          "คูณแล้วพิมพ์"),
        p(11, "BMI สั้น", "bmi_short",
          "เครื่องชั่งคำนวณ BMI แบบหยาบ\n\n**เงื่อนไข:**\n\n- สร้าง `show_bmi(weight, height)` คำนวณ `weight / (height ** 2)` แล้วพิมพ์ `BMI: <ค่า:.1f>`\n- เรียกกับ `(60, 1.70)`",
          "1 บรรทัด", "BMI: 20.8",
          "# show_bmi",
          'def show_bmi(weight, height):\n    bmi = weight / (height ** 2)\n    print(f"BMI: {bmi:.1f}")\n\nshow_bmi(60, 1.70)',
          "ใช้ ** 2 แล้ว :.1f"),
        p(12, "หาค่ามากกว่า", "show_max",
          "เปรียบเทียบคะแนนสองคนแล้วพิมพ์คนที่ได้มากกว่า\n\n**เงื่อนไข:**\n\n- สร้าง `show_higher(a, b)` ถ้า a > b พิมพ์ a ไม่งั้นพิมพ์ b\n- เรียก `(80, 65)` และ `(40, 55)`",
          "2 บรรทัด", "80\n55",
          "# show_higher",
          "def show_higher(a, b):\n    if a > b:\n        print(a)\n    else:\n        print(b)\n\nshow_higher(80, 65)\nshow_higher(40, 55)",
          "เทียบสองพารามิเตอร์"),
        p(13, "ใบเสร็จ 2 รายการ", "two_item_bill",
          "พิมพ์ใบเสร็จสองรายการพร้อมยอดรวม\n\n**เงื่อนไข:**\n\n- สร้าง `bill(item1, price1, item2, price2)` แสดงตามตัวอย่าง\n- เรียก `bill(\"Pen\", 20, \"Book\", 80)`",
          "3 บรรทัด", "Pen: 20\nBook: 80\nTotal: 100",
          "# bill",
          'def bill(item1, price1, item2, price2):\n    print(f"{item1}: {price1}")\n    print(f"{item2}: {price2}")\n    print(f"Total: {price1 + price2}")\n\nbill("Pen", 20, "Book", 80)',
          "พิมพ์ทีละรายการแล้วรวม"),
        p(5, "ตั๋วหนัง", "movie_ticket",
          "ราคาตั๋วตามอายุ\n\n**เงื่อนไข:**\n\n- สร้าง `ticket(age)` ถ้า age < 12 พิมพ์ `Price: 80` ไม่งั้น `Price: 120`\n- เรียกกับ `10` และ `15`",
          "2 บรรทัด", "Price: 80\nPrice: 120",
          "# ticket",
          'def ticket(age):\n    if age < 12:\n        print("Price: 80")\n    else:\n        print("Price: 120")\n\nticket(10)\nticket(15)',
          "เด็กต่ำกว่า 12 จ่ายถูกกว่า"),
        p(14, "เข้าสู่ระบบสั้น", "login_check",
          "ตรวจรหัสผ่านแบบง่าย\n\n**เงื่อนไข:**\n\n- สร้าง `login(password)` ถ้า password เท่ากับ `\"open123\"` พิมพ์ `Access OK` ไม่งั้น `Denied`\n- เรียกกับ `\"open123\"` และ `\"wrong\"`",
          "2 บรรทัด", "Access OK\nDenied",
          "# login",
          'def login(password):\n    if password == "open123":\n        print("Access OK")\n    else:\n        print("Denied")\n\nlogin("open123")\nlogin("wrong")',
          "เทียบสตริงกับรหัสคงที่"),
        p(15, "สรุปคะแนน 3 วิชา", "three_scores",
          "สรุปคะแนนสามวิชาและค่าเฉลี่ยแบบจำนวนเต็มหาร\n\n**เงื่อนไข:**\n\n- สร้าง `report(a, b, c)` พิมพ์ `Sum: ...` และ `Avg: ...` (ใช้ `// 3`)\n- เรียกกับ `(80, 70, 90)`",
          "2 บรรทัด", "Sum: 240\nAvg: 80",
          "# report",
          'def report(a, b, c):\n    total = a + b + c\n    print(f"Sum: {total}")\n    print(f"Avg: {total // 3}")\n\nreport(80, 70, 90)',
          "รวมก่อนแล้วหารลงตัว"),
        p(16, "บิลส่วนลดเงื่อนไข", "bill_if_discount",
          "ซื้อครบ 300 ลด 50 ไม่งั้นไม่ลด\n\n**เงื่อนไข:**\n\n- สร้าง `pay(price)` ถ้า price >= 300 พิมพ์ `Pay: <price-50>` ไม่งั้น `Pay: <price>`\n- เรียกกับ `350` และ `200`",
          "2 บรรทัด", "Pay: 300\nPay: 200",
          "# pay",
          'def pay(price):\n    if price >= 300:\n        print(f"Pay: {price - 50}")\n    else:\n        print(f"Pay: {price}")\n\npay(350)\npay(200)',
          "เช็กเกณฑ์ 300 ก่อนหัก"),
    ]
    write_week("038-parameters", chapter="Parameters", emoji="📥", index_md=index, problems=probs)


# ───────── 039 return: avoid grade 80/70/60 clone ─────────
def week_039():
    items = [
        ("กำลังสอง", "return ค่าคำนวณ"),
        ("เช็กเลขคู่", "return True/False"),
        ("พื้นที่วงกลมหยาบ", "return ค่า"),
        ("ค่าสัมบูรณ์แบบง่าย", "if + return"),
        ("ส่วนลดเปอร์เซ็นต์", "return ราคาใหม่"),
        ("ผ่าน/ไม่ผ่านเกณฑ์", "return สตริง"),
        ("แปลง ซม.→ม.", "return float"),
        ("clamp คะแนน 0-100", "หลาย return"),
        ("อุณหภูมิเป็น F", "สูตรแปลง"),
        ("ค่าตั๋วตามอายุ", "return ตัวเลข"),
        ("ผลคูณสะสม 1..n", "ลูป+return"),
        ("หาค่ามากกว่า (return)", "เปรียบเทียบ"),
        ("สถานะกระเป๋าเงิน", "หลายเกณฑ์"),
        ("คะแนนโบนัสคู่/คี่", "คำนวณ+return"),
        ("สรุปออเดอร์อาหาร", "หลายฟังก์ชัน"),
    ]
    index = idx(
        "บท 039 Return Values",
        "`return` · เก็บค่าที่คืน · return ใน if/elif/else · ความรู้ถึง 038",
        "ห้าม clone เกรด 80/70/60 → A/B/C/F จากบทเรียน · ห้าม return หลายค่าพร้อมกัน",
        rows(items),
        "หลีกเลี่ยง get_grade แบบ 80/70/60 — ใช้สถานการณ์อื่นแทน",
    )
    probs = [
        p(2, "กำลังสอง", "square_n",
          "เครื่องคิดเลขยกกำลังสอง\n\n**เงื่อนไข:**\n\n- สร้าง `square(n)` ที่ `return n * n`\n- พิมพ์ผลของ `square(5)` `square(4)` `square(10)`",
          "3 บรรทัด", "25\n16\n100",
          "def square(n):\n    # return\n    pass\n\nprint(square(5))\nprint(square(4))\nprint(square(10))",
          "def square(n):\n    return n * n\n\nprint(square(5))\nprint(square(4))\nprint(square(10))"),
        p(3, "เช็กเลขคู่", "is_even_ret",
          "ตรวจเลขคู่ว่า True หรือ False\n\n**เงื่อนไข:**\n\n- สร้าง `is_even(n)` คืน True ถ้าหาร 2 ลงตัว ไม่งั้น False\n- พิมพ์ผลของ `is_even(8)` และ `is_even(7)`",
          "2 บรรทัด", "True\nFalse",
          "def is_even(n):\n    # return\n    pass\n\nprint(is_even(8))\nprint(is_even(7))",
          "def is_even(n):\n    if n % 2 == 0:\n        return True\n    else:\n        return False\n\nprint(is_even(8))\nprint(is_even(7))"),
        p(4, "พื้นที่วงกลมหยาบ", "circle_area",
          "ใช้สูตรหยาบ area = 3 * r * r\n\n**เงื่อนไข:**\n\n- สร้าง `circle_area(r)` คืนค่าพื้นที่\n- พิมพ์ผลของ `circle_area(2)` และ `circle_area(5)`",
          "2 บรรทัด", "12\n75",
          "def circle_area(r):\n    # return\n    pass\n\nprint(circle_area(2))\nprint(circle_area(5))",
          "def circle_area(r):\n    return 3 * r * r\n\nprint(circle_area(2))\nprint(circle_area(5))"),
        p(8, "ค่าสัมบูรณ์แบบง่าย", "abs_simple",
          "ถ้าติดลบให้กลับเป็นบวก\n\n**เงื่อนไข:**\n\n- สร้าง `make_positive(n)` ถ้า n < 0 คืน -n ไม่งั้นคืน n\n- พิมพ์ผลของ `-5` และ `8`",
          "2 บรรทัด", "5\n8",
          "def make_positive(n):\n    # return\n    pass\n\nprint(make_positive(-5))\nprint(make_positive(8))",
          "def make_positive(n):\n    if n < 0:\n        return -n\n    else:\n        return n\n\nprint(make_positive(-5))\nprint(make_positive(8))"),
        p(9, "ส่วนลดเปอร์เซ็นต์", "pct_off",
          "ลด 10% จากราคา\n\n**เงื่อนไข:**\n\n- สร้าง `ten_off(price)` คืน `price * 0.9`\n- พิมพ์ผลของ `100` และ `250` ด้วยทศนิยม 1 ตำแหน่งใน f-string นอกฟังก์ชัน\n- ตัวอย่างแสดง `90.0` และ `225.0`",
          "2 บรรทัด", "90.0\n225.0",
          "def ten_off(price):\n    # return\n    pass\n\nprint(ten_off(100))\nprint(ten_off(250))",
          "def ten_off(price):\n    return price * 0.9\n\nprint(ten_off(100))\nprint(ten_off(250))"),
        p(6, "ผ่าน/ไม่ผ่านเกณฑ์", "pass_fail_ret",
          "เกณฑ์ผ่านสนามวิ่งคือเวลาไม่เกิน 60 วินาที\n\n**เงื่อนไข:**\n\n- สร้าง `race_result(seconds)` คืน `Pass` ถ้า seconds <= 60 ไม่งั้น `Fail`\n- พิมพ์ผลของ `55` และ `72`",
          "2 บรรทัด", "Pass\nFail",
          "def race_result(seconds):\n    # return\n    pass\n\nprint(race_result(55))\nprint(race_result(72))",
          'def race_result(seconds):\n    if seconds <= 60:\n        return "Pass"\n    else:\n        return "Fail"\n\nprint(race_result(55))\nprint(race_result(72))',
          "คืนสตริง ไม่ใช่พิมพ์ในฟังก์ชัน"),
        p(7, "แปลง ซม.→ม.", "cm_to_m",
          "แปลงเซนติเมตรเป็นเมตร\n\n**เงื่อนไข:**\n\n- สร้าง `to_meters(cm)` คืน `cm / 100`\n- พิมพ์ผลของ `175` และ `200`",
          "2 บรรทัด", "1.75\n2.0",
          "def to_meters(cm):\n    # return\n    pass\n\nprint(to_meters(175))\nprint(to_meters(200))",
          "def to_meters(cm):\n    return cm / 100\n\nprint(to_meters(175))\nprint(to_meters(200))",
          "หาร 100 แล้ว return"),
        p(10, "clamp คะแนน 0-100", "clamp_score",
          "บังคับคะแนนให้อยู่ระหว่าง 0 ถึง 100\n\n**เงื่อนไข:**\n\n- สร้าง `clamp(score)` ถ้า < 0 คืน 0 ถ้า > 100 คืน 100 ไม่งั้นคืน score\n- พิมพ์ผลของ `-5` `40` `150`",
          "3 บรรทัด", "0\n40\n100",
          "def clamp(score):\n    # return\n    pass\n\nprint(clamp(-5))\nprint(clamp(40))\nprint(clamp(150))",
          "def clamp(score):\n    if score < 0:\n        return 0\n    elif score > 100:\n        return 100\n    else:\n        return score\n\nprint(clamp(-5))\nprint(clamp(40))\nprint(clamp(150))",
          "ใช้ if/elif/else คืนค่า"),
        p(11, "อุณหภูมิเป็น F", "c_to_f",
          "แปลงองศา C เป็น F ด้วยสูตร `c * 9 / 5 + 32`\n\n**เงื่อนไข:**\n\n- สร้าง `to_f(c)` คืนค่า F\n- พิมพ์ผลของ `0` และ `100`",
          "2 บรรทัด", "32.0\n212.0",
          "def to_f(c):\n    # return\n    pass\n\nprint(to_f(0))\nprint(to_f(100))",
          "def to_f(c):\n    return c * 9 / 5 + 32\n\nprint(to_f(0))\nprint(to_f(100))",
          "ใช้สูตรแล้ว return"),
        p(12, "ค่าตั๋วตามอายุ", "fare_by_age",
          "ค่าโดยสาร: อายุ < 6 ฟรี (0) อายุ < 18 จ่าย 20 นอกนั้น 40\n\n**เงื่อนไข:**\n\n- สร้าง `fare(age)` คืนตัวเลขราคา\n- พิมพ์ผลของ `4` `10` `30`",
          "3 บรรทัด", "0\n20\n40",
          "def fare(age):\n    # return\n    pass\n\nprint(fare(4))\nprint(fare(10))\nprint(fare(30))",
          "def fare(age):\n    if age < 6:\n        return 0\n    elif age < 18:\n        return 20\n    else:\n        return 40\n\nprint(fare(4))\nprint(fare(10))\nprint(fare(30))",
          "คืนตัวเลขราคา ไม่พิมพ์ในฟังก์ชัน"),
        p(13, "ผลคูณสะสม 1..n", "product_to_n",
          "หาผลคูณ 1*2*...*n\n\n**เงื่อนไข:**\n\n- สร้าง `product(n)` คืนผลคูณ\n- พิมพ์ผลของ `4` และ `5`",
          "2 บรรทัด", "24\n120",
          "def product(n):\n    # return\n    pass\n\nprint(product(4))\nprint(product(5))",
          "def product(n):\n    result = 1\n    for i in range(1, n + 1):\n        result *= i\n    return result\n\nprint(product(4))\nprint(product(5))",
          "สะสมในลูปแล้ว return"),
        p(5, "หาค่ามากกว่า (return)", "max2_ret",
          "คืนค่าที่มากกว่าระหว่างสองจำนวน\n\n**เงื่อนไข:**\n\n- สร้าง `bigger(a, b)` คืนค่าที่มากกว่า (เท่ากันคืน a ก็ได้)\n- พิมพ์ผลของ `(9, 4)` และ `(3, 8)`",
          "2 บรรทัด", "9\n8",
          "def bigger(a, b):\n    # return\n    pass\n\nprint(bigger(9, 4))\nprint(bigger(3, 8))",
          "def bigger(a, b):\n    if a >= b:\n        return a\n    else:\n        return b\n\nprint(bigger(9, 4))\nprint(bigger(3, 8))",
          "เทียบแล้ว return ค่า"),
        p(14, "สถานะกระเป๋าเงิน", "wallet_status",
          "สถานะเงินในกระเป๋า\n\n**เงื่อนไข:**\n\n- สร้าง `wallet_status(money)` คืน `Broke` ถ้า money < 50, `OK` ถ้า < 200, ไม่งั้น `Rich`\n- พิมพ์ผลของ `30` `120` `500`",
          "3 บรรทัด", "Broke\nOK\nRich",
          "def wallet_status(money):\n    # return\n    pass\n\nprint(wallet_status(30))\nprint(wallet_status(120))\nprint(wallet_status(500))",
          'def wallet_status(money):\n    if money < 50:\n        return "Broke"\n    elif money < 200:\n        return "OK"\n    else:\n        return "Rich"\n\nprint(wallet_status(30))\nprint(wallet_status(120))\nprint(wallet_status(500))',
          "ใช้ elif หลายขั้น คืนสตริง"),
        p(15, "คะแนนโบนัสคู่/คี่", "bonus_parity",
          "ถ้าคะแนนเป็นคู่ได้โบนัส +5 ถ้าคี่ +3\n\n**เงื่อนไข:**\n\n- สร้าง `with_bonus(score)` คืนคะแนนหลังโบนัส\n- พิมพ์ผลของ `10` และ `7`",
          "2 บรรทัด", "15\n10",
          "def with_bonus(score):\n    # return\n    pass\n\nprint(with_bonus(10))\nprint(with_bonus(7))",
          "def with_bonus(score):\n    if score % 2 == 0:\n        return score + 5\n    else:\n        return score + 3\n\nprint(with_bonus(10))\nprint(with_bonus(7))",
          "เช็กคู่/คี่แล้วบวก"),
        p(16, "สรุปออเดอร์อาหาร", "food_order",
          "คำนวณราคารวมแล้วคิด VAT 7%\n\n**เงื่อนไข:**\n\n- สร้าง `subtotal(a, b)` คืน a+b\n- สร้าง `with_vat(amount)` คืน amount * 1.07\n- พิมพ์ `with_vat(subtotal(100, 50))` ด้วยทศนิยม 2 ตำแหน่ง",
          "1 บรรทัด", "160.50",
          "def subtotal(a, b):\n    # return\n    pass\n\ndef with_vat(amount):\n    # return\n    pass\n\nprint(f\"{with_vat(subtotal(100, 50)):.2f}\")",
          "def subtotal(a, b):\n    return a + b\n\ndef with_vat(amount):\n    return amount * 1.07\n\nprint(f\"{with_vat(subtotal(100, 50)):.2f}\")",
          "ประกอบสองฟังก์ชันด้วย return"),
    ]
    # Fix starter with pass - check if pass is flagged. NEVER_TAUGHT doesn't include pass.
    # But pass is "used never explained" - better avoid pass in starters, use comments only.
    for i, pr in enumerate(probs):
        if "pass\n" in pr["starter"]:
            probs[i] = dict(pr)
            probs[i]["starter"] = pr["starter"].replace("    pass\n", "    # เขียนโค้ดตรงนี้\n")
    write_week("039-return-values", chapter="Return Values", emoji="↩️", index_md=index, problems=probs)


# ───────── 040 reshape: sum() OK, standard 5+6+4 ─────────
def week_040():
    items = [
        ("ผลรวม list", "return ผลรวม"),
        ("ค่าเฉลี่ย list", "sum/len"),
        ("นับผ่านเกณฑ์", "นับในลูป"),
        ("แปลง C→F", "return สูตร"),
        ("แสดงนักเรียนจาก dict", "วน .items()"),
        ("บิล+VAT สองฟังก์ชัน", "ประกอบฟังก์ชัน"),
        ("กรองคะแนนผ่าน", "สร้าง list ใหม่"),
        ("เครื่องคิดเลขสองปุ่ม", "add/mul"),
        ("เพิ่มชื่อเข้าค่าย", "append ในฟังก์ชัน"),
        ("อุณหภูมิสองทาง", "to_f / to_c"),
        ("สรุปตะกร้า", "list ราคา"),
        ("ระบบคะแนน dict", "หลายฟังก์ชัน"),
        ("กระเป๋าเงินเกม", "dict + ฟังก์ชัน"),
        ("ห้องสมุดยืม", "list หนังสือ"),
        ("ตัวละคร HP", "dict สถานะ"),
    ]
    index = idx(
        "บท 040 Function Practice",
        "ฝึกประกอบฟังก์ชันกับ list/dict · `sum()` ใช้ได้ · ความรู้ถึง 039",
        "ห้าม default/keyword args · ห้าม clone เกรด 80/70/60 จากบทเรียนเป็นโจทย์หลัก",
        rows(items),
        "ดัดแปลงจากชุดเดิมให้เข้ามาตรฐาน 5+6+4 และรูปแบบตัวอย่าง text block",
    )
    probs = [
        p(2, "ผลรวม list", "list_sum",
          "คิดยอดรวมราคาในตะกร้า\n\n**เงื่อนไข:**\n\n- สร้าง `list_sum(numbers)` คืนผลรวม\n- พิมพ์ผลของสอง list ตามตัวอย่าง",
          "2 บรรทัด", "150\n413",
          "def list_sum(numbers):\n    # เขียนโค้ดตรงนี้\n    ...\n\nprint(list_sum([10, 20, 30, 40, 50]))\nprint(list_sum([78, 85, 92, 70, 88]))",
          "def list_sum(numbers):\n    total = 0\n    for n in numbers:\n        total += n\n    return total\n\nprint(list_sum([10, 20, 30, 40, 50]))\nprint(list_sum([78, 85, 92, 70, 88]))"),
        p(3, "ค่าเฉลี่ย list", "avg_list",
          "หาค่าเฉลี่ยคะแนนด้วย `sum` และ `len`\n\n**เงื่อนไข:**\n\n- สร้าง `average(scores)` คืน `sum(scores) / len(scores)`\n- พิมพ์ผลของ `[80, 90, 100]` ด้วยทศนิยม 1 ตำแหน่ง",
          "1 บรรทัด", "90.0",
          "def average(scores):\n    # เขียนโค้ดตรงนี้\n    ...\n\nprint(average([80, 90, 100]))",
          "def average(scores):\n    return sum(scores) / len(scores)\n\nprint(average([80, 90, 100]))"),
        p(4, "นับผ่านเกณฑ์", "count_pass",
          "นับจำนวนคะแนนที่ >= 50\n\n**เงื่อนไข:**\n\n- สร้าง `count_pass(scores)` คืนจำนวนที่ผ่าน\n- พิมพ์ผลของ `[40, 55, 70, 30, 90]`",
          "1 บรรทัด", "3",
          "def count_pass(scores):\n    # เขียนโค้ดตรงนี้\n    ...\n\nprint(count_pass([40, 55, 70, 30, 90]))",
          "def count_pass(scores):\n    count = 0\n    for s in scores:\n        if s >= 50:\n            count += 1\n    return count\n\nprint(count_pass([40, 55, 70, 30, 90]))"),
        p(8, "แปลง C→F", "c_to_f_func",
          "แปลงอุณหภูมิ\n\n**เงื่อนไข:**\n\n- สร้าง `to_f(c)` คืน `c * 9 / 5 + 32`\n- พิมพ์ผลของ `25`",
          "1 บรรทัด", "77.0",
          "def to_f(c):\n    # เขียนโค้ดตรงนี้\n    ...\n\nprint(to_f(25))",
          "def to_f(c):\n    return c * 9 / 5 + 32\n\nprint(to_f(25))"),
        p(9, "แสดงนักเรียนจาก dict", "show_student",
          "แสดงข้อมูลนักเรียนจาก dict\n\n**เงื่อนไข:**\n\n- สร้าง `show_student(student)` วน `.items()` พิมพ์ `key: value`\n- เรียกกับ `{\"name\": \"Alice\", \"score\": 92}`",
          "2 บรรทัด", "name: Alice\nscore: 92",
          'def show_student(student):\n    # เขียนโค้ดตรงนี้\n    ...\n\nshow_student({"name": "Alice", "score": 92})',
          'def show_student(student):\n    for key, value in student.items():\n        print(f"{key}: {value}")\n\nshow_student({"name": "Alice", "score": 92})'),
        p(6, "บิล+VAT สองฟังก์ชัน", "bill_vat",
          "รวมราคาสินค้าแล้วคิด VAT 7%\n\n**เงื่อนไข:**\n\n- `calc_total(prices)` คืนผลรวม\n- `add_vat(total)` คืน total * 1.07\n- พิมพ์ `add_vat(calc_total([100, 50]))` ทศนิยม 2 ตำแหน่ง",
          "1 บรรทัด", "160.50",
          "def calc_total(prices):\n    # เขียนโค้ดตรงนี้\n    ...\n\ndef add_vat(total):\n    # เขียนโค้ดตรงนี้\n    ...\n\nprint(f\"{add_vat(calc_total([100, 50])):.2f}\")",
          "def calc_total(prices):\n    total = 0\n    for p in prices:\n        total += p\n    return total\n\ndef add_vat(total):\n    return total * 1.07\n\nprint(f\"{add_vat(calc_total([100, 50])):.2f}\")",
          "ประกอบสองฟังก์ชัน"),
        p(7, "กรองคะแนนผ่าน", "filter_pass",
          "เก็บเฉพาะคะแนนที่ >= 60 เป็น list ใหม่\n\n**เงื่อนไข:**\n\n- สร้าง `get_passed(scores)` คืน list ที่ผ่าน\n- พิมพ์ผลของ `[50, 60, 75, 40, 90]`",
          "1 บรรทัด", "[60, 75, 90]",
          "def get_passed(scores):\n    # เขียนโค้ดตรงนี้\n    ...\n\nprint(get_passed([50, 60, 75, 40, 90]))",
          "def get_passed(scores):\n    result = []\n    for s in scores:\n        if s >= 60:\n            result.append(s)\n    return result\n\nprint(get_passed([50, 60, 75, 40, 90]))",
          "สร้าง list ว่างแล้ว append"),
        p(10, "เครื่องคิดเลขสองปุ่ม", "add_mul",
          "มีปุ่มบวกและคูณ\n\n**เงื่อนไข:**\n\n- `add(a, b)` และ `mul(a, b)` คืนผล\n- พิมพ์ `add(3, 4)` และ `mul(3, 4)`",
          "2 บรรทัด", "7\n12",
          "def add(a, b):\n    # เขียนโค้ดตรงนี้\n    ...\n\ndef mul(a, b):\n    # เขียนโค้ดตรงนี้\n    ...\n\nprint(add(3, 4))\nprint(mul(3, 4))",
          "def add(a, b):\n    return a + b\n\ndef mul(a, b):\n    return a * b\n\nprint(add(3, 4))\nprint(mul(3, 4))",
          "แต่ละฟังก์ชัน return ค่า"),
        p(11, "เพิ่มชื่อเข้าค่าย", "camp_names",
          "เพิ่มชื่อเข้า list แล้วแสดงทั้งหมด\n\n**เงื่อนไข:**\n\n- `add_name(names, name)` ใช้ append แล้วคืน names\n- `show_names(names)` พิมพ์ทีละชื่อ\n- เริ่มจาก `[]` เพิ่ม `\"Ann\"` กับ `\"Ben\"` แล้ว show",
          "2 บรรทัด", "Ann\nBen",
          "def add_name(names, name):\n    # เขียนโค้ดตรงนี้\n    ...\n\ndef show_names(names):\n    # เขียนโค้ดตรงนี้\n    ...\n\nnames = []\nnames = add_name(names, \"Ann\")\nnames = add_name(names, \"Ben\")\nshow_names(names)",
          'def add_name(names, name):\n    names.append(name)\n    return names\n\ndef show_names(names):\n    for n in names:\n        print(n)\n\nnames = []\nnames = add_name(names, "Ann")\nnames = add_name(names, "Ben")\nshow_names(names)',
          "append แล้วคืน list เดิม"),
        p(12, "อุณหภูมิสองทาง", "temp_both",
          "แปลงสองทิศทาง\n\n**เงื่อนไข:**\n\n- `to_f(c)` คืน c*9/5+32\n- `to_c(f)` คืน (f-32)*5/9\n- พิมพ์ `to_f(0)` และ `to_c(32)`",
          "2 บรรทัด", "32.0\n0.0",
          "def to_f(c):\n    # เขียนโค้ดตรงนี้\n    ...\n\ndef to_c(f):\n    # เขียนโค้ดตรงนี้\n    ...\n\nprint(to_f(0))\nprint(to_c(32))",
          "def to_f(c):\n    return c * 9 / 5 + 32\n\ndef to_c(f):\n    return (f - 32) * 5 / 9\n\nprint(to_f(0))\nprint(to_c(32))",
          "ระวังวงเล็บใน to_c"),
        p(13, "สรุปตะกร้า", "cart_summary",
          "สรุปจำนวนชิ้นและยอดรวม\n\n**เงื่อนไข:**\n\n- `cart_info(prices)` คืน dict `{\"count\": จำนวน, \"total\": ผลรวม}`\n- พิมพ์ผลของ `[25, 40, 35]`",
          "1 บรรทัด", "{'count': 3, 'total': 100}",
          "def cart_info(prices):\n    # เขียนโค้ดตรงนี้\n    ...\n\nprint(cart_info([25, 40, 35]))",
          'def cart_info(prices):\n    total = 0\n    for p in prices:\n        total += p\n    return {"count": len(prices), "total": total}\n\nprint(cart_info([25, 40, 35]))',
          "สร้าง dict แล้ว return"),
        p(5, "ระบบคะแนน dict", "score_system",
          "เก็บคะแนนนักเรียนใน dict\n\n**เงื่อนไข:**\n\n- `add_score(scores, name, score)` ใส่คะแนนแล้วคืน scores\n- `get_average(scores)` คืนค่าเฉลี่ยจาก `.values()`\n- เพิ่ม Alice=80 Bob=100 แล้วพิมพ์ค่าเฉลี่ย",
          "1 บรรทัด", "90.0",
          "def add_score(scores, name, score):\n    # เขียนโค้ดตรงนี้\n    ...\n\ndef get_average(scores):\n    # เขียนโค้ดตรงนี้\n    ...\n\nscores = {}\nscores = add_score(scores, \"Alice\", 80)\nscores = add_score(scores, \"Bob\", 100)\nprint(get_average(scores))",
          'def add_score(scores, name, score):\n    scores[name] = score\n    return scores\n\ndef get_average(scores):\n    total = 0\n    for v in scores.values():\n        total += v\n    return total / len(scores)\n\nscores = {}\nscores = add_score(scores, "Alice", 80)\nscores = add_score(scores, "Bob", 100)\nprint(get_average(scores))',
          "ใช้ .values() รวมคะแนน"),
        p(14, "กระเป๋าเงินเกม", "wallet_game",
          "กระเป๋าเงินในเกม\n\n**เงื่อนไข:**\n\n- `add_money(wallet, amount)` เพิ่มเงินใน `wallet[\"coin\"]`\n- `spend_money(wallet, amount)` ลดเงิน\n- `show_wallet(wallet)` พิมพ์ `Coins: <จำนวน>`\n- เริ่ม `{ \"coin\": 100 }` เพิ่ม 50 ใช้ 30 แล้ว show",
          "1 บรรทัด", "Coins: 120",
          'def add_money(wallet, amount):\n    # เขียนโค้ดตรงนี้\n    ...\n\ndef spend_money(wallet, amount):\n    # เขียนโค้ดตรงนี้\n    ...\n\ndef show_wallet(wallet):\n    # เขียนโค้ดตรงนี้\n    ...\n\nwallet = {"coin": 100}\nadd_money(wallet, 50)\nspend_money(wallet, 30)\nshow_wallet(wallet)',
          'def add_money(wallet, amount):\n    wallet["coin"] = wallet["coin"] + amount\n\ndef spend_money(wallet, amount):\n    wallet["coin"] = wallet["coin"] - amount\n\ndef show_wallet(wallet):\n    print(f"Coins: {wallet[\'coin\']}")\n\nwallet = {"coin": 100}\nadd_money(wallet, 50)\nspend_money(wallet, 30)\nshow_wallet(wallet)',
          "แก้ค่าใน dict ผ่าน key"),
        p(15, "ห้องสมุดยืม", "library_books",
          "เพิ่มหนังสือและนับจำนวน\n\n**เงื่อนไข:**\n\n- `add_book(books, title)` append แล้วคืน books\n- `count_books(books)` คืน len\n- `show_books(books)` พิมพ์ทีละเล่ม\n- เพิ่ม Python กับ Math แล้วพิมพ์จำนวน และรายชื่อ",
          "3 บรรทัด", "2\nPython\nMath",
          'def add_book(books, title):\n    # เขียนโค้ดตรงนี้\n    ...\n\ndef count_books(books):\n    # เขียนโค้ดตรงนี้\n    ...\n\ndef show_books(books):\n    # เขียนโค้ดตรงนี้\n    ...\n\nbooks = []\nbooks = add_book(books, "Python")\nbooks = add_book(books, "Math")\nprint(count_books(books))\nshow_books(books)',
          'def add_book(books, title):\n    books.append(title)\n    return books\n\ndef count_books(books):\n    return len(books)\n\ndef show_books(books):\n    for b in books:\n        print(b)\n\nbooks = []\nbooks = add_book(books, "Python")\nbooks = add_book(books, "Math")\nprint(count_books(books))\nshow_books(books)',
          "แยกหน้าที่แต่ละฟังก์ชัน"),
        p(16, "ตัวละคร HP", "rpg_hp",
          "ตัวละครมีเลือด\n\n**เงื่อนไข:**\n\n- `create_player(name)` คืน `{\"name\": name, \"hp\": 100}`\n- `take_damage(player, dmg)` ลด hp\n- `is_alive(player)` คืน True ถ้า hp > 0\n- `show_status(player)` พิมพ์ `Name: ... / HP: ...`\n- สร้าง Hero โดน 40 แล้ว show และพิมพ์ is_alive",
          "3 บรรทัด", "Name: Hero\nHP: 60\nTrue",
          'def create_player(name):\n    # เขียนโค้ดตรงนี้\n    ...\n\ndef take_damage(player, dmg):\n    # เขียนโค้ดตรงนี้\n    ...\n\ndef is_alive(player):\n    # เขียนโค้ดตรงนี้\n    ...\n\ndef show_status(player):\n    # เขียนโค้ดตรงนี้\n    ...\n\np = create_player("Hero")\ntake_damage(p, 40)\nshow_status(p)\nprint(is_alive(p))',
          'def create_player(name):\n    return {"name": name, "hp": 100}\n\ndef take_damage(player, dmg):\n    player["hp"] = player["hp"] - dmg\n\ndef is_alive(player):\n    if player["hp"] > 0:\n        return True\n    else:\n        return False\n\ndef show_status(player):\n    print(f"Name: {player[\'name\']}")\n    print(f"HP: {player[\'hp\']}")\n\np = create_player("Hero")\ntake_damage(p, 40)\nshow_status(p)\nprint(is_alive(p))',
          "dict เก็บสถานะ แก้ผ่าน key"),
    ]
    # Remove `...` from starters (ellipsis may confuse); use comment only
    for i, pr in enumerate(probs):
        s = pr["starter"].replace("    ...\n", "")
        probs[i] = dict(pr)
        probs[i]["starter"] = s
    write_week("040-function-practice", chapter="Function Practice", emoji="🧩", index_md=index, problems=probs)


if __name__ == "__main__":
    week_037()
    week_038()
    week_039()
    week_040()
