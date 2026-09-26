# -*- coding: utf-8 -*-
"""Generate gold-standard practice for weeks 037-048."""
from __future__ import annotations
import os, re, shutil

ROOT = os.path.join(os.path.dirname(__file__), "..", "slide")


def md(title, diff, body_scenario, conditions, inp, out, sample_in, sample_out, hint, starter):
    cond = ""
    if conditions:
        cond = "\n**เงื่อนไข:**\n\n" + "\n".join(f"- {c}" for c in conditions) + "\n"
    sample = "## ตัวอย่าง\n\n"
    if sample_in is not None:
        sample += f"**Input:**\n\n```text\n{sample_in}```\n\n"
    sample += f"**Output:**\n\n```text\n{sample_out}```\n"
    hint_block = ""
    if hint:
        hint_block = f"\n---\n\n## 💡 Hint\n\n{hint}\n"
    return f"""# {title}

**Difficulty:** {diff}

---

## โจทย์

{body_scenario}
{cond}
---

## Input

{inp}

## Output

{out}

---

{sample}
{hint_block}
---

## Starter Code

```python
{starter}
```
"""


def write_chapter(folder, chapter_title, scope_note, teacher_notes, problems, keep_lesson=True, extra_keep=None):
    d = os.path.join(ROOT, folder)
    adir = os.path.join(d, "answer")
    os.makedirs(adir, exist_ok=True)
    extra_keep = extra_keep or []

    # remove old practice md + answers (keep 01_* lessons and extra_keep)
    for f in os.listdir(d):
        if not f.endswith(".md"):
            continue
        if f == "00_index.md":
            os.remove(os.path.join(d, f))
            continue
        if re.match(r"01_", f):
            continue
        if f in extra_keep:
            continue
        if "_readiness" in f:
            continue
        if re.match(r"\d\d_", f):
            os.remove(os.path.join(d, f))
    if os.path.isdir(adir):
        for f in os.listdir(adir):
            os.remove(os.path.join(adir, f))

    rows = []
    for i, p in enumerate(problems, 1):
        fname, aname, title, diff, axis = p["file"], p["answer"], p["title"], p["diff"], p["axis"]
        path = os.path.join(d, fname)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(md(
                p["title"], p["diff"], p["scenario"], p.get("conditions"),
                p["input_desc"], p["output_desc"],
                p.get("sample_in"), p["sample_out"],
                p.get("hint"), p["starter"],
            ))
        with open(os.path.join(adir, aname), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(p["code"].rstrip() + "\n")
        emoji = {"🟢 Easy": "🟢", "🟡 Medium": "🟡", "🔴 Challenge": "🔴"}[diff]
        short = title.split(":", 1)[-1].strip() if ":" in title else title
        rows.append((i, fname, emoji, short, axis))

    # index
    lines = [
        f"# 📋 สารบัญโจทย์ — {chapter_title}",
        "",
        scope_note,
        "",
        "---",
        "",
        "## ลำดับที่แนะนำ",
        "",
        "| # | ไฟล์ | ระดับ | โจทย์ | แกนการคิด |",
        "|---|------|-------|-------|-----------|",
    ]
    for i, fname, emoji, short, axis in rows:
        lines.append(f"| {i} | `{fname}` | {emoji} | {short} | {axis} |")
    lines += [
        "",
        "**สรุป:** 🟢 Easy 5 ข้อ · 🟡 Medium 6 ข้อ · 🔴 Challenge 4 ข้อ = **15 ข้อ**",
        "",
        "---",
        "",
        "## หมายเหตุสำหรับครู",
        "",
    ]
    for n in teacher_notes:
        lines.append(f"- {n}")
    lines.append("")
    with open(os.path.join(d, "00_index.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


# ═══════════════════════════════════════════════════════════════════
# 037 — functions: NO params, print only, NO return
# ═══════════════════════════════════════════════════════════════════
P037 = [
dict(
    file="02_test.md", answer="02_shop_hours.py",
    title="🏪 ฟังก์ชัน — ข้อ 1: ป้ายเวลาเปิดร้าน",
    diff="🟢 Easy", axis="def ไม่รับพารามิเตอร์ + เรียกหลายครั้ง",
    scenario="ร้านขายขนมเปิด 08:00–17:00 ครูอยากให้เด็กเขียนฟังก์ชันแสดงป้ายเวลาเปิดร้าน\n\nสร้างฟังก์ชัน `show_hours()` ที่พิมพ์ป้าย 2 บรรทัด แล้วเรียกใช้ 2 ครั้ง",
    conditions=["พิมพ์ `Open: 08:00 - 17:00`", "พิมพ์ `Welcome to Snack Shop`", "เรียกฟังก์ชัน 2 ครั้ง"],
    input_desc="ไม่มี (โปรแกรมนี้ไม่รับค่าจากผู้ใช้)",
    output_desc="ป้าย 2 บรรทัด × 2 ครั้ง รวม 4 บรรทัด",
    sample_in=None,
    sample_out="Open: 08:00 - 17:00\nWelcome to Snack Shop\nOpen: 08:00 - 17:00\nWelcome to Snack Shop\n",
    hint=None,
    starter="# สร้าง show_hours()\n\n# เรียก 2 ครั้ง\n",
    code='''def show_hours():
    print("Open: 08:00 - 17:00")
    print("Welcome to Snack Shop")

show_hours()
show_hours()
''',
),
dict(
    file="03_test.md", answer="03_bell.py",
    title="🔔 ฟังก์ชัน — ข้อ 2: กริ่งโรงเรียน",
    diff="🟢 Easy", axis="ฟังก์ชันพิมพ์หลายบรรทัด",
    scenario="ตอนพักกลางวัน ระบบเสียงประกาศข้อความเดิมทุกวัน\n\nสร้างฟังก์ชัน `ring_bell()` ที่พิมพ์ข้อความประกาศ แล้วเรียก 1 ครั้ง",
    conditions=["พิมพ์ `Break time!`", "พิมพ์ `Please go to the cafeteria.`"],
    input_desc="ไม่มี",
    output_desc="2 บรรทัด",
    sample_in=None,
    sample_out="Break time!\nPlease go to the cafeteria.\n",
    hint=None,
    starter="# สร้าง ring_bell()\n\n# เรียกใช้\n",
    code='''def ring_bell():
    print("Break time!")
    print("Please go to the cafeteria.")

ring_bell()
''',
),
dict(
    file="04_test.md", answer="04_separator.py",
    title="➖ ฟังก์ชัน — ข้อ 3: เส้นคั่นรายงาน",
    diff="🟢 Easy", axis="ฟังก์ชันช่วยพิมพ์เส้นคั่นซ้ำ",
    scenario="ตอนพิมพ์ใบรายงาน อยากมีเส้นคั่นสวยๆ ระหว่างหัวข้อ\n\nสร้างฟังก์ชัน `line()` ที่พิมพ์เส้น `==========` แล้วใช้คั่นข้อความตามตัวอย่าง",
    conditions=["มีฟังก์ชัน `line()`", "เรียก `line()` ทั้งก่อนและหลังหัวข้อ"],
    input_desc="ไม่มี",
    output_desc="3 บรรทัด",
    sample_in=None,
    sample_out="==========\nWeekly Report\n==========\n",
    hint=None,
    starter="# สร้าง line()\n\n# พิมพ์รายงานโดยเรียก line()\n",
    code='''def line():
    print("==========")

line()
print("Weekly Report")
line()
''',
),
dict(
    file="05_easy.md", answer="05_weather.py",
    title="🌤️ ฟังก์ชัน — ข้อ 4: พยากรณ์อากาศวันนี้",
    diff="🟢 Easy", axis="ฟังก์ชันแสดงข้อมูลคงที่",
    scenario="ป้าย LED หน้าโรงเรียนแสดงอากาศทุกเช้าด้วยค่าคงที่\n\nสร้างฟังก์ชัน `show_weather()` ที่พิมพ์อุณหภูมิและความชื้นตามตัวอย่าง แล้วเรียก 1 ครั้ง",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="2 บรรทัด",
    sample_in=None,
    sample_out="Temp: 32 C\nHumidity: 70%\n",
    hint=None,
    starter="# สร้าง show_weather()\n\n# เรียกใช้\n",
    code='''def show_weather():
    print("Temp: 32 C")
    print("Humidity: 70%")

show_weather()
''',
),
dict(
    file="06_easy.md", answer="06_rules.py",
    title="📜 ฟังก์ชัน — ข้อ 5: กติกาห้องคอม",
    diff="🟢 Easy", axis="ฟังก์ชันพิมพ์รายการสั้นๆ",
    scenario="ครูติดกติกาห้องคอมพิวเตอร์ไว้หน้าจอตอนเปิดเครื่อง\n\nสร้างฟังก์ชัน `show_rules()` ที่พิมพ์กติกา 3 ข้อ แล้วเรียก 1 ครั้ง",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="3 บรรทัด",
    sample_in=None,
    sample_out="1. No food\n2. Speak softly\n3. Push in chairs\n",
    hint=None,
    starter="# สร้าง show_rules()\n\n# เรียกใช้\n",
    code='''def show_rules():
    print("1. No food")
    print("2. Speak softly")
    print("3. Push in chairs")

show_rules()
''',
),
dict(
    file="07_medium.md", answer="07_menu.py",
    title="🎮 ฟังก์ชัน — ข้อ 6: เมนูเกม",
    diff="🟡 Medium", axis="ฟังก์ชัน + เรียกซ้ำด้วย for",
    scenario="เกมเปิดหน้าเมนูทุกครั้งที่เริ่มด่าน\n\nสร้างฟังก์ชัน `show_menu()` ที่พิมพ์เมนู 3 บรรทัด แล้วเรียกด้วย `for` ให้แสดง 2 รอบ",
    conditions=["ใช้ `for` ร่วมกับเรียกฟังก์ชัน", "ห้ามคัดลอก `print` เมนูซ้ำเองนอกฟังก์ชัน"],
    input_desc="ไม่มี",
    output_desc="เมนู 3 บรรทัด × 2 รอบ",
    sample_in=None,
    sample_out="1) Start\n2) Load\n3) Quit\n1) Start\n2) Load\n3) Quit\n",
    hint="สร้างฟังก์ชันก่อน แล้วค่อย `for i in range(2):` เรียกฟังก์ชันข้างใน",
    starter="# สร้าง show_menu()\n\n# เรียก 2 ครั้งด้วย for\n",
    code='''def show_menu():
    print("1) Start")
    print("2) Load")
    print("3) Quit")

for i in range(2):
    show_menu()
''',
),
dict(
    file="08_medium.md", answer="08_countdown.py",
    title="🚀 ฟังก์ชัน — ข้อ 7: นับถอยหลังปล่อยจรวด",
    diff="🟡 Medium", axis="for อยู่ภายในฟังก์ชัน",
    scenario="ชมรมวิทยาศาสตร์จำลองการปล่อยจรวด\n\nสร้างฟังก์ชัน `countdown()` ที่นับจาก 5 ถึง 1 แล้วพิมพ์ `Liftoff!`",
    conditions=["ใช้ `for` กับ `range` ภายในฟังก์ชัน", "เรียกฟังก์ชัน 1 ครั้ง"],
    input_desc="ไม่มี",
    output_desc="ตัวเลข 5 บรรทัด แล้วตามด้วย Liftoff!",
    sample_in=None,
    sample_out="5\n4\n3\n2\n1\nLiftoff!\n",
    hint="ใช้ `for i in range(5, 0, -1)` ยังไม่สอน — ใช้ `range(5)` แล้วคำนวณเลขจาก 5 ลงมาแทน",
    starter="# สร้าง countdown()\n\n# เรียกใช้\n",
    code='''def countdown():
    for i in range(5):
        print(5 - i)
    print("Liftoff!")

countdown()
''',
),
dict(
    file="09_medium.md", answer="09_receipt_header.py",
    title="🧾 ฟังก์ชัน — ข้อ 8: หัวบิลร้านกาแฟ",
    diff="🟡 Medium", axis="หลายฟังก์ชันทำงานร่วมกัน",
    scenario="ร้านกาแฟพิมพ์หัวบิลและท้ายบิลแยกฟังก์ชัน\n\nสร้าง `print_header()` และ `print_footer()` แล้วเรียกตามลำดับ พร้อมพิมพ์รายการกลางบิล 1 บรรทัด",
    conditions=["มีอย่างน้อย 2 ฟังก์ชัน", "กลางบิลพิมพ์ `Item: Latte`"],
    input_desc="ไม่มี",
    output_desc="หัวบิล + รายการ + ท้ายบิล",
    sample_in=None,
    sample_out="=== COFFEE SHOP ===\nItem: Latte\n=== THANK YOU ===\n",
    hint="แยกหัวกับท้ายเป็นคนละฟังก์ชัน จะได้เรียกซ้ำตอนทำบิลจริงได้",
    starter="# สร้าง print_header() และ print_footer()\n\n# เรียกใช้ตามลำดับ\n",
    code='''def print_header():
    print("=== COFFEE SHOP ===")

def print_footer():
    print("=== THANK YOU ===")

print_header()
print("Item: Latte")
print_footer()
''',
),
dict(
    file="10_medium.md", answer="10_temp_board.py",
    title="🌡️ ฟังก์ชัน — ข้อ 9: แปลงอุณหภูมิบนป้าย",
    diff="🟡 Medium", axis="คำนวณค่าคงที่ในฟังก์ชันแล้วพิมพ์",
    scenario="ป้ายท่องเที่ยวแสดงอุณหภูมิทั้งองศา C และ F จากค่าคงที่ 30°C\n\nสร้างฟังก์ชัน `show_temp()` คำนวณ F = C * 9 / 5 + 32 แล้วพิมพ์ทั้งสองค่า (ใช้ค่า C = 30 ในฟังก์ชัน)",
    conditions=["ห้ามรับพารามิเตอร์", "พิมพ์ทั้ง C และ F"],
    input_desc="ไม่มี",
    output_desc="2 บรรทัด",
    sample_in=None,
    sample_out="C: 30\nF: 86.0\n",
    hint="เก็บค่า C ไว้ในตัวแปรภายในฟังก์ชัน แล้วคำนวณ F จากสูตร",
    starter="# สร้าง show_temp()\n\n# เรียกใช้\n",
    code='''def show_temp():
    c = 30
    f = c * 9 / 5 + 32
    print(f"C: {c}")
    print(f"F: {f}")

show_temp()
''',
),
dict(
    file="11_medium.md", answer="11_ask_name.py",
    title="👋 ฟังก์ชัน — ข้อ 10: เคาน์เตอร์ต้อนรับ",
    diff="🟡 Medium", axis="input อยู่ภายในฟังก์ชัน (ยังไม่มีพารามิเตอร์)",
    scenario="เคาน์เตอร์ต้อนรับถามชื่อแล้วทักทาย\n\nสร้างฟังก์ชัน `welcome()` ที่รับชื่อด้วย `input()` แล้วพิมพ์คำทักทาย เรียกฟังก์ชัน 2 ครั้ง",
    conditions=["`input()` อยู่ภายในฟังก์ชัน", "เรียก 2 ครั้ง"],
    input_desc="ชื่อ 2 บรรทัด (ครั้งละ 1 ชื่อต่อหนึ่งครั้งที่เรียกฟังก์ชัน)",
    output_desc="คำทักทาย 2 บรรทัด",
    sample_in="Mina\nPom\n",
    sample_out="Welcome, Mina!\nWelcome, Pom!\n",
    hint="ฟังก์ชันยังไม่รับพารามิเตอร์ แต่เรียก input() ข้างในได้",
    starter="# สร้าง welcome()\n\n# เรียก 2 ครั้ง\n",
    code='''def welcome():
    name = input()
    print(f"Welcome, {name}!")

welcome()
welcome()
''',
),
dict(
    file="12_medium.md", answer="12_scoreboard.py",
    title="🏆 ฟังก์ชัน — ข้อ 11: กระดานคะแนน",
    diff="🟡 Medium", axis="ฟังก์ชัน + ลูปรับคะแนนแล้วสรุป",
    scenario="กรรมการกีฬาต้องพิมพ์คะแนนผู้เล่น 3 คน แล้วสรุป\n\nสร้างฟังก์ชัน `show_scores()` ที่รับคะแนน 3 ค่า พิมพ์แต่ละคน แล้วพิมพ์ผลรวม",
    conditions=["ใช้ลูปหรือรับ input 3 ครั้งภายในฟังก์ชัน", "พิมพ์ Total ท้ายสุด"],
    input_desc="คะแนนจำนวนเต็ม 3 บรรทัด",
    output_desc="คะแนนรายคน 3 บรรทัด + Total 1 บรรทัด",
    sample_in="10\n15\n20\n",
    sample_out="Player: 10\nPlayer: 15\nPlayer: 20\nTotal: 45\n",
    hint="สะสมผลรวมไว้ในตัวแปรภายในฟังก์ชันขณะวนรับค่า",
    starter="# สร้าง show_scores()\n\n# เรียกใช้\n",
    code='''def show_scores():
    total = 0
    for i in range(3):
        score = int(input())
        print(f"Player: {score}")
        total = total + score
    print(f"Total: {total}")

show_scores()
''',
),
dict(
    file="13_challenge.md", answer="13_snack_shop.py",
    title="🍪 ฟังก์ชัน — ข้อ 12: ร้านขายขนมในโรงเรียน",
    diff="🔴 Challenge", axis="หลายฟังก์ชัน + คำนวณบิล",
    scenario="ร้านขนมในโรงเรียนคิดเงินด้วยฟังก์ชันแยกส่วน\n\nสร้าง `show_title()` พิมพ์ชื่อร้าน และ `calc_bill()` รับราคาต่อชิ้นกับจำนวน แล้วพิมพ์ยอดรวม เรียกทั้งสองตามลำดับ",
    conditions=["มีอย่างน้อย 2 ฟังก์ชัน", "ยอดรวม = ราคา × จำนวน"],
    input_desc="ราคา (จำนวนจริง) 1 บรรทัด และจำนวนชิ้น (จำนวนเต็ม) 1 บรรทัด",
    output_desc="ชื่อร้าน + รายละเอียดบิล",
    sample_in="15.0\n3\n",
    sample_out="Snack Shop\nPrice: 15.0\nQty: 3\nTotal: 45.0\n",
    hint="แยกส่วนที่แค่พิมพ์ข้อความ กับส่วนที่ต้องคำนวณออกจากกัน",
    starter="# สร้าง show_title() และ calc_bill()\n\n# เรียกตามลำดับ\n",
    code='''def show_title():
    print("Snack Shop")

def calc_bill():
    price = float(input())
    qty = int(input())
    total = price * qty
    print(f"Price: {price}")
    print(f"Qty: {qty}")
    print(f"Total: {total}")

show_title()
calc_bill()
''',
),
dict(
    file="14_challenge.md", answer="14_school_day.py",
    title="🏫 ฟังก์ชัน — ข้อ 13: วันหนึ่งที่โรงเรียน",
    diff="🔴 Challenge", axis="ลำดับเรียกหลายฟังก์ชันเล่าเรื่อง",
    scenario="ต้องการจำลองหนึ่งวันเรียนด้วยฟังก์ชันย่อย\n\nสร้าง `morning()`, `class_time()`, `goodbye()` แล้วเรียกตามลำดับให้ได้ข้อความตามตัวอย่าง",
    conditions=["มี 3 ฟังก์ชัน", "ห้ามรวมข้อความทั้งหมดไว้ในฟังก์ชันเดียว"],
    input_desc="ไม่มี",
    output_desc="4 บรรทัดตามลำดับวัน",
    sample_in=None,
    sample_out="Good morning!\nMath class starts\nScience class starts\nSee you tomorrow!\n",
    hint="แต่ละช่วงวันเป็นคนละฟังก์ชัน แล้วเรียกเรียงลำดับในโปรแกรมหลัก",
    starter="# สร้าง morning(), class_time(), goodbye()\n\n# เรียกตามลำดับ\n",
    code='''def morning():
    print("Good morning!")

def class_time():
    print("Math class starts")
    print("Science class starts")

def goodbye():
    print("See you tomorrow!")

morning()
class_time()
goodbye()
''',
),
dict(
    file="15_challenge.md", answer="15_library_slip.py",
    title="📚 ฟังก์ชัน — ข้อ 14: สลิปยืมหนังสือ",
    diff="🔴 Challenge", axis="ฟังก์ชันรับ input + จัดรูปแบบกล่อง",
    scenario="ห้องสมุดพิมพ์สลิปยืมหนังสือเป็นกล่องข้อความ\n\nสร้างฟังก์ชัน `print_slip()` รับชื่อหนังสือและจำนวนวัน แล้วพิมพ์สลิปตามตัวอย่าง",
    conditions=["ใช้เส้น `====================` บนและล่าง", "เรียกฟังก์ชัน 1 ครั้ง"],
    input_desc="ชื่อหนังสือ 1 บรรทัด และจำนวนวัน (จำนวนเต็ม) 1 บรรทัด",
    output_desc="กล่องสลิป",
    sample_in="Python Basics\n7\n",
    sample_out="====================\nBook : Python Basics\nDays : 7\n====================\n",
    hint="จัดช่องว่างหลังเครื่องหมาย : ให้ตรงกันตามตัวอย่าง",
    starter="# สร้าง print_slip()\n\n# เรียกใช้\n",
    code='''def print_slip():
    book = input()
    days = int(input())
    print("====================")
    print(f"Book : {book}")
    print(f"Days : {days}")
    print("====================")

print_slip()
''',
),
dict(
    file="16_challenge.md", answer="16_vending.py",
    title="🥤 ฟังก์ชัน — ข้อ 15: ตู้กดน้ำโรงเรียน",
    diff="🔴 Challenge", axis="ฟังก์ชัน + if เลือกเมนูจาก input",
    scenario="ตู้กดน้ำมี 2 เมนู คิดเงินในฟังก์ชันเดียว\n\nสร้าง `order_drink()` รับรหัสเมนู (`1` หรือ `2`) และเงินที่ใส่ แล้วพิมพ์ชื่อเครื่องดื่มกับเงินทอน",
    conditions=["เมนู 1 = Water ราคา 10", "เมนู 2 = Juice ราคา 20", "เงินทอน = เงินที่ใส่ - ราคา"],
    input_desc="รหัสเมนู 1 บรรทัด และเงินที่ใส่ (จำนวนเต็ม) 1 บรรทัด",
    output_desc="ชื่อเครื่องดื่มและเงินทอน",
    sample_in="2\n50\n",
    sample_out="Drink: Juice\nChange: 30\n",
    hint="ใช้ if/else เลือกราคาจากรหัสเมนู แล้วค่อยคำนวณเงินทอน",
    starter="# สร้าง order_drink()\n\n# เรียกใช้\n",
    code='''def order_drink():
    menu = int(input())
    paid = int(input())
    if menu == 1:
        name = "Water"
        price = 10
    else:
        name = "Juice"
        price = 20
    print(f"Drink: {name}")
    print(f"Change: {paid - price}")

order_drink()
''',
),
]


# ═══════════════════════════════════════════════════════════════════
# 038 — parameters: params OK, print not return, no defaults/kwargs
# ═══════════════════════════════════════════════════════════════════
P038 = [
dict(
    file="02_test.md", answer="02_greet_name.py",
    title="👋 พารามิเตอร์ — ข้อ 1: ทักทายด้วยชื่อ",
    diff="🟢 Easy", axis="พารามิเตอร์ 1 ตัว",
    scenario="ต้องการฟังก์ชันทักทายที่รับชื่อแล้วพิมพ์คำทัก\n\nสร้าง `greet(name)` แล้วเรียกกับชื่อจาก input 1 ครั้ง",
    conditions=["ห้ามใช้ `return`", "พิมพ์ `Hello, <name>!`"],
    input_desc="ชื่อ 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="Alice\n",
    sample_out="Hello, Alice!\n",
    hint=None,
    starter="name = input()\n\n# สร้าง greet(name) แล้วเรียก\n",
    code='''def greet(name):
    print(f"Hello, {name}!")

name = input()
greet(name)
''',
),
dict(
    file="03_test.md", answer="03_add_print.py",
    title="➕ พารามิเตอร์ — ข้อ 2: บวกแล้วพิมพ์",
    diff="🟢 Easy", axis="พารามิเตอร์ 2 ตัว คำนวณแล้วพิมพ์",
    scenario="เครื่องคิดเลขแบบง่ายที่ยังไม่ต้องเก็บผลลัพธ์\n\nสร้าง `add(a, b)` ที่พิมพ์ผลบวก แล้วเรียกด้วยเลข 2 ค่าจาก input",
    conditions=["ห้ามใช้ `return`"],
    input_desc="จำนวนเต็ม 2 บรรทัด",
    output_desc="ผลบวก 1 บรรทัด",
    sample_in="3\n5\n",
    sample_out="8\n",
    hint=None,
    starter="a = int(input())\nb = int(input())\n\n# สร้าง add(a, b) แล้วเรียก\n",
    code='''def add(a, b):
    print(a + b)

a = int(input())
b = int(input())
add(a, b)
''',
),
dict(
    file="04_test.md", answer="04_show_price.py",
    title="🏷️ พารามิเตอร์ — ข้อ 3: ป้ายราคาสินค้า",
    diff="🟢 Easy", axis="พารามิเตอร์คนละชนิด",
    scenario="ชั้นวางสินค้าแสดงชื่อกับราคา\n\nสร้าง `show_price(item, price)` แล้วเรียกด้วยค่าจาก input",
    conditions=None,
    input_desc="ชื่อสินค้า 1 บรรทัด และราคา (จำนวนเต็ม) 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="Pencil\n12\n",
    sample_out="Pencil costs 12 baht\n",
    hint=None,
    starter="item = input()\nprice = int(input())\n\n# สร้าง show_price(item, price) แล้วเรียก\n",
    code='''def show_price(item, price):
    print(f"{item} costs {price} baht")

item = input()
price = int(input())
show_price(item, price)
''',
),
dict(
    file="05_easy.md", answer="05_rect.py",
    title="📐 พารามิเตอร์ — ข้อ 4: พื้นที่สี่เหลี่ยม",
    diff="🟢 Easy", axis="คำนวณจากพารามิเตอร์แล้วพิมพ์",
    scenario="ครูให้นักเรียนหาพื้นที่สนามสี่เหลี่ยม\n\nสร้าง `show_area(width, height)` พิมพ์พื้นที่ = กว้าง × สูง",
    conditions=["ห้ามใช้ `return`"],
    input_desc="ความกว้างและความสูง เป็นจำนวนเต็มอย่างละ 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="4\n6\n",
    sample_out="Area: 24\n",
    hint=None,
    starter="width = int(input())\nheight = int(input())\n\n# สร้าง show_area(width, height) แล้วเรียก\n",
    code='''def show_area(width, height):
    print(f"Area: {width * height}")

width = int(input())
height = int(input())
show_area(width, height)
''',
),
dict(
    file="06_easy.md", answer="06_describe.py",
    title="🧍 พารามิเตอร์ — ข้อ 5: แนะนำตัว",
    diff="🟢 Easy", axis="พารามิเตอร์ 2 ตัวใน f-string",
    scenario="แอปโปรไฟล์แสดงชื่อกับอายุ\n\nสร้าง `describe(name, age)` แล้วเรียกด้วยค่าจาก input",
    conditions=["ห้ามซ้ำตัวอย่างบทเรียนแบบ hard-code Alice/Bob"],
    input_desc="ชื่อ 1 บรรทัด และอายุ (จำนวนเต็ม) 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="Mali\n14\n",
    sample_out="Mali is 14 years old.\n",
    hint=None,
    starter="name = input()\nage = int(input())\n\n# สร้าง describe(name, age) แล้วเรียก\n",
    code='''def describe(name, age):
    print(f"{name} is {age} years old.")

name = input()
age = int(input())
describe(name, age)
''',
),
dict(
    file="07_medium.md", answer="07_vote.py",
    title="🗳️ พารามิเตอร์ — ข้อ 6: ตรวจสิทธิ์เลือกตั้งชมรม",
    diff="🟡 Medium", axis="พารามิเตอร์ + if/else",
    scenario="ชมรมนักเรียนให้สิทธิ์โหวตเมื่ออายุถึง 15\n\nสร้าง `check_vote(age)` พิมพ์ `Can vote` หรือ `Too young`",
    conditions=["อายุ `>= 15` → Can vote", "น้อยกว่า → Too young"],
    input_desc="อายุจำนวนเต็ม 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="16\n",
    sample_out="Can vote\n",
    hint="ส่งอายุเข้าฟังก์ชัน แล้วใช้ if/else ข้างใน",
    starter="age = int(input())\n\n# สร้าง check_vote(age) แล้วเรียก\n",
    code='''def check_vote(age):
    if age >= 15:
        print("Can vote")
    else:
        print("Too young")

age = int(input())
check_vote(age)
''',
),
dict(
    file="08_medium.md", answer="08_bill.py",
    title="🍽️ พารามิเตอร์ — ข้อ 7: บิลร้านอาหาร",
    diff="🟡 Medium", axis="พารามิเตอร์หลายตัว + คำนวณ",
    scenario="ร้านอาหารคิดเงินจากราคาอาหารและค่าบริการ\n\nสร้าง `show_total(food, service)` พิมพ์ยอดรวม food + service",
    conditions=None,
    input_desc="ราคาอาหารและค่าบริการ เป็นจำนวนเต็มอย่างละ 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="120\n20\n",
    sample_out="Total: 140\n",
    hint="คำนวณในฟังก์ชันแล้วพิมพ์ผล รวมทั้งป้าย Total",
    starter="food = int(input())\nservice = int(input())\n\n# สร้าง show_total(food, service) แล้วเรียก\n",
    code='''def show_total(food, service):
    print(f"Total: {food + service}")

food = int(input())
service = int(input())
show_total(food, service)
''',
),
dict(
    file="09_medium.md", answer="09_discount.py",
    title="💸 พารามิเตอร์ — ข้อ 8: วันลดราคา",
    diff="🟡 Medium", axis="คำนวณส่วนลดจากพารามิเตอร์",
    scenario="ร้านเสื้อผ้าลดราคาตามจำนวนบาทที่กำหนด\n\nสร้าง `show_sale(price, discount)` พิมพ์ราคาสุทธิ = ราคา − ส่วนลด",
    conditions=["ส่วนลดไม่เกินราคา (โจทย์รับประกัน)"],
    input_desc="ราคาและส่วนลด เป็นจำนวนเต็มอย่างละ 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="500\n80\n",
    sample_out="Pay: 420\n",
    hint="ลบส่วนลดออกจากราคาภายในฟังก์ชัน",
    starter="price = int(input())\ndiscount = int(input())\n\n# สร้าง show_sale(price, discount) แล้วเรียก\n",
    code='''def show_sale(price, discount):
    print(f"Pay: {price - discount}")

price = int(input())
discount = int(input())
show_sale(price, discount)
''',
),
dict(
    file="10_medium.md", answer="10_bmi_card.py",
    title="💪 พารามิเตอร์ — ข้อ 9: บัตรสุขภาพในคลาสพละ",
    diff="🟡 Medium", axis="สูตรคำนวณ + จัดรูปแบบทศนิยม",
    scenario="ครูพละคำนวณค่า BMI แล้วพิมพ์บนบัตรสุขภาพ\n\nสร้าง `show_bmi(weight, height)` คำนวณ weight / (height ** 2) แล้วพิมพ์ทศนิยม 1 ตำแหน่ง\n\n(ต่างจากตัวอย่างบทเรียน — ครั้งนี้รับค่าจาก input และมีป้าย Card)",
    conditions=["พิมพ์บรรทัด `BMI Card`", "พิมพ์ `BMI: x.x`"],
    input_desc="น้ำหนัก (กก.) และส่วนสูง (เมตร) เป็นจำนวนจริงอย่างละ 1 บรรทัด",
    output_desc="2 บรรทัด",
    sample_in="60\n1.70\n",
    sample_out="BMI Card\nBMI: 20.8\n",
    hint="ใช้ `:.1f` ใน f-string เหมือนบทเรียน",
    starter="weight = float(input())\nheight = float(input())\n\n# สร้าง show_bmi(weight, height) แล้วเรียก\n",
    code='''def show_bmi(weight, height):
    bmi = weight / (height ** 2)
    print("BMI Card")
    print(f"BMI: {bmi:.1f}")

weight = float(input())
height = float(input())
show_bmi(weight, height)
''',
),
dict(
    file="11_medium.md", answer="11_older.py",
    title="🎂 พารามิเตอร์ — ข้อ 10: ใครอายุมากกว่า",
    diff="🟡 Medium", axis="เทียบสองพารามิเตอร์",
    scenario="เพื่อนสองคนอยากรู้ว่าใครอายุมากกว่า\n\nสร้าง `show_older(a, b)` พิมพ์อายุที่มากกว่า (ถ้าเท่ากันพิมพ์ค่านั้น)",
    conditions=None,
    input_desc="อายุจำนวนเต็ม 2 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="14\n16\n",
    sample_out="Older: 16\n",
    hint="ใช้ if/else เทียบ a กับ b ในฟังก์ชัน",
    starter="a = int(input())\nb = int(input())\n\n# สร้าง show_older(a, b) แล้วเรียก\n",
    code='''def show_older(a, b):
    if a >= b:
        print(f"Older: {a}")
    else:
        print(f"Older: {b}")

a = int(input())
b = int(input())
show_older(a, b)
''',
),
dict(
    file="12_medium.md", answer="12_c_to_f.py",
    title="🌡️ พารามิเตอร์ — ข้อ 11: แปลงอุณหภูมิท่องเที่ยว",
    diff="🟡 Medium", axis="พารามิเตอร์เดียว + สูตรแปลง",
    scenario="แอปท่องเที่ยวแปลงองศา C เป็น F\n\nสร้าง `show_f(c)` พิมพ์ค่า F = c * 9 / 5 + 32",
    conditions=None,
    input_desc="อุณหภูมิ C เป็นจำนวนจริง 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="25\n",
    sample_out="F: 77.0\n",
    hint="คำนวณในฟังก์ชันแล้วพิมพ์พร้อมป้าย F:",
    starter="c = float(input())\n\n# สร้าง show_f(c) แล้วเรียก\n",
    code='''def show_f(c):
    f = c * 9 / 5 + 32
    print(f"F: {f}")

c = float(input())
show_f(c)
''',
),
dict(
    file="13_challenge.md", answer="13_login.py",
    title="🔐 พารามิเตอร์ — ข้อ 12: Login เข้าเกม",
    diff="🔴 Challenge", axis="เทียบข้อความสองพารามิเตอร์",
    scenario="เกมตรวจรหัสผ่านตอนเข้าเล่น\n\nสร้าง `login(user, password)` ถ้า user เป็น `admin` และ password เป็น `1234` พิมพ์ `Access granted` ไม่งั้น `Access denied`",
    conditions=["ใช้ `and`", "ห้ามใช้ `return`"],
    input_desc="username 1 บรรทัด และ password 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="admin\n1234\n",
    sample_out="Access granted\n",
    hint="เปรียบเทียบทั้งสองค่าในเงื่อนไขเดียวด้วย and",
    starter="user = input()\npassword = input()\n\n# สร้าง login(user, password) แล้วเรียก\n",
    code='''def login(user, password):
    if user == "admin" and password == "1234":
        print("Access granted")
    else:
        print("Access denied")

user = input()
password = input()
login(user, password)
''',
),
dict(
    file="14_challenge.md", answer="14_movie.py",
    title="🎬 พารามิเตอร์ — ข้อ 13: ตู้ขายตั๋วหนัง",
    diff="🔴 Challenge", axis="หลายเงื่อนไขจากพารามิเตอร์",
    scenario="ตู้ขายตั๋วคิดราคาตามอายุ\n\nสร้าง `ticket(age)` — อายุ `< 12` ราคา 80, อายุ `>= 60` ราคา 90, อื่นๆ 120 แล้วพิมพ์ราคา",
    conditions=["ใช้ if / elif / else"],
    input_desc="อายุจำนวนเต็ม 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="10\n",
    sample_out="Price: 80\n",
    hint="เรียงเงื่อนไขเด็กก่อน ผู้สูงอายุ แล้วค่อยราคาปกติ",
    starter="age = int(input())\n\n# สร้าง ticket(age) แล้วเรียก\n",
    code='''def ticket(age):
    if age < 12:
        price = 80
    elif age >= 60:
        price = 90
    else:
        price = 120
    print(f"Price: {price}")

age = int(input())
ticket(age)
''',
),
dict(
    file="15_challenge.md", answer="15_cart.py",
    title="🛒 พารามิเตอร์ — ข้อ 14: รายการในตะกร้า",
    diff="🔴 Challenge", axis="พารามิเตอร์ 3 ตัว + จัดรูปแบบ",
    scenario="แอปช้อปปิ้งพิมพ์รายการสินค้าหนึ่งบรรทัดในตะกร้า\n\nสร้าง `show_item(name, qty, price)` พิมพ์ชื่อ จำนวน และราคารวม (qty * price) ตามตัวอย่าง",
    conditions=None,
    input_desc="ชื่อ 1 บรรทัด, จำนวน 1 บรรทัด, ราคาต่อชิ้น 1 บรรทัด (จำนวนเต็ม)",
    output_desc="กล่องสรุปรายการ",
    sample_in="Book\n2\n50\n",
    sample_out="====================\nItem  : Book\nQty   : 2\nTotal : 100\n====================\n",
    hint="คำนวณยอดรวมในฟังก์ชัน แล้วจัดคอลัมน์ : ให้ตรงกัน",
    starter="name = input()\nqty = int(input())\nprice = int(input())\n\n# สร้าง show_item(name, qty, price) แล้วเรียก\n",
    code='''def show_item(name, qty, price):
    total = qty * price
    print("====================")
    print(f"Item  : {name}")
    print(f"Qty   : {qty}")
    print(f"Total : {total}")
    print("====================")

name = input()
qty = int(input())
price = int(input())
show_item(name, qty, price)
''',
),
dict(
    file="16_challenge.md", answer="16_shipping.py",
    title="📦 พารามิเตอร์ — ข้อ 15: ค่าส่งพัสดุ",
    diff="🔴 Challenge", axis="คำนวณก่อนเทียบในฟังก์ชัน",
    scenario="ร้านออนไลน์คิดค่าส่งตามน้ำหนัก\n\nสร้าง `show_shipping(weight)` — ถ้าน้ำหนัก `<= 1` ค่าส่ง 30, ถ้า `<= 5` ค่าส่ง 50, มากกว่านั้น 80",
    conditions=["น้ำหนักเป็นจำนวนจริง", "พิมพ์ค่าส่งเป็นจำนวนเต็ม"],
    input_desc="น้ำหนัก 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="3.5\n",
    sample_out="Shipping: 50\n",
    hint="ใช้ elif ไล่ช่วงน้ำหนักจากน้อยไปมาก",
    starter="weight = float(input())\n\n# สร้าง show_shipping(weight) แล้วเรียก\n",
    code='''def show_shipping(weight):
    if weight <= 1:
        fee = 30
    elif weight <= 5:
        fee = 50
    else:
        fee = 80
    print(f"Shipping: {fee}")

weight = float(input())
show_shipping(weight)
''',
),
]

# continued in _gen_039_048_data.py
from _gen_039_048_data import P039, P040, P041, P042, P043, P044, P045, P046, P047, P048


def main():
    write_chapter(
        "037-functions",
        "บท 037 ฟังก์ชัน (ยังไม่มีพารามิเตอร์ / return)",
        "**ขอบเขตของบทนี้:** ทุกอย่างถึงบท 036 + **`def name():` ไม่มีพารามิเตอร์** + เรียกฟังก์ชัน\n\n"
        "> ❌ ยังไม่มีพารามิเตอร์ (บท 038) · ยังไม่มี `return` (บท 039) · ยังไม่มี `global` (บท 041)",
        [
            "ข้อ `02` ไม่ซ้ำตัวอย่างบทเรียน (`greet()` พิมพ์ Hello!)",
            "ทุกฟังก์ชันในบทนี้ **ห้ามมีพารามิเตอร์และห้าม return** — ใช้ print เป็นผลข้างเคียงเท่านั้น",
            "input() ภายในฟังก์ชันทำได้ เพราะยังไม่ใช่พารามิเตอร์",
        ],
        P037,
    )
    write_chapter(
        "038-parameters",
        "บท 038 พารามิเตอร์",
        "**ขอบเขตของบทนี้:** ทุกอย่างถึงบท 037 + **พารามิเตอร์ / อาร์กิวเมนต์**\n\n"
        "> ❌ ยังไม่มี `return` (บท 039) · ไม่มี default / keyword arguments (ไม่สอนในหลักสูตร)",
        [
            "ข้อ `02` ไม่ซ้ำตัวอย่างบทเรียนแบบ hard-code Alice/Bob",
            "ทุกฟังก์ชันยัง **print ไม่ return**",
            "ห้ามใช้ค่าเริ่มต้นของพารามิเตอร์และ kwargs",
        ],
        P038,
    )
    write_chapter(
        "039-return-values",
        "บท 039 ค่า return",
        "**ขอบเขตของบทนี้:** ทุกอย่างถึงบท 038 + **`return`**\n\n"
        "> ❌ ยังไม่มี `global` (บท 041) · ห้าม `return a, b` หลายค่า",
        [
            "หลีกเลี่ยงโจทย์เกรด 80/70/60 → A/B/C/F (ซ้ำบทเรียน)",
            "เน้นจับค่าที่ return มาเก็บในตัวแปร แล้วค่อยพิมพ์",
        ],
        P039,
    )
    write_chapter(
        "040-function-practice",
        "บท 040 ฝึกฟังก์ชัน",
        "**ขอบเขตของบทนี้:** ทุกอย่างถึงบท 039 + ส่ง list/dict เข้าฟังก์ชัน + ประกอบฟังก์ชัน\n\n"
        "> `sum()` ใช้ได้ในบทนี้ (ปรากฏในบทเรียน) แต่หลีกเลี่ยง API อื่นที่ยังไม่สอน",
        [
            "จัดสัดส่วน 5/6/4 และมี `00_index.md`",
            "หลีกเลี่ยงเกรด 80/70/60 ซ้ำบทเรียน",
        ],
        P040,
    )
    write_chapter(
        "041-scope",
        "บท 041 Scope",
        "**ขอบเขตของบทนี้:** ทุกอย่างถึงบท 040 + **local / global / `global` keyword**",
        [
            "โจทย์เน้น local กับ global และการใช้ `global`",
            "ให้เขียนโปรแกรมที่รันได้ (ไม่ใช่แค่ทำนายบนกระดาษอย่างเดียว)",
        ],
        P041,
    )
    write_chapter(
        "042-debugging",
        "บท 042 Debugging",
        "**ขอบเขตของบทนี้:** ทุกอย่างถึงบท 041 + แนวคิด Syntax / Runtime / Logic error\n\n"
        "> ❌ ห้าม `try` / `except` (ยังไม่สอน)",
        [
            "โจทย์ให้เขียนโค้ดที่ถูกต้อง หรือจำแนกประเภท error ผ่านโปรแกรมที่รันได้",
            "ห้ามใช้ try/except",
        ],
        P042,
    )
    write_chapter(
        "043-code-readability",
        "บท 043 ความอ่านง่ายของโค้ด",
        "**ขอบเขตของบทนี้:** ทุกอย่างถึงบท 042 + แนวคิดตั้งชื่อ / ค่าคงที่ ALL_CAPS / แยกฟังก์ชัน",
        [
            "โจทย์เน้นเขียนใหม่จากโค้ดรก → โค้ดสะอาด เป็นแบบฝึกหัด",
        ],
        P043,
    )
    write_chapter(
        "044-practice-review",
        "บท 044 ทบทวนรวม",
        "**ขอบเขตของบทนี้:** บูรณาการบท 025–043 (list/dict/function/scope)",
        [
            "หลีกเลี่ยงเกรด 80/70/60 ซ้ำบทเรียน",
            "dict ของ list ใช้ได้",
        ],
        P044,
    )
    write_chapter(
        "045-logic-integration",
        "บท 045 รวมตรรกะ",
        "**ขอบเขตของบทนี้:** ทุกอย่างถึงบท 044 + แนวคิดแตกโจทย์เป็นขั้นตอน\n\n"
        "> ❌ หลีกเลี่ยง `.startswith()` (ไม่เคยสอนจริง — ใช้วิธีอื่นแทน)",
        [
            "ห้ามใช้ `.startswith()` — ใช้การเทียบตัวอักษรด้วย index หรือเงื่อนไขอื่น",
        ],
        P045,
    )
    write_chapter(
        "046-read-code",
        "บท 046 อ่านโค้ด",
        "**ขอบเขตของบทนี้:** ทุกอย่างถึงบท 045 + การไล่ค่าตัวแปร / ฟังก์ชันเรียกฟังก์ชัน",
        [
            "โจทย์ให้เขียนโปรแกรมตามสเปกที่อ่านออกจากโจทย์ (ฝึกอ่าน logic)",
        ],
        P046,
    )
    write_chapter(
        "047-final-review",
        "บท 047 ทบทวนปิด Phase 1",
        "**ขอบเขตของบทนี้:** ทุกอย่างที่เรียนมาใน Phase 1 (ถึงบท 046)",
        [
            "โจทย์รวมหลายหัวข้อในขอบเขต Phase 1",
            "ห้ามใช้ของ Phase 2 (class / file / import / try)",
        ],
        P047,
    )
    write_chapter(
        "048-transition-prep",
        "บท 048 เตรียมสู่ Phase 2",
        "**ขอบเขตของบทนี้:** ใช้ได้เฉพาะ Phase 1 (ถึงบท 047) — ห้าม syntax Phase 2\n\n"
        "> ไฟล์บทเรียน `01_transition_prep.md` และ `02_readiness.md` คงไว้ (ไม่นับเป็นโจทย์)",
        [
            "โจทย์เป็นแบบฝึกโค้ดเกี่ยวกับ checklist / ความพร้อม โดยใช้เฉพาะความรู้ Phase 1",
            "`02_readiness.md` ถูกเครื่องตรวจตัดออกจากนับโจทย์เพราะมี `_readiness` ในชื่อ",
        ],
        P048,
        extra_keep=["02_readiness.md"],
    )
    print("generated 037-048")


if __name__ == "__main__":
    main()
