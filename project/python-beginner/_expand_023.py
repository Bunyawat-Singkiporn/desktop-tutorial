# -*- coding: utf-8 -*-
"""Expand 023-debugging-loops to 15-problem standard. NO min()/max()."""
from _expand_helpers import write_week

INDEX = """
# 📋 สารบัญโจทย์ — บท 023 Debugging Loops

**ขอบเขตของบทนี้:** ทบทวน loop + ฝึกแก้บั๊ก (off-by-one / infinite / indent / ชื่อตัวแปรผิด)

> ❌ ห้าม `min()` / `max()` · ห้าม `.append()` / `sum()`
> ❌ ข้อ `02` ไม่ซ้ำตัวอย่างในบทเรียนเป๊ะ

---

## ลำดับที่แนะนำ

| # | ไฟล์ | ระดับ | โจทย์ | แกนการคิด |
|---|------|-------|-------|-----------|
| 1 | `02_test.md` | 🟢 | แก้ range นับคะแนน | off-by-one |
| 2 | `03_test.md` | 🟢 | แก้ while นับลูกค้า | ลืมอัปเดตตัวนับ |
| 3 | `04_test.md` | 🟢 | แก้ indent ใบเสร็จ | print ใน loop |
| 4 | `08_easy.md` | 🟢 | แก้พิมพ์สมาชิกทีม | ใช้ตัวแปรวนไม่ใช่ list |
| 5 | `09_easy.md` | 🟢 | แก้ range คู่ | stop ผิด |
| 6 | `06_medium.md` | 🟡 | แก้รวมยอดใน list | สะสมผิดที่ |
| 7 | `07_medium.md` | 🟡 | แก้ while ทายรหัส | เงื่อนไขวนผิด |
| 8 | `10_medium.md` | 🟡 | แก้ข้ามเลขศูนย์ | continue ผิดตำแหน่ง |
| 9 | `11_medium.md` | 🟡 | แก้ตารางดาว | ลูปใน range ผิด |
| 10 | `12_medium.md` | 🟡 | แก้ break เร็วเกิน | break ก่อนพิมพ์ |
| 11 | `13_medium.md` | 🟡 | แก้เฉลี่ยอุณหภูมิ | หารก่อนรวมครบ |
| 12 | `05_challenge.md` | 🔴 | แก้รายงานยอดขาย | หลายจุดผิดพร้อมกัน |
| 13 | `14_challenge.md` | 🔴 | แก้คิวสั่งอาหาร | while True + break |
| 14 | `15_challenge.md` | 🔴 | แก้ผังที่นั่ง | nested + ป้าย |
| 15 | `16_challenge.md` | 🔴 | แก้สรุปสต็อก | นับ/ข้าม/รวม |

**สรุป:** 🟢 Easy 5 ข้อ · 🟡 Medium 6 ข้อ · 🔴 Challenge 4 ข้อ = **15 ข้อ**
"""

NO_IN = "ไม่มี (แก้โค้ดที่ให้มา)"


def P(n, title, slug, body, out_desc, sample_out, starter, answer,
      hint=None, sample_in=None, in_desc=NO_IN):
    return dict(
        n=n, title=title, slug=slug, body=body,
        input_desc=in_desc, output_desc=out_desc,
        sample_input=sample_in, sample_output=sample_out,
        hint=hint, starter=starter, answer=answer,
    )


PROBLEMS = [
    P(2, "แก้ range นับคะแนน", "fix_score_range",
      "โปรแกรมต้องการพิมพ์คะแนนโบนัส `1` ถึง `6` แต่ตอนนี้ได้แค่ถึง `5`\n"
      "แก้ `range` ให้ถูกต้อง",
      "เลข 1 ถึง 6 ทีละบรรทัด",
      "1\n2\n3\n4\n5\n6",
      "for i in range(1, 6):  # ← แก้บรรทัดนี้\n    print(i)",
      "for i in range(1, 7):\n    print(i)",
      "range หยุดก่อนค่าสุดท้าย"),

    P(3, "แก้ while นับลูกค้า", "fix_customer_while",
      "ต้องการนับลูกค้าจาก 1 ถึง 4 แต่ยังไม่อัปเดต `count` ในลูป\n"
      "เติมบรรทัดอัปเดตให้ถูกต้อง",
      "เลข 1 ถึง 4",
      "1\n2\n3\n4",
      "count = 1\nwhile count <= 4:\n    print(count)\n    # เติมบรรทัดอัปเดตตรงนี้",
      "count = 1\nwhile count <= 4:\n    print(count)\n    count = count + 1",
      "ต้องเปลี่ยนค่า count ในทุกๆ รอบ"),

    P(4, "แก้ indent ใบเสร็จ", "fix_receipt_indent",
      "ต้องการพิมพ์รายการสินค้า 3 ชิ้นในลูป แต่ `print` อยู่นอกลูป\n"
      "จัด indent ให้พิมพ์ครบ",
      "Item 1 ถึง Item 3",
      "Item 1\nItem 2\nItem 3",
      'for i in range(1, 4):\n    pass\nprint(f"Item {i}")  # ← จัด indent / ลบ pass',
      'for i in range(1, 4):\n    print(f"Item {i}")',
      "คำสั่งที่ต้องทำทุกรอบต้องอยู่ในลูป"),

    P(8, "แก้พิมพ์สมาชิกทีม", "fix_team_names",
      "ต้องการพิมพ์ชื่อสมาชิกทีมทีละคน แต่โค้ดพิมพ์ list ทั้งก้อนทุกรอบ",
      "สามชื่อทีละบรรทัด",
      "Ann\nBen\nCara",
      'members = ["Ann", "Ben", "Cara"]\nfor member in members:\n    print(members)  # ← แก้ตรงนี้',
      'members = ["Ann", "Ben", "Cara"]\nfor member in members:\n    print(member)',
      "ในลูปให้ใช้ตัวแปรวน ไม่ใช่ชื่อ list"),

    P(9, "แก้ range คู่", "fix_even_range",
      "ต้องการพิมพ์เลขคู่ `2 4 6 8 10` แต่ตอนนี้หยุดที่ `8`\n"
      "แก้ค่า stop ของ `range`",
      "เลขคู่ 2 ถึง 10",
      "2\n4\n6\n8\n10",
      "for i in range(2, 10, 2):  # ← แก้\n    print(i)",
      "for i in range(2, 11, 2):\n    print(i)",
      "ต้องตั้ง stop ให้เลยค่าสุดท้ายที่ต้องการ"),

    P(6, "แก้รวมยอดใน list", "fix_sum_list",
      "ต้องการรวมราคา `[25, 40, 15]` แต่เขียน `total = price` ทำให้เหลือแค่ราคาสุดท้าย",
      "บรรทัดเดียว Total",
      "Total: 80",
      'prices = [25, 40, 15]\ntotal = 0\nfor price in prices:\n    total = price  # ← แก้\nprint(f"Total: {total}")',
      'prices = [25, 40, 15]\ntotal = 0\nfor price in prices:\n    total = total + price\nprint(f"Total: {total}")',
      "ต้องบวกเข้า total เดิม ไม่ใช่แทนที่"),

    P(7, "แก้ while ทายรหัส", "fix_pin_while",
      "รหัสลับคือ `7` รับเดาจนกว่าจะถูกแล้วพิมพ์ `Unlocked`\n"
      "เงื่อนไข while กลับด้าน — แก้ให้ถูก",
      "Unlocked เมื่อเดาถูก",
      "Unlocked",
      'secret = 7\nguess = int(input())\nwhile guess == secret:  # ← แก้เงื่อนไข\n    guess = int(input())\nprint("Unlocked")',
      'secret = 7\nguess = int(input())\nwhile guess != secret:\n    guess = int(input())\nprint("Unlocked")',
      "วนซ้ำขณะที่ยังเดาไม่ถูก",
      sample_in="3\n7",
      in_desc="ตัวเลขทายทีละบรรทัด จนตรงรหัส"),

    P(10, "แก้ข้ามเลขศูนย์", "fix_skip_zero",
      "พิมพ์เลขใน list `[3, 0, 5, 0, 2]` แต่ข้ามศูนย์\n"
      "`continue` อยู่หลัง `print` — จัดลำดับใหม่",
      "เลขที่ไม่ใช่ศูนย์",
      "3\n5\n2",
      "nums = [3, 0, 5, 0, 2]\nfor n in nums:\n    print(n)\n    if n == 0:\n        continue",
      "nums = [3, 0, 5, 0, 2]\nfor n in nums:\n    if n == 0:\n        continue\n    print(n)",
      "ต้องตัดสินใจข้ามก่อนพิมพ์"),

    P(11, "แก้ตารางดาว", "fix_star_table",
      "ต้องการตารางดาว 2 แถว ละ 4 ดอก แต่ลูปในใช้ `range(row)`",
      "สองแถวดาวละ 4",
      "****\n****",
      'for row in range(2):\n    for col in range(row):  # ← แก้\n        print("*", end="")\n    print()',
      'for row in range(2):\n    for col in range(4):\n        print("*", end="")\n    print()',
      "ความกว้างคงที่ ไม่ผูกกับหมายเลขแถว"),

    P(12, "แก้ break เร็วเกิน", "fix_early_break",
      'พิมพ์คิว `["Wait", "Wait", "Serve", "Wait"]` จนเจอ `Serve` รวมการพิมพ์ Serve ด้วย',
      "Wait Wait Serve",
      "Wait\nWait\nServe",
      'queue = ["Wait", "Wait", "Serve", "Wait"]\nfor item in queue:\n    if item == "Serve":\n        break\n    print(item)',
      'queue = ["Wait", "Wait", "Serve", "Wait"]\nfor item in queue:\n    print(item)\n    if item == "Serve":\n        break',
      "พิมพ์ก่อน แล้วค่อย break"),

    P(13, "แก้เฉลี่ยอุณหภูมิ", "fix_avg_temps",
      "อุณหภูมิ `[28, 30, 32]` ต้องได้ `Average: 30.0`\n"
      "ย้ายการหารออกมานอกลูป",
      "บรรทัดเดียว Average",
      "Average: 30.0",
      'temps = [28, 30, 32]\ntotal = 0\nfor t in temps:\n    total = total + t\n    average = total / len(temps)\nprint(f"Average: {average:.1f}")',
      'temps = [28, 30, 32]\ntotal = 0\nfor t in temps:\n    total = total + t\naverage = total / len(temps)\nprint(f"Average: {average:.1f}")',
      "รวมให้ครบก่อน แล้วค่อยหารครั้งเดียว"),

    P(5, "แก้รายงานยอดขาย", "fix_sales_report",
      "จากยอด `[100, 50, 150]` ต้องพิมพ์ยอดทีละบรรทัด แล้ว `Total: 300` และ `Count: 3`\n"
      "โค้ดเริ่มต้นผิดหลายจุด — แก้ให้ครบ",
      "รายการ + Total + Count",
      "100\n50\n150\nTotal: 300\nCount: 3",
      'sales = [100, 50, 150]\ntotal = 0\ncount = 0\nfor sale in sales:\n    print(sales)\n    total = sale\nprint(f"Total: {total}")\nprint(f"Count: {count}")',
      'sales = [100, 50, 150]\ntotal = 0\ncount = 0\nfor sale in sales:\n    print(sale)\n    total = total + sale\n    count = count + 1\nprint(f"Total: {total}")\nprint(f"Count: {count}")',
      "ตรวจทีละจุด: สิ่งที่พิมพ์ / วิธีสะสม / จุดที่นับ"),

    P(14, "แก้คิวสั่งอาหาร", "fix_food_queue",
      "รับชื่อเมนูทีละบรรทัดจนเจอ `end`\n"
      "พิมพ์เมนูที่รับจริง (ไม่รวม end) แล้วปิดท้ายด้วย `Count: <จำนวน>`\n"
      "โค้ดเริ่มต้นพิมพ์ end และนับรวม end — แก้ลำดับเงื่อนไขให้ถูก",
      "รายการเมนูแล้วตามด้วย Count",
      "Pad Thai\nGreen Curry\nCount: 2",
      'count = 0\nwhile True:\n    menu = input()\n    print(menu)\n    count = count + 1\n    if menu == "end":\n        break\nprint(f"Count: {count}")',
      'count = 0\nwhile True:\n    menu = input()\n    if menu == "end":\n        break\n    print(menu)\n    count = count + 1\nprint(f"Count: {count}")',
      "เช็คคำจบก่อนพิมพ์และก่อนนับ",
      sample_in="Pad Thai\nGreen Curry\nend",
      in_desc="ชื่อเมนูทีละบรรทัด จบด้วย end"),

    P(15, "แก้ผังที่นั่ง", "fix_seat_map",
      "ต้องการผัง 2 แถว ละ 3 ที่แบบ `R1: 1 2 3` และ `R2: 1 2 3`\n"
      "โค้ดเริ่มต้นใช้หมายเลขแถวผิดและลูปในสั้นเกิน — แก้ให้ถูก",
      "สองบรรทัดผังที่นั่ง",
      "R1: 1 2 3 \nR2: 1 2 3 ",
      'for row in range(2):\n    print(f"R{row}:", end=" ")\n    for seat in range(2):\n        print(seat, end=" ")\n    print()',
      'for row in range(1, 3):\n    print(f"R{row}:", end=" ")\n    for seat in range(1, 4):\n        print(seat, end=" ")\n    print()',
      "แถวและที่นั่งควรเริ่มที่ 1 และที่นั่งมี 3 ช่อง"),

    P(16, "แก้สรุปสต็อก", "fix_stock_summary",
      "จำนวนสินค้าในชั้น `[4, 0, 7, 0, 3]`\n"
      "- ข้ามช่องที่เป็น 0\n"
      "- รวมจำนวนที่เหลือ\n"
      "- นับจำนวนชั้นที่มีของ\n"
      "ต้องได้ `Shelves: 3` และ `Items: 14`\n"
      "โค้ดเริ่มต้นนับศูนย์และสะสมผิด — แก้ให้ถูก",
      "สองบรรทัดสรุป",
      "Shelves: 3\nItems: 14",
      'stock = [4, 0, 7, 0, 3]\nshelves = 0\nitems = 0\nfor qty in stock:\n    shelves = shelves + 1\n    items = qty\nprint(f"Shelves: {shelves}")\nprint(f"Items: {items}")',
      'stock = [4, 0, 7, 0, 3]\nshelves = 0\nitems = 0\nfor qty in stock:\n    if qty == 0:\n        continue\n    shelves = shelves + 1\n    items = items + qty\nprint(f"Shelves: {shelves}")\nprint(f"Items: {items}")',
      "ข้ามศูนย์ก่อน แล้วค่อยนับชั้นและบวกจำนวน"),
]


if __name__ == "__main__":
    write_week(
        "023-debugging-loops",
        chapter="debugging-loops",
        emoji="🐛",
        index_md=INDEX,
        problems=PROBLEMS,
    )
