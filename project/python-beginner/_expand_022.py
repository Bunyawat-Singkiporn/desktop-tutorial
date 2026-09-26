# -*- coding: utf-8 -*-
"""Expand 022-loop-review to 15-problem standard. NO .append() / sum()."""
from _expand_helpers import write_week

INDEX = """
# 📋 สารบัญโจทย์ — บท 022 Loop Review

**ขอบเขตของบทนี้:** ทบทวน loop ทุกแบบจากบท 017–021 + ใช้ `+=` ได้

> ❌ ห้าม `.append()` (บท 026) · ห้าม `sum()` (บท 040) · ห้าม `min()`/`max()`
> ❌ list ใช้แบบ hardcode + `for x in list` ได้ (บท 018)
> ❌ ข้อ `02` ไม่ซ้ำตัวอย่างในบทเรียน (รวมคะแนน list เดิม / while จน 0 / สามเหลี่ยมดาวตาม n)

---

## ลำดับที่แนะนำ

| # | ไฟล์ | ระดับ | โจทย์ | แกนการคิด |
|---|------|-------|-------|-----------|
| 1 | `02_test.md` | 🟢 | รวมแต้มเกม | for range + accumulator |
| 2 | `03_test.md` | 🟢 | แสดงเมนูของหวาน | for-in list |
| 3 | `04_test.md` | 🟢 | นับถอยหลังเปิดร้าน | while นับลง |
| 4 | `08_easy.md` | 🟢 | พิมพ์คู่ถึง n | for range step 2 |
| 5 | `09_easy.md` | 🟢 | ข้ามเลขหายนะ | continue ใน for |
| 6 | `06_medium.md` | 🟡 | รวมยอดบิลจนจบ | while True + break |
| 7 | `07_medium.md` | 🟡 | ค่าเฉลี่ยอุณหภูมิ | list + รวม + len |
| 8 | `10_medium.md` | 🟡 | นับสินค้าเกินเกณฑ์ | if ใน for-list |
| 9 | `11_medium.md` | 🟡 | ตารางดาวตามกว้าง | nested ตาม input |
| 10 | `12_medium.md` | 🟡 | หยุดเมื่อเจอ SoldOut | break ใน list |
| 11 | `13_medium.md` | 🟡 | รวมเฉพาะเลขคี่ | continue + สะสม |
| 12 | `05_challenge.md` | 🔴 | สรุปคะแนนสอบย่อย | list + สถิติ + เกรด |
| 13 | `14_challenge.md` | 🔴 | รับคะแนนจน -1 | while True สรุป |
| 14 | `15_challenge.md` | 🔴 | ผังดาวห้องโชว์ | nested + หัวข้อ |
| 15 | `16_challenge.md` | 🔴 | กรองออเดอร์บวก | continue + รวม + นับ |

**สรุป:** 🟢 Easy 5 ข้อ · 🟡 Medium 6 ข้อ · 🔴 Challenge 4 ข้อ = **15 ข้อ**
"""

NO_IN = "ไม่มี (กำหนดค่าในโปรแกรม)"


def P(n, title, slug, body, out_desc, sample_out, starter, answer,
      hint=None, sample_in=None, in_desc=NO_IN):
    return dict(
        n=n, title=title, slug=slug, body=body,
        input_desc=in_desc, output_desc=out_desc,
        sample_input=sample_in, sample_output=sample_out,
        hint=hint, starter=starter, answer=answer,
    )


PROBLEMS = [
    P(2, "รวมแต้มเกม", "game_points",
      "เกมให้แต้มรอบละเท่ากับหมายเลขรอบตั้งแต่ 1 ถึง `n`\n"
      "รับ `n` แล้วรวมแต้มทั้งหมดด้วย `for` และ `+=`",
      "บรรทัดเดียว Total Points: <ผลรวม>",
      "Total Points: 15",
      "n = int(input())\ntotal = 0\n\n# รวมแต้มแล้วพิมพ์",
      "n = int(input())\n"
      "total = 0\n"
      "for i in range(1, n + 1):\n"
      "    total += i\n"
      'print(f"Total Points: {total}")',
      sample_in="5",
      in_desc="จำนวนเต็ม n 1 บรรทัด"),

    P(3, "แสดงเมนูของหวาน", "dessert_menu",
      'ร้านมีเมนูของหวานใน list: `"Cake"`, `"Pudding"`, `"Ice Cream"`\n'
      "วนพิมพ์ทีละรายการ",
      "3 บรรทัดชื่อของหวาน",
      "Cake\nPudding\nIce Cream",
      'desserts = ["Cake", "Pudding", "Ice Cream"]\n\n# วนพิมพ์',
      'desserts = ["Cake", "Pudding", "Ice Cream"]\n'
      "for item in desserts:\n"
      "    print(item)"),

    P(4, "นับถอยหลังเปิดร้าน", "open_countdown",
      "ป้ายร้านนับถอยหลังจาก 3 ถึง 1 ด้วย `while` แล้วพิมพ์ `Open!`",
      "เลข 3 2 1 แล้ว Open!",
      "3\n2\n1\nOpen!",
      "count = 3\n\n# while นับลง แล้วพิมพ์ Open!",
      "count = 3\n"
      "while count > 0:\n"
      "    print(count)\n"
      "    count = count - 1\n"
      'print("Open!")'),

    P(8, "พิมพ์คู่ถึง n", "even_to_n",
      "รับ `n` แล้วพิมพ์เลขคู่ตั้งแต่ 2 ถึง `n` inclusive ด้วย `range` แบบมี step",
      "เลขคู่ทีละบรรทัด",
      "2\n4\n6\n8\n10",
      "n = int(input())\n\n# พิมพ์เลขคู่",
      "n = int(input())\n"
      "for i in range(2, n + 1, 2):\n"
      "    print(i)",
      sample_in="10",
      in_desc="จำนวนเต็ม n 1 บรรทัด"),

    P(9, "ข้ามเลขหายนะ", "skip_unlucky",
      "พิมพ์เลข 1 ถึง 8 แต่ข้ามเลข `4` ด้วย `continue`",
      "เลข 1–8 ยกเว้น 4",
      "1\n2\n3\n5\n6\n7\n8",
      "# for + continue",
      "for i in range(1, 9):\n"
      "    if i == 4:\n"
      "        continue\n"
      "    print(i)"),

    P(6, "รวมยอดบิลจนจบ", "bill_until_done",
      "แคชเชียร์รับยอดสินค้าทีละบรรทัด\n"
      'เมื่อรับข้อความ `done` ให้หยุด แล้วพิมพ์ยอดรวมเป็นจำนวนเต็มของยอดที่รับมาก่อนหน้า\n'
      "(ยอดแต่ละรายการเป็นจำนวนเต็ม)",
      "บรรทัดเดียว Total: <ยอดรวม>",
      "Total: 120",
      "total = 0\n\n# while True รับยอดจน done",
      "total = 0\n"
      "while True:\n"
      "    text = input()\n"
      '    if text == "done":\n'
      "        break\n"
      "    total += int(text)\n"
      'print(f"Total: {total}")',
      "แปลงเป็น int หลังเช็คว่ายังไม่ใช่ done",
      sample_in="50\n70\ndone",
      in_desc="ยอดเป็นตัวเลขทีละบรรทัด จบด้วยคำว่า done"),

    P(7, "ค่าเฉลี่ยอุณหภูมิ", "temp_average",
      "อุณหภูมิ 5 วันอยู่ใน list `[30, 32, 29, 31, 33]`\n"
      "หาผลรวมแล้วคำนวณค่าเฉลี่ย แสดงทศนิยม 1 ตำแหน่ง",
      "สองบรรทัด Total และ Average",
      "Total: 155\nAverage: 31.0",
      "temps = [30, 32, 29, 31, 33]\ntotal = 0\n\n# รวม แล้วหาเฉลี่ย",
      "temps = [30, 32, 29, 31, 33]\n"
      "total = 0\n"
      "for t in temps:\n"
      "    total += t\n"
      "average = total / len(temps)\n"
      'print(f"Total: {total}")\n'
      'print(f"Average: {average:.1f}")',
      "หารด้วย len หลังรวมครบ"),

    P(10, "นับสินค้าเกินเกณฑ์", "count_expensive",
      "ราคาสินค้า `[120, 45, 200, 80, 150]`\n"
      "นับว่ามีกี่ชิ้นที่ราคา `>= 100` แล้วพิมพ์จำนวน",
      "บรรทัดเดียว Count: <จำนวน>",
      "Count: 3",
      "prices = [120, 45, 200, 80, 150]\ncount = 0\n\n# นับแล้วพิมพ์",
      "prices = [120, 45, 200, 80, 150]\n"
      "count = 0\n"
      "for price in prices:\n"
      "    if price >= 100:\n"
      "        count += 1\n"
      'print(f"Count: {count}")',
      "เพิ่มตัวนับเฉพาะเมื่อผ่านเกณฑ์"),

    P(11, "ตารางดาวตามกว้าง", "star_grid",
      "รับจำนวนแถว `rows` และความกว้าง `width`\n"
      "พิมพ์ตารางดาว `*` ตามขนาดนั้น",
      "ตารางดาว",
      "**\n**\n**",
      "rows = int(input())\nwidth = int(input())\n\n# nested loops",
      "rows = int(input())\n"
      "width = int(input())\n"
      "for r in range(rows):\n"
      "    for c in range(width):\n"
      '        print("*", end="")\n'
      "    print()",
      "ลูปนอกตามแถว ลูปในตามความกว้าง",
      sample_in="3\n2",
      in_desc="จำนวนแถว 1 บรรทัด แล้วความกว้าง 1 บรรทัด"),

    P(12, "หยุดเมื่อเจอ SoldOut", "stop_soldout",
      'สถานะสินค้าในคิว: `"Ready"`, `"Ready"`, `"SoldOut"`, `"Ready"`\n'
      "พิมพ์สถานะทีละตัว จนเจอ `SoldOut` ให้พิมพ์มันแล้ว `break`",
      "สถานะจนถึง SoldOut",
      "Ready\nReady\nSoldOut",
      'statuses = ["Ready", "Ready", "SoldOut", "Ready"]\n\n# วนพิมพ์และ break',
      'statuses = ["Ready", "Ready", "SoldOut", "Ready"]\n'
      "for status in statuses:\n"
      "    print(status)\n"
      '    if status == "SoldOut":\n'
      "        break",
      "พิมพ์ก่อน แล้วค่อยเช็คเพื่อ break"),

    P(13, "รวมเฉพาะเลขคี่", "sum_odds",
      "รับ `n` แล้วรวมเฉพาะเลขคี่ตั้งแต่ 1 ถึง `n`\n"
      "เลขคู่ให้ `continue` ข้าม",
      "บรรทัดเดียว Odd Total: <ผลรวม>",
      "Odd Total: 9",
      "n = int(input())\ntotal = 0\n\n# รวมเลขคี่",
      "n = int(input())\n"
      "total = 0\n"
      "for i in range(1, n + 1):\n"
      "    if i % 2 == 0:\n"
      "        continue\n"
      "    total += i\n"
      'print(f"Odd Total: {total}")',
      "ข้ามคู่ด้วย continue แล้วค่อยบวกคี่",
      sample_in="5",
      in_desc="จำนวนเต็ม n 1 บรรทัด"),

    P(5, "สรุปคะแนนสอบย่อย", "quiz_summary",
      "คะแนนสอบย่อย `[70, 85, 60, 90]`\n"
      "แสดงผลรวม ค่าเฉลี่ยทศนิยม 1 ตำแหน่ง และสถานะ\n"
      "- เฉลี่ย `>= 70` → `Status: Good`\n"
      "- น้อยกว่านั้น → `Status: Needs Work`",
      "สามบรรทัดสรุป",
      "Total: 305\nAverage: 76.2\nStatus: Good",
      "scores = [70, 85, 60, 90]\ntotal = 0\n\n# สรุปผล",
      "scores = [70, 85, 60, 90]\n"
      "total = 0\n"
      "for score in scores:\n"
      "    total += score\n"
      "average = total / len(scores)\n"
      'print(f"Total: {total}")\n'
      'print(f"Average: {average:.1f}")\n'
      "if average >= 70:\n"
      '    print("Status: Good")\n'
      "else:\n"
      '    print("Status: Needs Work")',
      "คำนวณเฉลี่ยก่อน แล้วค่อยตัดสินสถานะ"),

    P(14, "รับคะแนนจน -1", "scores_until_neg",
      "รับคะแนนทีละบรรทัดจนเจอ `-1` แล้วหยุด\n"
      "แสดงจำนวนครั้งที่รับ (ไม่นับ -1) และผลรวม",
      "สองบรรทัด Count และ Total",
      "Count: 3\nTotal: 240",
      "count = 0\ntotal = 0\n\n# while True จน -1",
      "count = 0\n"
      "total = 0\n"
      "while True:\n"
      "    score = int(input())\n"
      "    if score == -1:\n"
      "        break\n"
      "    count += 1\n"
      "    total += score\n"
      'print(f"Count: {count}")\n'
      'print(f"Total: {total}")',
      "เช็ค -1 ก่อนนับและก่อนบวก",
      sample_in="80\n70\n90\n-1",
      in_desc="คะแนนทีละบรรทัด จบด้วย -1"),

    P(15, "ผังดาวห้องโชว์", "showroom_stars",
      "พิมพ์หัวข้อ `SHOWROOM` แล้วตามด้วยตารางดาว 3 แถว กว้าง 5 ดอก\n"
      "ปิดท้ายด้วย `END`",
      "หัวข้อ + ตาราง + END",
      "SHOWROOM\n*****\n*****\n*****\nEND",
      "# พิมพ์หัวข้อ ตารางดาว และ END",
      'print("SHOWROOM")\n'
      "for row in range(3):\n"
      "    for col in range(5):\n"
      '        print("*", end="")\n'
      "    print()\n"
      'print("END")',
      "หัวท้ายอยู่นอกลูป ตารางใช้ลูปซ้อน"),

    P(16, "กรองออเดอร์บวก", "filter_orders",
      "ยอดออเดอร์ `[50, -10, 30, 0, 20]`\n"
      "- ข้ามค่าที่ `<= 0` ด้วย `continue`\n"
      "- รวมเฉพาะยอดบวก และนับจำนวนออเดอร์ที่นับได้\n"
      "แสดง Count และ Total",
      "สองบรรทัด Count และ Total",
      "Count: 3\nTotal: 100",
      "orders = [50, -10, 30, 0, 20]\ncount = 0\ntotal = 0\n\n# กรองแล้วสรุป",
      "orders = [50, -10, 30, 0, 20]\n"
      "count = 0\n"
      "total = 0\n"
      "for order in orders:\n"
      "    if order <= 0:\n"
      "        continue\n"
      "    count += 1\n"
      "    total += order\n"
      'print(f"Count: {count}")\n'
      'print(f"Total: {total}")',
      "continue ก่อน แล้วค่อยนับและบวก"),
]


if __name__ == "__main__":
    write_week(
        "022-loop-review",
        chapter="loop-review",
        emoji="🔁",
        index_md=INDEX,
        problems=PROBLEMS,
    )
