# -*- coding: utf-8 -*-
"""Expand weeks 025-028 to 15-problem standard."""
from _expand_helpers import write_week

NO_IN = "ไม่มี (กำหนดค่าในโปรแกรม)"


def p(n, title, slug, body, out_desc, sample_out, starter, answer, hint=None, sample_in=None, in_desc=None):
    return {
        "n": n, "title": title, "slug": slug, "body": body,
        "input_desc": in_desc if in_desc is not None else (NO_IN if sample_in is None else "ดูตัวอย่าง"),
        "output_desc": out_desc, "sample_input": sample_in, "sample_output": sample_out,
        "hint": hint, "starter": starter, "answer": answer,
    }


def idx(title, scope, bans, rows, notes=""):
    table = "\n".join(f"| {i} | `{a}` | {b} | {c} | {d} |" for i, (a, b, c, d) in enumerate(rows, 1))
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


# ─── 025 lists ───────────────────────────────────────────────────────────────
# Scope: index / neg index / for / len — NO append/remove/sort, no print(whole list) required

write_week(
    "025-lists",
    chapter="Lists",
    emoji="📋",
    index_md=idx(
        "บท 025 Lists",
        "list literal · indexing `[0]` · negative index `[-1]` · `len()` · `for x in list` · รวมด้วย `+=`",
        "ไม่มี `.append()` / `.remove()` / `.sort()` (บท 026) · ไม่มี `in` (บท 030) · ไม่มี `min()`/`max()`",
        [
            ("02_test.md", "🟢", "ป้ายชั้นเรียนหน้า-หลัง", "index แรกและท้าย"),
            ("03_test.md", "🟢", "เมนูของว่างสามอย่าง", "วน for พิมพ์สมาชิก"),
            ("04_test.md", "🟢", "นับจำนวนเพื่อนในกลุ่ม", "ใช้ len อย่างเดียว"),
            ("08_easy.md", "🟢", "ราคาตั๋วที่นั่งกลาง", "index กลางของ list"),
            ("09_easy.md", "🟢", "ของชิ้นรองสุดท้าย", "negative index [-2]"),
            ("06_medium.md", "🟡", "รวมคะแนนแบบทดสอบ", "accumulator + for"),
            ("07_medium.md", "🟡", "ป้ายชั้นเรียนพร้อมเลขที่", "นับเองใน loop"),
            ("10_medium.md", "🟡", "อุณหภูมิสูงสุดรายวัน", "หาค่าสูงสุดด้วยมือ"),
            ("11_medium.md", "🟡", "ค่าเฉลี่ยอุณหภูมิ", "รวม / len"),
            ("12_medium.md", "🟡", "หัวท้ายของคิว", "index + กล่องสรุป"),
            ("13_medium.md", "🟡", "นับของที่ราคาแพง", "if ใน loop + นับ"),
            ("05_challenge.md", "🔴", "ใบสรุปเมนูร้านกาแฟ", "วนพิมพ์ + len + รวม"),
            ("14_challenge.md", "🔴", "รายงานคะแนนสอบ", "Pass/Fail รายคน + สรุป"),
            ("15_challenge.md", "🔴", "สรุปยอดขาย 4 วัน", "รวม + เฉลี่ย + สูงสุด"),
            ("16_challenge.md", "🔴", "ป้ายชั้นเรียนแบบกล่อง", "index + for + กรอบ"),
        ],
        "- ข้อ 02 ไม่ซ้ำตัวอย่าง fruits/scores ในบทเรียน — ใช้สถานการณ์ชั้นเรียน\n"
        "- ห้าม `.append`/`.remove`/`.sort` และห้าม `in`\n"
        "- หาค่าสูงสุดใช้ loop เทียบเอง ห้าม `max()`",
    ),
    problems=[
        p(2, "ป้ายชั้นเรียนหน้า-หลัง", "class_ends",
          "ครูอยากโชว์ชื่อนักเรียนคนแรกและคนสุดท้ายในแถวบนจอ\n\n"
          "กำหนด `students = [\"Ann\", \"Ben\", \"Cara\", \"Dan\"]`\n\n"
          "แสดงชื่อคนแรกบรรทัดหนึ่ง และคนสุดท้ายอีกบรรทัด",
          "ชื่อ 2 บรรทัด", "Ann\nDan",
          'students = ["Ann", "Ben", "Cara", "Dan"]\n\n# เขียนโค้ดตรงนี้',
          'students = ["Ann", "Ben", "Cara", "Dan"]\nprint(students[0])\nprint(students[-1])'),
        p(3, "เมนูของว่างสามอย่าง", "snack_menu",
          "ร้านของว่างติดป้ายเมนูสั้นๆ บนจอ\n\n"
          "กำหนด `snacks = [\"Cookie\", \"Chips\", \"Jelly\"]`\n\n"
          "วนพิมพ์ชื่อของว่างทีละบรรทัด",
          "ชื่อของว่าง 3 บรรทัด", "Cookie\nChips\nJelly",
          'snacks = ["Cookie", "Chips", "Jelly"]\n\n# เขียนโค้ดตรงนี้',
          'snacks = ["Cookie", "Chips", "Jelly"]\nfor snack in snacks:\n    print(snack)'),
        p(4, "นับจำนวนเพื่อนในกลุ่ม", "friend_count",
          "แอปนับจำนวนเพื่อนในกลุ่มแชท\n\n"
          "กำหนด `friends = [\"Mew\", \"Pim\", \"Ohm\", \"Fern\", \"Beam\"]`\n\n"
          "แสดงจำนวนเพื่อนในรูปแบบ `Friends: N`",
          "บรรทัดเดียว", "Friends: 5",
          'friends = ["Mew", "Pim", "Ohm", "Fern", "Beam"]\n\n# เขียนโค้ดตรงนี้',
          'friends = ["Mew", "Pim", "Ohm", "Fern", "Beam"]\nprint(f"Friends: {len(friends)}")'),
        p(8, "ราคาตั๋วที่นั่งกลาง", "middle_seat",
          "โรงหนังมีราคาตั๋วตามแถว 3 แถว อยากรู้ราคาแถวกลาง\n\n"
          "กำหนด `prices = [120, 180, 250]`\n\n"
          "แสดงราคาแถวกลางในรูปแบบ `Middle: 180`",
          "บรรทัดเดียว", "Middle: 180",
          "prices = [120, 180, 250]\n\n# เขียนโค้ดตรงนี้",
          'prices = [120, 180, 250]\nprint(f"Middle: {prices[1]}")'),
        p(9, "ของชิ้นรองสุดท้าย", "second_last",
          "คลังสินค้าอยากดูชื่อสินค้าชิ้นรองสุดท้ายในกล่อง\n\n"
          "กำหนด `items = [\"Pen\", \"Book\", \"Glue\", \"Tape\", \"Ruler\"]`\n\n"
          "แสดงชื่อชิ้นรองสุดท้ายด้วย negative index",
          "บรรทัดเดียว", "Tape",
          'items = ["Pen", "Book", "Glue", "Tape", "Ruler"]\n\n# เขียนโค้ดตรงนี้',
          'items = ["Pen", "Book", "Glue", "Tape", "Ruler"]\nprint(items[-2])'),
        p(6, "รวมคะแนนแบบทดสอบ", "quiz_total",
          "ครูรวมคะแนนแบบทดสอบ 5 ข้อ\n\n"
          "กำหนด `scores = [8, 7, 9, 6, 10]`\n\n"
          "รวมคะแนนแล้วแสดง `Total: ...`",
          "บรรทัดเดียว", "Total: 40",
          "scores = [8, 7, 9, 6, 10]\n\n# เขียนโค้ดตรงนี้",
          'scores = [8, 7, 9, 6, 10]\ntotal = 0\nfor score in scores:\n    total += score\nprint(f"Total: {total}")',
          "เริ่ม total = 0 แล้วบวกทีละคะแนนใน loop"),
        p(7, "ป้ายชั้นเรียนพร้อมเลขที่", "numbered_roll",
          "ครูอยากพิมพ์รายชื่อพร้อมเลขที่เริ่มที่ 1\n\n"
          "กำหนด `names = [\"Kate\", \"Leo\", \"Maya\"]`\n\n"
          "แสดงแบบ `1. Kate` ทีละบรรทัด (เพิ่มตัวนับเองใน loop)",
          "3 บรรทัด", "1. Kate\n2. Leo\n3. Maya",
          'names = ["Kate", "Leo", "Maya"]\n\n# เขียนโค้ดตรงนี้',
          'names = ["Kate", "Leo", "Maya"]\nnum = 1\nfor name in names:\n    print(f"{num}. {name}")\n    num += 1',
          "สร้างตัวแปรนับก่อน loop แล้วเพิ่มทีละ 1"),
        p(10, "อุณหภูมิสูงสุดรายวัน", "hot_day",
          "สถานีอากาศบันทึกอุณหภูมิ 5 วัน อยากรู้ค่าสูงสุด\n\n"
          "กำหนด `temps = [31, 28, 35, 30, 33]`\n\n"
          "หาค่าสูงสุดด้วยการเทียบใน loop (ห้ามใช้ max) แล้วแสดง `Hottest: ...`",
          "บรรทัดเดียว", "Hottest: 35",
          "temps = [31, 28, 35, 30, 33]\n\n# เขียนโค้ดตรงนี้",
          'temps = [31, 28, 35, 30, 33]\nhottest = temps[0]\nfor t in temps:\n    if t > hottest:\n        hottest = t\nprint(f"Hottest: {hottest}")',
          "เริ่มจากค่าแรก แล้วอัปเดตเมื่อเจอค่าที่มากกว่า"),
        p(11, "ค่าเฉลี่ยอุณหภูมิ", "avg_temp",
          "อยากรู้ค่าเฉลี่ยอุณหภูมิสัปดาห์นี้\n\n"
          "กำหนด `temps = [30, 32, 28, 31, 29]`\n\n"
          "แสดงค่าเฉลี่ยทศนิยม 1 ตำแหน่งแบบ `Average: 30.0`",
          "บรรทัดเดียว", "Average: 30.0",
          "temps = [30, 32, 28, 31, 29]\n\n# เขียนโค้ดตรงนี้",
          'temps = [30, 32, 28, 31, 29]\ntotal = 0\nfor t in temps:\n    total += t\naverage = total / len(temps)\nprint(f"Average: {average:.1f}")',
          "รวมก่อน แล้วหารด้วย len"),
        p(12, "หัวท้ายของคิว", "queue_ends",
          "ระบบคิวยากโชว์คนหัวคิวและท้ายคิวพร้อมจำนวนคน\n\n"
          "กำหนด `queue = [\"A01\", \"A02\", \"A03\", \"A04\"]`\n\n"
          "แสดงตามตัวอย่าง",
          "กล่องสรุป 3 บรรทัด",
          "Front: A01\nBack : A04\nCount: 4",
          'queue = ["A01", "A02", "A03", "A04"]\n\n# เขียนโค้ดตรงนี้',
          'queue = ["A01", "A02", "A03", "A04"]\nprint(f"Front: {queue[0]}")\nprint(f"Back : {queue[-1]}")\nprint(f"Count: {len(queue)}")',
          "ใช้ [0] และ [-1] คู่กับ len"),
        p(13, "นับของที่ราคาแพง", "pricey_count",
          "ร้านอยากรู้ว่ามีสินค้าราคาตั้งแต่ 100 ขึ้นไปกี่ชิ้น\n\n"
          "กำหนด `prices = [45, 120, 80, 200, 99, 150]`\n\n"
          "แสดง `Expensive: N`",
          "บรรทัดเดียว", "Expensive: 3",
          "prices = [45, 120, 80, 200, 99, 150]\n\n# เขียนโค้ดตรงนี้",
          'prices = [45, 120, 80, 200, 99, 150]\ncount = 0\nfor price in prices:\n    if price >= 100:\n        count += 1\nprint(f"Expensive: {count}")',
          "นับเฉพาะราคาที่ผ่านเกณฑ์"),
        p(5, "ใบสรุปเมนูร้านกาแฟ", "cafe_summary",
          "ร้านกาแฟอยากได้ใบสรุปเมนูสั้นๆ\n\n"
          "กำหนด `drinks = [\"Latte\", \"Mocha\", \"Tea\"]` และ `prices = [55, 60, 40]`\n\n"
          "พิมพ์ชื่อเครื่องดื่มทีละบรรทัด แล้วปิดท้ายด้วยจำนวนเมนูและราคารวม",
          "รายการ + สรุป",
          "Latte\nMocha\nTea\nMenus: 3\nTotal: 155",
          'drinks = ["Latte", "Mocha", "Tea"]\nprices = [55, 60, 40]\n\n# เขียนโค้ดตรงนี้',
          'drinks = ["Latte", "Mocha", "Tea"]\nprices = [55, 60, 40]\nfor drink in drinks:\n    print(drink)\ntotal = 0\nfor price in prices:\n    total += price\nprint(f"Menus: {len(drinks)}")\nprint(f"Total: {total}")',
          "วนพิมพ์ชื่อก่อน แล้วค่อยรวมราคา"),
        p(14, "รายงานคะแนนสอบ", "exam_report",
          "ครูต้องการรายงานผลสอบรายคน\n\n"
          "กำหนด `names = [\"Ann\", \"Ben\", \"Cara\"]` และ `scores = [72, 48, 91]`\n\n"
          "พิมพ์ `Name Score Status` โดย Status เป็น Pass ถ้าคะแนน >= 50 ไม่เช่นนั้น Fail\n"
          "แล้วปิดท้ายด้วยจำนวนคนผ่าน",
          "รายงานรายคน + สรุป",
          "Ann 72 Pass\nBen 48 Fail\nCara 91 Pass\nPassed: 2",
          'names = ["Ann", "Ben", "Cara"]\nscores = [72, 48, 91]\n\n# เขียนโค้ดตรงนี้',
          'names = ["Ann", "Ben", "Cara"]\nscores = [72, 48, 91]\npassed = 0\ni = 0\nfor name in names:\n    score = scores[i]\n    if score >= 50:\n        status = "Pass"\n        passed += 1\n    else:\n        status = "Fail"\n    print(f"{name} {score} {status}")\n    i += 1\nprint(f"Passed: {passed}")',
          "ใช้ตัวนับคู่กับ list คะแนน เพราะยังไม่มี range(len) ในบทนี้ก็ใช้ได้ด้วย index มือ"),
        p(15, "สรุปยอดขาย 4 วัน", "sales_summary",
          "ร้านสะดวกซื้อสรุปยอดขาย 4 วัน\n\n"
          "กำหนด `sales = [1200, 980, 1500, 1100]`\n\n"
          "แสดงยอดรวม ค่าเฉลี่ย และยอดสูงสุดตามตัวอย่าง",
          "สรุป 3 บรรทัด",
          "Total  : 4780\nAverage: 1195.0\nHighest: 1500",
          "sales = [1200, 980, 1500, 1100]\n\n# เขียนโค้ดตรงนี้",
          'sales = [1200, 980, 1500, 1100]\ntotal = 0\nhighest = sales[0]\nfor s in sales:\n    total += s\n    if s > highest:\n        highest = s\naverage = total / len(sales)\nprint(f"Total  : {total}")\nprint(f"Average: {average:.1f}")\nprint(f"Highest: {highest}")',
          "วนครั้งเดียวเก็บทั้งผลรวมและค่าสูงสุดได้"),
        p(16, "ป้ายชั้นเรียนแบบกล่อง", "class_box",
          "โรงเรียนอยากได้ป้ายชั้นเรียนแบบมีกรอบ\n\n"
          "กำหนด `students = [\"Ann\", \"Ben\", \"Cara\", \"Dan\"]`\n\n"
          "แสดงตามตัวอย่าง (หัวท้ายกรอบ ความยาว 20 ตัวอักษร `=`)",
          "กล่องสรุป",
          "====================\nFirst : Ann\nLast  : Dan\nCount : 4\n====================",
          'students = ["Ann", "Ben", "Cara", "Dan"]\n\n# เขียนโค้ดตรงนี้',
          'students = ["Ann", "Ben", "Cara", "Dan"]\nprint("====================")\nprint(f"First : {students[0]}")\nprint(f"Last  : {students[-1]}")\nprint(f"Count : {len(students)}")\nprint("====================")',
          "จัดช่องว่างหลังป้ายกำกับให้ตรงคอลัมน์"),
    ],
)


# ─── 026 list-methods ────────────────────────────────────────────────────────

write_week(
    "026-list-methods",
    chapter="List Methods",
    emoji="🛠️",
    index_md=idx(
        "บท 026 List Methods",
        "index assign · `.append()` · `.remove()` · `.sort()` / `.sort(reverse=True)` · `print(list)`",
        "ไม่มี `.insert()` / `.pop()` / `sorted()` · ไม่มี `in` (บท 030)",
        [
            ("02_test.md", "🟢", "เพิ่มชื่อเข้ากลุ่มแชท", "append ทีละชื่อ"),
            ("03_test.md", "🟢", "แก้ชื่อเมนูผิด", "index assignment"),
            ("04_test.md", "🟢", "เอาของหมดสต็อกออก", "remove ตามค่า"),
            ("08_easy.md", "🟢", "เรียงราคาน้อยไปมาก", "sort ปกติ"),
            ("09_easy.md", "🟢", "เรียงคะแนนมากไปน้อย", "sort reverse"),
            ("06_medium.md", "🟡", "อัปเดตรายการซื้อ", "append + remove"),
            ("07_medium.md", "🟡", "แก้แล้วเรียงเมนู", "index assign + sort"),
            ("10_medium.md", "🟡", "คะแนนหลังตัดทิ้ง", "remove + sort reverse"),
            ("11_medium.md", "🟡", "สร้างคิวจากว่าง", "append จากว่างหลายครั้ง"),
            ("12_medium.md", "🟡", "แก้ราคาแล้วเรียง", "index assign + sort"),
            ("13_medium.md", "🟡", "ลบสองรายการแล้วเรียง", "remove สองครั้ง + sort"),
            ("05_challenge.md", "🔴", "จัดการคะแนนสอบ", "append+remove+sort"),
            ("14_challenge.md", "🔴", "จัดชั้นวางสินค้า", "หลาย method ผสม"),
            ("15_challenge.md", "🔴", "คิวหน้าร้านกาแฟ", "append+remove+กล่อง"),
            ("16_challenge.md", "🔴", "กระดานคะแนนเกม", "ครบทุก method + สรุป"),
        ],
        "- ข้อ 02 ไม่ซ้ำตัวอย่าง fruits/scores ในบทเรียนแบบเดิมทุกขั้น\n"
        "- ใช้ได้เฉพาะ append / remove / sort / index assign\n"
        "- ห้าม insert / pop / sorted / in",
    ),
    problems=[
        p(2, "เพิ่มชื่อเข้ากลุ่มแชท", "chat_append",
          "กลุ่มแชทเริ่มว่าง แล้วมีเพื่อนเข้ามา 3 คน\n\n"
          "เริ่มจาก `members = []` แล้ว `.append()` ชื่อ `Mew`, `Pim`, `Ohm` ตามลำดับ\n\n"
          "แสดง list สุดท้าย",
          "list หนึ่งบรรทัด", "['Mew', 'Pim', 'Ohm']",
          "members = []\n\n# เขียนโค้ดตรงนี้\n\nprint(members)",
          'members = []\nmembers.append("Mew")\nmembers.append("Pim")\nmembers.append("Ohm")\nprint(members)'),
        p(3, "แก้ชื่อเมนูผิด", "fix_menu",
          "เมนูพิมพ์ผิดที่ตำแหน่งกลาง\n\n"
          "กำหนด `menu = [\"Soup\", \"Salad\", \"Cake\"]`\n\n"
          "แก้ค่าตำแหน่ง index 1 เป็น `Steak` แล้วแสดง list",
          "list หนึ่งบรรทัด", "['Soup', 'Steak', 'Cake']",
          'menu = ["Soup", "Salad", "Cake"]\n\n# เขียนโค้ดตรงนี้\n\nprint(menu)',
          'menu = ["Soup", "Salad", "Cake"]\nmenu[1] = "Steak"\nprint(menu)'),
        p(4, "เอาของหมดสต็อกออก", "remove_stock",
          "คลังต้องเอาสินค้าหมดสต็อกออกจากรายการ\n\n"
          "กำหนด `stock = [\"Rice\", \"Oil\", \"Soap\", \"Milk\"]`\n\n"
          "ลบ `Oil` ออกด้วย `.remove()` แล้วแสดง list",
          "list หนึ่งบรรทัด", "['Rice', 'Soap', 'Milk']",
          'stock = ["Rice", "Oil", "Soap", "Milk"]\n\n# เขียนโค้ดตรงนี้\n\nprint(stock)',
          'stock = ["Rice", "Oil", "Soap", "Milk"]\nstock.remove("Oil")\nprint(stock)'),
        p(8, "เรียงราคาน้อยไปมาก", "sort_prices",
          "ร้านอยากเรียงราคาสินค้าจากน้อยไปมาก\n\n"
          "กำหนด `prices = [45, 12, 80, 30]`\n\n"
          "เรียงด้วย `.sort()` แล้วแสดง list",
          "list หนึ่งบรรทัด", "[12, 30, 45, 80]",
          "prices = [45, 12, 80, 30]\n\n# เขียนโค้ดตรงนี้\n\nprint(prices)",
          "prices = [45, 12, 80, 30]\nprices.sort()\nprint(prices)"),
        p(9, "เรียงคะแนนมากไปน้อย", "sort_desc",
          "กระดานคะแนนต้องเรียงจากมากไปน้อย\n\n"
          "กำหนด `scores = [70, 95, 60, 88]`\n\n"
          "ใช้ `.sort(reverse=True)` แล้วแสดง list",
          "list หนึ่งบรรทัด", "[95, 88, 70, 60]",
          "scores = [70, 95, 60, 88]\n\n# เขียนโค้ดตรงนี้\n\nprint(scores)",
          "scores = [70, 95, 60, 88]\nscores.sort(reverse=True)\nprint(scores)"),
        p(6, "อัปเดตรายการซื้อ", "shopping_update",
          "แม่บ้านแก้รายการซื้อของ\n\n"
          "กำหนด `cart = [\"Milk\", \"Eggs\", \"Bread\"]`\n\n"
          "เพิ่ม `Butter` ด้วย append และลบ `Eggs` ด้วย remove แล้วแสดง list",
          "list หนึ่งบรรทัด", "['Milk', 'Bread', 'Butter']",
          'cart = ["Milk", "Eggs", "Bread"]\n\n# เขียนโค้ดตรงนี้\n\nprint(cart)',
          'cart = ["Milk", "Eggs", "Bread"]\ncart.append("Butter")\ncart.remove("Eggs")\nprint(cart)',
          "append เพิ่มท้าย remove ลบตามค่า"),
        p(7, "แก้แล้วเรียงเมนู", "fix_then_sort",
          "ร้านกาแฟแก้ชื่อเครื่องดื่มแล้วอยากเรียงชื่อ\n\n"
          "กำหนด `drinks = [\"Mocha\", \"Latte\", \"Tea\"]`\n\n"
          "แก้ค่าตำแหน่ง 2 เป็น `Americano` แล้ว `.sort()` และแสดง list",
          "list หนึ่งบรรทัด", "['Americano', 'Latte', 'Mocha']",
          'drinks = ["Mocha", "Latte", "Tea"]\n\n# เขียนโค้ดตรงนี้\n\nprint(drinks)',
          'drinks = ["Mocha", "Latte", "Tea"]\ndrinks[2] = "Americano"\ndrinks.sort()\nprint(drinks)',
          "แก้ค่าก่อน แล้วค่อย sort"),
        p(10, "คะแนนหลังตัดทิ้ง", "trim_scores",
          "ครูตัดคะแนนต่ำสุดออกแล้วเรียงจากมากไปน้อย\n\n"
          "กำหนด `scores = [85, 40, 90, 55, 70]`\n\n"
          "ลบ `40` แล้ว `.sort(reverse=True)` และแสดง list",
          "list หนึ่งบรรทัด", "[90, 85, 70, 55]",
          "scores = [85, 40, 90, 55, 70]\n\n# เขียนโค้ดตรงนี้\n\nprint(scores)",
          "scores = [85, 40, 90, 55, 70]\nscores.remove(40)\nscores.sort(reverse=True)\nprint(scores)",
          "remove ค่าที่รู้แน่ๆ แล้วค่อยเรียง"),
        p(11, "สร้างคิวจากว่าง", "build_queue",
          "ระบบคิวเริ่มว่างแล้วรับลูกค้าทีละคน\n\n"
          "เริ่ม `queue = []` แล้ว append เลขคิว `Q1`, `Q2`, `Q3`, `Q4`\n\n"
          "แสดง list และจำนวนคนในคิว",
          "2 บรรทัด", "['Q1', 'Q2', 'Q3', 'Q4']\nCount: 4",
          "queue = []\n\n# เขียนโค้ดตรงนี้",
          'queue = []\nqueue.append("Q1")\nqueue.append("Q2")\nqueue.append("Q3")\nqueue.append("Q4")\nprint(queue)\nprint(f"Count: {len(queue)}")',
          "append ทีละคิวแล้วค่อยดู len"),
        p(12, "แก้ราคาแล้วเรียง", "fix_price_sort",
          "ป้ายราคาพิมพ์ผิดที่ชิ้นแรก\n\n"
          "กำหนด `prices = [99, 45, 120, 30]`\n\n"
          "แก้ราคาตำแหน่ง 0 เป็น `50` แล้วเรียงน้อยไปมาก และแสดง list",
          "list หนึ่งบรรทัด", "[30, 45, 50, 120]",
          "prices = [99, 45, 120, 30]\n\n# เขียนโค้ดตรงนี้\n\nprint(prices)",
          "prices = [99, 45, 120, 30]\nprices[0] = 50\nprices.sort()\nprint(prices)",
          "index assign ก่อน sort"),
        p(13, "ลบสองรายการแล้วเรียง", "remove_two_sort",
          "คลังลบสินค้าเสียสองชิ้นแล้วเรียงชื่อที่เหลือ\n\n"
          "กำหนด `items = [\"Apple\", \"Banana\", \"Mango\", \"Durian\", \"Grape\"]`\n\n"
          "ลบ `Banana` และ `Durian` แล้ว `.sort()` และแสดง list",
          "list หนึ่งบรรทัด", "['Apple', 'Grape', 'Mango']",
          'items = ["Apple", "Banana", "Mango", "Durian", "Grape"]\n\n# เขียนโค้ดตรงนี้\n\nprint(items)',
          'items = ["Apple", "Banana", "Mango", "Durian", "Grape"]\nitems.remove("Banana")\nitems.remove("Durian")\nitems.sort()\nprint(items)',
          "remove ได้ทีละค่า เรียกสองครั้ง"),
        p(5, "จัดการคะแนนสอบ", "manage_scores",
          "ครูจัดการคะแนนสอบชุดหนึ่ง\n\n"
          "กำหนด `scores = [72, 55, 90]`\n\n"
          "เพิ่ม `88` ด้วย append ลบ `55` ด้วย remove แล้วเรียงมากไปน้อย และแสดง list",
          "list หนึ่งบรรทัด", "[90, 88, 72]",
          "scores = [72, 55, 90]\n\n# เขียนโค้ดตรงนี้\n\nprint(scores)",
          "scores = [72, 55, 90]\nscores.append(88)\nscores.remove(55)\nscores.sort(reverse=True)\nprint(scores)",
          "ลำดับ: append → remove → sort"),
        p(14, "จัดชั้นวางสินค้า", "shelf_arrange",
          "พนักงานจัดชั้นวางสินค้า\n\n"
          "กำหนด `shelf = [\"Soap\", \"Shampoo\", \"Cream\"]`\n\n"
          "แก้ตำแหน่ง 0 เป็น `Lotion` เพิ่ม `Toner` ลบ `Cream` แล้วเรียงชื่อ และแสดง list",
          "list หนึ่งบรรทัด", "['Lotion', 'Shampoo', 'Toner']",
          'shelf = ["Soap", "Shampoo", "Cream"]\n\n# เขียนโค้ดตรงนี้\n\nprint(shelf)',
          'shelf = ["Soap", "Shampoo", "Cream"]\nshelf[0] = "Lotion"\nshelf.append("Toner")\nshelf.remove("Cream")\nshelf.sort()\nprint(shelf)',
          "ทำทีละขั้นตามลำดับที่โจทย์บอก"),
        p(15, "คิวหน้าร้านกาแฟ", "cafe_queue",
          "คิวยากลบคนที่ยกเลิกและเพิ่มคนใหม่\n\n"
          "กำหนด `queue = [\"Ann\", \"Ben\", \"Cara\"]`\n\n"
          "ลบ `Ben` เพิ่ม `Dan` แล้วแสดง list และจำนวนคนตามตัวอย่าง",
          "2 บรรทัด", "['Ann', 'Cara', 'Dan']\nWaiting: 3",
          'queue = ["Ann", "Ben", "Cara"]\n\n# เขียนโค้ดตรงนี้',
          'queue = ["Ann", "Ben", "Cara"]\nqueue.remove("Ben")\nqueue.append("Dan")\nprint(queue)\nprint(f"Waiting: {len(queue)}")',
          "remove คนที่ยกเลิกก่อน แล้ว append คนใหม่"),
        p(16, "กระดานคะแนนเกม", "game_board",
          "เกมต้องการอัปเดตกระดานคะแนน\n\n"
          "กำหนด `scores = [120, 80, 95]`\n\n"
          "เพิ่ม `150` ลบ `80` แก้ตำแหน่ง 0 เป็น `130` แล้วเรียงมากไปน้อย\n"
          "แสดง list และคะแนนสูงสุด (ค่าแรกหลังเรียง)",
          "2 บรรทัด", "[150, 130, 95]\nTop: 150",
          "scores = [120, 80, 95]\n\n# เขียนโค้ดตรงนี้",
          'scores = [120, 80, 95]\nscores.append(150)\nscores.remove(80)\nscores[0] = 130\nscores.sort(reverse=True)\nprint(scores)\nprint(f"Top: {scores[0]}")',
          "หลัง sort reverse ค่าแรกคือคะแนนสูงสุด"),
    ],
)


# ─── 027 list-practice ───────────────────────────────────────────────────────

write_week(
    "027-list-practice",
    chapter="List Practice",
    emoji="🏋️",
    index_md=idx(
        "บท 027 List Practice",
        "ความรู้ list ทั้งหมด + filter เข้า list ใหม่ + นับด้วย counter + `for i in range(len(...))`",
        "ไม่มี `in` (บท 030) · ไม่มี `enumerate` · ไม่มี `min()`/`max()`/`sorted()`",
        [
            ("02_test.md", "🟢", "พิมพ์งานบ้านพร้อมเลข", "range(len) พื้นฐาน"),
            ("03_test.md", "🟢", "นับคะแนนผ่านเกณฑ์", "counter ใน loop"),
            ("04_test.md", "🟢", "กรองสินค้าราคาถูก", "filter เข้า list ใหม่"),
            ("08_easy.md", "🟢", "ป้ายชั้นเรียนแบบ index", "range(len) + ชื่อ"),
            ("09_easy.md", "🟢", "นับอุณหภูมิร้อน", "counter + เงื่อนไข"),
            ("06_medium.md", "🟡", "กรองชื่อสั้น", "filter ด้วย len(ชื่อ)"),
            ("07_medium.md", "🟡", "รวมเฉพาะคะแนนผ่าน", "accumulator มีเงื่อนไข"),
            ("10_medium.md", "🟡", "รายการงานพร้อมสถานะ", "range(len) + if"),
            ("11_medium.md", "🟡", "กรองแล้วเรียงราคา", "filter + sort"),
            ("12_medium.md", "🟡", "ค่าเฉลี่ยเฉพาะที่ผ่าน", "filter แล้วเฉลี่ย"),
            ("13_medium.md", "🟡", "นับและรวมราคาแพง", "counter + total คู่กัน"),
            ("05_challenge.md", "🔴", "รายงานงานบ้าน", "range(len) + สรุป"),
            ("14_challenge.md", "🔴", "ตะกร้าหลังกรอง", "filter+append+sort+สรุป"),
            ("15_challenge.md", "🔴", "ผลสอบแบบมีเลขที่", "range(len)+Pass/Fail"),
            ("16_challenge.md", "🔴", "สรุปอุณหภูมิรายสัปดาห์", "หลายสถิติจาก list เดียว"),
        ],
        "- ข้อ 02 ไม่ซ้ำตัวอย่าง todos ในบทเรียนทุกตัวอักษร — เปลี่ยนสถานการณ์\n"
        "- เน้น range(len) / filter / count\n"
        "- ห้ามใช้ in / enumerate / max",
    ),
    problems=[
        p(2, "พิมพ์งานบ้านพร้อมเลข", "chore_list",
          "แม่บ้านอยากพิมพ์รายการงานพร้อมเลขที่\n\n"
          "กำหนด `chores = [\"Wash dishes\", \"Fold clothes\", \"Water plants\"]`\n\n"
          "ใช้ `for i in range(len(chores)):` แสดงแบบ `1) Wash dishes`",
          "3 บรรทัด", "1) Wash dishes\n2) Fold clothes\n3) Water plants",
          'chores = ["Wash dishes", "Fold clothes", "Water plants"]\n\n# เขียนโค้ดตรงนี้',
          'chores = ["Wash dishes", "Fold clothes", "Water plants"]\nfor i in range(len(chores)):\n    print(f"{i + 1}) {chores[i]}")'),
        p(3, "นับคะแนนผ่านเกณฑ์", "pass_count",
          "ครูอยากรู้ว่ามีกี่คนได้คะแนนตั้งแต่ 60 ขึ้นไป\n\n"
          "กำหนด `scores = [55, 80, 42, 70, 90, 58]`\n\n"
          "แสดง `Passed: N`",
          "บรรทัดเดียว", "Passed: 3",
          "scores = [55, 80, 42, 70, 90, 58]\n\n# เขียนโค้ดตรงนี้",
          'scores = [55, 80, 42, 70, 90, 58]\npassed = 0\nfor score in scores:\n    if score >= 60:\n        passed += 1\nprint(f"Passed: {passed}")'),
        p(4, "กรองสินค้าราคาถูก", "cheap_items",
          "ร้านอยากได้เฉพาะสินค้าราคาต่ำกว่า 50\n\n"
          "กำหนด `prices = [20, 75, 40, 90, 15, 60]`\n\n"
          "สร้าง list ใหม่ชื่อ `cheap` เก็บราคาที่ต่ำกว่า 50 แล้วแสดง `cheap`",
          "list หนึ่งบรรทัด", "[20, 40, 15]",
          "prices = [20, 75, 40, 90, 15, 60]\ncheap = []\n\n# เขียนโค้ดตรงนี้\n\nprint(cheap)",
          "prices = [20, 75, 40, 90, 15, 60]\ncheap = []\nfor price in prices:\n    if price < 50:\n        cheap.append(price)\nprint(cheap)"),
        p(8, "ป้ายชั้นเรียนแบบ index", "index_roll",
          "ครูพิมพ์รายชื่อพร้อม index เริ่มที่ 0\n\n"
          "กำหนด `names = [\"Ann\", \"Ben\", \"Cara\"]`\n\n"
          "แสดงแบบ `0: Ann`",
          "3 บรรทัด", "0: Ann\n1: Ben\n2: Cara",
          'names = ["Ann", "Ben", "Cara"]\n\n# เขียนโค้ดตรงนี้',
          'names = ["Ann", "Ben", "Cara"]\nfor i in range(len(names)):\n    print(f"{i}: {names[i]}")'),
        p(9, "นับอุณหภูมิร้อน", "hot_days",
          "นับวันที่มีอุณหภูมิสูงกว่า 32\n\n"
          "กำหนด `temps = [30, 34, 29, 36, 31, 33]`\n\n"
          "แสดง `Hot days: N`",
          "บรรทัดเดียว", "Hot days: 3",
          "temps = [30, 34, 29, 36, 31, 33]\n\n# เขียนโค้ดตรงนี้",
          'temps = [30, 34, 29, 36, 31, 33]\nhot = 0\nfor t in temps:\n    if t > 32:\n        hot += 1\nprint(f"Hot days: {hot}")'),
        p(6, "กรองชื่อสั้น", "short_names",
          "อยากได้เฉพาะชื่อที่ยาวไม่เกิน 3 ตัวอักษร\n\n"
          "กำหนด `names = [\"Ann\", \"Bobby\", \"Cy\", \"Diana\", \"Ed\"]`\n\n"
          "สร้าง `short` แล้วแสดง list",
          "list หนึ่งบรรทัด", "['Ann', 'Cy', 'Ed']",
          'names = ["Ann", "Bobby", "Cy", "Diana", "Ed"]\nshort = []\n\n# เขียนโค้ดตรงนี้\n\nprint(short)',
          'names = ["Ann", "Bobby", "Cy", "Diana", "Ed"]\nshort = []\nfor name in names:\n    if len(name) <= 3:\n        short.append(name)\nprint(short)',
          "ใช้ len(name) เป็นเงื่อนไข"),
        p(7, "รวมเฉพาะคะแนนผ่าน", "sum_passed",
          "รวมเฉพาะคะแนนที่ผ่านเกณฑ์ 50\n\n"
          "กำหนด `scores = [40, 70, 55, 30, 90]`\n\n"
          "แสดง `Sum passed: ...`",
          "บรรทัดเดียว", "Sum passed: 215",
          "scores = [40, 70, 55, 30, 90]\n\n# เขียนโค้ดตรงนี้",
          'scores = [40, 70, 55, 30, 90]\ntotal = 0\nfor score in scores:\n    if score >= 50:\n        total += score\nprint(f"Sum passed: {total}")',
          "บวกเฉพาะตอนเงื่อนไขเป็นจริง"),
        p(10, "รายการงานพร้อมสถานะ", "task_status",
          "แอปงานบ้านทำเครื่องหมาย Done ให้งานข้อคู่ (index คู่)\n\n"
          "กำหนด `tasks = [\"Sweep\", \"Mop\", \"Dust\", \"Wipe\"]`\n\n"
          "ใช้ range(len) แสดง `0 Sweep Done` หรือ `1 Mop Todo` ตามว่า index หาร 2 ลงตัวหรือไม่",
          "4 บรรทัด",
          "0 Sweep Done\n1 Mop Todo\n2 Dust Done\n3 Wipe Todo",
          'tasks = ["Sweep", "Mop", "Dust", "Wipe"]\n\n# เขียนโค้ดตรงนี้',
          'tasks = ["Sweep", "Mop", "Dust", "Wipe"]\nfor i in range(len(tasks)):\n    if i % 2 == 0:\n        status = "Done"\n    else:\n        status = "Todo"\n    print(f"{i} {tasks[i]} {status}")',
          "ใช้ i % 2 == 0 แยกสถานะ"),
        p(11, "กรองแล้วเรียงราคา", "filter_sort_price",
          "อยากได้ราคาสินค้าที่ >= 100 แล้วเรียงน้อยไปมาก\n\n"
          "กำหนด `prices = [80, 150, 120, 40, 200, 95]`\n\n"
          "สร้าง `picked` เรียงแล้วแสดง",
          "list หนึ่งบรรทัด", "[120, 150, 200]",
          "prices = [80, 150, 120, 40, 200, 95]\npicked = []\n\n# เขียนโค้ดตรงนี้\n\nprint(picked)",
          "prices = [80, 150, 120, 40, 200, 95]\npicked = []\nfor price in prices:\n    if price >= 100:\n        picked.append(price)\npicked.sort()\nprint(picked)",
          "กรองก่อน แล้วค่อย sort"),
        p(12, "ค่าเฉลี่ยเฉพาะที่ผ่าน", "avg_passed",
          "หาค่าเฉลี่ยเฉพาะคะแนนที่ >= 50\n\n"
          "กำหนด `scores = [40, 80, 60, 30, 90]`\n\n"
          "แสดง `Average: ...` ทศนิยม 1 ตำแหน่ง",
          "บรรทัดเดียว", "Average: 76.7",
          "scores = [40, 80, 60, 30, 90]\n\n# เขียนโค้ดตรงนี้",
          'scores = [40, 80, 60, 30, 90]\npassed = []\nfor score in scores:\n    if score >= 50:\n        passed.append(score)\ntotal = 0\nfor score in passed:\n    total += score\naverage = total / len(passed)\nprint(f"Average: {average:.1f}")',
          "สร้าง list ของคะแนนที่ผ่านก่อน แล้วค่อยเฉลี่ย"),
        p(13, "นับและรวมราคาแพง", "count_sum_pricey",
          "นับและรวมสินค้าราคา >= 100 พร้อมกัน\n\n"
          "กำหนด `prices = [50, 120, 80, 200, 150]`\n\n"
          "แสดงตามตัวอย่าง",
          "2 บรรทัด", "Count: 3\nTotal: 470",
          "prices = [50, 120, 80, 200, 150]\n\n# เขียนโค้ดตรงนี้",
          'prices = [50, 120, 80, 200, 150]\ncount = 0\ntotal = 0\nfor price in prices:\n    if price >= 100:\n        count += 1\n        total += price\nprint(f"Count: {count}")\nprint(f"Total: {total}")',
          "อัปเดตทั้งตัวนับและผลรวมในเงื่อนไขเดียวกัน"),
        p(5, "รายงานงานบ้าน", "chore_report",
          "พิมพ์รายงานงานบ้านพร้อมเลขที่และจำนวนงาน\n\n"
          "กำหนด `chores = [\"Cook\", \"Clean\", \"Shop\"]`\n\n"
          "แสดงตามตัวอย่าง",
          "รายการ + สรุป",
          "1. Cook\n2. Clean\n3. Shop\nJobs: 3",
          'chores = ["Cook", "Clean", "Shop"]\n\n# เขียนโค้ดตรงนี้',
          'chores = ["Cook", "Clean", "Shop"]\nfor i in range(len(chores)):\n    print(f"{i + 1}. {chores[i]}")\nprint(f"Jobs: {len(chores)}")',
          "ใช้ range(len) แล้วปิดท้ายด้วย len"),
        p(14, "ตะกร้าหลังกรอง", "cart_filter",
          "ลูกค้าเก็บเฉพาะสินค้าราคาต่ำกว่า 80 แล้วเรียงราคา\n\n"
          "กำหนด `prices = [45, 90, 30, 120, 60, 75]`\n\n"
          "สร้าง `cart` เรียงแล้วแสดง list จำนวนชิ้น และยอดรวม",
          "3 บรรทัด",
          "[30, 45, 60, 75]\nItems: 4\nTotal: 210",
          "prices = [45, 90, 30, 120, 60, 75]\ncart = []\n\n# เขียนโค้ดตรงนี้",
          'prices = [45, 90, 30, 120, 60, 75]\ncart = []\nfor price in prices:\n    if price < 80:\n        cart.append(price)\ncart.sort()\ntotal = 0\nfor price in cart:\n    total += price\nprint(cart)\nprint(f"Items: {len(cart)}")\nprint(f"Total: {total}")',
          "กรอง → เรียง → รวม"),
        p(15, "ผลสอบแบบมีเลขที่", "exam_indexed",
          "รายงานผลสอบพร้อมเลขที่\n\n"
          "กำหนด `scores = [72, 40, 88, 55]`\n\n"
          "ใช้ range(len) แสดง `1) 72 Pass` หรือ Fail ถ้า < 50 แล้วปิดท้ายจำนวนผ่าน",
          "รายงาน + สรุป",
          "1) 72 Pass\n2) 40 Fail\n3) 88 Pass\n4) 55 Pass\nPassed: 3",
          "scores = [72, 40, 88, 55]\n\n# เขียนโค้ดตรงนี้",
          'scores = [72, 40, 88, 55]\npassed = 0\nfor i in range(len(scores)):\n    score = scores[i]\n    if score >= 50:\n        status = "Pass"\n        passed += 1\n    else:\n        status = "Fail"\n    print(f"{i + 1}) {score} {status}")\nprint(f"Passed: {passed}")',
          "range(len) ให้ทั้งเลขที่และค่าคะแนน"),
        p(16, "สรุปอุณหภูมิรายสัปดาห์", "week_temps",
          "สรุปอุณหภูมิ 7 วัน\n\n"
          "กำหนด `temps = [28, 33, 30, 35, 29, 34, 31]`\n\n"
          "นับวันร้อน (>32) หาค่าสูงสุดด้วยมือ และค่าเฉลี่ยทศนิยม 1 ตำแหน่ง",
          "3 บรรทัด",
          "Hot   : 3\nHighest: 35\nAverage: 31.4",
          "temps = [28, 33, 30, 35, 29, 34, 31]\n\n# เขียนโค้ดตรงนี้",
          'temps = [28, 33, 30, 35, 29, 34, 31]\nhot = 0\nhighest = temps[0]\ntotal = 0\nfor t in temps:\n    total += t\n    if t > 32:\n        hot += 1\n    if t > highest:\n        highest = t\naverage = total / len(temps)\nprint(f"Hot   : {hot}")\nprint(f"Highest: {highest}")\nprint(f"Average: {average:.1f}")',
          "วนครั้งเดียวเก็บหลายสถิติ"),
    ],
)


# ─── 028 review-lists ────────────────────────────────────────────────────────

write_week(
    "028-review-lists",
    chapter="Review Lists",
    emoji="🔁",
    index_md=idx(
        "บท 028 Review Lists",
        "ทบทวน list ทั้งก้อน: index / len / for / append / remove / sort / range(len) / filter / count",
        "ไม่มี `in` (สอนจริงบท 030) · ไม่มี insert/pop/sorted/min/max",
        [
            ("02_test.md", "🟢", "หัวท้ายชั้นวาง", "index + len"),
            ("03_test.md", "🟢", "เพิ่มของเข้าตะกร้า", "append"),
            ("04_test.md", "🟢", "ลบเมนูเลิกขาย", "remove"),
            ("08_easy.md", "🟢", "เรียงคะแนนทบทวน", "sort reverse"),
            ("09_easy.md", "🟢", "พิมพ์พร้อมเลขที่", "range(len)"),
            ("06_medium.md", "🟡", "กรองอุณหภูมิเย็น", "filter"),
            ("07_medium.md", "🟡", "ค่าเฉลี่ยคะแนน", "รวม / len"),
            ("10_medium.md", "🟡", "อัปเดตแล้วเรียงคิว", "append+remove+sort"),
            ("11_medium.md", "🟡", "นับงานเสร็จ", "counter + เงื่อนไขชื่อ"),
            ("12_medium.md", "🟡", "แก้ราคาแล้วสรุป", "index assign + รวม"),
            ("13_medium.md", "🟡", "กรองแล้วหาสูงสุด", "filter + manual max"),
            ("05_challenge.md", "🔴", "รายงานชั้นเรียน", "range(len)+สถิติ"),
            ("14_challenge.md", "🔴", "จัดการสต็อกสินค้า", "หลาย method + สรุป"),
            ("15_challenge.md", "🔴", "สรุปผลสอบทบทวน", "Pass/Fail + เฉลี่ย"),
            ("16_challenge.md", "🔴", "กล่องสรุปยอดขาย", "ครบชุด list skills"),
        ],
        "- ข้อ 02 ไม่ซ้ำตัวอย่าง fruits/scores ในบทเรียน\n"
        "- ห้ามใช้ `in` แม้บทเรียนจะเอ่ยในตาราง\n"
        "- ทบทวนให้ครบทั้งอ่าน list และแก้ list",
    ),
    problems=[
        p(2, "หัวท้ายชั้นวาง", "shelf_ends",
          "พนักงานอยากรู้ของชิ้นแรก ชิ้นสุดท้าย และจำนวนบนชั้น\n\n"
          "กำหนด `shelf = [\"Mug\", \"Plate\", \"Bowl\", \"Cup\"]`\n\n"
          "แสดงตามตัวอย่าง",
          "3 บรรทัด", "First: Mug\nLast : Cup\nCount: 4",
          'shelf = ["Mug", "Plate", "Bowl", "Cup"]\n\n# เขียนโค้ดตรงนี้',
          'shelf = ["Mug", "Plate", "Bowl", "Cup"]\nprint(f"First: {shelf[0]}")\nprint(f"Last : {shelf[-1]}")\nprint(f"Count: {len(shelf)}")'),
        p(3, "เพิ่มของเข้าตะกร้า", "cart_add",
          "ลูกค้าหยิบของเพิ่มเข้าตะกร้า\n\n"
          "กำหนด `cart = [\"Milk\", \"Bread\"]` แล้ว append `Eggs` และ `Butter`\n\n"
          "แสดง list",
          "list หนึ่งบรรทัด", "['Milk', 'Bread', 'Eggs', 'Butter']",
          'cart = ["Milk", "Bread"]\n\n# เขียนโค้ดตรงนี้\n\nprint(cart)',
          'cart = ["Milk", "Bread"]\ncart.append("Eggs")\ncart.append("Butter")\nprint(cart)'),
        p(4, "ลบเมนูเลิกขาย", "menu_remove",
          "ร้านเลิกขายเมนูหนึ่งรายการ\n\n"
          "กำหนด `menu = [\"Pad Thai\", \"Soup\", \"Salad\", \"Curry\"]`\n\n"
          "ลบ `Soup` แล้วแสดง list",
          "list หนึ่งบรรทัด", "['Pad Thai', 'Salad', 'Curry']",
          'menu = ["Pad Thai", "Soup", "Salad", "Curry"]\n\n# เขียนโค้ดตรงนี้\n\nprint(menu)',
          'menu = ["Pad Thai", "Soup", "Salad", "Curry"]\nmenu.remove("Soup")\nprint(menu)'),
        p(8, "เรียงคะแนนทบทวน", "review_sort",
          "เรียงคะแนนจากมากไปน้อยเพื่อติดบอร์ด\n\n"
          "กำหนด `scores = [65, 90, 72, 88]`\n\n"
          "เรียง reverse แล้วแสดง",
          "list หนึ่งบรรทัด", "[90, 88, 72, 65]",
          "scores = [65, 90, 72, 88]\n\n# เขียนโค้ดตรงนี้\n\nprint(scores)",
          "scores = [65, 90, 72, 88]\nscores.sort(reverse=True)\nprint(scores)"),
        p(9, "พิมพ์พร้อมเลขที่", "numbered_items",
          "พิมพ์รายการของใช้พร้อมเลขที่\n\n"
          "กำหนด `items = [\"Bag\", \"Key\", \"Phone\"]`\n\n"
          "แสดง `1 - Bag` ด้วย range(len)",
          "3 บรรทัด", "1 - Bag\n2 - Key\n3 - Phone",
          'items = ["Bag", "Key", "Phone"]\n\n# เขียนโค้ดตรงนี้',
          'items = ["Bag", "Key", "Phone"]\nfor i in range(len(items)):\n    print(f"{i + 1} - {items[i]}")'),
        p(6, "กรองอุณหภูมิเย็น", "cool_days",
          "กรองวันที่มีอุณหภูมิต่ำกว่า 30\n\n"
          "กำหนด `temps = [31, 28, 33, 27, 30, 26]`\n\n"
          "สร้าง `cool` แล้วแสดง",
          "list หนึ่งบรรทัด", "[28, 27, 26]",
          "temps = [31, 28, 33, 27, 30, 26]\ncool = []\n\n# เขียนโค้ดตรงนี้\n\nprint(cool)",
          "temps = [31, 28, 33, 27, 30, 26]\ncool = []\nfor t in temps:\n    if t < 30:\n        cool.append(t)\nprint(cool)",
          "append เฉพาะวันที่เข้าเงื่อนไข"),
        p(7, "ค่าเฉลี่ยคะแนน", "avg_scores",
          "หาค่าเฉลี่ยคะแนนสอบย่อย\n\n"
          "กำหนด `scores = [80, 70, 90, 60]`\n\n"
          "แสดง `Average: 75.0`",
          "บรรทัดเดียว", "Average: 75.0",
          "scores = [80, 70, 90, 60]\n\n# เขียนโค้ดตรงนี้",
          'scores = [80, 70, 90, 60]\ntotal = 0\nfor score in scores:\n    total += score\naverage = total / len(scores)\nprint(f"Average: {average:.1f}")',
          "รวมแล้วหาร len"),
        p(10, "อัปเดตแล้วเรียงคิว", "queue_update",
          "คิวยากอัปเดตรายชื่อแล้วเรียงตามตัวอักษร\n\n"
          "กำหนด `queue = [\"Cara\", \"Ann\", \"Ben\"]`\n\n"
          "ลบ `Ben` เพิ่ม `Dan` แล้ว sort และแสดง",
          "list หนึ่งบรรทัด", "['Ann', 'Cara', 'Dan']",
          'queue = ["Cara", "Ann", "Ben"]\n\n# เขียนโค้ดตรงนี้\n\nprint(queue)',
          'queue = ["Cara", "Ann", "Ben"]\nqueue.remove("Ben")\nqueue.append("Dan")\nqueue.sort()\nprint(queue)',
          "remove → append → sort"),
        p(11, "นับงานเสร็จ", "done_count",
          "นับงานที่ขึ้นต้นด้วยคำว่า Done ในข้อความสถานะ\n\n"
          "กำหนด `status = [\"Done\", \"Todo\", \"Done\", \"Todo\", \"Done\"]`\n\n"
          "แสดง `Done: N` โดยเทียบว่าค่าเท่ากับ `Done`",
          "บรรทัดเดียว", "Done: 3",
          'status = ["Done", "Todo", "Done", "Todo", "Done"]\n\n# เขียนโค้ดตรงนี้',
          'status = ["Done", "Todo", "Done", "Todo", "Done"]\ncount = 0\nfor s in status:\n    if s == "Done":\n        count += 1\nprint(f"Done: {count}")',
          "เทียบด้วย == ไม่ใช้ in"),
        p(12, "แก้ราคาแล้วสรุป", "fix_sum",
          "แก้ราคาสินค้าชิ้นที่สองแล้วรวมยอด\n\n"
          "กำหนด `prices = [40, 99, 60]`\n\n"
          "แก้ตำแหน่ง 1 เป็น `50` แล้วแสดง list และยอดรวม",
          "2 บรรทัด", "[40, 50, 60]\nTotal: 150",
          "prices = [40, 99, 60]\n\n# เขียนโค้ดตรงนี้",
          'prices = [40, 99, 60]\nprices[1] = 50\ntotal = 0\nfor price in prices:\n    total += price\nprint(prices)\nprint(f"Total: {total}")',
          "แก้ค่าก่อน แล้วค่อยรวม"),
        p(13, "กรองแล้วหาสูงสุด", "filter_max",
          "กรองคะแนนที่ >= 70 แล้วหาค่าสูงสุดด้วยมือ\n\n"
          "กำหนด `scores = [60, 85, 70, 40, 95, 75]`\n\n"
          "แสดง list ที่กรองและค่าสูงสุด",
          "2 บรรทัด", "[85, 70, 95, 75]\nHighest: 95",
          "scores = [60, 85, 70, 40, 95, 75]\nhigh = []\n\n# เขียนโค้ดตรงนี้",
          'scores = [60, 85, 70, 40, 95, 75]\nhigh = []\nfor score in scores:\n    if score >= 70:\n        high.append(score)\nhighest = high[0]\nfor score in high:\n    if score > highest:\n        highest = score\nprint(high)\nprint(f"Highest: {highest}")',
          "กรองก่อน แล้วเทียบหาสูงสุดเอง"),
        p(5, "รายงานชั้นเรียน", "class_report",
          "พิมพ์รายงานชั้นเรียนพร้อมเลขที่และจำนวนคน\n\n"
          "กำหนด `students = [\"Ann\", \"Ben\", \"Cara\", \"Dan\"]`\n\n"
          "แสดงตามตัวอย่าง",
          "รายการ + สรุป",
          "1) Ann\n2) Ben\n3) Cara\n4) Dan\nStudents: 4",
          'students = ["Ann", "Ben", "Cara", "Dan"]\n\n# เขียนโค้ดตรงนี้',
          'students = ["Ann", "Ben", "Cara", "Dan"]\nfor i in range(len(students)):\n    print(f"{i + 1}) {students[i]}")\nprint(f"Students: {len(students)}")',
          "range(len) + สรุปจำนวน"),
        p(14, "จัดการสต็อกสินค้า", "stock_manage",
          "คลังอัปเดตสต็อกสินค้า\n\n"
          "กำหนด `stock = [\"Rice\", \"Oil\", \"Salt\"]`\n\n"
          "แก้ตำแหน่ง 1 เป็น `Sugar` เพิ่ม `Flour` ลบ `Salt` แล้วเรียงชื่อ\n"
          "แสดง list และจำนวนชิ้น",
          "2 บรรทัด", "['Flour', 'Rice', 'Sugar']\nItems: 3",
          'stock = ["Rice", "Oil", "Salt"]\n\n# เขียนโค้ดตรงนี้',
          'stock = ["Rice", "Oil", "Salt"]\nstock[1] = "Sugar"\nstock.append("Flour")\nstock.remove("Salt")\nstock.sort()\nprint(stock)\nprint(f"Items: {len(stock)}")',
          "ทำทีละขั้นแล้วปิดด้วย sort"),
        p(15, "สรุปผลสอบทบทวน", "exam_review",
          "สรุปผลสอบรายคนจากสอง list\n\n"
          "กำหนด `names = [\"Ann\", \"Ben\", \"Cara\"]` และ `scores = [45, 80, 70]`\n\n"
          "ใช้ range(len) พิมพ์ Pass/Fail (>=50) แล้วแสดงจำนวนผ่านและค่าเฉลี่ยทุกคนทศนิยม 1 ตำแหน่ง",
          "รายงาน + สรุป",
          "Ann Fail\nBen Pass\nCara Pass\nPassed : 2\nAverage: 65.0",
          'names = ["Ann", "Ben", "Cara"]\nscores = [45, 80, 70]\n\n# เขียนโค้ดตรงนี้',
          'names = ["Ann", "Ben", "Cara"]\nscores = [45, 80, 70]\npassed = 0\ntotal = 0\nfor i in range(len(names)):\n    total += scores[i]\n    if scores[i] >= 50:\n        print(f"{names[i]} Pass")\n        passed += 1\n    else:\n        print(f"{names[i]} Fail")\naverage = total / len(scores)\nprint(f"Passed : {passed}")\nprint(f"Average: {average:.1f}")',
          "วนด้วย index คู่สอง list"),
        p(16, "กล่องสรุปยอดขาย", "sales_box",
          "สรุปยอดขายรายวันแบบมีกรอบ\n\n"
          "กำหนด `sales = [900, 1200, 750, 1100]`\n\n"
          "ลบยอดผิดปกติ `750` เพิ่ม `1300` แล้วเรียงน้อยไปมาก\n"
          "แสดง list ยอดรวม และยอดสูงสุด (ตัวท้ายหลังเรียง) ตามตัวอย่าง",
          "กล่องสรุป",
          "====================\n[900, 1100, 1200, 1300]\nTotal  : 4500\nHighest: 1300\n====================",
          "sales = [900, 1200, 750, 1100]\n\n# เขียนโค้ดตรงนี้",
          'sales = [900, 1200, 750, 1100]\nsales.remove(750)\nsales.append(1300)\nsales.sort()\ntotal = 0\nfor s in sales:\n    total += s\nprint("====================")\nprint(sales)\nprint(f"Total  : {total}")\nprint(f"Highest: {sales[-1]}")\nprint("====================")',
          "หลัง sort น้อย→มาก ค่าท้ายคือสูงสุด"),
    ],
)

print("done 025-028")
