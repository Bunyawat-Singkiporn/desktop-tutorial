# -*- coding: utf-8 -*-
"""Expand 004-comments to 15-problem standard."""
from _expand_helpers import write_week

INDEX = """
# 📋 สารบัญโจทย์ — บท 004 Comments

**ขอบเขตของบทนี้:** `print("...")` และ `#` comment (บรรทัดเดียว / ท้ายบรรทัด)

> ❌ บทนี้ยังไม่มีตัวแปรอย่างเป็นทางการ (บท 005) · ไม่มี `input()` · ไม่มี `if` · ไม่มี f-string

---

## ลำดับที่แนะนำ

| # | ไฟล์ | ระดับ | โจทย์ | แกนการคิด |
|---|------|-------|-------|-----------|
| 1 | `02_test.md` | 🟢 | ป้ายร้านพร้อม comment | comment อธิบายก่อน print |
| 2 | `03_test.md` | 🟢 | ทักทายสองบรรทัด | comment คั่นสองส่วน |
| 3 | `04_test.md` | 🟢 | หัวข้อรายงาน | comment ท้ายบรรทัด |
| 4 | `08_easy.md` | 🟢 | ขั้นตอนต้มมาม่า | comment ลำดับขั้นตอน |
| 5 | `09_easy.md` | 🟢 | ป้ายปิดร้าน | comment หลายบรรทัดหัวไฟล์ |
| 6 | `06_medium.md` | 🟡 | เมนูของหวาน | comment + จัดคอลัมน์ |
| 7 | `07_medium.md` | 🟡 | ใบเสร็จเล็ก | comment แต่ละส่วนใบเสร็จ |
| 8 | `10_medium.md` | 🟡 | ตารางเวร | comment อธิบายคอลัมน์ |
| 9 | `11_medium.md` | 🟡 | ป้ายคิว | comment + กรอบข้อความ |
| 10 | `12_medium.md` | 🟡 | สลิปยืมของ | comment แยกส่วนหัว/รายการ |
| 11 | `13_medium.md` | 🟡 | หน้าจอต้อนรับ | comment บล็อกใหญ่ |
| 12 | `05_challenge.md` | 🔴 | ใบเสร็จร้านกาแฟ | comment หนาแน่น + กรอบ |
| 13 | `14_challenge.md` | 🔴 | คู่มือเปิดเครื่อง | comment ทีละขั้นละเอียด |
| 14 | `15_challenge.md` | 🔴 | เกียรติบัตรสั้น | comment + จัดกึ่งกลาง |
| 15 | `16_challenge.md` | 🔴 | หน้าจอ ATM สองหน้า | comment คั่นหลายหน้าจอ |

**สรุป:** 🟢 Easy 5 ข้อ · 🟡 Medium 6 ข้อ · 🔴 Challenge 4 ข้อ = **15 ข้อ**

---

## หมายเหตุสำหรับครู

- ข้อ 02 ไม่ซ้ำตัวอย่างป้ายร้านยาวในบทเรียน — ใช้ป้ายสั้นและเน้น comment
- ความยากอยู่ที่ **คุณภาพ comment + การจัดข้อความ** ไม่ใช่คำสั่งใหม่
- ตรวจว่านักเรียนมี `#` จริงในโค้ด (อย่างน้อยตามที่โจทย์กำหนด)
"""

NO_INPUT = "ไม่มี (โปรแกรมนี้ไม่รับค่าจากผู้ใช้)"


def P(n, title, slug, body, output_desc, sample_output, starter, answer, hint=None):
    return {
        "n": n,
        "title": title,
        "slug": slug,
        "body": body,
        "input_desc": NO_INPUT,
        "output_desc": output_desc,
        "sample_input": None,
        "sample_output": sample_output,
        "hint": hint,
        "starter": starter,
        "answer": answer,
    }


PROBLEMS = [
    P(
        2,
        "ป้ายร้านพร้อม comment",
        "shop_sign_comment",
        "ร้านขนมปังอยากได้ป้ายชื่อร้านบนหน้าจอ\n\nเขียนโปรแกรมแสดงชื่อร้าน 1 บรรทัด และใส่ comment อย่างน้อย 1 บรรทัดอธิบายว่ากำลังแสดงป้ายร้าน",
        "ข้อความ 1 บรรทัด",
        "BEST BAKERY",
        "# เขียนโค้ดตรงนี้",
        '# Show shop name on screen\nprint("BEST BAKERY")',
    ),
    P(
        3,
        "ทักทายสองบรรทัด",
        "two_line_hello",
        "โปรแกรมต้อนรับแขกต้องทักทายสองบรรทัด\n\nแสดงข้อความตามตัวอย่าง และใส่ comment คั่นระหว่างสองคำสั่ง print เพื่อบอกว่าเป็นบรรทัดที่ 1 และ 2",
        "ข้อความ 2 บรรทัด",
        "Hello\nWelcome",
        "# เขียนโค้ดตรงนี้",
        '# Line 1 greeting\nprint("Hello")\n# Line 2 greeting\nprint("Welcome")',
    ),
    P(
        4,
        "หัวข้อรายงาน",
        "report_title",
        "เด็กต้องพิมพ์หัวข้อรายงานสั้นๆ\n\nแสดงข้อความตามตัวอย่าง และใส่ comment ท้ายบรรทัด print ว่าเป็นชื่อรายงาน",
        "ข้อความ 1 บรรทัด",
        "My Science Report",
        "# เขียนโค้ดตรงนี้",
        'print("My Science Report")  # report title',
    ),
    P(
        8,
        "ขั้นตอนต้มมาม่า",
        "noodle_steps",
        "เขียนขั้นตอนต้มมาม่าสามขั้นบนจอ เพื่อติดตู้เย็น\n\nแสดง 3 บรรทัดตามตัวอย่าง และใส่ comment อย่างน้อย 1 บรรทัดอธิบายว่านี่คือขั้นตอนทำอาหาร",
        "ข้อความ 3 บรรทัด",
        "1. Boil water\n2. Add noodles\n3. Wait 3 minutes",
        "# เขียนโค้ดตรงนี้",
        '# Cooking steps for instant noodles\nprint("1. Boil water")\nprint("2. Add noodles")\nprint("3. Wait 3 minutes")',
    ),
    P(
        9,
        "ป้ายปิดร้าน",
        "closed_sign",
        "ร้านปิดแล้ว ต้องการป้ายบอกเวลาเปิดวันถัดไป\n\nแสดง 2 บรรทัดตามตัวอย่าง และใส่ comment หัวไฟล์อย่างน้อย 2 บรรทัด (ชื่อโปรแกรม / ผู้เขียนก็ได้)",
        "ข้อความ 2 บรรทัด",
        "CLOSED\nOpen tomorrow 9am",
        "# เขียนโค้ดตรงนี้",
        '# Program: closed sign\n# Author: student\nprint("CLOSED")\nprint("Open tomorrow 9am")',
    ),
    P(
        6,
        "เมนูของหวาน",
        "dessert_menu",
        "ร้านของหวานอยากได้เมนูสั้นๆ อ่านง่าย\n\nแสดงเมนูตามตัวอย่าง (จัดช่องว่างให้ราคาตรงคอลัมน์) และใส่ comment อธิบายว่ากำลังพิมพ์เมนู",
        "เมนู 3 บรรทัด",
        "Cake     45\nPudding  30\nCookie   20",
        "# เขียนโค้ดตรงนี้",
        '# Print dessert menu with aligned prices\nprint("Cake     45")\nprint("Pudding  30")\nprint("Cookie   20")',
        "นับช่องว่างหลังชื่อขนมให้ราคาเริ่มตรงกันทุกบรรทัด",
    ),
    P(
        7,
        "ใบเสร็จเล็ก",
        "mini_receipt",
        "ร้านสะดวกซื้ออยากได้ใบเสร็จสั้น\n\nแสดงตามตัวอย่าง และใส่ comment อย่างน้อย 2 จุด แยกว่าส่วนหัวกับส่วนท้าย",
        "ใบเสร็จหลายบรรทัด",
        "==== RECEIPT ====\nWater  10\nTotal  10\n================",
        "# เขียนโค้ดตรงนี้",
        '# Header\nprint("==== RECEIPT ====")\nprint("Water  10")\n# Footer\nprint("Total  10")\nprint("================")',
        "แยก comment ส่วนหัวกับส่วนสรุปยอด",
    ),
    P(
        10,
        "ตารางเวร",
        "duty_table",
        "ครูต้องการตารางเวรทำความสะอาดสั้นๆ\n\nแสดงตามตัวอย่าง และใส่ comment อธิบายความหมายของคอลัมน์ Day/Name",
        "ตาราง 4 บรรทัดรวมหัวตาราง",
        "Day  Name\nMon  Ann\nTue  Ben\nWed  Cat",
        "# เขียนโค้ดตรงนี้",
        '# Columns: Day and Name\nprint("Day  Name")\nprint("Mon  Ann")\nprint("Tue  Ben")\nprint("Wed  Cat")',
        "หัวตารางควรมี comment อธิบายว่าแต่ละคอลัมน์คืออะไร",
    ),
    P(
        11,
        "ป้ายคิว",
        "queue_ticket",
        "คลินิกอยากพิมพ์บัตรคิวง่ายๆ\n\nแสดงตามตัวอย่าง และใส่ comment บอกว่าตัวเลขคือหมายเลขคิว",
        "บัตรคิวหลายบรรทัด",
        "********\n* A-12 *\n********",
        "# เขียนโค้ดตรงนี้",
        '# Queue number ticket\nprint("********")\nprint("* A-12 *")  # ticket id\nprint("********")',
        "เส้นขอบบน-ล่างควรยาวเท่ากัน",
    ),
    P(
        12,
        "สลิปยืมของ",
        "borrow_slip",
        "ห้องสมุดพิมพ์สลิปยืมหนังสือสั้นๆ\n\nแสดงตามตัวอย่าง ใส่ comment แยกส่วนชื่อผู้ยืมกับรายการหนังสือ",
        "สลิปหลายบรรทัด",
        "BORROW SLIP\nName: Mina\nBook: Robot Tales\nDue: Friday",
        "# เขียนโค้ดตรงนี้",
        '# Borrower section\nprint("BORROW SLIP")\nprint("Name: Mina")\n# Item section\nprint("Book: Robot Tales")\nprint("Due: Friday")',
        "ใช้ comment แบ่งบล็อกข้อมูลคนละส่วน",
    ),
    P(
        13,
        "หน้าจอต้อนรับ",
        "welcome_screen",
        "โปรแกรมเปิดเครื่องแสดงหน้าจอต้อนรับ\n\nแสดงตามตัวอย่าง และใส่ comment บล็อก 3 บรรทัดที่หัวไฟล์อธิบายโปรแกรม",
        "หน้าจอหลายบรรทัด",
        "================\n   WELCOME\n================\nPress START",
        "# เขียนโค้ดตรงนี้",
        '# Welcome screen demo\n# Shows title box\n# Then instruction line\nprint("================")\nprint("   WELCOME")\nprint("================")\nprint("Press START")',
        "บรรทัด WELCOME มีช่องว่างนำหน้าให้ดูกลางๆ",
    ),
    P(
        5,
        "ใบเสร็จร้านกาแฟ",
        "coffee_receipt",
        "ร้านกาแฟต้องการใบเสร็จที่มีกรอบและรายการ\n\nแสดงตามตัวอย่างเป๊ะ และใส่ comment อย่างน้อย 3 จุด แยกหัว / รายการ / รวม",
        "ใบเสร็จแบบมีกรอบ",
        "====================\n   COFFEE HOUSE\n====================\nLatte         55\nMuffin        35\n--------------------\nTotal         90\n====================",
        "# เขียนโค้ดตรงนี้",
        '# Header block\nprint("====================")\nprint("   COFFEE HOUSE")\nprint("====================")\n# Items\nprint("Latte         55")\nprint("Muffin        35")\nprint("--------------------")\n# Total\nprint("Total         90")\nprint("====================")',
        "จัดช่องว่างให้ตัวเลขราคาเริ่มตรงคอลัมน์เดียวกัน",
    ),
    P(
        14,
        "คู่มือเปิดเครื่อง",
        "startup_guide",
        "ติดคู่มือเปิดคอมพิวเตอร์ข้างเครื่อง\n\nแสดง 5 ขั้นตอนตามตัวอย่าง และใส่ comment ท้ายแต่ละ print อธิบายสั้นๆ ว่าขั้นนั้นทำอะไร",
        "รายการ 5 บรรทัด",
        "1. Power on\n2. Wait for desktop\n3. Open browser\n4. Go to class site\n5. Start coding",
        "# เขียนโค้ดตรงนี้",
        'print("1. Power on")  # press button\nprint("2. Wait for desktop")  # loading\nprint("3. Open browser")  # chrome/edge\nprint("4. Go to class site")  # url\nprint("5. Start coding")  # practice',
        "comment ท้ายบรรทัดควรสั้นและบอกเหตุผลของขั้นนั้น",
    ),
    P(
        15,
        "เกียรติบัตรสั้น",
        "mini_certificate",
        "พิมพ์เกียรติบัตรสั้นสำหรับงานโรงเรียน\n\nแสดงตามตัวอย่าง (จัดช่องว่างให้อ่านเหมือนใบประกาศ) และใส่ comment หัวไฟล์ 2 บรรทัด",
        "เกียรติบัตรหลายบรรทัด",
        "************************\n*   CERTIFICATE OF FUN  *\n*      Awarded to       *\n*        SAM            *\n************************",
        "# เขียนโค้ดตรงนี้",
        '# Mini certificate printer\n# School event version\nprint("************************")\nprint("*   CERTIFICATE OF FUN  *")\nprint("*      Awarded to       *")\nprint("*        SAM            *")\nprint("************************")',
        "นับช่องว่างในแต่ละบรรทัดให้ดอกจันขอบซ้าย-ขวาตรงแนว",
    ),
    P(
        16,
        "หน้าจอ ATM สองหน้า",
        "atm_two_screens",
        "จำลองหน้าจอตู้ ATM สองหน้า คั่นด้วยบรรทัดว่าง\n\nแสดงตามตัวอย่าง และใส่ comment บอกว่าบรรทัดไหนคือหน้า 1 / หน้า 2",
        "สองหน้าจอคั่นบรรทัดว่าง",
        "=== ATM ===\n1) Balance\n2) Exit\n\n=== DONE ===\nThank you",
        "# เขียนโค้ดตรงนี้",
        '# Screen 1 menu\nprint("=== ATM ===")\nprint("1) Balance")\nprint("2) Exit")\nprint("")\n# Screen 2 goodbye\nprint("=== DONE ===")\nprint("Thank you")',
        "บรรทัดว่างใช้ print(\"\") คั่นระหว่างสองหน้าจอ",
    ),
]


if __name__ == "__main__":
    write_week(
        "004-comments",
        chapter="Comments",
        emoji="💬",
        index_md=INDEX,
        problems=PROBLEMS,
    )
