# -*- coding: utf-8 -*-
"""Generate medium drills (slide/) + homework (homework/) for weeks 001-024 Thai."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent
SLIDE = ROOT / "slide"
HW = ROOT / "homework"

WEEKS = [
    "001-what-is-python",
    "002-python-environment",
    "003-python-syntax",
    "004-comments",
    "005-variables",
    "006-naming-rules",
    "007-data-types",
    "008-type-conversion",
    "009-input",
    "010-output-formatting",
    "011-operators",
    "012-review",
    "013-if-else",
    "014-even-odd",
    "015-elif",
    "016-logical-operator",
    "017-for-loop",
    "018-loop-with-lists",
    "019-while-loop",
    "020-loop-safety",
    "021-nested-loops",
    "022-loop-review",
    "023-debugging-loops",
    "024-midyear-review",
]


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.lstrip("\n").rstrip() + "\n", encoding="utf-8")


def medium_md(topic: str, letter: str, title: str, body: str, hint: str, starter: str, io: str = "") -> str:
    io_block = f"\n\n---\n\n## ตัวอย่าง Input / Output\n\n{io}" if io else ""
    return f"""# Practice: {topic} — Medium {letter}: {title}

**Difficulty:** 🟡 Medium

---

## โจทย์

{body}
{io_block}

---

## 💡 Hint

{hint}

---

## Starter Code

```python
{starter}
```
"""


def hw_md(week_title: str, n: int, title: str, body: str, hint: str, starter: str = "# เขียนโค้ดตรงนี้", io: str = "") -> str:
    io_block = f"\n\n---\n\n## ตัวอย่าง\n\n{io}" if io else ""
    return f"""# Homework: {week_title} — ข้อ {n}: {title}

**Difficulty:** 🟢 Easy

---

## โจทย์

{body}
{io_block}

---

## 💡 Hint

{hint}

---

## Starter Code

```python
{starter}
```
"""


# ---------- content definitions ----------
# Each week: mediums=[(title, body, hint, starter, answer, io?), ...],
#            homeworks=[(title, body, hint, starter, answer, io?), ...] x10

def content() -> dict:
    data = {}

    # ===== 001 =====
    data["001-what-is-python"] = {
        "topic": "What is Python",
        "medium_nums": (6, 7),
        "mediums": [
            (
                "ป้ายเมนูร้านกาแฟ",
                "ใช้ `print()` แสดงป้ายเมนูตามรูปแบบนี้ **ทุกตัวอักษรต้องตรงกัน:**\n\n```\n====================\n   COFFEE MENU\n====================\nLatte      80\nMocha      90\n====================\n```",
                "- นับช่องว่างและ `=` ให้ตรง\n- ใช้ `print()` หลายครั้ง",
                "# แสดงป้ายเมนู",
                'print("====================")\nprint("   COFFEE MENU")\nprint("====================")\nprint("Latte      80")\nprint("Mocha      90")\nprint("====================")',
                "",
            ),
            (
                "ใบเสร็จสั้นๆ",
                "แสดงใบเสร็จตามนี้:\n\n```\nItem : Notebook\nQty  : 2\nPrice: 45\nThank you\n```",
                "ใช้ `print()` 4 ครั้ง (หรือมากกว่าถ้าต้องการ)",
                "# แสดงใบเสร็จ",
                'print("Item : Notebook")\nprint("Qty  : 2")\nprint("Price: 45")\nprint("Thank you")',
                "",
            ),
        ],
        "homeworks": [
            ("Hello", 'แสดงข้อความ `Hello, Python!`', "ใช้ print()", 'print("Hello, Python!")', 'print("Hello, Python!")'),
            ("ชื่อตัวเอง", 'แสดงชื่อของคุณในบรรทัดเดียว เช่น `My name is Sam`', "ใส่ชื่อในเครื่องหมายคำพูด", 'print("My name is Sam")', 'print("My name is Sam")'),
            ("สามบรรทัด", "แสดง A / B / C คนละบรรทัด", "print สามครั้ง", 'print("A")\nprint("B")\nprint("C")', 'print("A")\nprint("B")\nprint("C")'),
            ("เส้นคั่น", 'แสดง `***` สามบรรทัด', "print สามครั้ง", 'print("***")\nprint("***")\nprint("***")', 'print("***")\nprint("***")\nprint("***")'),
            ("หัวข้อ", 'แสดง `=== SCORE ===`', "print หนึ่งครั้ง", 'print("=== SCORE ===")', 'print("=== SCORE ===")'),
            ("สองค่า", 'แสดง `Cat` แล้ว `Dog` คนละบรรทัด', "print สองครั้ง", 'print("Cat")\nprint("Dog")', 'print("Cat")\nprint("Dog")'),
            ("ตัวเลขเป็นข้อความ", 'แสดง `100` โดยใช้ print กับ string', 'print("100")', 'print("100")', 'print("100")'),
            ("ว่างหนึ่งบรรทัด", 'แสดง `Hi` แล้วบรรทัดว่าง แล้ว `Bye` (ใช้ print("") ได้)', "print สามครั้ง", 'print("Hi")\nprint("")\nprint("Bye")', 'print("Hi")\nprint("")\nprint("Bye")'),
            ("กรอบง่าย", 'แสดง\n```\n****\n*  *\n****\n```', "นับดาว", 'print("****")\nprint("*  *")\nprint("****")', 'print("****")\nprint("*  *")\nprint("****")'),
            ("ทักทาย", 'แสดง `Good morning!`', "print", 'print("Good morning!")', 'print("Good morning!")'),
        ],
    }

    # ===== 002 =====
    data["002-python-environment"] = {
        "topic": "Environment",
        "medium_nums": (6, 7),
        "mediums": [
            (
                "จับคู่ Error",
                "เขียนคำตอบเป็นข้อความ (print) ตามตาราง — แต่ละบรรทัดเป็นชนิด Error ที่ถูกต้อง\n\n| สาเหตุ | Error |\n|--------|-------|\n| พิมพ์ `Print` ตัวใหญ่ | NameError |\n| ลืมปิด `)` | SyntaxError |\n| มี space นำหน้าโดยไม่จำเป็น | IndentationError |\n\n**Output:**\n```\nNameError\nSyntaxError\nIndentationError\n```",
                "แค่ print ชื่อ Error ตามลำดับตาราง",
                "# พิมพ์ชื่อ Error ตามลำดับ",
                'print("NameError")\nprint("SyntaxError")\nprint("IndentationError")',
                "",
            ),
            (
                "แก้โค้ดให้รันได้",
                "โค้ดด้านล่างผิด — เขียนเวอร์ชันที่ถูกต้องให้แสดง `Ready`\n\n```python\nPrint(\"Ready\"\n```",
                "ตัวพิมพ์เล็ก + ปิดวงเล็บ",
                "# เขียนโค้ดที่ถูกต้อง",
                'print("Ready")',
                "",
            ),
        ],
        "homeworks": [
            ("รันได้ไหม", 'แสดง `OK` ด้วย print ที่ถูกต้อง', "print ตัวเล็ก", 'print("OK")', 'print("OK")'),
            ("ปิดวงเล็บ", 'แก้แนวคิด: ต้องมี ) ปิด — แสดง `Closed`', "print ครบคู่", 'print("Closed")', 'print("Closed")'),
            ("ปิดคำพูด", 'แสดง `Quotes` ให้เครื่องหมายครบ', "ใช้ \"...\" ", 'print("Quotes")', 'print("Quotes")'),
            ("ชื่อ Error 1", 'แสดงคำว่า `SyntaxError`', "print", 'print("SyntaxError")', 'print("SyntaxError")'),
            ("ชื่อ Error 2", 'แสดงคำว่า `NameError`', "print", 'print("NameError")', 'print("NameError")'),
            ("บรรทัดที่ถูก", 'แสดง `line 1` (จำว่า Error มักบอกบรรทัด)', "print", 'print("line 1")', 'print("line 1")'),
            ("สองคำสั่ง", 'แสดง `One` และ `Two` คนละบรรทัด', "สอง print", 'print("One")\nprint("Two")', 'print("One")\nprint("Two")'),
            ("ห้าม Print ใหญ่", 'แสดง `small print` ด้วย print ที่ถูก', "ตัวเล็ก", 'print("small print")', 'print("small print")'),
            ("ข้อความช่วย", 'แสดง `Read the error message`', "print", 'print("Read the error message")', 'print("Read the error message")'),
            ("พร้อมเรียน", 'แสดง `Server of learning: ready`', "print", 'print("Server of learning: ready")', 'print("Server of learning: ready")'),
        ],
    }

    # ===== 003 =====
    data["003-python-syntax"] = {
        "topic": "Syntax",
        "medium_nums": (6, 7),
        "mediums": [
            (
                "แก้ snippet ให้ถูก",
                "เขียนโปรแกรมที่แสดงผลดังนี้โดยใช้ syntax ที่ถูกต้อง:\n\n```\nHi\nPython\n```",
                "print สองครั้ง ตัวพิมพ์เล็ก ปิดวงเล็บและคำพูด",
                "# แสดง Hi และ Python",
                'print("Hi")\nprint("Python")',
                "",
            ),
            (
                "กฎสามข้อ",
                "แสดงสรุปกฎ 3 ข้อ คนละบรรทัด:\n\n```\nlowercase\npairs\nindent\n```",
                "print สามครั้ง",
                "# สรุปกฎ",
                'print("lowercase")\nprint("pairs")\nprint("indent")',
                "",
            ),
        ],
        "homeworks": [
            ("print ถูก", 'แสดง `syntax ok`', "ตัวเล็ก", 'print("syntax ok")', 'print("syntax ok")'),
            ("คู่คำพูด", 'แสดง `pair`', "ปิด \"", 'print("pair")', 'print("pair")'),
            ("คู่วงเล็บ", 'แสดง `parens`', "ปิด )", 'print("parens")', 'print("parens")'),
            ("ไม่เยื้องแปลกๆ", 'แสดง `no random indent` ที่คอลัมน์ซ้ายสุด', "อย่าเว้น space นำ", 'print("no random indent")', 'print("no random indent")'),
            ("สองบรรทัด", 'แสดง `A` แล้ว `B`', "สอง print", 'print("A")\nprint("B")', 'print("A")\nprint("B")'),
            ("ตัวเลขในคำพูด", 'แสดงข้อความ `42`', "เป็น str ใน print", 'print("42")', 'print("42")'),
            ("เว้นวรรคในข้อความ", 'แสดง `Hello World`', "ช่องว่างใน \"...\"", 'print("Hello World")', 'print("Hello World")'),
            ("เครื่องหมาย", 'แสดง `Yes!`', "print", 'print("Yes!")', 'print("Yes!")'),
            ("สามคำ", 'แสดง `one` `two` `three` คนละบรรทัด', "สาม print", 'print("one")\nprint("two")\nprint("three")', 'print("one")\nprint("two")\nprint("three")'),
            ("จบบท", 'แสดง `syntax done`', "print", 'print("syntax done")', 'print("syntax done")'),
        ],
    }

    # ===== 004 =====
    data["004-comments"] = {
        "topic": "Comments",
        "medium_nums": (6, 7),
        "mediums": [
            (
                "เขียนตามแผน comment",
                "มีแผน comment ด้านล่าง — เขียนโค้ดให้ตรงแผน และแสดงผล:\n\n```\nLibrary\nOpen: 9am\n```\n\nแผน:\n```python\n# แสดงชื่อสถานที่\n# แสดงเวลาเปิด\n```",
                "หลัง comment แต่ละบรรทัดมี print",
                "# แสดงชื่อสถานที่\n\n# แสดงเวลาเปิด\n",
                '# แสดงชื่อสถานที่\nprint("Library")\n# แสดงเวลาเปิด\nprint("Open: 9am")',
                "",
            ),
            (
                "ใส่ comment ให้โค้ด",
                "เขียนโปรแกรมแสดง `Goal: 100` โดยมี comment อธิบายอย่างน้อย 1 บรรทัดก่อน print",
                "ใช้ # อธิบายว่าทำไมถึงพิมพ์ข้อความนี้",
                "# อธิบายตรงนี้\n",
                '# เป้าหมายคะแนนของด่านนี้\nprint("Goal: 100")',
                "",
            ),
        ],
        "homeworks": [
            ("comment เดียว", 'มี comment แล้วแสดง `Hi`', "ใส่ # ก่อน", '# ทักทาย\nprint("Hi")', '# ทักทาย\nprint("Hi")'),
            ("สอง comment", 'comment สองบรรทัด แล้วแสดง `OK`', "สอง #", '# step 1\n# step 2\nprint("OK")', '# step 1\n# step 2\nprint("OK")'),
            ("comment ท้ายบรรทัด", 'แสดง `End` และมี comment ท้ายบรรทัด print', "print(...)  # ...", 'print("End")  # จบโปรแกรม', 'print("End")  # จบโปรแกรม'),
            ("แผนร้าน", 'comment ว่าเป็นชื่อร้าน แล้วแสดง `Bakery`', "# ชื่อร้าน", '# ชื่อร้าน\nprint("Bakery")', '# ชื่อร้าน\nprint("Bakery")'),
            ("แผนราคา", 'comment แล้วแสดง `Price: 50`', "#", '# ราคา\nprint("Price: 50")', '# ราคา\nprint("Price: 50")'),
            ("ข้าม comment", 'มี comment ภาษาไทยยาวๆ แล้วแสดง `Run` (comment ไม่โชว์ใน output)', "# ...", '# นี่ไม่แสดงบนจอ\nprint("Run")', '# นี่ไม่แสดงบนจอ\nprint("Run")'),
            ("หัวข้อ", 'comment หัวข้อ แล้วแสดง `Title`', "#", '# หัวข้อหน้า\nprint("Title")', '# หัวข้อหน้า\nprint("Title")'),
            ("สอง print + comment", 'แสดง `A` และ `B` มี comment คั่น', "#", 'print("A")\n# บรรทัดถัดไป\nprint("B")', 'print("A")\n# บรรทัดถัดไป\nprint("B")'),
            ("เตือนตัวเอง", 'comment ว่าอย่าลืมปิดวงเล็บ แล้วแสดง `Safe`', "#", '# อย่าลืมปิดวงเล็บ\nprint("Safe")', '# อย่าลืมปิดวงเล็บ\nprint("Safe")'),
            ("จบ", 'แสดง `comment practice done`', "print", 'print("comment practice done")', 'print("comment practice done")'),
        ],
    }

    # ===== 005 =====
    data["005-variables"] = {
        "topic": "Variables",
        "medium_nums": (6, 7),
        "mediums": [
            (
                "สลับค่าด้วยตัวแปรชั่วคราว",
                "กำหนด `a = 3`, `b = 7` แล้วสลับค่าด้วยตัวแปร `temp` จากนั้นแสดง:\n\n```\na = 7\nb = 3\n```",
                "temp = a แล้วค่อยย้ายค่า",
                "a = 3\nb = 7\n# สลับค่า\n",
                'a = 3\nb = 7\ntemp = a\na = b\nb = temp\nprint("a =", a)\nprint("b =", b)',
                "",
            ),
            (
                "อัปเดตคะแนนทีละขั้น",
                "เริ่ม `score = 0` แล้วบวก 10 สองครั้ง (อัปเดตตัวแปรเดิม) แสดงคะแนนทุกขั้น:\n\n```\n0\n10\n20\n```",
                "score = score + 10",
                "score = 0\nprint(score)\n# บวกต่อ\n",
                "score = 0\nprint(score)\nscore = score + 10\nprint(score)\nscore = score + 10\nprint(score)",
                "",
            ),
        ],
        "homeworks": [
            ("สร้างตัวแปร", 'สร้าง `name = "Ann"` แล้ว print', "=", 'name = "Ann"\nprint(name)', 'name = "Ann"\nprint(name)'),
            ("อายุ", "age = 12 แล้วแสดง", "print(age)", "age = 12\nprint(age)", "age = 12\nprint(age)"),
            ("บวกง่าย", "x=5 y=2 แสดง x+y", "total = x+y", "x = 5\ny = 2\nprint(x + y)", "x = 5\ny = 2\nprint(x + y)"),
            ("เปลี่ยนค่า", "n=1 แล้วเปลี่ยนเป็น 2 แล้วแสดง", "นับครั้งสุดท้าย", "n = 1\nn = 2\nprint(n)", "n = 1\nn = 2\nprint(n)"),
            ("ข้อความ+ตัวแปร", 'city="Bangkok" แสดง city', "print", 'city = "Bangkok"\nprint(city)', 'city = "Bangkok"\nprint(city)'),
            ("ราคา", "price=99 แสดง", "print", "price = 99\nprint(price)", "price = 99\nprint(price)"),
            ("สองตัวแปร", "a=1 b=2 แสดงทั้งคู่คนละบรรทัด", "สอง print", "a = 1\nb = 2\nprint(a)\nprint(b)", "a = 1\nb = 2\nprint(a)\nprint(b)"),
            ("ผลรวมสามตัว", "p=10 q=20 r=30 แสดงผลรวม", "+", "p = 10\nq = 20\nr = 30\nprint(p + q + r)", "p = 10\nq = 20\nr = 30\nprint(p + q + r)"),
            ("อัปเดตครั้งเดียว", "lives=3 แล้ว lives=lives-1 แสดง", "ลบ 1", "lives = 3\nlives = lives - 1\nprint(lives)", "lives = 3\nlives = lives - 1\nprint(lives)"),
            ("ชื่อผลรวม", 'สร้าง total จาก 40+60 แล้วแสดง', "total =", "total = 40 + 60\nprint(total)", "total = 40 + 60\nprint(total)"),
        ],
    }

    # ===== 006 =====
    data["006-naming-rules"] = {
        "topic": "Naming Rules",
        "medium_nums": (6, 7),
        "mediums": [
            (
                "เขียนใหม่ด้วยชื่อที่ดี",
                "แทนที่โค้ดแนว `x`/`y` ด้วยชื่อที่สื่อความหมาย แล้วแสดงส่วนต่างราคา:\n\nกำหนดราคาเดิม 200 ส่วนลด 30 แสดง:\n```\n170\n```",
                "ใช้เช่น original_price, discount",
                "# ตั้งชื่อให้ดี แล้วคำนวณ",
                "original_price = 200\ndiscount = 30\nprint(original_price - discount)",
                "",
            ),
            (
                "เลือกชื่อที่ถูก",
                "แสดงเฉพาะชื่อที่ถูกต้องตามกฎ (คนละบรรทัด) จากรายการนี้: `1score`, `my_score`, `my-score`, `total_price`\n\n**Output:**\n```\nmy_score\ntotal_price\n```",
                "ห้ามขึ้นต้นด้วยตัวเลข ห้ามมี -",
                "# print เฉพาะชื่อที่ถูก",
                'print("my_score")\nprint("total_price")',
                "",
            ),
        ],
        "homeworks": [
            ("snake_case", 'สร้าง first_name = "Ada" แล้วแสดง', "_", 'first_name = "Ada"\nprint(first_name)', 'first_name = "Ada"\nprint(first_name)'),
            ("ไม่ใช้ x", "ใช้ score = 10 แทน x", "ชื่อสื่อ", "score = 10\nprint(score)", "score = 10\nprint(score)"),
            ("player1", "สร้าง player1 = 1 แล้วแสดง", "ตัวเลขท้ายได้", "player1 = 1\nprint(player1)", "player1 = 1\nprint(player1)"),
            ("total_price", "total_price = 500 แสดง", "snake", "total_price = 500\nprint(total_price)", "total_price = 500\nprint(total_price)"),
            ("is_ok", "is_ok = True แสดง", "bool ชื่อดี", "is_ok = True\nprint(is_ok)", "is_ok = True\nprint(is_ok)"),
            ("สองคำ", "user_age = 15 แสดง", "_", "user_age = 15\nprint(user_age)", "user_age = 15\nprint(user_age)"),
            ("อ่านง่าย", "item_count = 4 แสดง", "print", "item_count = 4\nprint(item_count)", "item_count = 4\nprint(item_count)"),
            ("ไม่ใช้ keyword", "ใช้ message แทนการตั้งชื่อว่า print", "หลีก keyword", 'message = "hi"\nprint(message)', 'message = "hi"\nprint(message)'),
            ("ค่าคงที่แนว", "max_score = 100 แสดง", "ชื่อชัด", "max_score = 100\nprint(max_score)", "max_score = 100\nprint(max_score)"),
            ("สรุป", 'แสดงข้อความ `naming ok`', "print", 'print("naming ok")', 'print("naming ok")'),
        ],
    }

    return data  # will extend below


# Build remaining weeks in second function to keep file editable
def content_rest(data: dict) -> dict:
    # ===== 007 =====
    data["007-data-types"] = {
        "topic": "Data Types",
        "medium_nums": (6, 7),
        "mediums": [
            (
                "ทาย type()",
                "สร้างตัวแปรตามตาราง แล้วพิมพ์ชนิดทีละบรรทัดด้วย `type(...)` (แสดงผลตามที่ Python ให้):\n\n| ตัวแปร | ค่า |\n|--------|-----|\n| a | 10 |\n| b | 2.5 |\n| c | \"10\" |\n| d | False |",
                "ใช้ print(type(a)) ฯลฯ",
                "a = 10\nb = 2.5\nc = \"10\"\nd = False\n",
                'a = 10\nb = 2.5\nc = "10"\nd = False\nprint(type(a))\nprint(type(b))\nprint(type(c))\nprint(type(d))',
                "",
            ),
            (
                "อย่าสับสน str กับ int",
                'กำหนด `n = 3` และ `s = "3"` แล้วแสดงผลของ `n + n` และ `s + s` คนละบรรทัด:\n\n```\n6\n33\n```',
                "int บวกเลข / str ต่อข้อความ",
                'n = 3\ns = "3"\n',
                'n = 3\ns = "3"\nprint(n + n)\nprint(s + s)',
                "",
            ),
        ],
        "homeworks": [
            ("int", "x=7 แสดง type(x)", "type", "x = 7\nprint(type(x))", "x = 7\nprint(type(x))"),
            ("float", "y=1.5 แสดง type(y)", "type", "y = 1.5\nprint(type(y))", "y = 1.5\nprint(type(y))"),
            ("str", 'z="hi" แสดง type(z)', "type", 'z = "hi"\nprint(type(z))', 'z = "hi"\nprint(type(z))'),
            ("bool", "flag=True แสดง type(flag)", "True ตัวใหญ่", "flag = True\nprint(type(flag))", "flag = True\nprint(type(flag))"),
            ("สร้างครบ", "สร้าง int float str อย่างละตัว แล้ว print ค่า", "สามตัวแปร", 'a=1\nb=1.0\nc="1"\nprint(a)\nprint(b)\nprint(c)', 'a=1\nb=1.0\nc="1"\nprint(a)\nprint(b)\nprint(c)'),
            ("False", "ok=False แสดง ok", "F ใหญ่", "ok = False\nprint(ok)", "ok = False\nprint(ok)"),
            ("ข้อความเลข", 'แสดง type ของ "99"', "str", 'print(type("99"))', 'print(type("99"))'),
            ("ทศนิยม", "แสดง type ของ 0.25", "float", "print(type(0.25))", "print(type(0.25))"),
            ("บวก int", "แสดง 4+5", "int", "print(4 + 5)", "print(4 + 5)"),
            ("ต่อ str", 'แสดง "4"+"5"', "str", 'print("4" + "5")', 'print("4" + "5")'),
        ],
    }

    data["008-type-conversion"] = {
        "topic": "Type Conversion",
        "medium_nums": (6, 7),
        "mediums": [
            (
                "บิล + VAT จากข้อความ",
                'กำหนด `price_text = "100"` แปลงเป็นตัวเลข แล้วคำนวณราคาหลัง VAT 7% แสดงผลเป็นตัวเลข (เช่น 107.0):\n\n```\n107.0\n```',
                "float(price_text) * 1.07",
                'price_text = "100"\n',
                'price_text = "100"\nprice = float(price_text)\nprint(price * 1.07)',
                "",
            ),
            (
                "อายุทศวรรษหน้า",
                'กำหนด `age_text = "14"` แปลงเป็น int แล้วแสดงอายุหลังอีก 10 ปี:\n\n```\n24\n```',
                "int(age_text) + 10",
                'age_text = "14"\n',
                'age_text = "14"\nage = int(age_text)\nprint(age + 10)',
                "",
            ),
        ],
        "homeworks": [
            ("int()", 'แปลง "8" เป็น int แล้วแสดง', "int", 'print(int("8"))', 'print(int("8"))'),
            ("float()", 'แปลง "2.5" เป็น float แล้วแสดง', "float", 'print(float("2.5"))', 'print(float("2.5"))'),
            ("str()", "แปลง 12 เป็น str แล้วต่อกับ Hi: แสดง Hi:12", "str", 'print("Hi:" + str(12))', 'print("Hi:" + str(12))'),
            ("บวกหลังแปลง", 'a="5" แปลงแล้ว +1 แสดง 6', "int(a)+1", 'a = "5"\nprint(int(a) + 1)', 'a = "5"\nprint(int(a) + 1)'),
            ("สองเท่า", 't="9" แปลงแล้ว *2', "int", 'print(int("9") * 2)', 'print(int("9") * 2)'),
            ("ราคา", 'p="50" แปลง float แสดง', "float", 'print(float("50"))', 'print(float("50"))'),
            ("ข้อความคะแนน", 'score=90 แสดง "Score:"+str(score)', "str", 'score = 90\nprint("Score:" + str(score))', 'score = 90\nprint("Score:" + str(score))'),
            ("ปีหน้า", 'y="2026" แปลง +1', "int", 'print(int("2026") + 1)', 'print(int("2026") + 1)'),
            ("ครึ่ง", 'n="10" แปลง /2 แสดง 5.0', "float หรือ int", 'print(int("10") / 2)', 'print(int("10") / 2)'),
            ("สรุป", 'แสดง type หลัง int("3")', "type(int(...))", 'print(type(int("3")))', 'print(type(int("3")))'),
        ],
    }

    data["009-input"] = {
        "topic": "Input",
        "medium_nums": (6, 7),
        "mediums": [
            (
                "การ์ดชื่อ+อายุ",
                "รับชื่อ (string) และอายุ (int) แล้วแสดง:\n\n```\nName: <name>\nAge: <age>\n```",
                "input แล้ว int(input())",
                "name = input()\nage = int(input())\n",
                'name = input()\nage = int(input())\nprint("Name:", name)\nprint("Age:", age)',
                "**Input:**\n```\nMina\n11\n```\n\n**Output:**\n```\nName: Mina\nAge: 11\n```",
            ),
            (
                "ราคารวม",
                "รับราคาสินค้าต่อชิ้น (int) และจำนวน (int) แสดงผลคูณ:\n\n```\nTotal: <price*qty>\n```",
                "สอง int(input())",
                "price = int(input())\nqty = int(input())\n",
                'price = int(input())\nqty = int(input())\nprint("Total:", price * qty)',
                "**Input:**\n```\n25\n4\n```\n\n**Output:**\n```\nTotal: 100\n```",
            ),
        ],
        "homeworks": [
            ("รับชื่อ", "รับชื่อแล้วแสดง Hello, <name>", "input", 'name = input()\nprint("Hello,", name)', 'name = input()\nprint("Hello,", name)'),
            ("รับเลข", "รับ int แล้วแสดงเลขนั้น", "int(input())", "n = int(input())\nprint(n)", "n = int(input())\nprint(n)"),
            ("+1", "รับอายุ แสดงอายุ+1", "int", "age = int(input())\nprint(age + 1)", "age = int(input())\nprint(age + 1)"),
            ("สองชื่อ", "รับชื่อจริง นามสกุล แสดงต่อกันด้วยช่องว่าง", "สอง input", 'a = input()\nb = input()\nprint(a, b)', 'a = input()\nb = input()\nprint(a, b)'),
            ("float", "รับ float แสดงค่า", "float(input())", "x = float(input())\nprint(x)", "x = float(input())\nprint(x)"),
            ("สองเท่า", "รับ int แสดง *2", "*", "n = int(input())\nprint(n * 2)", "n = int(input())\nprint(n * 2)"),
            ("ผลต่าง", "รับ a b เป็น int แสดง a-b", "-", "a = int(input())\nb = int(input())\nprint(a - b)", "a = int(input())\nb = int(input())\nprint(a - b)"),
            ("ข้อความซ้ำใจความ", "รับคำ แล้วแสดงคำนั้นสองบรรทัด", "print สองครั้ง", "w = input()\nprint(w)\nprint(w)", "w = input()\nprint(w)\nprint(w)"),
            ("ผลรวม", "รับสอง int แสดงผลรวม", "+", "a = int(input())\nb = int(input())\nprint(a + b)", "a = int(input())\nb = int(input())\nprint(a + b)"),
            ("เมือง", 'รับเมือง แสดง "City: ..."', "f หรือ ,", 'city = input()\nprint("City:", city)', 'city = input()\nprint("City:", city)'),
        ],
    }

    data["010-output-formatting"] = {
        "topic": "Output Formatting",
        "medium_nums": (6, 7),
        "mediums": [
            (
                "ใบเสร็จ f-string",
                'กำหนด item="Pen", price=15, qty=3 ใช้ f-string แสดง:\n\n```\nItem: Pen\nLine total: 45\n```',
                "f\"...{var}...\"",
                'item = "Pen"\nprice = 15\nqty = 3\n',
                'item = "Pen"\nprice = 15\nqty = 3\nprint(f"Item: {item}")\nprint(f"Line total: {price * qty}")',
                "",
            ),
            (
                "เงินทศนิยม 2 ตำแหน่ง",
                "กำหนด `amount = 12.5` แสดงด้วย `:.2f` เป็น:\n\n```\nPay: 12.50\n```",
                "f\"Pay: {amount:.2f}\"",
                "amount = 12.5\n",
                'amount = 12.5\nprint(f"Pay: {amount:.2f}")',
                "",
            ),
        ],
        "homeworks": [
            ("f ชื่อ", 'name="Bob" แสดง f"Hi {name}"', "f-string", 'name = "Bob"\nprint(f"Hi {name}")', 'name = "Bob"\nprint(f"Hi {name}")'),
            ("f คะแนน", "score=88 แสดง Score: 88 ด้วย f", "f", "score = 88\nprint(f\"Score: {score}\")", "score = 88\nprint(f\"Score: {score}\")"),
            (":.1f", "x=3.14159 แสดง 3.1", ":.1f", "x = 3.14159\nprint(f\"{x:.1f}\")", "x = 3.14159\nprint(f\"{x:.1f}\")"),
            (":.2f", "y=2 แสดง 2.00", ":.2f", "y = 2\nprint(f\"{y:.2f}\")", "y = 2\nprint(f\"{y:.2f}\")"),
            ("สองค่า", 'a=1 b=2 แสดง f"{a},{b}"', "f", "a = 1\nb = 2\nprint(f\"{a},{b}\")", "a = 1\nb = 2\nprint(f\"{a},{b}\")"),
            ("sep", 'print 1 2 3 ด้วย sep="-"', "sep", 'print(1, 2, 3, sep="-")', 'print(1, 2, 3, sep="-")'),
            ("end", 'print "Hi" end=" " แล้ว print "there"', "end", 'print("Hi", end=" ")\nprint("there")', 'print("Hi", end=" ")\nprint("there")'),
            ("ราคา", "price=99.9 แสดง Price: 99.90", ":.2f", 'price = 99.9\nprint(f"Price: {price:.2f}")', 'price = 99.9\nprint(f"Price: {price:.2f}")'),
            ("คำนวณใน f", "แสดงผล 3*4 ใน f-string เป็น 12", "f\"{3*4}\"", 'print(f"{3 * 4}")', 'print(f"{3 * 4}")'),
            ("โปรไฟล์", 'age=10 แสดง f"I am {age}"', "f", "age = 10\nprint(f\"I am {age}\")", "age = 10\nprint(f\"I am {age}\")"),
        ],
    }

    data["011-operators"] = {
        "topic": "Operators",
        "medium_nums": (6, 7),
        "mediums": [
            (
                "ทอนเงิน",
                "รับราคาและเงินที่จ่าย (int) แสดงเงินทอน:\n\n```\nChange: <paid-price>\n```",
                "change = paid - price",
                "price = int(input())\npaid = int(input())\n",
                'price = int(input())\npaid = int(input())\nprint(f"Change: {paid - price}")',
                "**Input:**\n```\n40\n100\n```\n\n**Output:**\n```\nChange: 60\n```",
            ),
            (
                "เปรียบเทียบคะแนน",
                "รับคะแนนสองคน แสดงผลการเปรียบเทียบเป็น True/False ของ `a > b` เท่านั้นหนึ่งบรรทัด",
                "print(a > b)",
                "a = int(input())\nb = int(input())\n",
                "a = int(input())\nb = int(input())\nprint(a > b)",
                "**Input:**\n```\n9\n7\n```\n\n**Output:**\n```\nTrue\n```",
            ),
        ],
        "homeworks": [
            ("บวก", "รับสองจำนวน แสดงผลบวก", "+", "a=int(input()); b=int(input()); print(a+b)", "a = int(input())\nb = int(input())\nprint(a + b)"),
            ("คูณ", "รับสองจำนวน แสดงผลคูณ", "*", "a=int(input()); b=int(input()); print(a*b)", "a = int(input())\nb = int(input())\nprint(a * b)"),
            ("//", "แสดง 17//5", "//", "print(17 // 5)", "print(17 // 5)"),
            ("%", "แสดง 17%5", "%", "print(17 % 5)", "print(17 % 5)"),
            ("**", "แสดง 2**4", "**", "print(2 ** 4)", "print(2 ** 4)"),
            ("==", "รับ n แสดง n==10", "==", "n=int(input()); print(n==10)", "n = int(input())\nprint(n == 10)"),
            (">=", "รับ n แสดง n>=50", ">=", "n=int(input()); print(n>=50)", "n = int(input())\nprint(n >= 50)"),
            ("ลำดับ", "แสดงผล 2+3*4", "คูณก่อน", "print(2 + 3 * 4)", "print(2 + 3 * 4)"),
            ("วงเล็บ", "แสดงผล (2+3)*4", "()", "print((2 + 3) * 4)", "print((2 + 3) * 4)"),
            ("หาร", "แสดง 9/2", "/", "print(9 / 2)", "print(9 / 2)"),
        ],
    }

    data["012-review"] = {
        "topic": "Review",
        "medium_nums": (6, 7),
        "mediums": [
            (
                "แคชเชียร์มินิ (ยังไม่ใช้ if)",
                "รับชื่อสินค้า (str) ราคา (int) จำนวน (int) แสดง:\n\n```\n<item> x<qty>\nTotal: <price*qty>\n```",
                "ใช้ input + f-string ได้",
                "item = input()\nprice = int(input())\nqty = int(input())\n",
                'item = input()\nprice = int(input())\nqty = int(input())\nprint(f"{item} x{qty}")\nprint(f"Total: {price * qty}")',
                "**Input:**\n```\nEraser\n10\n3\n```\n\n**Output:**\n```\nEraser x3\nTotal: 30\n```",
            ),
            (
                "โปรไฟล์สั้น",
                "รับชื่อ และเมือง แสดงการ์ด:\n\n```\nPROFILE\nName: ...\nCity: ...\n```",
                "สอง input + print หัวข้อ",
                "name = input()\ncity = input()\n",
                'name = input()\ncity = input()\nprint("PROFILE")\nprint(f"Name: {name}")\nprint(f"City: {city}")',
                "**Input:**\n```\nLee\nChiang Mai\n```\n\n**Output:**\n```\nPROFILE\nName: Lee\nCity: Chiang Mai\n```",
            ),
        ],
        "homeworks": [
            ("ทบทวน print", 'แสดง `Review day`', "print", 'print("Review day")', 'print("Review day")'),
            ("ตัวแปร", "a=5 แสดง", "=", "a = 5\nprint(a)", "a = 5\nprint(a)"),
            ("แปลง", 'int("7")+3', "int", 'print(int("7") + 3)', 'print(int("7") + 3)'),
            ("input ชื่อ", "รับชื่อแสดง", "input", "print(input())", "print(input())"),
            ("f-string", 'n=2 แสดง f"n={n}"', "f", "n = 2\nprint(f\"n={n}\")", "n = 2\nprint(f\"n={n}\")"),
            ("บวกอินพุต", "สอง int ผลรวม", "+", "print(int(input())+int(input()))", "a = int(input())\nb = int(input())\nprint(a + b)"),
            (":.1f", "แสดง 2/3 แบบทศนิยม 1 ตำแหน่ง", ":.1f", 'print(f"{(2/3):.1f}")', 'print(f"{(2 / 3):.1f}")'),
            ("%", "แสดง 10%4", "%", "print(10 % 4)", "print(10 % 4)"),
            ("type", "แสดง type(True)", "type", "print(type(True))", "print(type(True))"),
            ("รวมทักษะ", 'รับเลข แสดง f"Value: {n}"', "int+f", 'n = int(input())\nprint(f"Value: {n}")', 'n = int(input())\nprint(f"Value: {n}")'),
        ],
    }

    # 013-024 continue
    data["013-if-else"] = {
        "topic": "if/else",
        "medium_nums": (6, 7),
        "mediums": [
            (
                "เปิด-ปิดตามชั่วโมง",
                "รับชั่วโมง (0–23) ถ้าอยู่ในช่วง 9 ถึง 17 inclusive แสดง `Open` ไม่เช่นนั้น `Closed`",
                "if 9 <= hour <= 17",
                "hour = int(input())\n",
                'hour = int(input())\nif 9 <= hour <= 17:\n    print("Open")\nelse:\n    print("Closed")',
                "**Input:** `10` → `Open`",
            ),
            (
                "ผ่านเกณฑ์พิเศษ",
                "รับคะแนน ถ้า >= 60 แสดง `Pass` ไม่เช่นนั้น `Fail` (เกณฑ์ต่างจากข้อง่ายในคลาสถ้ามี)",
                "if/else",
                "score = int(input())\n",
                'score = int(input())\nif score >= 60:\n    print("Pass")\nelse:\n    print("Fail")',
                "**Input:** `59` → `Fail`",
            ),
        ],
        "homeworks": [
            ("บวกหรือไม่", "รับ n ถ้า n>0 แสดง Positive ไม่เช่นนั้น Non-positive", "if", 'n=int(input())\nif n>0:\n    print("Positive")\nelse:\n    print("Non-positive")', 'n = int(input())\nif n > 0:\n    print("Positive")\nelse:\n    print("Non-positive")'),
            ("เท่ากับ 0", "รับ n ถ้า n==0 แสดง Zero else Other", "==", 'n=int(input())\nif n==0:\n    print("Zero")\nelse:\n    print("Other")', 'n = int(input())\nif n == 0:\n    print("Zero")\nelse:\n    print("Other")'),
            ("อายุเข้างาน", "รับอายุ ถ้า >=18 แสดง Adult else Kid", ">=", 'age=int(input())\nif age>=18:\n    print("Adult")\nelse:\n    print("Kid")', 'age = int(input())\nif age >= 18:\n    print("Adult")\nelse:\n    print("Kid")'),
            ("รหัสถูก", "รับรหัส int ถ้า ==1234 แสดง OK else No", "==", 'c=int(input())\nif c==1234:\n    print("OK")\nelse:\n    print("No")', 'c = int(input())\nif c == 1234:\n    print("OK")\nelse:\n    print("No")'),
            ("ร้อนไหม", "รับอุณหภูมิ ถ้า >=30 แสดง Hot else Cool", ">=", 't=int(input())\nif t>=30:\n    print("Hot")\nelse:\n    print("Cool")', 't = int(input())\nif t >= 30:\n    print("Hot")\nelse:\n    print("Cool")'),
            ("ส่วนลดเบื้องต้น", "รับราคา ถ้า >=100 แสดง Discount else Normal", ">=", 'p=int(input())\nif p>=100:\n    print("Discount")\nelse:\n    print("Normal")', 'p = int(input())\nif p >= 100:\n    print("Discount")\nelse:\n    print("Normal")'),
            ("ยาวกว่า", "รับเลข n แทนความยาว: ถ้า n>5 แสดง Long else Short", ">", 'n=int(input())\nif n>5:\n    print("Long")\nelse:\n    print("Short")', 'n = int(input())\nif n > 5:\n    print("Long")\nelse:\n    print("Short")'),
            ("คู่แรก", "รับ n ถ้า n%2==0 แสดง Even else Odd (ใช้ % จากบท operators)", "%", 'n=int(input())\nif n%2==0:\n    print("Even")\nelse:\n    print("Odd")', 'n = int(input())\nif n % 2 == 0:\n    print("Even")\nelse:\n    print("Odd")'),
            ("เกณฑ์ 80", "รับคะแนน ถ้า >=80 แสดง Great else Keep going", ">=", 's=int(input())\nif s>=80:\n    print("Great")\nelse:\n    print("Keep going")', 's = int(input())\nif s >= 80:\n    print("Great")\nelse:\n    print("Keep going")'),
            ("มินิ", "รับ n ถ้า n<0 แสดง Neg else Non-neg", "<", 'n=int(input())\nif n<0:\n    print("Neg")\nelse:\n    print("Non-neg")', 'n = int(input())\nif n < 0:\n    print("Neg")\nelse:\n    print("Non-neg")'),
        ],
    }

    data["014-even-odd"] = {
        "topic": "Even/Odd",
        "medium_nums": (6, 7),
        "mediums": [
            (
                "ที่นั่งคู่-คี่",
                "รับเลขที่นั่ง ถ้าเป็นเลขคู่แสดง `Window` ถ้าคี่แสดง `Aisle`",
                "n % 2 == 0",
                "seat = int(input())\n",
                'seat = int(input())\nif seat % 2 == 0:\n    print("Window")\nelse:\n    print("Aisle")',
                "**Input:** `14` → `Window`",
            ),
            (
                "แสตมป์หาร 5 ลงตัว",
                "รับจำนวน ถ้าหาร 5 ลงตัวแสดง `Stamp` ไม่เช่นนั้น `No stamp`",
                "n % 5 == 0",
                "n = int(input())\n",
                'n = int(input())\nif n % 5 == 0:\n    print("Stamp")\nelse:\n    print("No stamp")',
                "**Input:** `20` → `Stamp`",
            ),
        ],
        "homeworks": [
            ("คู่ไหม", "รับ n แสดง Even/Odd", "%2", 'n=int(input())\nif n%2==0:\n    print("Even")\nelse:\n    print("Odd")', 'n = int(input())\nif n % 2 == 0:\n    print("Even")\nelse:\n    print("Odd")'),
            ("เศษ 2", "รับ n แสดงค่า n%2", "%", "print(int(input()) % 2)", "print(int(input()) % 2)"),
            ("หาร 3", "ถ้า %3==0 แสดง Yes else No", "%3", 'n=int(input())\nif n%3==0:\n    print("Yes")\nelse:\n    print("No")', 'n = int(input())\nif n % 3 == 0:\n    print("Yes")\nelse:\n    print("No")'),
            ("หาร 10", "ถ้าลงตัว 10 แสดง Round", "%10", 'n=int(input())\nif n%10==0:\n    print("Round")\nelse:\n    print("Not")', 'n = int(input())\nif n % 10 == 0:\n    print("Round")\nelse:\n    print("Not")'),
            ("เลขท้าย", "แสดง n%10", "%", "print(int(input()) % 10)", "print(int(input()) % 10)"),
            ("คู่และบวก", "ถ้าคู่และ >0 แสดง OK else No", "and ยังไม่บังคับ — ใช้ if ซ้อนไม่ได้ถ้ายังไม่สอน nested if มาก — ใช้ % และ > แยกง่าย: ถ้าคู่แสดง Even+ ถ้าคี่ Odd", 'n=int(input())\nif n%2==0:\n    print("Even")\nelse:\n    print("Odd")', 'n = int(input())\nif n % 2 == 0:\n    print("Even")\nelse:\n    print("Odd")'),
            ("0 เป็นคู่", "รับ 0 แล้วดูว่าแสดง Even", "%", 'n=int(input())\nif n%2==0:\n    print("Even")\nelse:\n    print("Odd")', 'n = int(input())\nif n % 2 == 0:\n    print("Even")\nelse:\n    print("Odd")'),
            ("เลขรถ", "รับเลขทะเบียนจำลอง int ถ้าคี่แสดง Odd plate", "%", 'n=int(input())\nif n%2!=0:\n    print("Odd plate")\nelse:\n    print("Even plate")', 'n = int(input())\nif n % 2 != 0:\n    print("Odd plate")\nelse:\n    print("Even plate")'),
            ("หาร 4", "%4==0 → Block A else Block B", "%4", 'n=int(input())\nif n%4==0:\n    print("Block A")\nelse:\n    print("Block B")', 'n = int(input())\nif n % 4 == 0:\n    print("Block A")\nelse:\n    print("Block B")'),
            ("สรุป", "รับ n แสดงคำว่า Checked หลังตัดสิน Even/Odd คนละบรรทัด", "สอง print", 'n=int(input())\nif n%2==0:\n    print("Even")\nelse:\n    print("Odd")\nprint("Checked")', 'n = int(input())\nif n % 2 == 0:\n    print("Even")\nelse:\n    print("Odd")\nprint("Checked")'),
        ],
    }

    data["015-elif"] = {
        "topic": "elif",
        "medium_nums": (6, 7),
        "mediums": [
            (
                "ราคาตั๋วตามอายุ",
                "รับอายุ: <5 ฟรีแสดง `Free`, 5–12 แสดง `Child`, อื่นๆ แสดง `Adult`",
                "if / elif / else",
                "age = int(input())\n",
                'age = int(input())\nif age < 5:\n    print("Free")\nelif age <= 12:\n    print("Child")\nelse:\n    print("Adult")',
                "**Input:** `8` → `Child`",
            ),
            (
                "เกรดตัวอักษร",
                "รับคะแนน: >=80 A, >=70 B, >=60 C, อื่นๆ D",
                "elif เรียงจากมากไปน้อย",
                "score = int(input())\n",
                'score = int(input())\nif score >= 80:\n    print("A")\nelif score >= 70:\n    print("B")\nelif score >= 60:\n    print("C")\nelse:\n    print("D")',
                "**Input:** `75` → `B`",
            ),
        ],
        "homeworks": [
            ("3 ทาง", "รับ n: >0 Pos, <0 Neg, else Zero", "elif", 'n=int(input())\nif n>0:\n    print("Pos")\nelif n<0:\n    print("Neg")\nelse:\n    print("Zero")', 'n = int(input())\nif n > 0:\n    print("Pos")\nelif n < 0:\n    print("Neg")\nelse:\n    print("Zero")'),
            ("ขนาด", "รับ size: >=100 L, >=50 M, else S", "elif", 'n=int(input())\nif n>=100:\n    print("L")\nelif n>=50:\n    print("M")\nelse:\n    print("S")', 'n = int(input())\nif n >= 100:\n    print("L")\nelif n >= 50:\n    print("M")\nelse:\n    print("S")'),
            ("อุณหภูมิ", ">=35 Hot, >=20 Warm, else Cold", "elif", 't=int(input())\nif t>=35:\n    print("Hot")\nelif t>=20:\n    print("Warm")\nelse:\n    print("Cold")', 't = int(input())\nif t >= 35:\n    print("Hot")\nelif t >= 20:\n    print("Warm")\nelse:\n    print("Cold")'),
            ("เลเวล", ">=10 High, >=5 Mid, else Low", "elif", 'n=int(input())\nif n>=10:\n    print("High")\nelif n>=5:\n    print("Mid")\nelse:\n    print("Low")', 'n = int(input())\nif n >= 10:\n    print("High")\nelif n >= 5:\n    print("Mid")\nelse:\n    print("Low")'),
            ("เกรดง่าย", ">=50 Pass else Fail — ยังใช้ if อย่างเดียวได้ แต่ลองมี elif สำหรับ ==50 แสดง Border", "elif", 's=int(input())\nif s>50:\n    print("Pass")\nelif s==50:\n    print("Border")\nelse:\n    print("Fail")', 's = int(input())\nif s > 50:\n    print("Pass")\nelif s == 50:\n    print("Border")\nelse:\n    print("Fail")'),
            ("มื้ออาหาร", "รับชั่วโมง: <11 Breakfast, <15 Lunch, else Dinner", "elif", 'h=int(input())\nif h<11:\n    print("Breakfast")\nelif h<15:\n    print("Lunch")\nelse:\n    print("Dinner")', 'h = int(input())\nif h < 11:\n    print("Breakfast")\nelif h < 15:\n    print("Lunch")\nelse:\n    print("Dinner")'),
            ("ความเร็ว", ">=120 Fast, >=60 OK, else Slow", "elif", 'v=int(input())\nif v>=120:\n    print("Fast")\nelif v>=60:\n    print("OK")\nelse:\n    print("Slow")', 'v = int(input())\nif v >= 120:\n    print("Fast")\nelif v >= 60:\n    print("OK")\nelse:\n    print("Slow")'),
            ("คะแนน 4 ระดับ", ">=90 S, >=80 A, >=70 B, else C", "elif", 's=int(input())\nif s>=90:\n    print("S")\nelif s>=80:\n    print("A")\nelif s>=70:\n    print("B")\nelse:\n    print("C")', 's = int(input())\nif s >= 90:\n    print("S")\nelif s >= 80:\n    print("A")\nelif s >= 70:\n    print("B")\nelse:\n    print("C")'),
            ("เลือกเมนูเลข", "รับ 1/2/อื่นๆ แสดง Water/Juice/Other", "elif", 'n=int(input())\nif n==1:\n    print("Water")\nelif n==2:\n    print("Juice")\nelse:\n    print("Other")', 'n = int(input())\nif n == 1:\n    print("Water")\nelif n == 2:\n    print("Juice")\nelse:\n    print("Other")'),
            ("จบ", "รับคะแนน แสดงเกรดแบบ >=60 Pass elif >=40 Retake else Fail", "elif", 's=int(input())\nif s>=60:\n    print("Pass")\nelif s>=40:\n    print("Retake")\nelse:\n    print("Fail")', 's = int(input())\nif s >= 60:\n    print("Pass")\nelif s >= 40:\n    print("Retake")\nelse:\n    print("Fail")'),
        ],
    }

    data["016-logical-operator"] = {
        "topic": "Logical Operators",
        "medium_nums": (6, 7),
        "mediums": [
            (
                "ขึ้นเครื่องเล่นได้ไหม",
                "รับส่วนสูง (ซม.) และอายุ — ถ้าสูง >=120 และอายุ >=10 แสดง `Allowed` ไม่เช่นนั้น `Denied`",
                "and",
                "height = int(input())\nage = int(input())\n",
                'height = int(input())\nage = int(input())\nif height >= 120 and age >= 10:\n    print("Allowed")\nelse:\n    print("Denied")',
                "**Input:**\n```\n130\n12\n```\n→ `Allowed`",
            ),
            (
                "ร้านเปิดวันพิเศษ",
                "รับค่า is_weekend เป็น 1/0 และ is_holiday เป็น 1/0 — ถ้าอย่างใดอย่างหนึ่งเป็น 1 แสดง `Open` ไม่เช่นนั้น `Closed`",
                "or",
                "is_weekend = int(input())\nis_holiday = int(input())\n",
                'is_weekend = int(input())\nis_holiday = int(input())\nif is_weekend == 1 or is_holiday == 1:\n    print("Open")\nelse:\n    print("Closed")',
                "**Input:**\n```\n0\n1\n```\n→ `Open`",
            ),
        ],
        "homeworks": [
            ("and พื้นฐาน", "รับ a b ถ้าทั้งคู่ >0 แสดง Both", "and", 'a=int(input()); b=int(input())\nif a>0 and b>0:\n    print("Both")\nelse:\n    print("No")', 'a = int(input())\nb = int(input())\nif a > 0 and b > 0:\n    print("Both")\nelse:\n    print("No")'),
            ("or พื้นฐาน", "ถ้า a==0 หรือ b==0 แสดง Has zero", "or", 'a=int(input()); b=int(input())\nif a==0 or b==0:\n    print("Has zero")\nelse:\n    print("None")', 'a = int(input())\nb = int(input())\nif a == 0 or b == 0:\n    print("Has zero")\nelse:\n    print("None")'),
            ("not", "รับค่า 0/1 เป็น raining — ถ้า not raining แสดง Go out", "not", 'r=int(input())\nif not r:\n    print("Go out")\nelse:\n    print("Stay")', 'r = int(input())\nif not r:\n    print("Go out")\nelse:\n    print("Stay")'),
            ("ช่วง", "รับ n ถ้า 1<=n<=10 แสดง In range", "and", 'n=int(input())\nif n>=1 and n<=10:\n    print("In range")\nelse:\n    print("Out")', 'n = int(input())\nif n >= 1 and n <= 10:\n    print("In range")\nelse:\n    print("Out")'),
            ("ผ่านวิชา", "คะแนน>=50 และเข้าเรียน>=80 แสดง Pass", "and", 's=int(input()); a=int(input())\nif s>=50 and a>=80:\n    print("Pass")\nelse:\n    print("Fail")', 's = int(input())\na = int(input())\nif s >= 50 and a >= 80:\n    print("Pass")\nelse:\n    print("Fail")'),
            ("ส่วนลด", "สมาชิก 1 หรือ ยอด>=1000 แสดง Discount", "or", 'm=int(input()); t=int(input())\nif m==1 or t>=1000:\n    print("Discount")\nelse:\n    print("No")', 'm = int(input())\nt = int(input())\nif m == 1 or t >= 1000:\n    print("Discount")\nelse:\n    print("No")'),
            ("ล็อกอินง่าย", "user ถูก (1) และ pass ถูก (1)", "and", 'u=int(input()); p=int(input())\nif u==1 and p==1:\n    print("Login")\nelse:\n    print("Deny")', 'u = int(input())\np = int(input())\nif u == 1 and p == 1:\n    print("Login")\nelse:\n    print("Deny")'),
            ("ห้าม", "ถ้าอายุ<13 หรือสูง<100 แสดง Too small", "or", 'age=int(input()); h=int(input())\nif age<13 or h<100:\n    print("Too small")\nelse:\n    print("OK")', 'age = int(input())\nh = int(input())\nif age < 13 or h < 100:\n    print("Too small")\nelse:\n    print("OK")'),
            ("ไฟเปิด", "รับ night 1/0 — ถ้า not night แสดง Lights off idea: แสดง Day", "not", 'n=int(input())\nif not n:\n    print("Day")\nelse:\n    print("Night")', 'n = int(input())\nif not n:\n    print("Day")\nelse:\n    print("Night")'),
            ("คอมโบ", "คะแนน>=80 และ (โบนัส==1 หรือวิเศษ==1) แสดง Star", "and/or", 's=int(input()); b=int(input()); m=int(input())\nif s>=80 and (b==1 or m==1):\n    print("Star")\nelse:\n    print("Normal")', 's = int(input())\nb = int(input())\nm = int(input())\nif s >= 80 and (b == 1 or m == 1):\n    print("Star")\nelse:\n    print("Normal")'),
        ],
    }

    return data


def content_loops(data: dict) -> dict:
    data["017-for-loop"] = {
        "topic": "for Loop",
        "medium_nums": (7, 8),
        "mediums": [
            (
                "ผลรวม 1 ถึง n",
                "รับ n แล้วหาผลรวม 1+2+...+n แสดงผลรวมอย่างเดียว",
                "for i in range(1, n+1)",
                "n = int(input())\ntotal = 0\n",
                "n = int(input())\ntotal = 0\nfor i in range(1, n + 1):\n    total = total + i\nprint(total)",
                "**Input:** `4` → `10`",
            ),
            (
                "พหูคูณของ 3",
                "รับ n แสดงพหูคูณของ 3 จาก 3,6,... ที่ยัง <= n คนละบรรทัด",
                "range(3, n+1, 3)",
                "n = int(input())\n",
                "n = int(input())\nfor i in range(3, n + 1, 3):\n    print(i)",
                "**Input:** `12` →\n```\n3\n6\n9\n12\n```",
            ),
        ],
        "homeworks": [
            ("วน 3 รอบ", "พิมพ์ Hi สามครั้งด้วย for", "range(3)", 'for i in range(3):\n    print("Hi")', 'for i in range(3):\n    print("Hi")'),
            ("0 ถึง 3", "พิมพ์ i ใน range(4)", "range", "for i in range(4):\n    print(i)", "for i in range(4):\n    print(i)"),
            ("1 ถึง 5", "range(1,6)", "start stop", "for i in range(1, 6):\n    print(i)", "for i in range(1, 6):\n    print(i)"),
            ("ทีละ 2", "range(2,11,2)", "step", "for i in range(2, 11, 2):\n    print(i)", "for i in range(2, 11, 2):\n    print(i)"),
            ("ดาว 5", "พิมพ์ * ห้าบรรทัด", "range(5)", 'for i in range(5):\n    print("*")', 'for i in range(5):\n    print("*")'),
            ("รับ n รอบ", "รับ n พิมพ์ OK n ครั้ง", "range(n)", 'n=int(input())\nfor i in range(n):\n    print("OK")', 'n = int(input())\nfor i in range(n):\n    print("OK")'),
            ("ผลรวม 3 รอบ", "บวก 1+1+1 ด้วย loop แสดง 3", "total", "total=0\nfor i in range(3):\n    total=total+1\nprint(total)", "total = 0\nfor i in range(3):\n    total = total + 1\nprint(total)"),
            ("นับถอยหลังแบบ for", "พิมพ์ 3 2 1 ด้วย range", "range(3,0,-1)", "for i in range(3, 0, -1):\n    print(i)", "for i in range(3, 0, -1):\n    print(i)"),
            ("ตารางเล็ก", "พิมพ์ 5 10 15 20 25", "range(5,26,5)", "for i in range(5, 26, 5):\n    print(i)", "for i in range(5, 26, 5):\n    print(i)"),
            ("กำลังสอง", "พิมพ์ i*i สำหรับ i=1..4", "range(1,5)", "for i in range(1, 5):\n    print(i * i)", "for i in range(1, 5):\n    print(i * i)"),
        ],
    }

    data["018-loop-with-lists"] = {
        "topic": "Loop with Lists",
        "medium_nums": (6, 7),
        "mediums": [
            (
                "รวมคะแนนในลิสต์",
                "กำหนด scores = [70, 80, 90] หาผลรวมด้วย for แสดงผลรวม",
                "for s in scores",
                "scores = [70, 80, 90]\ntotal = 0\n",
                "scores = [70, 80, 90]\ntotal = 0\nfor s in scores:\n    total = total + s\nprint(total)",
                "",
            ),
            (
                "นับที่ผ่าน",
                "กำหนด scores = [40, 55, 60, 30] นับว่ามีกี่ตัวที่ >=50 แสดงจำนวน",
                "if ใน loop (เรียน if แล้ว)",
                "scores = [40, 55, 60, 30]\ncount = 0\n",
                "scores = [40, 55, 60, 30]\ncount = 0\nfor s in scores:\n    if s >= 50:\n        count = count + 1\nprint(count)",
                "",
            ),
        ],
        "homeworks": [
            ("พิมพ์สมาชิก", 'วน ["a","b","c"] แสดงทีละตัว', "for x in list", 'for x in ["a", "b", "c"]:\n    print(x)', 'for x in ["a", "b", "c"]:\n    print(x)'),
            ("len", "แสดง len([1,2,3,4])", "len", "print(len([1, 2, 3, 4]))", "print(len([1, 2, 3, 4]))"),
            ("index 0", "แสดงตัวแรกของ [9,8,7]", "[0]", "print([9, 8, 7][0])", "print([9, 8, 7][0])"),
            ("ผลรวมง่าย", "รวม [1,2,3]", "for", "t=0\nfor n in [1,2,3]:\n    t=t+n\nprint(t)", "t = 0\nfor n in [1, 2, 3]:\n    t = t + n\nprint(t)"),
            ("คูณสองแสดง", "แต่ละตัวใน [2,4] แสดง *2", "for", "for n in [2, 4]:\n    print(n * 2)", "for n in [2, 4]:\n    print(n * 2)"),
            ("นับสมาชิก", "นับจำนวนใน [1,1,1] ด้วย len หรือ loop", "len", "print(len([1, 1, 1]))", "print(len([1, 1, 1]))"),
            ("ข้อความ", 'วน ["red","blue"] แสดง', "for", 'for c in ["red", "blue"]:\n    print(c)', 'for c in ["red", "blue"]:\n    print(c)'),
            ("มากกว่า 5", "นับใน [3,6,9] ที่ >5", "if", "c=0\nfor n in [3,6,9]:\n    if n>5:\n        c=c+1\nprint(c)", "c = 0\nfor n in [3, 6, 9]:\n    if n > 5:\n        c = c + 1\nprint(c)"),
            ("append แนว", "สร้างลิสต์ว่าง แล้วไม่บังคับ append ถ้ายังไม่เน้น — แสดงสมาชิกของ [10,20]", "for", "for n in [10, 20]:\n    print(n)", "for n in [10, 20]:\n    print(n)"),
            ("เฉลี่ยง่าย", "รวม [10,20] / 2 แสดง 15.0", "total/len", "xs=[10,20]\nt=0\nfor x in xs:\n    t=t+x\nprint(t/len(xs))", "xs = [10, 20]\nt = 0\nfor x in xs:\n    t = t + x\nprint(t / len(xs))"),
        ],
    }

    data["019-while-loop"] = {
        "topic": "while Loop",
        "medium_nums": (6, 7),
        "mediums": [
            (
                "นับถอยหลัง",
                "รับ n แล้วพิมพ์ n, n-1, ... 1 ด้วย while",
                "อย่าลืม n = n - 1",
                "n = int(input())\n",
                "n = int(input())\nwhile n > 0:\n    print(n)\n    n = n - 1",
                "**Input:** `3` →\n```\n3\n2\n1\n```",
            ),
            (
                "ทายเลขจนถูก",
                "กำหนดรหัสลับ 7 — รับทายซ้ำด้วย while จนถูก แล้วแสดง `Correct!` (ระหว่างผิดแสดง `Wrong`)",
                "while guess != secret",
                "secret = 7\nguess = int(input())\n",
                'secret = 7\nguess = int(input())\nwhile guess != secret:\n    print("Wrong")\n    guess = int(input())\nprint("Correct!")',
                "**Input:**\n```\n1\n7\n```\n**Output:**\n```\nWrong\nCorrect!\n```",
            ),
        ],
        "homeworks": [
            ("while 1-3", "พิมพ์ 1 2 3 ด้วย while", "i+=1", "i=1\nwhile i<=3:\n    print(i)\n    i=i+1", "i = 1\nwhile i <= 3:\n    print(i)\n    i = i + 1"),
            ("ห้าครั้ง", "พิมพ์ Go 5 ครั้ง", "while", 'c=0\nwhile c<5:\n    print("Go")\n    c=c+1', 'c = 0\nwhile c < 5:\n    print("Go")\n    c = c + 1'),
            ("นับขึ้น", "พิมพ์ 0 ถึง 2", "while", "i=0\nwhile i<=2:\n    print(i)\n    i=i+1", "i = 0\nwhile i <= 2:\n    print(i)\n    i = i + 1"),
            ("ผลรวม", "บวก 1..4 ด้วย while แสดง 10", "while", "i=1\nt=0\nwhile i<=4:\n    t=t+i\n    i=i+1\nprint(t)", "i = 1\nt = 0\nwhile i <= 4:\n    t = t + i\n    i = i + 1\nprint(t)"),
            ("ลดชีวิต", "lives=3 ลดจน 0 พิมพ์เหลือก่อนลด", "while lives>0", "lives=3\nwhile lives>0:\n    print(lives)\n    lives=lives-1", "lives = 3\nwhile lives > 0:\n    print(lives)\n    lives = lives - 1"),
            ("รับจนไม่ใช่ 0 — แบบง่าย", "รับเลข ถ้าไม่ใช่ 0 พิมพ์เลขนั้น แล้วรับใหม่ จนได้ 0 (ไม่พิมพ์ 0)", "while", "n=int(input())\nwhile n!=0:\n    print(n)\n    n=int(input())", "n = int(input())\nwhile n != 0:\n    print(n)\n    n = int(input())"),
            ("สองเท่าจนเกิน", "เริ่ม x=1 ขณะ x<=8 พิมพ์แล้ว x*=2", "while", "x=1\nwhile x<=8:\n    print(x)\n    x=x*2", "x = 1\nwhile x <= 8:\n    print(x)\n    x = x * 2"),
            ("นับตัวอักษรแนว", "พิมพ์ A สามครั้งด้วย while", "while", 'i=0\nwhile i<3:\n    print("A")\n    i=i+1', 'i = 0\nwhile i < 3:\n    print("A")\n    i = i + 1'),
            ("หยุดที่ 5", "i=0 เพิ่มจนพิมพ์ถึง 5", "while i<=5", "i=0\nwhile i<=5:\n    print(i)\n    i=i+1", "i = 0\nwhile i <= 5:\n    print(i)\n    i = i + 1"),
            ("ระวังลืมอัปเดต", "เขียน while ที่ถูกต้องพิมพ์ 1 ครั้งคำว่า Once", "อัปเดตตัวแปร", 'done=False\nwhile not done:\n    print("Once")\n    done=True', 'done = False\nwhile not done:\n    print("Once")\n    done = True'),
        ],
    }

    data["020-loop-safety"] = {
        "topic": "Loop Safety",
        "medium_nums": (6, 7),
        "mediums": [
            (
                "หยุดเมื่อเจอคำ quit",
                "รับข้อความซ้ำด้วย while True — ถ้าได้ `quit` ให้ break ไม่ต้องพิมพ์ quit; คำอื่นพิมพ์ `Echo: ...`",
                "break",
                "while True:\n    word = input()\n",
                'while True:\n    word = input()\n    if word == "quit":\n        break\n    print(f"Echo: {word}")',
                "**Input:**\n```\nhi\nquit\n```\n**Output:**\n```\nEcho: hi\n```",
            ),
            (
                "ข้ามเลขติดลบ",
                "กำหนด nums = [3, -1, 4, -2, 5] พิมพ์เฉพาะค่าที่ >=0 ด้วย continue",
                "continue",
                "nums = [3, -1, 4, -2, 5]\n",
                "nums = [3, -1, 4, -2, 5]\nfor n in nums:\n    if n < 0:\n        continue\n    print(n)",
                "",
            ),
        ],
        "homeworks": [
            ("break พื้นฐาน", "for i in range(10) พิมพ์ i จน break ที่ 3 (พิมพ์ 0 1 2)", "break", "for i in range(10):\n    if i==3:\n        break\n    print(i)", "for i in range(10):\n    if i == 3:\n        break\n    print(i)"),
            ("continue พื้นฐาน", "range(5) ข้าม 2", "continue", "for i in range(5):\n    if i==2:\n        continue\n    print(i)", "for i in range(5):\n    if i == 2:\n        continue\n    print(i)"),
            ("while True หนึ่งรอบ", "พิมพ์ Start แล้ว break", "break", 'while True:\n    print("Start")\n    break', 'while True:\n    print("Start")\n    break'),
            ("ข้ามคู่", "range(1,6) ข้ามเลขคู่", "continue %", "for i in range(1,6):\n    if i%2==0:\n        continue\n    print(i)", "for i in range(1, 6):\n    if i % 2 == 0:\n        continue\n    print(i)"),
            ("หาแล้วหยุด", "ใน [1,2,9,4] พิมพ์จนเจอ 9 แล้ว break (พิมพ์ 9 ด้วย)", "break", "for n in [1,2,9,4]:\n    print(n)\n    if n==9:\n        break", "for n in [1, 2, 9, 4]:\n    print(n)\n    if n == 9:\n        break"),
            ("sentinel 0", "รับเลขรวมจนเจอ 0 ไม่บวก 0", "break", "t=0\nwhile True:\n    n=int(input())\n    if n==0:\n        break\n    t=t+n\nprint(t)", "t = 0\nwhile True:\n    n = int(input())\n    if n == 0:\n        break\n    t = t + n\nprint(t)"),
            ("ข้ามว่างแนว", "ลิสต์ [1,0,2] ข้าม 0", "continue", "for n in [1,0,2]:\n    if n==0:\n        continue\n    print(n)", "for n in [1, 0, 2]:\n    if n == 0:\n        continue\n    print(n)"),
            ("ปลอดภัย", "while นับ 1..3 มีอัปเดตครบ", "i+=1", "i=1\nwhile i<=3:\n    print(i)\n    i=i+1", "i = 1\nwhile i <= 3:\n    print(i)\n    i = i + 1"),
            ("สองเงื่อนไข", "range(10) ข้าม <3 หยุดเมื่อ >7 พิมพ์ค่าที่ผ่าน", "continue+break", "for i in range(10):\n    if i<3:\n        continue\n    if i>7:\n        break\n    print(i)", "for i in range(10):\n    if i < 3:\n        continue\n    if i > 7:\n        break\n    print(i)"),
            ("จบ", 'พิมพ์ Done หลัง loop ที่มี break ทันที', "หลัง while", 'while True:\n    break\nprint("Done")', 'while True:\n    break\nprint("Done")'),
        ],
    }

    data["021-nested-loops"] = {
        "topic": "Nested Loops",
        "medium_nums": (6, 7),
        "mediums": [
            (
                "สี่เหลี่ยมดาว",
                "รับแถว r และคอลัมน์ c พิมพ์สี่เหลี่ยมดาว (ใช้ end=\"\")",
                "nested for + print()",
                "r = int(input())\nc = int(input())\n",
                'r = int(input())\nc = int(input())\nfor i in range(r):\n    for j in range(c):\n        print("*", end="")\n    print()',
                "**Input:**\n```\n2\n3\n```\n**Output:**\n```\n***\n***\n```",
            ),
            (
                "ตารางคูณมุมเล็ก",
                "พิมพ์ตารางคูณ 1..3 กับ 1..3 (ช่องคั่นด้วยช่องว่าง จบแถวขึ้นบรรทัดใหม่)",
                "nested range(1,4)",
                "# ตาราง 3x3",
                "for i in range(1, 4):\n    for j in range(1, 4):\n        print(i * j, end=\" \")\n    print()",
                "",
            ),
        ],
        "homeworks": [
            ("2x2 ดาว", "พิมพ์ ** สองแถว", "nested", 'for i in range(2):\n    for j in range(2):\n        print("*", end="")\n    print()', 'for i in range(2):\n    for j in range(2):\n        print("*", end="")\n    print()'),
            ("คู่ i j", "range(2)x range(2) พิมพ์ i j", "print i,j", "for i in range(2):\n    for j in range(2):\n        print(i, j)", "for i in range(2):\n    for j in range(2):\n        print(i, j)"),
            ("สามเหลี่ยม 3", "แถว 1..3 พิมพ์ * ตามแถว", "range(row)", 'for row in range(1,4):\n    for k in range(row):\n        print("*", end="")\n    print()', 'for row in range(1, 4):\n    for k in range(row):\n        print("*", end="")\n    print()'),
            ("ซ้ำข้อความ", "นอก 2 รอบ ในพิมพ์ Hi", "nested", 'for i in range(2):\n    for j in range(2):\n        print("Hi")', 'for i in range(2):\n    for j in range(2):\n        print("Hi")'),
            ("ผลคูณแถว", "i=1..2 j=1..2 พิมพ์ i*j", "nested", "for i in range(1,3):\n    for j in range(1,3):\n        print(i*j)", "for i in range(1, 3):\n    for j in range(1, 3):\n        print(i * j)"),
            ("กรอบตัวเลข", "พิมพ์ 1 2 3 สองแถวด้วย nested", "end", "for i in range(2):\n    for j in range(1,4):\n        print(j, end=\" \")\n    print()", "for i in range(2):\n    for j in range(1, 4):\n        print(j, end=\" \")\n    print()"),
            ("นับรอบรวม", "นอก 3 ใน 2 — พิมพ์ x รวม 6 ครั้ง", "3*2", 'for i in range(3):\n    for j in range(2):\n        print("x")', 'for i in range(3):\n    for j in range(2):\n        print("x")'),
            ("แถวเลข", "สำหรับ i in 1..3 พิมพ์เลข 1..i", "nested", "for i in range(1,4):\n    for j in range(1,i+1):\n        print(j, end=\"\")\n    print()", "for i in range(1, 4):\n    for j in range(1, i + 1):\n        print(j, end=\"\")\n    print()"),
            ("ว่างคั่น", "2 แถว แต่ละแถว a b", "end space", 'for i in range(2):\n    print("a", end=" ")\n    print("b")', 'for i in range(2):\n    print("a", end=" ")\n    print("b")'),
            ("รับขนาด", "รับ n พิมพ์สี่เหลี่ยม nxn เป็น #", "input", 'n=int(input())\nfor i in range(n):\n    for j in range(n):\n        print("#", end="")\n    print()', 'n = int(input())\nfor i in range(n):\n    for j in range(n):\n        print("#", end="")\n    print()'),
        ],
    }

    data["022-loop-review"] = {
        "topic": "Loop Review",
        "medium_nums": (16, 17),
        "mediums": [
            (
                "for สร้างยอด แล้ว while ตรวจ",
                "รับ n — ใช้ for รวม 1..n เก็บใน total จากนั้นใช้ while ลด total ทีละ 1 พิมพ์ค่าจนกว่าจะเหลือ 0 (พิมพ์ลงไปถึง 1)",
                " fore + while",
                "n = int(input())\n",
                "n = int(input())\ntotal = 0\nfor i in range(1, n + 1):\n    total = total + i\nwhile total > 0:\n    print(total)\n    total = total - 1",
                "**Input:** `2` → รวม=3 แล้วพิมพ์ 3 2 1",
            ),
            (
                "กรองด้วย continue",
                "รับจำนวนกี่ตัว k แล้วรับเลข k ครั้ง — พิมพ์เฉพาะเลขที่หาร 2 ลงตัว (ข้ามคี่ด้วย continue)",
                "continue",
                "k = int(input())\n",
                "k = int(input())\nfor _ in range(k):\n    n = int(input())\n    if n % 2 != 0:\n        continue\n    print(n)",
                "**Input:**\n```\n3\n1\n4\n5\n```\n**Output:**\n```\n4\n```",
            ),
        ],
        "homeworks": [
            ("for สั้น", "range(3) พิมพ์ i", "for", "for i in range(3):\n    print(i)", "for i in range(3):\n    print(i)"),
            ("while สั้น", "พิมพ์ 1 2 ด้วย while", "while", "i=1\nwhile i<=2:\n    print(i)\n    i=i+1", "i = 1\nwhile i <= 2:\n    print(i)\n    i = i + 1"),
            ("list loop", "วน [5,6] พิมพ์", "for", "for n in [5, 6]:\n    print(n)", "for n in [5, 6]:\n    print(n)"),
            ("break", "range(5) หยุดที่ 2 หลังพิมพ์ 2", "break", "for i in range(5):\n    print(i)\n    if i==2:\n        break", "for i in range(5):\n    print(i)\n    if i == 2:\n        break"),
            ("continue", "range(4) ข้าม 1", "continue", "for i in range(4):\n    if i==1:\n        continue\n    print(i)", "for i in range(4):\n    if i == 1:\n        continue\n    print(i)"),
            ("ผลรวม", "รวม range(1,4)", "for", "t=0\nfor i in range(1,4):\n    t+=i\nprint(t)", "t = 0\nfor i in range(1, 4):\n    t = t + i\nprint(t)"),
            ("nested มินิ", "2x2 พิมพ์ #", "nested", 'for i in range(2):\n    for j in range(2):\n        print("#", end="")\n    print()', 'for i in range(2):\n    for j in range(2):\n        print("#", end="")\n    print()'),
            ("while True", "พิมพ์ X แล้ว break", "break", 'while True:\n    print("X")\n    break', 'while True:\n    print("X")\n    break'),
            ("นับคู่", "นับเลขคู่ใน [1,2,3,4]", "%", "c=0\nfor n in [1,2,3,4]:\n    if n%2==0:\n        c=c+1\nprint(c)", "c = 0\nfor n in [1, 2, 3, 4]:\n    if n % 2 == 0:\n        c = c + 1\nprint(c)"),
            ("สรุปรอบ", 'พิมพ์ `loops ok`', "print", 'print("loops ok")', 'print("loops ok")'),
        ],
    }

    data["023-debugging-loops"] = {
        "topic": "Debugging Loops",
        "medium_nums": (6, 7),
        "mediums": [
            (
                "แก้ off-by-one",
                "ต้องการพิมพ์ 1 ถึง 4 — โค้ดผิดใช้ range(1,4) อยู่ เขียนเวอร์ชันที่ถูก",
                "range(1,5)",
                "# พิมพ์ 1..4",
                "for i in range(1, 5):\n    print(i)",
                "",
            ),
            (
                "แก้ infinite while",
                "ต้องการพิมพ์ 1 2 3 ด้วย while — อย่าลืมอัปเดตตัวแปร",
                "i = i + 1",
                "i = 1\nwhile i <= 3:\n    print(i)\n    # แก้ตรงนี้\n",
                "i = 1\nwhile i <= 3:\n    print(i)\n    i = i + 1",
                "",
            ),
        ],
        "homeworks": [
            ("range ถูก", "พิมพ์ 1..3 ด้วย range ที่ถูก", "range(1,4)", "for i in range(1, 4):\n    print(i)", "for i in range(1, 4):\n    print(i)"),
            ("อัปเดต", "while พิมพ์สองครั้ง Hi", "ตัวนับ", 'c=0\nwhile c<2:\n    print("Hi")\n    c=c+1', 'c = 0\nwhile c < 2:\n    print("Hi")\n    c = c + 1'),
            ("indent", "for พิมพ์ 0 1 2 ให้ indent ถูก", "indent", "for i in range(3):\n    print(i)", "for i in range(3):\n    print(i)"),
            ("ตัวแปรวน", 'for name in ["A","B"]: พิมพ์ name ไม่ใช่ลิสต์', "name", 'for name in ["A", "B"]:\n    print(name)', 'for name in ["A", "B"]:\n    print(name)'),
            ("debug print", "วน range(2) พิมพ์ค่า debug แบบ f", "f", 'for i in range(2):\n    print(f"i={i}")', 'for i in range(2):\n    print(f"i={i}")'),
            ("หยุดก่อน", "อย่าใช้ range(5) เมื่อต้องการแค่ 0..3", "range(4)", "for i in range(4):\n    print(i)", "for i in range(4):\n    print(i)"),
            ("เงื่อนไข while", "พิมพ์จน i<3 เมื่อเริ่ม 0", "while i<3", "i=0\nwhile i<3:\n    print(i)\n    i=i+1", "i = 0\nwhile i < 3:\n    print(i)\n    i = i + 1"),
            ("ไม่ลืม break", "while True พิมพ์ End แล้ว break", "break", 'while True:\n    print("End")\n    break', 'while True:\n    print("End")\n    break'),
            ("ข้ามบั๊ก", "continue เมื่อ i==0 ใน range(3) — พิมพ์ 1 2", "continue", "for i in range(3):\n    if i==0:\n        continue\n    print(i)", "for i in range(3):\n    if i == 0:\n        continue\n    print(i)"),
            ("พร้อม", 'แสดง `bugs fixed`', "print", 'print("bugs fixed")', 'print("bugs fixed")'),
        ],
    }

    data["024-midyear-review"] = {
        "topic": "Midyear Review",
        "medium_nums": (6, 7),
        "mediums": [
            (
                "เฉลี่ย 3 วิชา + เกรด",
                "รับคะแนน 3 วิชา (int) หาเฉลี่ย แสดงเฉลี่ยทศนิยม 1 ตำแหน่ง แล้วเกรด A ถ้า >=80, B ถ้า >=60, else C",
                "loop หรือบวกสามค่า + elif",
                "s1 = int(input())\ns2 = int(input())\ns3 = int(input())\n",
                's1 = int(input())\ns2 = int(input())\ns3 = int(input())\navg = (s1 + s2 + s3) / 3\nprint(f"{avg:.1f}")\nif avg >= 80:\n    print("A")\nelif avg >= 60:\n    print("B")\nelse:\n    print("C")',
                "**Input:**\n```\n80\n70\n90\n```\n**Output:**\n```\n80.0\nA\n```",
            ),
            (
                "ตะกร้า + ภาษี",
                "รับราคาสินค้า 2 ชิ้น (int) รวมกัน แล้วบวก VAT 7% แสดงยอดสุดท้ายทศนิยม 2 ตำแหน่ง",
                "ผลรวม * 1.07 และ :.2f",
                "a = int(input())\nb = int(input())\n",
                'a = int(input())\nb = int(input())\ntotal = (a + b) * 1.07\nprint(f"{total:.2f}")',
                "**Input:**\n```\n100\n100\n```\n**Output:**\n```\n214.00\n```",
            ),
        ],
        "homeworks": [
            ("input+print", "รับชื่อแสดง Hello", "input", 'print("Hello,", input())', 'name = input()\nprint("Hello,", name)'),
            ("แปลง", "รับเลข +5", "int", "print(int(input()) + 5)", "print(int(input()) + 5)"),
            ("if", ">=50 Pass", "if", 'n=int(input())\nif n>=50:\n    print("Pass")\nelse:\n    print("Fail")', 'n = int(input())\nif n >= 50:\n    print("Pass")\nelse:\n    print("Fail")'),
            ("%", "Even/Odd", "%", 'n=int(input())\nif n%2==0:\n    print("Even")\nelse:\n    print("Odd")', 'n = int(input())\nif n % 2 == 0:\n    print("Even")\nelse:\n    print("Odd")'),
            ("elif", "A/B/C แบบ >=80/>=60", "elif", 's=int(input())\nif s>=80:\n    print("A")\nelif s>=60:\n    print("B")\nelse:\n    print("C")', 's = int(input())\nif s >= 80:\n    print("A")\nelif s >= 60:\n    print("B")\nelse:\n    print("C")'),
            ("for", "พิมพ์ 1..n", "for", "n=int(input())\nfor i in range(1,n+1):\n    print(i)", "n = int(input())\nfor i in range(1, n + 1):\n    print(i)"),
            ("list", "รวม [2,2,2]", "for", "t=0\nfor x in [2,2,2]:\n    t+=x\nprint(t)", "t = 0\nfor x in [2, 2, 2]:\n    t = t + x\nprint(t)"),
            ("while", "นับ 1..3", "while", "i=1\nwhile i<=3:\n    print(i)\n    i+=1", "i = 1\nwhile i <= 3:\n    print(i)\n    i = i + 1"),
            ("f-string", "เฉลี่ยง่าย (10+20)/2 แบบ :.1f", "f", 'print(f"{(10+20)/2:.1f}")', 'print(f"{(10 + 20) / 2:.1f}")'),
            ("รวมท้าย", 'แสดง `midyear done`', "print", 'print("midyear done")', 'print("midyear done")'),
        ],
    }
    return data


def answer_name(num: int, title_slug: str) -> str:
    return f"{num:02d}_{title_slug}.py"


def slugify(title: str) -> str:
    # simple ascii slug from thai/english title
    mapping = {
        "ป้ายเมนูร้านกาแฟ": "coffee_menu",
        "ใบเสร็จสั้นๆ": "mini_receipt",
        "จับคู่ Error": "match_errors",
        "แก้โค้ดให้รันได้": "fix_ready",
        "แก้ snippet ให้ถูก": "fix_snippet",
        "กฎสามข้อ": "three_rules",
        "เขียนตามแผน comment": "from_comments",
        "ใส่ comment ให้โค้ด": "add_comments",
        "สลับค่าด้วยตัวแปรชั่วคราว": "swap_temp",
        "อัปเดตคะแนนทีละขั้น": "score_steps",
        "เขียนใหม่ด้วยชื่อที่ดี": "rename_good",
        "เลือกชื่อที่ถูก": "valid_names",
        "ทาย type()": "guess_types",
        "อย่าสับสน str กับ int": "str_vs_int",
        "บิล + VAT จากข้อความ": "vat_from_text",
        "อายุทศวรรษหน้า": "age_decade",
        "การ์ดชื่อ+อายุ": "name_age_card",
        "ราคารวม": "line_total",
        "ใบเสร็จ f-string": "fstring_receipt",
        "เงินทศนิยม 2 ตำแหน่ง": "money_2f",
        "ทอนเงิน": "change",
        "เปรียบเทียบคะแนน": "compare_scores",
        "แคชเชียร์มินิ (ยังไม่ใช้ if)": "mini_cashier",
        "โปรไฟล์สั้น": "mini_profile",
        "เปิด-ปิดตามชั่วโมง": "open_hours",
        "ผ่านเกณฑ์พิเศษ": "pass_60",
        "ที่นั่งคู่-คี่": "seat_parity",
        "แสตมป์หาร 5 ลงตัว": "div_by_5",
        "ราคาตั๋วตามอายุ": "ticket_age",
        "เกรดตัวอักษร": "letter_grade",
        "ขึ้นเครื่องเล่นได้ไหม": "ride_allowed",
        "ร้านเปิดวันพิเศษ": "weekend_open",
        "ผลรวม 1 ถึง n": "sum_to_n",
        "พหูคูณของ 3": "multiples_of_3",
        "รวมคะแนนในลิสต์": "sum_list",
        "นับที่ผ่าน": "count_pass",
        "นับถอยหลัง": "countdown",
        "ทายเลขจนถูก": "guess_until",
        "หยุดเมื่อเจอคำ quit": "break_quit",
        "ข้ามเลขติดลบ": "skip_negatives",
        "สี่เหลี่ยมดาว": "rect_stars",
        "ตารางคูณมุมเล็ก": "mini_mult_table",
        "for สร้างยอด แล้ว while ตรวจ": "for_then_while",
        "กรองด้วย continue": "filter_continue",
        "แก้ off-by-one": "fix_offbyone",
        "แก้ infinite while": "fix_infinite",
        "เฉลี่ย 3 วิชา + เกรด": "avg_grade",
        "ตะกร้า + ภาษี": "cart_vat",
    }
    return mapping.get(title, "exercise")


def main() -> None:
    # Late import of scaffold helper so regenerating homework keeps incomplete starters
    import importlib.util

    fix_path = Path(__file__).resolve().parent / "_fix_homework_starters.py"
    spec = importlib.util.spec_from_file_location("fix_hw", fix_path)
    fix_mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(fix_mod)

    data = content()
    data = content_rest(data)
    data = content_loops(data)

    # README homework
    write(
        HW / "README.md",
        """# Homework — Python Beginner (ถึง Midyear)

แบบฝึกบ้านหลังเรียนจบแต่ละบท **สัปดาห์ 001–024**

| โฟลเดอร์ | ความหมาย |
|---------|----------|
| `01.md` … `10.md` | โจทย์ง่าย–กลางเบา ทำเองที่บ้าน |
| `answer/` | เฉลยสำหรับตรวจคำตอบ |

## วิธีใช้

1. เรียนจบบทใน `slide/0xx-.../` แล้ว
2. เปิดโฟลเดอร์ homework ชื่อเดียวกัน
3. ทำข้อ 1 → 10 ตามลำดับ (Starter Code เป็นโครงว่าง — อย่าเปิดเฉลยก่อน)
4. เทียบเฉลยใน `answer/` หลังลองเองแล้ว

## กฎสำคัญ

ใช้ได้เฉพาะความรู้**ถึงบทนั้นและบทก่อนหน้า** — ยังไม่ใช้เรื่องที่ยังไม่เรียน
""",
    )

    for week in WEEKS:
        if week not in data:
            raise SystemExit(f"Missing content for {week}")
        info = data[week]
        topic = info["topic"]
        n1, n2 = info["medium_nums"]
        slide_week = SLIDE / week
        hw_week = HW / week
        (hw_week / "answer").mkdir(parents=True, exist_ok=True)
        (slide_week / "answer").mkdir(parents=True, exist_ok=True)

        for idx, m in enumerate(info["mediums"]):
            title, body, hint, starter, answer, io = m
            num = n1 if idx == 0 else n2
            letter = "A" if idx == 0 else "B"
            md = medium_md(topic, letter, title, body, hint, starter, io)
            write(slide_week / f"{num:02d}_medium.md", md)
            slug = slugify(title)
            write(slide_week / "answer" / answer_name(num, slug), answer if answer.endswith("\n") else answer + "\n")

        for i, h in enumerate(info["homeworks"], start=1):
            title, body, hint, answer = h[0], h[1], h[2], h[4]
            # Ignore packed full starters from data; always scaffold from answer
            answer_text = answer if answer.endswith("\n") else answer + "\n"
            starter = fix_mod.scaffold(answer_text)
            if starter.strip() == answer_text.strip():
                starter = "# เขียนโค้ดตรงนี้\n"
            io = h[5] if len(h) > 5 else ""
            write(hw_week / f"{i:02d}.md", hw_md(topic, i, title, body, hint, starter, io))
            write(hw_week / "answer" / f"{i:02d}.py", answer_text)

    print(f"Generated medium+homework for {len(WEEKS)} weeks")


if __name__ == "__main__":
    main()
