# -*- coding: utf-8 -*-
"""Expand 005-variables to 15-problem standard. No input/if/f-string/*/ /. """
from _expand_helpers import write_week

INDEX = """
# 📋 สารบัญโจทย์ — บท 005 Variables

**ขอบเขตของบทนี้:** ตัวแปร `=` / เปลี่ยนค่า / `print(var)` / `print("label:", var)` / บวกตัวเลขด้วย `+`

> ❌ ไม่มี `input()` · ไม่มี `*` `/` (บท 011) · ไม่มี f-string (บท 010) · ไม่มี `if`

---

## ลำดับที่แนะนำ

| # | ไฟล์ | ระดับ | โจทย์ | แกนการคิด |
|---|------|-------|-------|-----------|
| 1 | `02_test.md` | 🟢 | การ์ดนักเรียน | เก็บ str/int แล้วพิมพ์ป้ายกำกับ |
| 2 | `03_test.md` | 🟢 | คะแนนสองวิชา | บวกสองตัวแปร |
| 3 | `04_test.md` | 🟢 | เปลี่ยนค่าคะแนน | reassignment แล้วพิมพ์ |
| 4 | `08_easy.md` | 🟢 | ราคาผลไม้สองลูก | เก็บราคาแล้วรวม |
| 5 | `09_easy.md` | 🟢 | ทักทายด้วยชื่อ | print หลายอาร์กิวเมนต์ |
| 6 | `06_medium.md` | 🟡 | ยอดเงินในกระเป๋า | เก็บหลายค่าแล้วสรุป |
| 7 | `07_medium.md` | 🟡 | อุณหภูมิเช้า-เย็น | สองค่า + ผลต่างด้วยการบวกของติดลบ |
| 8 | `10_medium.md` | 🟡 | คะแนนควิซสามข้อ | รวมสามค่า |
| 9 | `11_medium.md` | 🟡 | สต็อกสินค้า | เปลี่ยนค่าแล้วพิมพ์สถานะ |
| 10 | `12_medium.md` | 🟡 | ใบเสร็จสองรายการ | ป้ายกำกับหลายบรรทัด |
| 11 | `13_medium.md` | 🟡 | โปรไฟล์เกม | ผสม str/int/float |
| 12 | `05_challenge.md` | 🔴 | บิลร้านอาหาร | รวมหลายรายการ + จัดรูปแบบ |
| 13 | `14_challenge.md` | 🔴 | สมุดพกคะแนน | รวมแล้วเปลี่ยนค่าโบนัส |
| 14 | `15_challenge.md` | 🔴 | สรุปทริป | หลายตัวแปร + ผลรวม |
| 15 | `16_challenge.md` | 🔴 | กระปุกออมสิน | เติมเงินทีละขั้นด้วย reassignment |

**สรุป:** 🟢 Easy 5 ข้อ · 🟡 Medium 6 ข้อ · 🔴 Challenge 4 ข้อ = **15 ข้อ**

---

## หมายเหตุสำหรับครู

- ข้อ 02 ไม่ซ้ำตัวอย่าง name/age/city ในบทเรียนเป๊ะ — ใช้การ์ดนักเรียนเลขประจำตัว
- ห้ามใช้ `*` `/` สำหรับส่วนลดเปอร์เซ็นต์ — ยังไม่สอนในบทนี้
"""

NO_INPUT = "ไม่มี (ค่าถูกกำหนดในตัวแปรแล้ว)"


def P(n, title, slug, body, output_desc, sample_output, starter, answer, hint=None):
    return dict(
        n=n, title=title, slug=slug, body=body, input_desc=NO_INPUT,
        output_desc=output_desc, sample_input=None, sample_output=sample_output,
        hint=hint, starter=starter, answer=answer,
    )


PROBLEMS = [
    P(2, "การ์ดนักเรียน", "student_card",
      "สร้างตัวแปรเก็บข้อมูลนักเรียนแล้วแสดงการ์ดสั้นๆ\n\n| Variable | ค่า |\n|----------|-----|\n| `name` | `\"Lina\"` |\n| `room` | `5` |\n| `number` | `12` |",
      "3 บรรทัดมีป้ายกำกับ",
      "Name: Lina\nRoom: 5\nNumber: 12",
      'name = \nroom = \nnumber = \n\n# แสดงผลตรงนี้',
      'name = "Lina"\nroom = 5\nnumber = 12\nprint("Name:", name)\nprint("Room:", room)\nprint("Number:", number)'),
    P(3, "คะแนนสองวิชา", "two_scores",
      "เก็บคะแนนวิชาคณิต `math_score = 80` และวิทย์ `science_score = 75` แล้วแสดงผลรวมในตัวแปร `total`",
      "บรรทัดเดียวแสดงผลรวม",
      "Total: 155",
      "math_score = 80\nscience_score = 75\n\n# คำนวณและแสดงผล",
      'math_score = 80\nscience_score = 75\ntotal = math_score + science_score\nprint("Total:", total)'),
    P(4, "เปลี่ยนค่าคะแนน", "reassign_score",
      "เริ่มจาก `score = 40` แล้วเปลี่ยนเป็น `90` จากนั้นแสดงค่าล่าสุด",
      "ค่าคะแนนหลังเปลี่ยน",
      "Score: 90",
      "score = 40\n\n# เปลี่ยนค่าแล้วแสดงผล",
      'score = 40\nscore = 90\nprint("Score:", score)'),
    P(8, "ราคาผลไม้สองลูก", "two_fruits",
      "แอปเปิลราคา `apple = 25` กล้วย `banana = 15` แสดงราคารวม `total`",
      "ยอดรวม",
      "Total: 40",
      "apple = 25\nbanana = 15\n\n# รวมราคา",
      'apple = 25\nbanana = 15\ntotal = apple + banana\nprint("Total:", total)'),
    P(9, "ทักทายด้วยชื่อ", "greet_name",
      "เก็บ `name = \"Ken\"` แล้วทักทายแบบ `Hello, Ken` โดยใช้ `print` หลายอาร์กิวเมนต์",
      "ประโยคทักทาย 1 บรรทัด",
      "Hello, Ken",
      'name = "Ken"\n\n# แสดงคำทักทาย',
      'name = "Ken"\nprint("Hello,", name)'),
    P(6, "ยอดเงินในกระเป๋า", "wallet_total",
      "มีเงิน `cash = 100` และ `coin = 20` แสดงทั้งสองค่าและยอดรวม",
      "3 บรรทัด",
      "Cash: 100\nCoin: 20\nTotal: 120",
      "cash = 100\ncoin = 20\n\n# แสดงผล",
      'cash = 100\ncoin = 20\ntotal = cash + coin\nprint("Cash:", cash)\nprint("Coin:", coin)\nprint("Total:", total)',
      "คำนวณ total เก็บในตัวแปรก่อนพิมพ์"),
    P(7, "อุณหภูมิเช้า-เย็น", "temp_change",
      "`morning = 28` และ `evening = 24` แสดงทั้งสองค่า และ `drop` ซึ่งคืออุณหภูมิที่ลดลงโดยใช้ `morning + (-evening)` ไม่ใช้เครื่องหมายลบถ้ายังไม่ชิน — หรือใช้ค่าคงที่ `drop = 4` ที่คำนวณไว้แล้วก็ได้ตามตัวอย่าง\n\nให้กำหนด `drop = 4` แล้วแสดงผลตามตัวอย่าง",
      "3 บรรทัด",
      "Morning: 28\nEvening: 24\nDrop: 4",
      "morning = 28\nevening = 24\ndrop = 4\n\n# แสดงผล",
      'morning = 28\nevening = 24\ndrop = 4\nprint("Morning:", morning)\nprint("Evening:", evening)\nprint("Drop:", drop)',
      "บทนี้โฟกัสการเก็บค่า — กำหนด drop ตามที่โจทย์ให้"),
    P(10, "คะแนนควิซสามข้อ", "quiz_sum",
      "`q1 = 8`, `q2 = 9`, `q3 = 7` รวมเป็น `total` แล้วแสดง",
      "ยอดรวม",
      "Quiz Total: 24",
      "q1 = 8\nq2 = 9\nq3 = 7\n\n# รวมคะแนน",
      'q1 = 8\nq2 = 9\nq3 = 7\ntotal = q1 + q2 + q3\nprint("Quiz Total:", total)',
      "บวกทีละตัวเข้า total"),
    P(11, "สต็อกสินค้า", "stock_update",
      "เริ่ม `stock = 50` ขายไปแล้วเหลือ `stock = 35` แสดงค่าก่อนขาย (เก็บใน `before`) และหลังขาย",
      "2 บรรทัด",
      "Before: 50\nAfter: 35",
      "stock = 50\nbefore = stock\n\n# อัปเดตแล้วแสดง",
      'stock = 50\nbefore = stock\nstock = 35\nprint("Before:", before)\nprint("After:", stock)',
      "เก็บค่าเดิมไว้ใน before ก่อนเขียนทับ"),
    P(12, "ใบเสร็จสองรายการ", "two_item_bill",
      "`item1 = \"Milk\"`, `price1 = 28`, `item2 = \"Bread\"`, `price2 = 25` แสดงรายการและยอดรวม",
      "ใบเสร็จ",
      "Item: Milk\nPrice: 28\nItem: Bread\nPrice: 25\nTotal: 53",
      'item1 = "Milk"\nprice1 = 28\nitem2 = "Bread"\nprice2 = 25\n\n# แสดงใบเสร็จ',
      'item1 = "Milk"\nprice1 = 28\nitem2 = "Bread"\nprice2 = 25\ntotal = price1 + price2\nprint("Item:", item1)\nprint("Price:", price1)\nprint("Item:", item2)\nprint("Price:", price2)\nprint("Total:", total)',
      "รวมราคาเก็บใน total"),
    P(13, "โปรไฟล์เกม", "game_profile",
      '`player = "Nova"`, `level = 3`, `hp = 12.5` แสดงโปรไฟล์ 3 บรรทัด',
      "โปรไฟล์",
      "Player: Nova\nLevel: 3\nHP: 12.5",
      'player = "Nova"\nlevel = 3\nhp = 12.5\n\n# แสดงโปรไฟล์',
      'player = "Nova"\nlevel = 3\nhp = 12.5\nprint("Player:", player)\nprint("Level:", level)\nprint("HP:", hp)',
      "float เก็บได้เหมือน int"),
    P(5, "บิลร้านอาหาร", "restaurant_bill",
      "`food = 120`, `drink = 40`, `dessert = 55` รวมเป็น `total` แสดงรายการครบและยอดรวมตามตัวอย่าง",
      "ใบเสร็จ",
      "Food: 120\nDrink: 40\nDessert: 55\nTotal: 215",
      "food = 120\ndrink = 40\ndessert = 55\n\n# คำนวณและแสดง",
      'food = 120\ndrink = 40\ndessert = 55\ntotal = food + drink + dessert\nprint("Food:", food)\nprint("Drink:", drink)\nprint("Dessert:", dessert)\nprint("Total:", total)',
      "บวกสามค่าเข้าด้วยกัน"),
    P(14, "สมุดพกคะแนน", "scorebook",
      "`base = 70` แล้วได้โบนัสเปลี่ยนเป็น `base = 70 + 10` (หรือกำหนด `bonus = 10` แล้ว `base = base + bonus`) แสดงคะแนนตั้งต้นที่เก็บไว้และคะแนนสุดท้าย",
      "2 บรรทัด",
      "Start: 70\nFinal: 80",
      "base = 70\nstart = base\nbonus = 10\n\n# อัปเดตแล้วแสดง",
      'base = 70\nstart = base\nbonus = 10\nbase = base + bonus\nprint("Start:", start)\nprint("Final:", base)',
      "เก็บ start ก่อนบวกโบนัส"),
    P(15, "สรุปทริป", "trip_summary",
      '`place = "Beach"`, `days = 3`, `budget = 1500`, `spent = 900` แสดงข้อมูลและเงินเหลือ `left = budget + 0` โดยกำหนด `left = 600` ตามที่ยอดจริง (หรือคิดเป็นงบคงเหลือที่กำหนดไว้)',
      "สรุปทริป",
      "Place: Beach\nDays: 3\nBudget: 1500\nSpent: 900\nLeft: 600",
      'place = "Beach"\ndays = 3\nbudget = 1500\nspent = 900\nleft = 600\n\n# แสดงสรุป',
      'place = "Beach"\ndays = 3\nbudget = 1500\nspent = 900\nleft = 600\nprint("Place:", place)\nprint("Days:", days)\nprint("Budget:", budget)\nprint("Spent:", spent)\nprint("Left:", left)',
      "บทนี้ยังไม่เน้นการลบ — กำหนด left ตามโจทย์ได้"),
    P(16, "กระปุกออมสิน", "piggy_bank",
      "เริ่ม `saving = 0` แล้วเก็บเงินสามครั้ง: เพิ่มเป็น 20, แล้ว 50, แล้ว 80 โดยใช้การเปลี่ยนค่าตัวแปรทีละขั้น สุดท้ายแสดงยอด",
      "ยอดออม",
      "Saving: 80",
      "saving = 0\n\n# เก็บทีละครั้งแล้วแสดง",
      'saving = 0\nsaving = 20\nsaving = 50\nsaving = 80\nprint("Saving:", saving)',
      "เปลี่ยนค่า saving ตามลำดับจนถึง 80"),
]


if __name__ == "__main__":
    write_week("005-variables", chapter="Variables", emoji="📦", index_md=INDEX, problems=PROBLEMS)
