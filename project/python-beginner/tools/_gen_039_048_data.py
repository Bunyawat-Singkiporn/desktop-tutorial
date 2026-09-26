# -*- coding: utf-8 -*-
"""Problem data for weeks 039-040; remaining weeks imported below."""
from _gen_041_042_data import P041, P042
from _gen_043_044_data import P043, P044
from _gen_045_048_data import P045, P046, P047, P048

# ═══════════════════════════════════════════════════════════════════
# 039 — return values (avoid get_grade 80/70/60)
# ═══════════════════════════════════════════════════════════════════
P039 = [
dict(
    file="02_test.md", answer="02_square.py",
    title="² ค่า return — ข้อ 1: กำลังสอง",
    diff="🟢 Easy", axis="return ค่าเดียวแล้วพิมพ์นอกฟังก์ชัน",
    scenario="ต้องการคำนวณกำลังสองแล้วนำไปใช้ต่อ\n\nสร้าง `square(n)` ที่ `return n * n` แล้วพิมพ์ผลที่ได้",
    conditions=["ต้องใช้ `return`", "พิมพ์ผลนอกฟังก์ชัน"],
    input_desc="จำนวนเต็ม 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="5\n",
    sample_out="25\n",
    hint=None,
    starter="n = int(input())\n\n# สร้าง square(n) แล้วพิมพ์ผล\n",
    code='''def square(n):
    return n * n

n = int(input())
print(square(n))
''',
),
dict(
    file="03_test.md", answer="03_is_even.py",
    title="🔢 ค่า return — ข้อ 2: เลขคู่หรือไม่",
    diff="🟢 Easy", axis="return True/False",
    scenario="เกมตรวจว่าเลขที่สุ่มได้เป็นเลขคู่หรือไม่\n\nสร้าง `is_even(n)` ที่ return True/False แล้วพิมพ์ `Even` หรือ `Odd`",
    conditions=["ฟังก์ชันต้อง return bool", "ห้ามพิมพ์ในฟังก์ชัน"],
    input_desc="จำนวนเต็ม 1 บรรทัด",
    output_desc="Even หรือ Odd",
    sample_in="8\n",
    sample_out="Even\n",
    hint=None,
    starter="n = int(input())\n\n# สร้าง is_even(n) แล้วใช้ผลตัดสินใจพิมพ์\n",
    code='''def is_even(n):
    return n % 2 == 0

n = int(input())
if is_even(n):
    print("Even")
else:
    print("Odd")
''',
),
dict(
    file="04_test.md", answer="04_triple.py",
    title="✖️ ค่า return — ข้อ 3: คูณสาม",
    diff="🟢 Easy", axis="return ผลการคำนวณ",
    scenario="แต้มโบนัสในเกมคูณสามก่อนแสดง\n\nสร้าง `triple(n)` return n * 3 แล้วพิมพ์ผล",
    conditions=None,
    input_desc="จำนวนเต็ม 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="7\n",
    sample_out="21\n",
    hint=None,
    starter="n = int(input())\n\n# สร้าง triple(n) แล้วพิมพ์ผล\n",
    code='''def triple(n):
    return n * 3

n = int(input())
print(triple(n))
''',
),
dict(
    file="05_easy.md", answer="05_full_name.py",
    title="🪪 ค่า return — ข้อ 4: ต่อชื่อเต็ม",
    diff="🟢 Easy", axis="return สตริงที่ประกอบจากพารามิเตอร์",
    scenario="ฟอร์มสมัครต้องประกอบชื่อเต็มจากชื่อและนามสกุล\n\nสร้าง `full_name(first, last)` ที่ return ข้อความ `first last`",
    conditions=["พิมพ์ผลนอกฟังก์ชัน"],
    input_desc="ชื่อและนามสกุลอย่างละ 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="Mali\nSook\n",
    sample_out="Mali Sook\n",
    hint=None,
    starter="first = input()\nlast = input()\n\n# สร้าง full_name(first, last) แล้วพิมพ์ผล\n",
    code='''def full_name(first, last):
    return first + " " + last

first = input()
last = input()
print(full_name(first, last))
''',
),
dict(
    file="06_easy.md", answer="06_pass_check.py",
    title="✅ ค่า return — ข้อ 5: ผ่านเกณฑ์ 50",
    diff="🟢 Easy", axis="return bool จากเกณฑ์เดียว",
    scenario="ระบบตรวจว่าคะแนนสอบควิซผ่านเกณฑ์ 50 หรือไม่\n\nสร้าง `is_pass(score)` return True ถ้า `>= 50` แล้วพิมพ์ `Pass`/`Fail`",
    conditions=["ห้ามทำเกรด A/B/C/F แบบ 80/70/60"],
    input_desc="คะแนนจำนวนเต็ม 1 บรรทัด",
    output_desc="Pass หรือ Fail",
    sample_in="62\n",
    sample_out="Pass\n",
    hint=None,
    starter="score = int(input())\n\n# สร้าง is_pass(score) แล้วพิมพ์ผล\n",
    code='''def is_pass(score):
    return score >= 50

score = int(input())
if is_pass(score):
    print("Pass")
else:
    print("Fail")
''',
),
dict(
    file="07_medium.md", answer="07_rect_area.py",
    title="🏟️ ค่า return — ข้อ 6: พื้นที่สนาม",
    diff="🟡 Medium", axis="return แล้วไปคำนวณต่อ",
    scenario="ต้องการพื้นที่สนามเพื่อคิดค่าเช่าต่อตารางเมตร\n\nสร้าง `area(w, h)` return พื้นที่ แล้วพิมพ์ทั้งพื้นที่และค่าเช่า = พื้นที่ × 5",
    conditions=["ค่าเช่าคิดนอกฟังก์ชันจากค่าที่ return"],
    input_desc="ความกว้างและความสูง เป็นจำนวนเต็มอย่างละ 1 บรรทัด",
    output_desc="2 บรรทัด",
    sample_in="4\n5\n",
    sample_out="Area: 20\nRent: 100\n",
    hint="เก็บค่าที่ return ไว้ในตัวแปรก่อน แล้วค่อยเอาไปคูณ 5",
    starter="w = int(input())\nh = int(input())\n\n# สร้าง area(w, h) แล้วนำผลไปใช้ต่อ\n",
    code='''def area(w, h):
    return w * h

w = int(input())
h = int(input())
a = area(w, h)
print(f"Area: {a}")
print(f"Rent: {a * 5}")
''',
),
dict(
    file="08_medium.md", answer="08_clamp.py",
    title="🎮 ค่า return — ข้อ 7: จำกัดคะแนนเกม",
    diff="🟡 Medium", axis="return จากหลายกิ่ง if",
    scenario="คะแนนเกมต้องอยู่ในช่วง 0–100\n\nสร้าง `clamp(score)` — ถ้าน้อยกว่า 0 ให้ return 0, มากกว่า 100 ให้ return 100, อื่นๆ return ค่าเดิม",
    conditions=["ใช้ return ในหลายกิ่ง"],
    input_desc="จำนวนเต็ม 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="130\n",
    sample_out="100\n",
    hint="ตรวจขอบล่างก่อน แล้วขอบบน แล้วค่อยคืนค่าเดิม",
    starter="score = int(input())\n\n# สร้าง clamp(score) แล้วพิมพ์ผล\n",
    code='''def clamp(score):
    if score < 0:
        return 0
    if score > 100:
        return 100
    return score

score = int(input())
print(clamp(score))
''',
),
dict(
    file="09_medium.md", answer="09_to_f.py",
    title="🌡️ ค่า return — ข้อ 8: แปลงแล้วเก็บค่า",
    diff="🟡 Medium", axis="return ค่าแปลงหน่วย",
    scenario="แอปอากาศแปลง C เป็น F เพื่อไปแสดงต่อ\n\nสร้าง `to_f(c)` return ค่า F แล้วพิมพ์ผล",
    conditions=["สูตร F = C * 9 / 5 + 32"],
    input_desc="อุณหภูมิ C เป็นจำนวนจริง 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="10\n",
    sample_out="50.0\n",
    hint="return ค่าที่คำนวณได้ แล้วค่อย print นอกฟังก์ชัน",
    starter="c = float(input())\n\n# สร้าง to_f(c) แล้วพิมพ์ผล\n",
    code='''def to_f(c):
    return c * 9 / 5 + 32

c = float(input())
print(to_f(c))
''',
),
dict(
    file="10_medium.md", answer="10_discount_price.py",
    title="🛍️ ค่า return — ข้อ 9: ราคาสุทธิหลังลด",
    diff="🟡 Medium", axis="return ผลการคำนวณสองขั้น",
    scenario="ร้านค้าต้องการฟังก์ชันหาราคาหลังหักส่วนลดเป็นบาท\n\nสร้าง `final_price(price, discount)` return ราคา − ส่วนลด",
    conditions=None,
    input_desc="ราคาและส่วนลด เป็นจำนวนเต็มอย่างละ 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="299\n30\n",
    sample_out="269\n",
    hint="return ผลลบ แล้วพิมพ์นอกฟังก์ชัน",
    starter="price = int(input())\ndiscount = int(input())\n\n# สร้าง final_price(price, discount) แล้วพิมพ์ผล\n",
    code='''def final_price(price, discount):
    return price - discount

price = int(input())
discount = int(input())
print(final_price(price, discount))
''',
),
dict(
    file="11_medium.md", answer="11_level.py",
    title="⭐ ค่า return — ข้อ 10: ระดับผู้เล่น",
    diff="🟡 Medium", axis="return ข้อความจากช่วงคะแนน (ไม่ใช่เกรดเรียน)",
    scenario="เกมจัดระดับผู้เล่นจากแต้มสะสม\n\nสร้าง `get_level(points)` — `>= 1000` → Gold, `>= 500` → Silver, อื่นๆ → Bronze\n\n(ไม่ใช่เกรด A/B/C/F ของบทเรียน)",
    conditions=["return สตริงระดับ", "พิมพ์นอกฟังก์ชัน"],
    input_desc="แต้มจำนวนเต็ม 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="750\n",
    sample_out="Silver\n",
    hint="ใช้ if/elif/else แล้ว return ข้อความระดับ",
    starter="points = int(input())\n\n# สร้าง get_level(points) แล้วพิมพ์ผล\n",
    code='''def get_level(points):
    if points >= 1000:
        return "Gold"
    elif points >= 500:
        return "Silver"
    else:
        return "Bronze"

points = int(input())
print(get_level(points))
''',
),
dict(
    file="12_medium.md", answer="12_lucky.py",
    title="🍀 ค่า return — ข้อ 11: เลขนำโชค",
    diff="🟡 Medium", axis="return bool จากเงื่อนไขประกอบ",
    scenario="เกมสุ่มเลขนำโชค — เลขที่หาร 7 ลงตัวถือว่าโชคดี\n\nสร้าง `is_lucky(n)` return True ถ้า `n % 7 == 0` แล้วพิมพ์ `Lucky`/`Normal`",
    conditions=None,
    input_desc="จำนวนเต็ม 1 บรรทัด",
    output_desc="Lucky หรือ Normal",
    sample_in="21\n",
    sample_out="Lucky\n",
    hint="return ผลการเปรียบเทียบ แล้วค่อยตัดสินใจพิมพ์นอกฟังก์ชัน",
    starter="n = int(input())\n\n# สร้าง is_lucky(n) แล้วพิมพ์ผล\n",
    code='''def is_lucky(n):
    return n % 7 == 0

n = int(input())
if is_lucky(n):
    print("Lucky")
else:
    print("Normal")
''',
),
dict(
    file="13_challenge.md", answer="13_username.py",
    title="👤 ค่า return — ข้อ 12: ตรวจความยาว username",
    diff="🔴 Challenge", axis="return bool + ใช้ len",
    scenario="ระบบสมัครเกมรับ username ที่ยาวอย่างน้อย 4 ตัวอักษร\n\nสร้าง `is_valid(name)` return True ถ้า `len(name) >= 4` แล้วพิมพ์ `OK` หรือ `Too short`",
    conditions=["ห้ามพิมพ์ในฟังก์ชัน"],
    input_desc="username 1 บรรทัด",
    output_desc="OK หรือ Too short",
    sample_in="Mia\n",
    sample_out="Too short\n",
    hint="ใช้ len() ภายในฟังก์ชันแล้ว return ผลการเทียบ",
    starter="name = input()\n\n# สร้าง is_valid(name) แล้วพิมพ์ผล\n",
    code='''def is_valid(name):
    return len(name) >= 4

name = input()
if is_valid(name):
    print("OK")
else:
    print("Too short")
''',
),
dict(
    file="14_challenge.md", answer="14_food_order.py",
    title="🍔 ค่า return — ข้อ 13: สั่งอาหารออนไลน์",
    diff="🔴 Challenge", axis="return ราคาจากเมนู แล้วคิดเงินทอน",
    scenario="แอปสั่งอาหารมี 3 เมนู\n\nสร้าง `get_price(code)` — 1→45, 2→60, 3→80 แล้วรับเงินที่จ่าย คำนวณเงินทอนนอกฟังก์ชัน",
    conditions=["ฟังก์ชัน return ราคาเท่านั้น"],
    input_desc="รหัสเมนู 1 บรรทัด และเงินที่จ่าย 1 บรรทัด (จำนวนเต็ม)",
    output_desc="ราคาและเงินทอน",
    sample_in="2\n100\n",
    sample_out="Price: 60\nChange: 40\n",
    hint="แยกการหาราคา (return) กับการคิดเงินทอน (นอกฟังก์ชัน)",
    starter="code = int(input())\npaid = int(input())\n\n# สร้าง get_price(code) แล้วนำผลไปคิดเงินทอน\n",
    code='''def get_price(code):
    if code == 1:
        return 45
    elif code == 2:
        return 60
    else:
        return 80

code = int(input())
paid = int(input())
price = get_price(code)
print(f"Price: {price}")
print(f"Change: {paid - price}")
''',
),
dict(
    file="15_challenge.md", answer="15_chain.py",
    title="🔗 ค่า return — ข้อ 14: ต่อฟังก์ชันสองตัว",
    diff="🔴 Challenge", axis="นำผล return ไปเป็นอาร์กิวเมนต์ฟังก์ชันถัดไป",
    scenario="แต้มดิบต้องบวกโบนัส 10 ก่อน แล้วคูณสอง\n\nสร้าง `add_bonus(n)` return n+10 และ `double(n)` return n*2 แล้วเรียกแบบต่อกัน",
    conditions=["ต้องมี 2 ฟังก์ชัน", "ผลสุดท้ายพิมพ์นอกฟังก์ชัน"],
    input_desc="จำนวนเต็ม 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="5\n",
    sample_out="30\n",
    hint="เรียก `double(add_bonus(n))` หรือเก็บค่ากลางไว้ในตัวแปร",
    starter="n = int(input())\n\n# สร้าง add_bonus และ double แล้วประกอบกัน\n",
    code='''def add_bonus(n):
    return n + 10

def double(n):
    return n * 2

n = int(input())
print(double(add_bonus(n)))
''',
),
dict(
    file="16_challenge.md", answer="16_shipping_cost.py",
    title="📦 ค่า return — ข้อ 15: คืนค่าค่าส่ง",
    diff="🔴 Challenge", axis="return ค่าจากช่วง แล้วจัดใบเสร็จ",
    scenario="ระบบโลจิสติกส์คืนค่าค่าส่งตามน้ำหนัก\n\nสร้าง `shipping(weight)` return 30/50/80 ตามช่วง `<=1` / `<=5` / อื่นๆ แล้วพิมพ์ใบเสร็จ",
    conditions=["ฟังก์ชัน return ตัวเลขเท่านั้น"],
    input_desc="น้ำหนักจำนวนจริง 1 บรรทัด",
    output_desc="ใบเสร็จ 2 บรรทัด",
    sample_in="0.8\n",
    sample_out="Weight: 0.8\nShipping: 30\n",
    hint="return ค่าส่งตามช่วง แล้วพิมพ์ป้ายกำกับนอกฟังก์ชัน",
    starter="weight = float(input())\n\n# สร้าง shipping(weight) แล้วพิมพ์ใบเสร็จ\n",
    code='''def shipping(weight):
    if weight <= 1:
        return 30
    elif weight <= 5:
        return 50
    else:
        return 80

weight = float(input())
fee = shipping(weight)
print(f"Weight: {weight}")
print(f"Shipping: {fee}")
''',
),
]


# ═══════════════════════════════════════════════════════════════════
# 040 — function practice (reshape to 5/6/4; sum OK)
# ═══════════════════════════════════════════════════════════════════
P040 = [
dict(
    file="02_test.md", answer="02_list_sum.py",
    title="➕ ฝึกฟังก์ชัน — ข้อ 1: ผลรวมคะแนน",
    diff="🟢 Easy", axis="ส่ง list เข้าฟังก์ชัน + return ผลรวม",
    scenario="ครูส่งลิสต์คะแนนเข้าฟังก์ชันเพื่อหาผลรวม\n\nสร้าง `get_total(scores)` ที่วนบวกเอง (หรือใช้ `sum`) แล้วพิมพ์ผล",
    conditions=["รับ list เป็นพารามิเตอร์", "return ผลรวม"],
    input_desc="ไม่มี (ใช้ลิสต์ใน Starter)",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="Total: 398\n",
    hint=None,
    starter="scores = [80, 75, 90, 65, 88]\n\n# สร้าง get_total(scores) แล้วพิมพ์ผล\n",
    code='''def get_total(scores):
    total = 0
    for s in scores:
        total = total + s
    return total

scores = [80, 75, 90, 65, 88]
print(f"Total: {get_total(scores)}")
''',
),
dict(
    file="03_test.md", answer="03_count_pass.py",
    title="✅ ฝึกฟังก์ชัน — ข้อ 2: นับคนผ่าน",
    diff="🟢 Easy", axis="วน list ในฟังก์ชัน + นับเงื่อนไข",
    scenario="อยากรู้ว่าในลิสต์คะแนนมีกี่คนที่ได้ `>= 50`\n\nสร้าง `count_pass(scores)` return จำนวนคนที่ผ่าน",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="Passed: 3\n",
    hint=None,
    starter="scores = [40, 55, 70, 49, 90]\n\n# สร้าง count_pass(scores) แล้วพิมพ์ผล\n",
    code='''def count_pass(scores):
    count = 0
    for s in scores:
        if s >= 50:
            count = count + 1
    return count

scores = [40, 55, 70, 49, 90]
print(f"Passed: {count_pass(scores)}")
''',
),
dict(
    file="04_test.md", answer="04_show_student.py",
    title="👤 ฝึกฟังก์ชัน — ข้อ 3: แสดงข้อมูลนักเรียน",
    diff="🟢 Easy", axis="ส่ง dict เข้าฟังก์ชัน + .items()",
    scenario="บัตรนักเรียนเก็บเป็น dict แล้วให้ฟังก์ชันพิมพ์ทีละคู่\n\nสร้าง `show_student(student)` วน `.items()` แล้วพิมพ์ `key: value`",
    conditions=["ห้ามใช้ return (พิมพ์ในฟังก์ชันได้)"],
    input_desc="ไม่มี",
    output_desc="2 บรรทัด",
    sample_in=None,
    sample_out="name: Alice\nscore: 92\n",
    hint=None,
    starter='student = {"name": "Alice", "score": 92}\n\n# สร้าง show_student(student) แล้วเรียก\n',
    code='''def show_student(student):
    for key, value in student.items():
        print(f"{key}: {value}")

student = {"name": "Alice", "score": 92}
show_student(student)
''',
),
dict(
    file="05_easy.md", answer="05_average.py",
    title="📊 ฝึกฟังก์ชัน — ข้อ 4: ค่าเฉลี่ย",
    diff="🟢 Easy", axis="sum/len ในฟังก์ชัน",
    scenario="หาค่าเฉลี่ยคะแนนจากลิสต์\n\nสร้าง `get_average(scores)` return ผลรวม/จำนวน",
    conditions=["ใช้ `sum` ได้ หรือวนบวกเองก็ได้"],
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="Average: 84.33333333333333\n",
    hint=None,
    starter="scores = [80, 90, 83]\n\n# สร้าง get_average(scores) แล้วพิมพ์ผล\n",
    code='''def get_average(scores):
    return sum(scores) / len(scores)

scores = [80, 90, 83]
print(f"Average: {get_average(scores)}")
''',
),
dict(
    file="06_easy.md", answer="06_c_to_f.py",
    title="🌡️ ฝึกฟังก์ชัน — ข้อ 5: แปลงอุณหภูมิ",
    diff="🟢 Easy", axis="ฟังก์ชันเล็กๆ รับ input แล้วเรียก",
    scenario="รับค่า C จากผู้ใช้ แล้วส่งเข้าฟังก์ชันแปลงเป็น F\n\nสร้าง `to_f(c)` return ค่า F",
    conditions=None,
    input_desc="อุณหภูมิ C 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="0\n",
    sample_out="32.0\n",
    hint=None,
    starter="# สร้าง to_f(c)\n# รับ input แล้วพิมพ์ผล\n",
    code='''def to_f(c):
    return c * 9 / 5 + 32

c = float(input())
print(to_f(c))
''',
),
dict(
    file="07_medium.md", answer="07_filter_pass.py",
    title="🔍 ฝึกฟังก์ชัน — ข้อ 6: กรองคะแนนผ่าน",
    diff="🟡 Medium", axis="สร้าง list ใหม่ในฟังก์ชัน",
    scenario="ต้องการลิสต์เฉพาะคะแนนที่ `>= 50`\n\nสร้าง `filter_pass(scores)` return ลิสต์ใหม่ที่ผ่านเกณฑ์ แล้วพิมพ์ลิสต์",
    conditions=["ใช้ `.append()`"],
    input_desc="ไม่มี",
    output_desc="1 บรรทัด (ลิสต์)",
    sample_in=None,
    sample_out="[55, 70, 90]\n",
    hint="สร้างลิสต์ว่างในฟังก์ชัน แล้ว append เฉพาะค่าที่ผ่าน",
    starter="scores = [40, 55, 70, 49, 90]\n\n# สร้าง filter_pass(scores) แล้วพิมพ์ผล\n",
    code='''def filter_pass(scores):
    result = []
    for s in scores:
        if s >= 50:
            result.append(s)
    return result

scores = [40, 55, 70, 49, 90]
print(filter_pass(scores))
''',
),
dict(
    file="08_medium.md", answer="08_vat_bill.py",
    title="🧾 ฝึกฟังก์ชัน — ข้อ 7: บิลซูเปอร์ + VAT",
    diff="🟡 Medium", axis="ประกอบสองฟังก์ชัน",
    scenario="บิลซูเปอร์มาร์เก็ตคิดยอดก่อน VAT แล้วค่อยบวก 7%\n\nสร้าง `get_total(prices)` และ `add_vat(total)` แล้วพิมพ์ยอดสุทธิทศนิยม 2 ตำแหน่ง",
    conditions=["ต้องมี 2 ฟังก์ชัน"],
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="Pay: 214.00\n",
    hint="หาผลรวมก่อน แล้วค่อยส่งเข้าฟังก์ชันบวก VAT (× 1.07)",
    starter="prices = [100, 50, 50]\n\n# สร้าง get_total และ add_vat\n",
    code='''def get_total(prices):
    total = 0
    for p in prices:
        total = total + p
    return total

def add_vat(total):
    return total * 1.07

prices = [100, 50, 50]
pay = add_vat(get_total(prices))
print(f"Pay: {pay:.2f}")
''',
),
dict(
    file="09_medium.md", answer="09_password.py",
    title="🔑 ฝึกฟังก์ชัน — ข้อ 8: ตั้งรหัสผ่านเกม",
    diff="🟡 Medium", axis="ตรวจเงื่อนไขความยาวด้วยฟังก์ชัน",
    scenario="เกมรับรหัสผ่านที่ยาวอย่างน้อย 6 ตัวอักษร\n\nสร้าง `check_password(pw)` return True/False แล้วพิมพ์ `Strong`/`Weak`",
    conditions=None,
    input_desc="รหัสผ่าน 1 บรรทัด",
    output_desc="Strong หรือ Weak",
    sample_in="abc123\n",
    sample_out="Strong\n",
    hint="ใช้ len() ในฟังก์ชัน",
    starter="pw = input()\n\n# สร้าง check_password(pw) แล้วพิมพ์ผล\n",
    code='''def check_password(pw):
    return len(pw) >= 6

pw = input()
if check_password(pw):
    print("Strong")
else:
    print("Weak")
''',
),
dict(
    file="10_medium.md", answer="10_menu_calc.py",
    title="📱 ฝึกฟังก์ชัน — ข้อ 9: เครื่องคิดเลขมือถือ",
    diff="🟡 Medium", axis="ฟังก์ชันคำนวณตามตัวดำเนินการ",
    scenario="แอปเครื่องคิดเลขรับเลขสองตัวและตัวดำเนินการ `+` หรือ `*`\n\nสร้าง `calc(a, b, op)` return ผลลัพธ์",
    conditions=["รองรับ + และ *"],
    input_desc="a, b เป็นจำนวนเต็ม และ op เป็นข้อความ อย่างละ 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="6\n7\n*\n",
    sample_out="42\n",
    hint="ใช้ if/else เลือกการคำนวณจากข้อความ op",
    starter="a = int(input())\nb = int(input())\nop = input()\n\n# สร้าง calc(a, b, op) แล้วพิมพ์ผล\n",
    code='''def calc(a, b, op):
    if op == "+":
        return a + b
    else:
        return a * b

a = int(input())
b = int(input())
op = input()
print(calc(a, b, op))
''',
),
dict(
    file="11_medium.md", answer="11_camp_list.py",
    title="🏕️ ฝึกฟังก์ชัน — ข้อ 10: รายชื่อเข้าค่าย",
    diff="🟡 Medium", axis="รับ n ชื่อเข้า list ผ่านฟังก์ชัน",
    scenario="รับจำนวนคน แล้วรับชื่อทีละคนเก็บในลิสต์\n\nสร้าง `read_names(n)` return ลิสต์ชื่อ แล้วพิมพ์แต่ละชื่อ",
    conditions=None,
    input_desc="จำนวนคน 1 บรรทัด ตามด้วยชื่อ n บรรทัด",
    output_desc="ชื่อทีละบรรทัด",
    sample_in="3\nAnn\nBen\nCat\n",
    sample_out="Ann\nBen\nCat\n",
    hint="สร้างลิสต์ว่าง วนรับชื่อ n ครั้ง แล้ว return",
    starter="n = int(input())\n\n# สร้าง read_names(n) แล้วพิมพ์ชื่อทีละคน\n",
    code='''def read_names(n):
    names = []
    for i in range(n):
        names.append(input())
    return names

n = int(input())
names = read_names(n)
for name in names:
    print(name)
''',
),
dict(
    file="12_medium.md", answer="12_price_table.py",
    title="🛒 ฝึกฟังก์ชัน — ข้อ 11: ตารางราคา",
    diff="🟡 Medium", axis="ส่ง dict ราคา + หาผลรวม",
    scenario="dict ราคาสินค้า ต้องการพิมพ์ทุกรายการและยอดรวม\n\nสร้าง `show_prices(prices)` พิมพ์แต่ละชิ้น และ `get_total(prices)` return ผลรวม",
    conditions=["ใช้ `.items()` และ `.values()` ได้"],
    input_desc="ไม่มี",
    output_desc="รายการ + Total",
    sample_in=None,
    sample_out="apple: 15\nbanana: 8\nmango: 25\nTotal: 48\n",
    hint="แยกฟังก์ชันแสดงผลกับฟังก์ชันรวมยอด",
    starter='prices = {"apple": 15, "banana": 8, "mango": 25}\n\n# สร้าง show_prices และ get_total\n',
    code='''def show_prices(prices):
    for item, price in prices.items():
        print(f"{item}: {price}")

def get_total(prices):
    total = 0
    for price in prices.values():
        total = total + price
    return total

prices = {"apple": 15, "banana": 8, "mango": 25}
show_prices(prices)
print(f"Total: {get_total(prices)}")
''',
),
dict(
    file="13_challenge.md", answer="13_report_card.py",
    title="📑 ฝึกฟังก์ชัน — ข้อ 12: ใบรายงานผล",
    diff="🔴 Challenge", axis="ค่าเฉลี่ย + ระดับ (ไม่ใช่ A/B/C/F แบบบทเรียน)",
    scenario="ใบรายงานแสดงค่าเฉลี่ยและระดับความพร้อม\n\nสร้าง `get_average(scores)` และ `get_band(avg)` — avg `>= 80` → Ready, `>= 60` → Practice, อื่นๆ → Review",
    conditions=["ห้ามใช้เกรด A/B/C/F แบบ 80/70/60 ของบทเรียน", "พิมพ์ค่าเฉลี่ยทศนิยม 1 ตำแหน่ง"],
    input_desc="ไม่มี",
    output_desc="2 บรรทัด",
    sample_in=None,
    sample_out="Average: 84.3\nBand: Ready\n",
    hint="ประกอบสองฟังก์ชัน — ค่าเฉลี่ยก่อน แล้วค่อยหา band",
    starter="scores = [85, 90, 78]\n\n# สร้าง get_average และ get_band\n",
    code='''def get_average(scores):
    return sum(scores) / len(scores)

def get_band(avg):
    if avg >= 80:
        return "Ready"
    elif avg >= 60:
        return "Practice"
    else:
        return "Review"

scores = [85, 90, 78]
avg = get_average(scores)
print(f"Average: {avg:.1f}")
print(f"Band: {get_band(avg)}")
''',
),
dict(
    file="14_challenge.md", answer="14_wallet.py",
    title="💰 ฝึกฟังก์ชัน — ข้อ 13: กระเป๋าเงินในเกม",
    diff="🔴 Challenge", axis="dict ยอดเงิน + ฟังก์ชันเพิ่ม/ลด",
    scenario="เกมมีกระเป๋าเงินเป็น dict `{\"gold\": 100}`\n\nสร้าง `add_gold(wallet, amount)` และ `spend_gold(wallet, amount)` ที่แก้ค่าใน dict แล้วพิมพ์ยอดคงเหลือ",
    conditions=["เพิ่ม 50 แล้วใช้ไป 30", "พิมพ์ยอดสุดท้าย"],
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="Gold: 120\n",
    hint="ฟังก์ชันแก้ค่าใน dict ที่ส่งเข้ามาได้โดยตรง",
    starter='wallet = {"gold": 100}\n\n# สร้าง add_gold และ spend_gold\n',
    code='''def add_gold(wallet, amount):
    wallet["gold"] = wallet["gold"] + amount

def spend_gold(wallet, amount):
    wallet["gold"] = wallet["gold"] - amount

wallet = {"gold": 100}
add_gold(wallet, 50)
spend_gold(wallet, 30)
print(f"Gold: {wallet['gold']}")
''',
),
dict(
    file="15_challenge.md", answer="15_library.py",
    title="📚 ฝึกฟังก์ชัน — ข้อ 14: ห้องสมุดยืมหนังสือ",
    diff="🔴 Challenge", axis="list + ฟังก์ชันค้นหาชื่อ",
    scenario="รายชื่อหนังสือในชั้นเป็นลิสต์ ต้องการตรวจว่ามีหนังสือหรือไม่\n\nสร้าง `has_book(books, title)` return True/False แล้วรับชื่อจาก input พิมพ์ `Found`/`Not found`",
    conditions=None,
    input_desc="ชื่อหนังสือที่ค้นหา 1 บรรทัด",
    output_desc="Found หรือ Not found",
    sample_in="Math\n",
    sample_out="Found\n",
    hint="วนเทียบทีละชื่อในลิสต์ เจอแล้ว return True",
    starter='books = ["Math", "Science", "Art"]\ntitle = input()\n\n# สร้าง has_book(books, title) แล้วพิมพ์ผล\n',
    code='''def has_book(books, title):
    for b in books:
        if b == title:
            return True
    return False

books = ["Math", "Science", "Art"]
title = input()
if has_book(books, title):
    print("Found")
else:
    print("Not found")
''',
),
dict(
    file="16_challenge.md", answer="16_rpg.py",
    title="🗡️ ฝึกฟังก์ชัน — ข้อ 15: ตัวละคร RPG",
    diff="🔴 Challenge", axis="dict ตัวละคร + หลายฟังก์ชัน",
    scenario="ตัวละครเกมเป็น dict มี `name` และ `hp`\n\nสร้าง `heal(hero, amount)` เพิ่ม hp และ `show(hero)` พิมพ์สถานะ แล้ว heal 20 จาก hp เริ่ม 50",
    conditions=["มีอย่างน้อย 2 ฟังก์ชัน"],
    input_desc="ไม่มี",
    output_desc="สถานะหลังฮีล",
    sample_in=None,
    sample_out="Name: Knight\nHP: 70\n",
    hint="แก้ค่าใน dict ภายใน heal แล้วให้ show พิมพ์ค่าล่าสุด",
    starter='hero = {"name": "Knight", "hp": 50}\n\n# สร้าง heal และ show\n',
    code='''def heal(hero, amount):
    hero["hp"] = hero["hp"] + amount

def show(hero):
    print(f"Name: {hero['name']}")
    print(f"HP: {hero['hp']}")

hero = {"name": "Knight", "hp": 50}
heal(hero, 20)
show(hero)
''',
),
]
