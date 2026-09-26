# -*- coding: utf-8 -*-
"""Expand weeks 010-012."""
from _expand_helpers import write_week

NO_IN = "ไม่มี (กำหนดค่าในโปรแกรม)"


def p(n, title, slug, body, out_desc, sample_out, starter, answer, hint=None, sample_in=None, in_desc=None):
    return {
        "n": n, "title": title, "slug": slug, "body": body,
        "input_desc": in_desc if in_desc is not None else ("ดูตัวอย่าง" if sample_in is not None else NO_IN),
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


def week_010():
    items = [
        ("ทักทาย f-string", "f-string พื้นฐาน"),
        ("ราคาทศนิยม 2 ตำแหน่ง", ":.2f"),
        ("คั่นด้วยขีด", "sep="),
        ("พิมพ์ต่อบรรทัด", "end="),
        ("การ์ดชื่อ-อายุ", "f-string สองค่า"),
        ("ใบเสร็จส่วนลด", "หลายบรรทัด f-string"),
        ("ค่าพายสั้น", ":.2f กับค่าคงที่"),
        ("รายการคั่นด้วย |", "sep"),
        ("คำทักทายต่อกัน", "end space"),
        ("ป้ายคะแนน", "f-string จาก input"),
        ("สรุปยอดทศนิยม", ":.2f จากคำนวณ"),
        ("ใบเสร็จจัดคอลัมน์", "หลาย f-string"),
        ("เมนูคั่น sep", "sep กับหลายค่า"),
        ("รายงานนักเรียน", "f-string ผสม"),
        ("สลิปชำระเงิน", "กรอบด้วย f-string"),
    ]
    index = idx(
        "บท 010 Output Formatting",
        "f-string / `:.2f` / `sep=` / `end=` / input ได้",
        "ไม่มี `if` · ไม่มี loop",
        rows(items),
        "เน้นจัดรูปแบบ ไม่ใช้เงื่อนไข",
    )
    probs = [
        p(2, "ทักทาย f-string", "f_hello",
          'มี name = "Lina" แสดง Hello, Lina! ด้วย f-string',
          "1 บรรทัด", "Hello, Lina!",
          'name = "Lina"\n\n# แสดงด้วย f-string',
          'name = "Lina"\nprint(f"Hello, {name}!")'),
        p(3, "ราคาทศนิยม 2 ตำแหน่ง", "price_2f",
          "มี price = 12.5 แสดง Price: 12.50",
          "1 บรรทัด", "Price: 12.50",
          "price = 12.5\n\n# แสดงทศนิยม 2 ตำแหน่ง",
          'price = 12.5\nprint(f"Price: {price:.2f}")'),
        p(4, "คั่นด้วยขีด", "sep_dash",
          'พิมพ์ A B C โดยคั่นด้วย - ด้วย sep',
          "1 บรรทัด", "A-B-C",
          '# ใช้ sep',
          'print("A", "B", "C", sep="-")'),
        p(8, "พิมพ์ต่อบรรทัด", "end_space",
          'พิมพ์ Hello แล้วต่อด้วย World ในบรรทัดเดียว ด้วย end',
          "1 บรรทัด", "Hello World",
          '# ใช้ end',
          'print("Hello", end=" ")\nprint("World")'),
        p(9, "การ์ดชื่อ-อายุ", "f_name_age",
          'name = "Sam", age = 10 แสดง My name is Sam and I am 10 years old.',
          "1 บรรทัด", "My name is Sam and I am 10 years old.",
          'name = "Sam"\nage = 10\n\n# f-string',
          'name = "Sam"\nage = 10\nprint(f"My name is {name} and I am {age} years old.")'),
        p(6, "ใบเสร็จส่วนลด", "discount_receipt",
          "price = 250, discount = 50, final = 200 แสดงสามบรรทัดตามตัวอย่าง",
          "3 บรรทัด", "Price: 250\nDiscount: 50\nFinal: 200",
          "price = 250\ndiscount = 50\nfinal = 200\n\n# แสดงใบเสร็จ",
          'price = 250\ndiscount = 50\nfinal = 200\nprint(f"Price: {price}")\nprint(f"Discount: {discount}")\nprint(f"Final: {final}")',
          "ใช้ f-string ทุกบรรทัด"),
        p(7, "ค่าพายสั้น", "pi_2f",
          "pi = 3.14159 แสดง Pi = 3.14",
          "1 บรรทัด", "Pi = 3.14",
          "pi = 3.14159\n\n# แสดง",
          'pi = 3.14159\nprint(f"Pi = {pi:.2f}")',
          "ใช้ :.2f"),
        p(10, "รายการคั่นด้วย |", "sep_pipe",
          'พิมพ์ Red Green Blue คั่นด้วย " | "',
          "1 บรรทัด", "Red | Green | Blue",
          '# sep',
          'print("Red", "Green", "Blue", sep=" | ")',
          "ดูช่องว่างรอบ |"),
        p(11, "คำทักทายต่อกัน", "hi_there_end",
          'พิมพ์ Hi แล้วต่อ there! ในบรรทัดเดียว',
          "1 บรรทัด", "Hi there!",
          '# end',
          'print("Hi", end=" ")\nprint("there!")',
          "end เป็นช่องว่าง"),
        p(12, "ป้ายคะแนน", "score_label_f",
          "รับชื่อและคะแนน แสดง Name: ... / Score: ...",
          "2 บรรทัด", "Name: Oak\nScore: 92",
          "name = input()\nscore = int(input())\n\n# แสดง",
          'name = input()\nscore = int(input())\nprint(f"Name: {name}")\nprint(f"Score: {score}")',
          sample_in="Oak\n92"),
        p(13, "สรุปยอดทศนิยม", "total_2f",
          "รับราคาสองค่า float รวมแล้วแสดง Total: ด้วยทศนิยม 2 ตำแหน่ง",
          "1 บรรทัด", "Total: 33.50",
          "a = float(input())\nb = float(input())\n\n# รวม",
          'a = float(input())\nb = float(input())\nprint(f"Total: {a + b:.2f}")',
          sample_in="12.5\n21", hint="รวมก่อน แล้วค่อย :.2f"),
        p(5, "ใบเสร็จจัดคอลัมน์", "aligned_f_receipt",
          'item = "Book", price = 199.5 แสดงกรอบสั้นตามตัวอย่าง',
          "ใบเสร็จ", "================\nItem : Book\nPrice: 199.50\n================",
          'item = "Book"\nprice = 199.5\n\n# ใบเสร็จ',
          'item = "Book"\nprice = 199.5\nprint("================")\nprint(f"Item : {item}")\nprint(f"Price: {price:.2f}")\nprint("================")',
          "ใช้ :.2f กับราคา"),
        p(14, "เมนูคั่น sep", "menu_sep",
          'พิมพ์ Coffee Tea Juice คั่นด้วย /',
          "1 บรรทัด", "Coffee/Tea/Juice",
          '# sep',
          'print("Coffee", "Tea", "Juice", sep="/")',
          "sep เป็น /"),
        p(15, "รายงานนักเรียน", "student_report_f",
          "รับชื่อ เกรดตัวอักษร คะแนน แสดงหนึ่งประโยคด้วย f-string",
          "1 บรรทัด", "Mew got grade A with score 95",
          "name = input()\ngrade = input()\nscore = int(input())\n\n# รายงาน",
          'name = input()\ngrade = input()\nscore = int(input())\nprint(f"{name} got grade {grade} with score {score}")',
          sample_in="Mew\nA\n95"),
        p(16, "สลิปชำระเงิน", "payment_slip",
          "รับชื่อและยอด float แสดงสลิปตามตัวอย่าง",
          "สลิป", "==== PAYMENT ====\nPayer : Rin\nAmount: 120.00\n==================",
          "name = input()\namount = float(input())\n\n# สลิป",
          'name = input()\namount = float(input())\nprint("==== PAYMENT ====")\nprint(f"Payer : {name}")\nprint(f"Amount: {amount:.2f}")\nprint("==================")',
          sample_in="Rin\n120", hint="Amount ใช้ :.2f"),
    ]
    write_week("010-output-formatting", chapter="Output Formatting", emoji="🖨️", index_md=index, problems=probs)


def week_011():
    items = [
        ("บวกลบคูณหาร", "สี่運算พื้นฐาน"),
        ("หารลงตัว", "// และ %"),
        ("ยกกำลัง", "**"),
        ("เปรียบเทียบเท่ากัน", "พิมพ์ True/False"),
        ("เงินทอน", "paid - price"),
        ("พื้นที่สี่เหลี่ยม", "กว้าง*สูง"),
        ("เศษจากการแบ่งกลุ่ม", "%"),
        ("ลำดับความสำคัญ", "วงเล็บ"),
        ("มากกว่าเท่าไหร่", ">="),
        ("เฉลี่ยคร่าวๆ", "รวม/จำนวน"),
        ("ยกกำลังสอง", "** 2"),
        ("บิลร้าน + เปรียบเทียบ", "คำนวณแล้วเทียบ"),
        ("วินาทีเป็นนาที", "// และ %"),
        ("ส่วนลดคงที่", "คำนวณหลายขั้น"),
        ("เช็กเกณฑ์คะแนน", "เปรียบเทียบหลายค่า"),
    ]
    # fix Chinese in axis - use Thai
    items[0] = ("บวกลบคูณหาร", "สี่ตัวดำเนินการพื้นฐาน")
    index = idx(
        "บท 011 Operators",
        "`+ - * / // % **` / ตัวเปรียบเทียบ / f-string / input — พิมพ์ True/False ได้ แต่ยังไม่มี if",
        "ไม่มี `if` / `else` · ไม่มี loop",
        rows(items),
        "ห้ามใช้ if — ให้พิมพ์ผลเปรียบเทียบเป็น True/False",
    )
    probs = [
        p(2, "บวกลบคูณหาร", "arith_four",
          "รับจำนวนเต็ม a แล้วแสดง a+3, a-3, a*3, a/3 คนละบรรทัด",
          "4 บรรทัด", "13\n7\n30\n3.3333333333333335",
          "a = int(input())\n\n# แสดงผล",
          "a = int(input())\nprint(a + 3)\nprint(a - 3)\nprint(a * 3)\nprint(a / 3)",
          sample_in="10", hint="ใช้ / จะได้ทศนิยม"),
        p(3, "หารลงตัว", "floor_mod",
          "รับ n แสดง n//4 และ n%4",
          "2 บรรทัด", "4\n1",
          "n = int(input())\n\n# แสดง // และ %",
          "n = int(input())\nprint(n // 4)\nprint(n % 4)",
          sample_in="17"),
        p(4, "ยกกำลัง", "power_two",
          "รับ n แสดง n**2",
          "1 บรรทัด", "81",
          "n = int(input())\n\n# ยกกำลังสอง",
          "n = int(input())\nprint(n ** 2)",
          sample_in="9"),
        p(8, "เปรียบเทียบเท่ากัน", "compare_eq",
          "รับสองจำนวน แสดงผล a == b เป็น True/False",
          "1 บรรทัด", "False",
          "a = int(input())\nb = int(input())\n\n# เปรียบเทียบ",
          "a = int(input())\nb = int(input())\nprint(a == b)",
          sample_in="5\n7"),
        p(9, "เงินทอน", "change_ops",
          "รับราคาและเงินที่จ่าย แสดงเงินทอนด้วย f-string",
          "1 บรรทัด", "Change: 25",
          "price = int(input())\npaid = int(input())\n\n# เงินทอน",
          'price = int(input())\npaid = int(input())\nprint(f"Change: {paid - price}")',
          sample_in="75\n100"),
        p(6, "พื้นที่สี่เหลี่ยม", "rect_area",
          "รับกว้างและสูง แสดงพื้นที่",
          "1 บรรทัด", "Area: 40",
          "w = int(input())\nh = int(input())\n\n# พื้นที่",
          'w = int(input())\nh = int(input())\nprint(f"Area: {w * h}")',
          sample_in="5\n8", hint="กว้างคูณสูง"),
        p(7, "เศษจากการแบ่งกลุ่ม", "mod_groups",
          "รับจำนวนคน แสดงเศษเมื่อหาร 3 (เหลือกี่คนที่ไม่ครบกลุ่ม)",
          "1 บรรทัด", "Remainder: 2",
          "n = int(input())\n\n# เศษ",
          'n = int(input())\nprint(f"Remainder: {n % 3}")',
          sample_in="11", hint="ใช้ %"),
        p(10, "ลำดับความสำคัญ", "precedence",
          "แสดงผลของ 2 + 3 * 4 และ (2 + 3) * 4 คนละบรรทัด",
          "2 บรรทัด", "14\n20",
          "# พิมพ์สองค่า",
          "print(2 + 3 * 4)\nprint((2 + 3) * 4)",
          hint="คูณมาก่อนถ้าไม่มีวงเล็บ"),
        p(11, "มากกว่าเท่าไหร่", "gte_check",
          "รับคะแนน แสดงผล score >= 50 เป็น True/False",
          "1 บรรทัด", "True",
          "score = int(input())\n\n# เปรียบเทียบ",
          "score = int(input())\nprint(score >= 50)",
          sample_in="50"),
        p(12, "เฉลี่ยคร่าวๆ", "avg_two",
          "รับคะแนนสองค่า แสดงค่าเฉลี่ย (หารด้วย 2)",
          "1 บรรทัด", "Average: 85.0",
          "a = int(input())\nb = int(input())\n\n# เฉลี่ย",
          'a = int(input())\nb = int(input())\nprint(f"Average: {(a + b) / 2}")',
          sample_in="80\n90", hint="(a+b)/2"),
        p(13, "ยกกำลังสอง", "square_label",
          "รับ n แสดง Square: n**2",
          "1 บรรทัด", "Square: 16",
          "n = int(input())\n\n# แสดง",
          'n = int(input())\nprint(f"Square: {n ** 2}")',
          sample_in="4"),
        p(5, "บิลร้าน + เปรียบเทียบ", "bill_and_compare",
          "รับราคาสินค้าสองชิ้น แสดงยอดรวม และผลเปรียบเทียบว่ารวม >= 100 หรือไม่",
          "2 บรรทัด", "Total: 130\nBig Bill: True",
          "a = int(input())\nb = int(input())\n\n# รวมและเปรียบเทียบ",
          'a = int(input())\nb = int(input())\ntotal = a + b\nprint(f"Total: {total}")\nprint(f"Big Bill: {total >= 100}")',
          sample_in="70\n60", hint="ยังไม่ต้อง if — พิมพ์ True/False"),
        p(14, "วินาทีเป็นนาที", "sec_to_min",
          "รับวินาทีทั้งหมด แสดงนาทีและวินาทีที่เหลือ",
          "2 บรรทัด", "Minutes: 2\nSeconds: 5",
          "sec = int(input())\n\n# แปลง",
          'sec = int(input())\nprint(f"Minutes: {sec // 60}")\nprint(f"Seconds: {sec % 60}")',
          sample_in="125", hint="// 60 และ % 60"),
        p(15, "ส่วนลดคงที่", "fixed_discount",
          "รับราคา หักส่วนลด 20 แสดงราคาสุทธิ และผลว่าสุทธิ < 100 หรือไม่",
          "2 บรรทัด", "Final: 80\nUnder 100: True",
          "price = int(input())\n\n# คำนวณ",
          'price = int(input())\nfinal = price - 20\nprint(f"Final: {final}")\nprint(f"Under 100: {final < 100}")',
          sample_in="100", hint="ลบ 20 แล้วเปรียบเทียบ"),
        p(16, "เช็กเกณฑ์คะแนน", "multi_compare",
          "รับคะแนน แสดงสามบรรทัด: >=80, >=50, ==100 เป็น True/False",
          "3 บรรทัด", "A-range: False\nPass: True\nPerfect: False",
          "score = int(input())\n\n# เปรียบเทียบสามเกณฑ์",
          'score = int(input())\nprint(f"A-range: {score >= 80}")\nprint(f"Pass: {score >= 50}")\nprint(f"Perfect: {score == 100}")',
          sample_in="72", hint="พิมพ์ผลเปรียบเทียบ ไม่ใช้ if"),
    ]
    write_week("011-operators", chapter="Operators", emoji="🔢", index_md=index, problems=probs)


def week_012():
    items = [
        ("ทักทายจาก input", "input + print"),
        ("อายุปีหน้า", "int + 1"),
        ("ราคารูปแบบสวย", "f-string :.2f"),
        ("เงินทอน", "ลบและแสดง"),
        ("การ์ดแนะนำตัว", "หลาย input"),
        ("บิลสองชิ้น", "รวมราคา"),
        ("เช็กเกณฑ์แบบไม่ if", "พิมพ์ True/False"),
        ("แปลงวินาที", "// %"),
        ("ชื่อเต็ม", "สอง input"),
        ("เฉลี่ยสองวิชา", "หาร"),
        ("ป้ายสินค้า", "str จากตัวเลขก็ได้ด้วย f"),
        ("โปรแกรมครบสูตร", "input-process-output"),
        ("สลิปย่อ", "จัดรูปแบบ"),
        ("คำนวณพื้นที่", "* "),
        ("สรุปรอบทบทวน", "ผสมหลายทักษะ"),
    ]
    index = idx(
        "บท 012 Review",
        "ความรู้บท 001–011 รวมกัน (ยังไม่มี if / loop)",
        "ไม่มี `if` · ไม่มี `elif` · ไม่มี `for`/`while`",
        rows(items),
        "ทบทวนสูตร input → process → output",
    )
    probs = [
        p(2, "ทักทายจาก input", "review_hello",
          "รับชื่อ แสดง Hello, ชื่อ!",
          "1 บรรทัด", "Hello, Pat!",
          "name = input()\n\n# ทักทาย",
          'name = input()\nprint(f"Hello, {name}!")', sample_in="Pat"),
        p(3, "อายุปีหน้า", "review_age",
          "รับอายุ แสดง Next: อายุ+1",
          "1 บรรทัด", "Next: 13",
          "age = int(input())\n\n# ปีหน้า",
          'age = int(input())\nprint(f"Next: {age + 1}")', sample_in="12"),
        p(4, "ราคารูปแบบสวย", "review_price_fmt",
          "รับราคา float แสดง Price: ด้วยทศนิยม 2 ตำแหน่ง",
          "1 บรรทัด", "Price: 9.50",
          "price = float(input())\n\n# แสดง",
          'price = float(input())\nprint(f"Price: {price:.2f}")', sample_in="9.5"),
        p(8, "เงินทอน", "review_change",
          "รับราคาและเงินจ่าย แสดง Change",
          "1 บรรทัด", "Change: 15",
          "price = int(input())\npaid = int(input())\n\n# ทอน",
          'price = int(input())\npaid = int(input())\nprint(f"Change: {paid - price}")', sample_in="85\n100"),
        p(9, "การ์ดแนะนำตัว", "review_card",
          "รับชื่อ เมือง อายุ แสดงสามบรรทัด",
          "3 บรรทัด", "Name: Joy\nCity: Loei\nAge: 11",
          "name = input()\ncity = input()\nage = int(input())\n\n# การ์ด",
          'name = input()\ncity = input()\nage = int(input())\nprint(f"Name: {name}")\nprint(f"City: {city}")\nprint(f"Age: {age}")',
          sample_in="Joy\nLoei\n11"),
        p(6, "บิลสองชิ้น", "review_two_items",
          "รับราคาสองชิ้น แสดง Total ทศนิยม 2 ตำแหน่ง",
          "1 บรรทัด", "Total: 45.50",
          "a = float(input())\nb = float(input())\n\n# รวม",
          'a = float(input())\nb = float(input())\nprint(f"Total: {a + b:.2f}")',
          sample_in="20.25\n25.25", hint="รวมแล้ว :.2f"),
        p(7, "เช็กเกณฑ์แบบไม่ if", "review_bool",
          "รับคะแนน แสดง Pass: ตามด้วยผล score >= 50",
          "1 บรรทัด", "Pass: False",
          "score = int(input())\n\n# แสดงผลเปรียบเทียบ",
          'score = int(input())\nprint(f"Pass: {score >= 50}")',
          sample_in="40", hint="ยังไม่มี if"),
        p(10, "แปลงวินาที", "review_time",
          "รับวินาที แสดงนาทีและวินาทีเหลือ",
          "2 บรรทัด", "Min: 1\nSec: 10",
          "s = int(input())\n\n# แปลง",
          's = int(input())\nprint(f"Min: {s // 60}")\nprint(f"Sec: {s % 60}")',
          sample_in="70"),
        p(11, "ชื่อเต็ม", "review_fullname",
          "รับชื่อและนามสกุล แสดง Full: ...",
          "1 บรรทัด", "Full: Ann Bee",
          "a = input()\nb = input()\n\n# ชื่อเต็ม",
          'a = input()\nb = input()\nprint(f"Full: {a} {b}")', sample_in="Ann\nBee"),
        p(12, "เฉลี่ยสองวิชา", "review_avg",
          "รับคะแนนสองวิชา แสดง Average",
          "1 บรรทัด", "Average: 88.0",
          "a = int(input())\nb = int(input())\n\n# เฉลี่ย",
          'a = int(input())\nb = int(input())\nprint(f"Average: {(a + b) / 2}")',
          sample_in="86\n90"),
        p(13, "ป้ายสินค้า", "review_tag",
          "รับชื่อสินค้าและราคา แสดง Tag",
          "1 บรรทัด", "Tag: Gum (10.00)",
          "name = input()\nprice = float(input())\n\n# ป้าย",
          'name = input()\nprice = float(input())\nprint(f"Tag: {name} ({price:.2f})")',
          sample_in="Gum\n10"),
        p(5, "โปรแกรมครบสูตร", "review_ipo",
          "รับชื่อและราคา คิด VAT *1.07 แสดงชื่อและราคารวมทศนิยม 2 ตำแหน่ง",
          "2 บรรทัด", "Customer: Bee\nPay: 107.00",
          "name = input()\nprice = float(input())\n\n# คิดเงิน",
          'name = input()\nprice = float(input())\npay = price * 1.07\nprint(f"Customer: {name}")\nprint(f"Pay: {pay:.2f}")',
          sample_in="Bee\n100", hint="input → คูณ 1.07 → แสดง"),
        p(14, "สลิปย่อ", "review_slip",
          "รับชื่อและยอด แสดงสลิปสั้น",
          "3 บรรทัด", "=== SLIP ===\nName: Tam\nPaid: 50.00",
          "name = input()\npaid = float(input())\n\n# สลิป",
          'name = input()\npaid = float(input())\nprint("=== SLIP ===")\nprint(f"Name: {name}")\nprint(f"Paid: {paid:.2f}")',
          sample_in="Tam\n50"),
        p(15, "คำนวณพื้นที่", "review_area",
          "รับกว้างสูง แสดง Area",
          "1 บรรทัด", "Area: 24",
          "w = int(input())\nh = int(input())\n\n# พื้นที่",
          'w = int(input())\nh = int(input())\nprint(f"Area: {w * h}")',
          sample_in="4\n6"),
        p(16, "สรุปรอบทบทวน", "review_finale",
          "รับชื่อ คะแนน1 คะแนน2 แสดงชื่อ ผลรวม และผลว่าผลรวม >= 100",
          "3 บรรทัด", "Student: Win\nSum: 150\nCentury: True",
          "name = input()\na = int(input())\nb = int(input())\n\n# สรุป",
          'name = input()\na = int(input())\nb = int(input())\ntotal = a + b\nprint(f"Student: {name}")\nprint(f"Sum: {total}")\nprint(f"Century: {total >= 100}")',
          sample_in="Win\n70\n80", hint="ผสม f-string และเปรียบเทียบโดยไม่ใช้ if"),
    ]
    write_week("012-review", chapter="Review", emoji="📝", index_md=index, problems=probs)


if __name__ == "__main__":
    week_010()
    week_011()
    week_012()
    print("done 010-012")
