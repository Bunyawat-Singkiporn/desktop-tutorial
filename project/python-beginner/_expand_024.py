# -*- coding: utf-8 -*-
"""Expand 024-midyear-review. NO append/sum/split/min/max. Hardcoded lists OK."""
from _expand_helpers import write_week

INDEX = """
# 📋 สารบัญโจทย์ — บท 024 Mid-Year Review

**ขอบเขตของบทนี้:** ทบทวนความรู้บท 001–023

> ❌ ห้าม `.append()` / `sum()` / `.split()` / `min()` / `max()`
> ✅ list แบบ hardcode + `for x in list` ได้ (บท 018)
> ❌ ข้อ `02` ไม่ซ้ำโปรแกรมรวมในบทเรียน (ชื่อ+append คะแนน 3 วิชา)

---

## ลำดับที่แนะนำ

| # | ไฟล์ | ระดับ | โจทย์ | แกนการคิด |
|---|------|-------|-------|-----------|
| 1 | `02_test.md` | 🟢 | ป้ายชื่อนักเรียน | input + f-string |
| 2 | `03_test.md` | 🟢 | คิดเงินทอน | ตัวดำเนินการ |
| 3 | `04_test.md` | 🟢 | ผ่านเกณฑ์ไหม | if/else |
| 4 | `08_easy.md` | 🟢 | พิมพ์เลข 1 ถึง n | for range |
| 5 | `09_easy.md` | 🟢 | แสดงรายการของใช้ | for-in list |
| 6 | `06_medium.md` | 🟡 | ค่าเฉลี่ยคะแนนห้อง | list + accumulator |
| 7 | `07_medium.md` | 🟡 | นับถอยหลังเปิดงาน | while |
| 8 | `10_medium.md` | 🟡 | รวมยอดจนเจอ 0 | while True + break |
| 9 | `11_medium.md` | 🟡 | ข้ามคะแนนศูนย์ | continue |
| 10 | `12_medium.md` | 🟡 | ตารางดาวเล็ก | nested loops |
| 11 | `13_medium.md` | 🟡 | เกรดจากคะแนน | elif |
| 12 | `05_challenge.md` | 🔴 | ใบเสร็จร้านกาแฟ | input + คำนวณ + กล่อง |
| 13 | `14_challenge.md` | 🔴 | สรุปอุณหภูมิสัปดาห์ | list + สถิติ + สถานะ |
| 14 | `15_challenge.md` | 🔴 | ระบบเข้าคิวร้าน | while True เมนูสั้น |
| 15 | `16_challenge.md` | 🔴 | รายงานคะแนนห้อง | list + กรอง + สรุปกรอบ |

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
    P(2, "ป้ายชื่อนักเรียน", "student_badge",
      "รับชื่อนักเรียนแล้วพิมพ์ป้าย `Hello, <ชื่อ>!`",
      "บรรทัดเดียวทักทาย",
      "Hello, Mira!",
      "name = input()\n\n# พิมพ์ป้าย",
      'name = input()\nprint(f"Hello, {name}!")',
      sample_in="Mira",
      in_desc="ชื่อ 1 บรรทัด"),

    P(3, "คิดเงินทอน", "make_change",
      "รับราคาสินค้าและเงินที่จ่าย (จำนวนเต็ม) แล้วพิมพ์เงินทอน",
      "บรรทัดเดียว Change: <เงินทอน>",
      "Change: 30",
      "price = int(input())\npaid = int(input())\n\n# คำนวณแล้วพิมพ์",
      "price = int(input())\npaid = int(input())\nchange = paid - price\nprint(f\"Change: {change}\")",
      sample_in="70\n100",
      in_desc="ราคา 1 บรรทัด แล้วเงินที่จ่าย 1 บรรทัด"),

    P(4, "ผ่านเกณฑ์ไหม", "pass_check",
      "รับคะแนน ถ้า `>= 50` พิมพ์ `Pass` ไม่เช่นนั้นพิมพ์ `Fail`",
      "Pass หรือ Fail",
      "Pass",
      "score = int(input())\n\n# ตรวจเกณฑ์",
      "score = int(input())\nif score >= 50:\n    print(\"Pass\")\nelse:\n    print(\"Fail\")",
      sample_in="72",
      in_desc="คะแนนจำนวนเต็ม 1 บรรทัด"),

    P(8, "พิมพ์เลข 1 ถึง n", "print_to_n",
      "รับ `n` แล้วพิมพ์เลขจาก 1 ถึง n ทีละบรรทัด",
      "เลข 1 ถึง n",
      "1\n2\n3\n4",
      "n = int(input())\n\n# วนพิมพ์",
      "n = int(input())\nfor i in range(1, n + 1):\n    print(i)",
      sample_in="4",
      in_desc="จำนวนเต็ม n 1 บรรทัด"),

    P(9, "แสดงรายการของใช้", "supply_list",
      'รายการของใช้ `["Pen", "Notebook", "Eraser"]` วนพิมพ์ทีละชิ้น',
      "สามบรรทัด",
      "Pen\nNotebook\nEraser",
      'supplies = ["Pen", "Notebook", "Eraser"]\n\n# วนพิมพ์',
      'supplies = ["Pen", "Notebook", "Eraser"]\nfor item in supplies:\n    print(item)'),

    P(6, "ค่าเฉลี่ยคะแนนห้อง", "class_average",
      "คะแนนห้อง `[80, 70, 90, 60]` หาผลรวมและค่าเฉลี่ยทศนิยม 1 ตำแหน่ง",
      "สองบรรทัด Total และ Average",
      "Total: 300\nAverage: 75.0",
      "scores = [80, 70, 90, 60]\ntotal = 0\n\n# รวมและเฉลี่ย",
      "scores = [80, 70, 90, 60]\ntotal = 0\nfor score in scores:\n    total = total + score\naverage = total / len(scores)\nprint(f\"Total: {total}\")\nprint(f\"Average: {average:.1f}\")",
      "สะสมด้วยลูป ห้ามใช้ sum()"),

    P(7, "นับถอยหลังเปิดงาน", "event_countdown",
      "นับถอยหลังจาก 5 ถึง 1 ด้วย while แล้วพิมพ์ `Start!`",
      "5 ถึง 1 แล้ว Start!",
      "5\n4\n3\n2\n1\nStart!",
      "count = 5\n\n# while นับลง",
      "count = 5\nwhile count > 0:\n    print(count)\n    count = count - 1\nprint(\"Start!\")",
      "อัปเดตตัวนับทุกครั้ง"),

    P(10, "รวมยอดจนเจอ 0", "sum_until_zero",
      "รับจำนวนเต็มทีละบรรทัดจนเจอ `0` แล้วพิมพ์ผลรวมของค่าก่อนหน้า",
      "บรรทัดเดียว Total",
      "Total: 18",
      "total = 0\n\n# while True จน 0",
      "total = 0\nwhile True:\n    value = int(input())\n    if value == 0:\n        break\n    total = total + value\nprint(f\"Total: {total}\")",
      "เจอ 0 ให้หยุดโดยไม่บวก",
      sample_in="5\n7\n6\n0",
      in_desc="จำนวนเต็มทีละบรรทัด จบด้วย 0"),

    P(11, "ข้ามคะแนนศูนย์", "skip_zero_scores",
      "คะแนน `[10, 0, 8, 0, 9]` พิมพ์เฉพาะค่าที่มากกว่า 0",
      "คะแนนที่ไม่ใช่ศูนย์",
      "10\n8\n9",
      "scores = [10, 0, 8, 0, 9]\n\n# ข้ามศูนย์แล้วพิมพ์",
      "scores = [10, 0, 8, 0, 9]\nfor score in scores:\n    if score == 0:\n        continue\n    print(score)",
      "ใช้ continue เมื่อเจอศูนย์"),

    P(12, "ตารางดาวเล็ก", "mini_star_grid",
      "พิมพ์ตารางดาว 3 แถว กว้าง 3 ดอก",
      "ตาราง 3×3",
      "***\n***\n***",
      "# nested loops",
      'for row in range(3):\n    for col in range(3):\n        print("*", end="")\n    print()'),

    P(13, "เกรดจากคะแนน", "letter_grade",
      "รับคะแนนแล้วพิมพ์เกรด\n"
      "- `>= 80` → `A`\n"
      "- `>= 60` → `B`\n"
      "- น้อยกว่านั้น → `C`",
      "บรรทัดเดียว Grade: <ตัวอักษร>",
      "Grade: B",
      "score = int(input())\n\n# หาเกรด",
      "score = int(input())\nif score >= 80:\n    print(\"Grade: A\")\nelif score >= 60:\n    print(\"Grade: B\")\nelse:\n    print(\"Grade: C\")",
      sample_in="65",
      in_desc="คะแนนจำนวนเต็ม 1 บรรทัด"),

    P(5, "ใบเสร็จร้านกาแฟ", "coffee_receipt",
      "รับชื่อเมนู ราคากาแฟ และราคขนม (จำนวนเต็ม)\n"
      "คำนวณยอดรวม แล้วพิมพ์ใบเสร็จในกรอบดังตัวอย่าง",
      "ใบเสร็จในกรอบ",
      "====================\n"
      "      COFFEE\n"
      "====================\n"
      "Menu  : Latte\n"
      "Coffee: 55\n"
      "Snack : 20\n"
      "Total : 75\n"
      "====================",
      "menu = input()\ncoffee = int(input())\nsnack = int(input())\n\n# พิมพ์ใบเสร็จ",
      "menu = input()\ncoffee = int(input())\nsnack = int(input())\ntotal = coffee + snack\nprint(\"====================\")\nprint(\"      COFFEE\")\nprint(\"====================\")\nprint(f\"Menu  : {menu}\")\nprint(f\"Coffee: {coffee}\")\nprint(f\"Snack : {snack}\")\nprint(f\"Total : {total}\")\nprint(\"====================\")",
      "จัดคอลัมน์เครื่องหมาย : ให้ตรงกัน",
      sample_in="Latte\n55\n20",
      in_desc="ชื่อเมนู 1 บรรทัด แล้วราคากาแฟ 1 บรรทัด แล้วราคขนม 1 บรรทัด"),

    P(14, "สรุปอุณหภูมิสัปดาห์", "week_temps",
      "อุณหภูมิ `[29, 31, 30, 33, 28]`\n"
      "แสดงผลรวม ค่าเฉลี่ยทศนิยม 1 ตำแหน่ง และสถานะ\n"
      "- เฉลี่ย `>= 30` → `Hot Week`\n"
      "- น้อยกว่านั้น → `Cool Week`",
      "สามบรรทัดสรุป",
      "Total: 151\nAverage: 30.2\nStatus: Hot Week",
      "temps = [29, 31, 30, 33, 28]\ntotal = 0\n\n# สรุป",
      "temps = [29, 31, 30, 33, 28]\ntotal = 0\nfor t in temps:\n    total = total + t\naverage = total / len(temps)\nprint(f\"Total: {total}\")\nprint(f\"Average: {average:.1f}\")\nif average >= 30:\n    print(\"Status: Hot Week\")\nelse:\n    print(\"Status: Cool Week\")",
      "คำนวณเฉลี่ยก่อนตัดสินสถานะ"),

    P(15, "ระบบเข้าคิวร้าน", "shop_queue",
      "รับคำสั่งทีละบรรทัด\n"
      '- ถ้าเป็น `join` พิมพ์ `Added`\n'
      '- ถ้าเป็น `quit` พิมพ์ `Closed` แล้วหยุด\n'
      "- คำอื่นพิมพ์ `Unknown`",
      "ข้อความตอบกลับตามคำสั่ง",
      "Added\nUnknown\nClosed",
      "# while True อ่านคำสั่ง",
      "while True:\n    command = input()\n    if command == \"quit\":\n        print(\"Closed\")\n        break\n    elif command == \"join\":\n        print(\"Added\")\n    else:\n        print(\"Unknown\")",
      "ใช้ while True แล้วค่อยแยกคำสั่ง",
      sample_in="join\nhello\nquit",
      in_desc="คำสั่งทีละบรรทัด จบด้วย quit"),

    P(16, "รายงานคะแนนห้อง", "class_report",
      "คะแนน `[55, 80, 40, 90, 70]`\n"
      "พิมพ์เฉพาะคนที่ได้ `>= 50` เป็น `Pass: <คะแนน>`\n"
      "จากนั้นสรุปในกรอบ:\n"
      "- จำนวนที่ผ่าน\n"
      "- ผลรวมของคะแนนที่ผ่านเท่านั้น",
      "รายการ Pass แล้วตามด้วยกรอบสรุป",
      "Pass: 55\n"
      "Pass: 80\n"
      "Pass: 90\n"
      "Pass: 70\n"
      "==============\n"
      "Passed : 4\n"
      "SumPass: 295\n"
      "==============",
      "scores = [55, 80, 40, 90, 70]\npassed = 0\ntotal = 0\n\n# กรองและสรุป",
      "scores = [55, 80, 40, 90, 70]\npassed = 0\ntotal = 0\nfor score in scores:\n    if score < 50:\n        continue\n    print(f\"Pass: {score}\")\n    passed = passed + 1\n    total = total + score\nprint(\"==============\")\nprint(f\"Passed : {passed}\")\nprint(f\"SumPass: {total}\")\nprint(\"==============\")",
      "ข้ามคะแนนต่ำ แล้วค่อยสะสมเฉพาะที่ผ่าน"),
]


if __name__ == "__main__":
    write_week(
        "024-midyear-review",
        chapter="midyear-review",
        emoji="🏆",
        index_md=INDEX,
        problems=PROBLEMS,
    )
