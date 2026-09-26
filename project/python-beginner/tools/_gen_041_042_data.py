# -*- coding: utf-8 -*-
"""Problem data for weeks 041-048 (appended into main data module)."""

P041 = [
dict(
    file="02_test.md", answer="02_shadow.py",
    title="🌑 Scope — ข้อ 1: เงาตัวแปร",
    diff="🟢 Easy", axis="local บัง global",
    scenario="ต้องการโปรแกรมที่แสดงให้เห็นว่าตัวแปรในฟังก์ชันไม่เปลี่ยนค่าภายนอก\n\nกำหนด `x = 10` นอกฟังก์ชัน สร้าง `change()` ที่ตั้ง `x = 99` แล้วพิมพ์ Inside/Outside ตามตัวอย่าง",
    conditions=["ผลลัพธ์ต้องตรงตัวอย่างเป๊ะ"],
    input_desc="ไม่มี",
    output_desc="2 บรรทัด",
    sample_in=None,
    sample_out="Inside: 99\nOutside: 10\n",
    hint=None,
    starter="x = 10\n\n# สร้าง change() แล้วเรียก\n",
    code='''x = 10

def change():
    x = 99
    print(f"Inside: {x}")

change()
print(f"Outside: {x}")
''',
),
dict(
    file="03_test.md", answer="03_read_global.py",
    title="🌍 Scope — ข้อ 2: อ่านค่า global",
    diff="🟢 Easy", axis="อ่าน global จากในฟังก์ชัน",
    scenario="ชื่อโรงเรียนเก็บเป็นตัวแปรภายนอก ให้ฟังก์ชันอ่านแล้วพิมพ์\n\nกำหนด `school = \"Demo School\"` สร้าง `show_school()` พิมพ์ชื่อโรงเรียน",
    conditions=["ห้ามใช้ `global` (แค่อ่านค่า)"],
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="School: Demo School\n",
    hint=None,
    starter='school = "Demo School"\n\n# สร้าง show_school() แล้วเรียก\n',
    code='''school = "Demo School"

def show_school():
    print(f"School: {school}")

show_school()
''',
),
dict(
    file="04_test.md", answer="04_return_local.py",
    title="📤 Scope — ข้อ 3: ส่งค่า local ออกมา",
    diff="🟢 Easy", axis="local + return แทนการอ่านนอกฟังก์ชัน",
    scenario="ผลคำนวณถูกสร้างในฟังก์ชัน ต้องส่งออกด้วย return\n\nสร้าง `calc()` ที่ตั้ง `result = 42` แล้ว return ค่านั้น พิมพ์ค่านอกฟังก์ชัน",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="42\n",
    hint=None,
    starter="# สร้าง calc() ที่ return ค่า local\n",
    code='''def calc():
    result = 42
    return result

value = calc()
print(value)
''',
),
dict(
    file="05_easy.md", answer="05_counter_global.py",
    title="🔢 Scope — ข้อ 4: ตัวนับด้วย global",
    diff="🟢 Easy", axis="ใช้ keyword global",
    scenario="ตัวนับคะแนนเกมต้องเพิ่มค่าตัวแปรภายนอก\n\nกำหนด `count = 0` สร้าง `add_one()` ที่ใช้ `global count` แล้วเพิ่มทีละ 1 เรียก 2 ครั้ง แล้วพิมพ์ count",
    conditions=["ต้องมีบรรทัด `global count`"],
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="2\n",
    hint=None,
    starter="count = 0\n\n# สร้าง add_one() แล้วเรียก 2 ครั้ง\n",
    code='''count = 0

def add_one():
    global count
    count = count + 1

add_one()
add_one()
print(count)
''',
),
dict(
    file="06_easy.md", answer="06_score_board.py",
    title="🏆 Scope — ข้อ 5: กระดานแต้ม",
    diff="🟢 Easy", axis="global เพิ่มแต้มตามพารามิเตอร์",
    scenario="แต้มรวมเกมเก็บนอกฟังก์ชัน\n\nกำหนด `score = 0` สร้าง `add_points(n)` ใช้ global เพิ่มแต้ม เรียก `add_points(5)` และ `add_points(3)` แล้วพิมพ์ score",
    conditions=["ใช้ `global score`"],
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="Score: 8\n",
    hint=None,
    starter="score = 0\n\n# สร้าง add_points(n)\n",
    code='''score = 0

def add_points(n):
    global score
    score = score + n

add_points(5)
add_points(3)
print(f"Score: {score}")
''',
),
dict(
    file="07_medium.md", answer="07_bank.py",
    title="🏦 Scope — ข้อ 6: ยอดเงินในธนาคารจำลอง",
    diff="🟡 Medium", axis="global ถอน/ฝาก",
    scenario="ยอดเงินเริ่มที่ 100\n\nสร้าง `deposit(n)` และ `withdraw(n)` ที่แก้ `balance` ด้วย global แล้วฝาก 50 ถอน 30 พิมพ์ยอดคงเหลือ",
    conditions=["ใช้ global ทั้งสองฟังก์ชัน"],
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="Balance: 120\n",
    hint="ทั้งฝากและถอนต้องประกาศ global ก่อนแก้ค่า",
    starter="balance = 100\n\n# สร้าง deposit และ withdraw\n",
    code='''balance = 100

def deposit(n):
    global balance
    balance = balance + n

def withdraw(n):
    global balance
    balance = balance - n

deposit(50)
withdraw(30)
print(f"Balance: {balance}")
''',
),
dict(
    file="08_medium.md", answer="08_tax_rate.py",
    title="📉 Scope — ข้อ 7: อ่านเรตภาษี global",
    diff="🟡 Medium", axis="อ่านค่าคงที่ global ในฟังก์ชันคำนวณ",
    scenario="เรตภาษีเก็บเป็นตัวแปรภายนอก `TAX = 7`\n\nสร้าง `price_with_tax(price)` return ราคา + ราคา*TAX/100 แล้วพิมพ์ผลจาก input",
    conditions=["อ่าน TAX ในฟังก์ชันโดยไม่ใช้ global keyword"],
    input_desc="ราคาจำนวนเต็ม 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="100\n",
    sample_out="107.0\n",
    hint="แค่อ่านค่าภายนอก ไม่ต้องใช้คำว่า global",
    starter="TAX = 7\nprice = int(input())\n\n# สร้าง price_with_tax(price) แล้วพิมพ์ผล\n",
    code='''TAX = 7

def price_with_tax(price):
    return price + price * TAX / 100

price = int(input())
print(price_with_tax(price))
''',
),
dict(
    file="09_medium.md", answer="09_toggle.py",
    title="💡 Scope — ข้อ 8: สวิตช์เปิดปิด",
    diff="🟡 Medium", axis="global สลับ bool",
    scenario="ไฟในห้องมีสถานะ `is_on = False`\n\nสร้าง `toggle()` ที่สลับค่าด้วย global เรียก 1 ครั้ง แล้วพิมพ์ On/Off ตามค่าล่าสุด",
    conditions=["ใช้ `not is_on`"],
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="On\n",
    hint="ประกาศ global แล้วตั้งค่าเป็น not ของค่าเดิม",
    starter="is_on = False\n\n# สร้าง toggle() แล้วเรียก\n",
    code='''is_on = False

def toggle():
    global is_on
    is_on = not is_on

toggle()
if is_on:
    print("On")
else:
    print("Off")
''',
),
dict(
    file="10_medium.md", answer="10_name_tag.py",
    title="🏷️ Scope — ข้อ 9: ป้ายชื่อกับเงา",
    diff="🟡 Medium", axis="เปรียบเทียบ shadow กับค่าจริง",
    scenario="ชื่อจริงเก็บนอกฟังก์ชัน แต่ฟังก์ชันสร้างชื่อเล่น local\n\nกำหนด `name = \"Mali\"` สร้าง `nickname()` พิมพ์ Inside เป็น `MaliBee` และนอกฟังก์ชันยังเป็น Mali",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="2 บรรทัด",
    sample_in=None,
    sample_out="Inside: MaliBee\nOutside: Mali\n",
    hint="สร้างตัวแปร name ใหม่ในฟังก์ชัน จะไม่กระทบของภายนอก",
    starter='name = "Mali"\n\n# สร้าง nickname()\n',
    code='''name = "Mali"

def nickname():
    name = "MaliBee"
    print(f"Inside: {name}")

nickname()
print(f"Outside: {name}")
''',
),
dict(
    file="11_medium.md", answer="11_lives.py",
    title="❤️ Scope — ข้อ 10: ชีวิตในเกม",
    diff="🟡 Medium", axis="global ลดค่าหลายครั้ง",
    scenario="ผู้เล่นเริ่มมีชีวิต 3\n\nสร้าง `hit()` ที่ลด lives ด้วย global ทีละ 1 เรียก 2 ครั้ง แล้วพิมพ์ชีวิตคงเหลือ",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="Lives: 1\n",
    hint="ใช้ global แล้ว lives = lives - 1",
    starter="lives = 3\n\n# สร้าง hit() แล้วเรียก 2 ครั้ง\n",
    code='''lives = 3

def hit():
    global lives
    lives = lives - 1

hit()
hit()
print(f"Lives: {lives}")
''',
),
dict(
    file="12_medium.md", answer="12_settings.py",
    title="⚙️ Scope — ข้อ 11: ตั้งค่าเสียง",
    diff="🟡 Medium", axis="อ่าน global + return ค่าคำนวณ",
    scenario="ระดับเสียงพื้นฐาน `BASE = 5`\n\nสร้าง `volume(level)` return BASE + level แล้วรับ level จาก input พิมพ์ผล",
    conditions=None,
    input_desc="level จำนวนเต็ม 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="3\n",
    sample_out="Volume: 8\n",
    hint="อ่าน BASE ในฟังก์ชันได้เลยเพราะแค่ใช้ค่า",
    starter="BASE = 5\nlevel = int(input())\n\n# สร้าง volume(level) แล้วพิมพ์ผล\n",
    code='''BASE = 5

def volume(level):
    return BASE + level

level = int(input())
print(f"Volume: {volume(level)}")
''',
),
dict(
    file="13_challenge.md", answer="13_cart_total.py",
    title="🛒 Scope — ข้อ 12: ยอดตะกร้าสะสม",
    diff="🔴 Challenge", axis="global สะสมจากลิสต์",
    scenario="ยอดตะกร้าเริ่ม 0\n\nสร้าง `add_item(price)` ใช้ global บวกเข้า `total` แล้ววนเรียกกับลิสต์ราคา `[20, 35, 15]` พิมพ์ยอดรวม",
    conditions=["ใช้ global", "วนเรียกฟังก์ชันจากลิสต์"],
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="Cart: 70\n",
    hint="อย่าบวกรวมในลูปหลัก — ให้ฟังก์ชันเป็นคนอัปเดต total",
    starter="total = 0\nprices = [20, 35, 15]\n\n# สร้าง add_item(price) แล้ววนเรียก\n",
    code='''total = 0

def add_item(price):
    global total
    total = total + price

prices = [20, 35, 15]
for p in prices:
    add_item(p)
print(f"Cart: {total}")
''',
),
dict(
    file="14_challenge.md", answer="14_best_score.py",
    title="🎯 Scope — ข้อ 13: สถิติคะแนนสูงสุด",
    diff="🔴 Challenge", axis="global เก็บค่าที่ดีที่สุด",
    scenario="คะแนนสูงสุดเริ่มที่ 0\n\nสร้าง `update_best(score)` ถ้าคะแนนใหม่มากกว่า best ให้แทนค่าด้วย global แล้วอัปเดตจากลิสต์ `[40, 75, 60, 90, 55]` พิมพ์ best",
    conditions=["เปรียบเทียบก่อนอัปเดต"],
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="Best: 90\n",
    hint="ในฟังก์ชันตรวจว่า score > best ก่อนเปลี่ยนค่า",
    starter="best = 0\nscores = [40, 75, 60, 90, 55]\n\n# สร้าง update_best(score)\n",
    code='''best = 0

def update_best(score):
    global best
    if score > best:
        best = score

scores = [40, 75, 60, 90, 55]
for s in scores:
    update_best(s)
print(f"Best: {best}")
''',
),
dict(
    file="15_challenge.md", answer="15_mode.py",
    title="🌙 Scope — ข้อ 14: สลับโหมดกลางวันกลางคืน",
    diff="🔴 Challenge", axis="global สลับข้อความ",
    scenario="โหมดเริ่มเป็น `Day`\n\nสร้าง `switch_mode()` ถ้าเป็น Day ให้เป็น Night และกลับกัน เรียก 3 ครั้ง แล้วพิมพ์โหมดสุดท้าย",
    conditions=["ใช้ global"],
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="Mode: Night\n",
    hint="เรียกคี่ครั้งจะได้ Night จากจุดเริ่ม Day",
    starter='mode = "Day"\n\n# สร้าง switch_mode() แล้วเรียก 3 ครั้ง\n',
    code='''mode = "Day"

def switch_mode():
    global mode
    if mode == "Day":
        mode = "Night"
    else:
        mode = "Day"

switch_mode()
switch_mode()
switch_mode()
print(f"Mode: {mode}")
''',
),
dict(
    file="16_challenge.md", answer="16_inventory.py",
    title="🎒 Scope — ข้อ 15: กระเป๋าสต๊อกสินค้า",
    diff="🔴 Challenge", axis="global กับ dict",
    scenario="สต๊อกเริ่ม `stock = {\"pen\": 10}`\n\nสร้าง `sell(item, qty)` ลดจำนวนใน dict ด้วยการอ่าน/เขียนค่า (ไม่ต้อง global ถ้าไม่ rebound ชื่อ) — ในโจทย์นี้ให้ใช้การแก้ค่าใน dict แล้วขาย pen ไป 3 ชิ้น พิมพ์คงเหลือ",
    conditions=["ผลลัพธ์ pen เหลือ 7"],
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="pen: 7\n",
    hint="การแก้ค่าใน dict ไม่ต้องใช้ global เพราะไม่ได้สร้างชื่อใหม่",
    starter='stock = {"pen": 10}\n\n# สร้าง sell(item, qty) แล้วเรียก sell(\"pen\", 3)\n',
    code='''stock = {"pen": 10}

def sell(item, qty):
    stock[item] = stock[item] - qty

sell("pen", 3)
print(f"pen: {stock['pen']}")
''',
),
]


P042 = [
dict(
    file="02_test.md", answer="02_fix_colon.py",
    title="🔧 Debugging — ข้อ 1: ใส่โคลอนให้ถูก",
    diff="🟢 Easy", axis="แก้ SyntaxError จากขาด :",
    scenario="โปรแกรมตรวจอุณหภูมิมีบั๊ก syntax เพราะลืมโคลอน\n\nเขียนโปรแกรมที่ถูกต้อง: ถ้ารับค่า `>= 30` พิมพ์ `Hot` ไม่งั้น `Cool`",
    conditions=["โค้ดต้องรันได้ ไม่มี SyntaxError"],
    input_desc="อุณหภูมิจำนวนเต็ม 1 บรรทัด",
    output_desc="Hot หรือ Cool",
    sample_in="35\n",
    sample_out="Hot\n",
    hint=None,
    starter="temp = int(input())\n\n# เขียน if/else ให้ถูกต้อง (อย่าลืม :)\n",
    code='''temp = int(input())
if temp >= 30:
    print("Hot")
else:
    print("Cool")
''',
),
dict(
    file="03_test.md", answer="03_safe_div.py",
    title="➗ Debugging — ข้อ 2: หารอย่างปลอดภัย",
    diff="🟢 Easy", axis="ป้องกัน ZeroDivisionError",
    scenario="เครื่องคิดเลขหารเลขสองตัว แต่ต้องไม่พังเมื่อตัวหารเป็น 0\n\nรับ a, b ถ้า b เป็น 0 พิมพ์ `Cannot divide` ไม่งั้นพิมพ์ผลหาร",
    conditions=["ห้ามใช้ try/except"],
    input_desc="จำนวนเต็ม 2 บรรทัด",
    output_desc="ผลหารหรือข้อความเตือน",
    sample_in="10\n0\n",
    sample_out="Cannot divide\n",
    hint=None,
    starter="a = int(input())\nb = int(input())\n\n# ตรวจ b ก่อนหาร\n",
    code='''a = int(input())
b = int(input())
if b == 0:
    print("Cannot divide")
else:
    print(a / b)
''',
),
dict(
    file="04_test.md", answer="04_safe_index.py",
    title="📍 Debugging — ข้อ 3: กัน IndexError",
    diff="🟢 Easy", axis="ตรวจขอบเขตก่อนเข้า index",
    scenario="ลิสต์มี 3 ค่า ต้องการพิมพ์ตัวที่ตำแหน่งที่ผู้ใช้ระบุ\n\nถ้า index ไม่อยู่ในช่วง 0..2 พิมพ์ `Out of range` ไม่งั้นพิมพ์ค่านั้น",
    conditions=["ห้ามใช้ try/except"],
    input_desc="index จำนวนเต็ม 1 บรรทัด",
    output_desc="ค่าหรือข้อความ",
    sample_in="5\n",
    sample_out="Out of range\n",
    hint=None,
    starter="nums = [10, 20, 30]\nindex = int(input())\n\n# ตรวจช่วงก่อน nums[index]\n",
    code='''nums = [10, 20, 30]
index = int(input())
if index < 0 or index > 2:
    print("Out of range")
else:
    print(nums[index])
''',
),
dict(
    file="05_easy.md", answer="05_type_fix.py",
    title="🔤 Debugging — ข้อ 4: กัน TypeError",
    diff="🟢 Easy", axis="แปลงชนิดก่อนรวมข้อความ",
    scenario="โปรแกรมต่อข้อความกับตัวเลขผิดชนิด\n\nรับอายุเป็นจำนวนเต็ม แล้วพิมพ์ `Age: <อายุ>` โดยไม่เกิด TypeError",
    conditions=["ใช้ str() หรือ f-string"],
    input_desc="อายุจำนวนเต็ม 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="15\n",
    sample_out="Age: 15\n",
    hint=None,
    starter="age = int(input())\n\n# พิมพ์ Age: ... ให้ถูกต้อง\n",
    code='''age = int(input())
print(f"Age: {age}")
''',
),
dict(
    file="06_easy.md", answer="06_logic_sum.py",
    title="🧠 Debugging — ข้อ 5: แก้ logic รวมเลข",
    diff="🟢 Easy", axis="Logic error: ใช้ += แทนการทับค่า",
    scenario="โค้ดเดิมเขียน `total = i` ในลูปจึงได้ผลผิด\n\nเขียนโปรแกรมรวมเลข 1 ถึง 4 ให้ได้ 10",
    conditions=["ใช้ for กับ range", "ผลต้องเป็น 10"],
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="10\n",
    hint=None,
    starter="total = 0\n\n# รวมเลข 1 ถึง 4 ให้ถูก\n",
    code='''total = 0
for i in range(1, 5):
    total = total + i
print(total)
''',
),
dict(
    file="07_medium.md", answer="07_error_label.py",
    title="🏷️ Debugging — ข้อ 6: ติดป้ายประเภท error",
    diff="🟡 Medium", axis="จำแนกประเภทผ่านโปรแกรม",
    scenario="รับรหัสประเภท error เป็นตัวเลข แล้วพิมพ์ชื่อประเภท\n\n1 → Syntax, 2 → Runtime, 3 → Logic, อื่นๆ → Unknown",
    conditions=["ห้าม try/except"],
    input_desc="รหัสจำนวนเต็ม 1 บรรทัด",
    output_desc="ชื่อประเภท",
    sample_in="2\n",
    sample_out="Runtime\n",
    hint="ใช้ if/elif แม็พรหัสเป็นชื่อประเภทที่เรียน",
    starter="code = int(input())\n\n# แปลงรหัสเป็นชื่อประเภท error\n",
    code='''code = int(input())
if code == 1:
    print("Syntax")
elif code == 2:
    print("Runtime")
elif code == 3:
    print("Logic")
else:
    print("Unknown")
''',
),
dict(
    file="08_medium.md", answer="08_debug_prints.py",
    title="🖨️ Debugging — ข้อ 7: ใส่ debug print",
    diff="🟡 Medium", axis="แทรก print ตามรอยค่า",
    scenario="ฟังก์ชันคูณเลขต้องมีบรรทัด debug ตามแบบบทเรียน\n\nสร้าง `calc(x, y)` ที่พิมพ์ `x=...` และ `y=...` ก่อน คำนวณผล แล้วพิมพ์ `result=...` และ return ผล จากนั้นพิมพ์ผลที่ return อีกครั้งนอกฟังก์ชัน",
    conditions=["มี debug prints ตามตัวอย่าง"],
    input_desc="จำนวนเต็ม 2 บรรทัด",
    output_desc="4 บรรทัด",
    sample_in="3\n4\n",
    sample_out="x=3\ny=4\nresult=12\n12\n",
    hint="พิมพ์ค่าพารามิเตอร์ก่อนคำนวณ แล้วพิมพ์ผลก่อน return",
    starter="x = int(input())\ny = int(input())\n\n# สร้าง calc(x, y) พร้อม debug print\n",
    code='''def calc(x, y):
    print(f"x={x}")
    print(f"y={y}")
    result = x * y
    print(f"result={result}")
    return result

x = int(input())
y = int(input())
print(calc(x, y))
''',
),
dict(
    file="09_medium.md", answer="09_off_by_one.py",
    title="1️⃣ Debugging — ข้อ 8: แก้ off-by-one",
    diff="🟡 Medium", axis="range ให้ครบตามที่ต้องการ",
    scenario="ต้องการพิมพ์เลข 1 ถึง 5 แต่คนมักใช้ range ผิด\n\nเขียนโปรแกรมพิมพ์ 1 2 3 4 5 คนละบรรทัด",
    conditions=["ใช้ for + range"],
    input_desc="ไม่มี",
    output_desc="5 บรรทัด",
    sample_in=None,
    sample_out="1\n2\n3\n4\n5\n",
    hint="range(1, 6) ให้ค่าถึง 5 เพราะ stop ไม่รวม",
    starter="# พิมพ์ 1 ถึง 5\n",
    code='''for i in range(1, 6):
    print(i)
''',
),
dict(
    file="10_medium.md", answer="10_indent_fix.py",
    title="➡️ Debugging — ข้อ 9: เยื้องให้ถูก",
    diff="🟡 Medium", axis="IndentationError / logic จากเยื้องผิด",
    scenario="ต้องการทักทาย 3 ครั้งในลูป\n\nเขียนโปรแกรมใช้ for พิมพ์ `Hi` สามครั้ง (เยื้องให้ print อยู่ในลูป)",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="3 บรรทัด",
    sample_in=None,
    sample_out="Hi\nHi\nHi\n",
    hint="บรรทัดในลูปต้องเยื้องเข้าไป 4 ช่อง",
    starter="# พิมพ์ Hi สามครั้งด้วย for\n",
    code='''for i in range(3):
    print("Hi")
''',
),
dict(
    file="11_medium.md", answer="11_match_error.py",
    title="🧩 Debugging — ข้อ 10: จับคู่สถานการณ์กับประเภท",
    diff="🟡 Medium", axis="จำแนกจากคำอธิบายสั้น",
    scenario="รับคำอธิบายสั้นๆ แล้วพิมพ์ประเภท error\n\n`missing :` → Syntax, `divide 0` → Runtime, `wrong total` → Logic, อื่นๆ → Other",
    conditions=["เทียบข้อความด้วย =="],
    input_desc="ข้อความ 1 บรรทัด",
    output_desc="ประเภท",
    sample_in="divide 0\n",
    sample_out="Runtime\n",
    hint="เทียบสตริงทีละกรณี",
    starter="msg = input()\n\n# แปลงข้อความเป็นประเภท error\n",
    code='''msg = input()
if msg == "missing :":
    print("Syntax")
elif msg == "divide 0":
    print("Runtime")
elif msg == "wrong total":
    print("Logic")
else:
    print("Other")
''',
),
dict(
    file="12_medium.md", answer="12_list_loop_fix.py",
    title="🔁 Debugging — ข้อ 11: ใช้ตัวแปรลูปให้ถูก",
    diff="🟡 Medium", axis="พิมพ์สมาชิก ไม่ใช่ทั้งลิสต์ซ้ำ",
    scenario="บั๊กคลาสสิก: ในลูปพิมพ์ชื่อลิสต์แทนตัวแปรลูป\n\nเขียนโปรแกรมพิมพ์ชื่อใน `names = [\"Ann\", \"Ben\", \"Cat\"]` คนละบรรทัด",
    conditions=["ใช้ for-in-list"],
    input_desc="ไม่มี",
    output_desc="3 บรรทัด",
    sample_in=None,
    sample_out="Ann\nBen\nCat\n",
    hint="ในลูปให้พิมพ์ตัวแปรลูป ไม่ใช่ชื่อลิสต์",
    starter='names = ["Ann", "Ben", "Cat"]\n\n# พิมพ์ทีละชื่อ\n',
    code='''names = ["Ann", "Ben", "Cat"]
for name in names:
    print(name)
''',
),
dict(
    file="13_challenge.md", answer="13_validate_score.py",
    title="🛡️ Debugging — ข้อ 12: กันหลาย runtime พร้อมกัน",
    diff="🔴 Challenge", axis="ตรวจหลายเงื่อนไขก่อนคำนวณ",
    scenario="รับคะแนนดิบและตัวหารเพื่อคิดค่าเฉลี่ยแบบง่าย `score / parts`\n\nถ้า score `< 0` พิมพ์ `Bad score` ถ้า parts เป็น 0 พิมพ์ `Bad parts` ไม่งั้นพิมพ์ผลหาร",
    conditions=["ห้าม try/except", "ตรวจ score ก่อน parts"],
    input_desc="score และ parts เป็นจำนวนเต็มอย่างละ 1 บรรทัด",
    output_desc="ข้อความหรือผลหาร",
    sample_in="-5\n2\n",
    sample_out="Bad score\n",
    hint="เรียงการตรวจจากเงื่อนไขที่โจทย์กำหนด",
    starter="score = int(input())\nparts = int(input())\n\n# ตรวจแล้วค่อยคำนวณ\n",
    code='''score = int(input())
parts = int(input())
if score < 0:
    print("Bad score")
elif parts == 0:
    print("Bad parts")
else:
    print(score / parts)
''',
),
dict(
    file="14_challenge.md", answer="14_trace_fix.py",
    title="🔍 Debugging — ข้อ 13: แก้ผลรวมสินค้า",
    diff="🔴 Challenge", axis="Logic error ในลูปสะสม",
    scenario="ต้องการรวมราคาสินค้าในลิสต์ `[12, 18, 25]` แต่โค้ดเดิมทับค่า\n\nเขียนให้ถูกต้อง พิมพ์ยอดรวม",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="Total: 55\n",
    hint="เริ่ม total = 0 แล้วบวกทีละตัว",
    starter="prices = [12, 18, 25]\n\n# รวมยอดให้ถูก\n",
    code='''prices = [12, 18, 25]
total = 0
for p in prices:
    total = total + p
print(f"Total: {total}")
''',
),
dict(
    file="15_challenge.md", answer="15_find_max_safe.py",
    title="📈 Debugging — ข้อ 14: หาค่ามากสุดแบบปลอดภัย",
    diff="🔴 Challenge", axis="กันลิสต์ว่างก่อนหา max ด้วยมือ",
    scenario="รับจำนวน n แล้วรับเลข n ตัว หาค่ามากสุดด้วยการวนเอง\n\nถ้า n เป็น 0 พิมพ์ `Empty` ไม่งั้นพิมพ์ค่ามากสุด",
    conditions=["ห้ามใช้ max()", "ห้าม try/except"],
    input_desc="n แล้วตามด้วย n จำนวนเต็ม",
    output_desc="Empty หรือค่ามากสุด",
    sample_in="0\n",
    sample_out="Empty\n",
    hint="ตรวจ n ก่อน ถ้ามีข้อมูลให้เริ่มจากตัวแรกแล้วเทียบทีละตัว",
    starter="n = int(input())\n\n# ถ้าว่างพิมพ์ Empty ไม่งั้นหาค่ามากสุดเอง\n",
    code='''n = int(input())
if n == 0:
    print("Empty")
else:
    best = int(input())
    for i in range(n - 1):
        value = int(input())
        if value > best:
            best = value
    print(best)
''',
),
dict(
    file="16_challenge.md", answer="16_report_bug.py",
    title="📋 Debugging — ข้อ 15: รายงานบั๊กจากโค้ดสั้น",
    diff="🔴 Challenge", axis="โปรแกรมช่วยจำแนกจากคีย์เวิร์ด",
    scenario="ทีม QA ใส่คำสั้นๆ ว่าเจออะไร\n\nรับข้อความ ถ้ามีคำว่า `SyntaxError` ในข้อความ (เทียบทั้งสตริงเท่ากับคำนั้น) พิมพ์ `Fix colon or indent` ถ้าเป็น `ZeroDivisionError` พิมพ์ `Check divisor` ถ้าเป็น `IndexError` พิมพ์ `Check index` อื่นๆ พิมพ์ `Read code again`",
    conditions=["เทียบด้วย =="],
    input_desc="ชื่อ error 1 บรรทัด",
    output_desc="คำแนะนำสั้นๆ",
    sample_in="IndexError\n",
    sample_out="Check index\n",
    hint="แม็พชื่อ error ที่เรียนในบทนี้เป็นคำแนะนำ",
    starter="err = input()\n\n# แปลงชื่อ error เป็นคำแนะนำ\n",
    code='''err = input()
if err == "SyntaxError":
    print("Fix colon or indent")
elif err == "ZeroDivisionError":
    print("Check divisor")
elif err == "IndexError":
    print("Check index")
else:
    print("Read code again")
''',
),
]
