# -*- coding: utf-8 -*-
"""Problem data for weeks 043-048."""

P043 = [
dict(
    file="02_test.md", answer="02_rename.py",
    title="📝 Readability — ข้อ 1: ตั้งชื่อให้สื่อ",
    diff="🟢 Easy", axis="แทน x/y ด้วยชื่อสื่อความหมาย",
    scenario="โค้ดเดิมใช้ `x = 75` และพิมพ์ Pass/Fail จากเกณฑ์ 50\n\nเขียนใหม่โดยใช้ชื่อ `score` และพิมพ์ผลตามตัวอย่าง",
    conditions=["ใช้ชื่อตัวแปรที่สื่อความหมาย"],
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="Pass\n",
    hint=None,
    starter="# เขียนใหม่ให้ชื่อสื่อความหมาย score = 75 เกณฑ์ 50\n",
    code='''score = 75
if score >= 50:
    print("Pass")
else:
    print("Fail")
''',
),
dict(
    file="03_test.md", answer="03_fstring.py",
    title="🧵 Readability — ข้อ 2: ใช้ f-string",
    diff="🟢 Easy", axis="แทนการต่อสตริงด้วย +",
    scenario="โค้ดเดิมต่อสตริงด้วย `+` และ `str()`\n\nรับชื่อและอายุ แล้วพิมพ์ `Name: <name>, Age: <age>` ด้วย f-string",
    conditions=["ใช้ f-string"],
    input_desc="ชื่อ 1 บรรทัด อายุ 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="Sam\n15\n",
    sample_out="Name: Sam, Age: 15\n",
    hint=None,
    starter="name = input()\nage = int(input())\n\n# พิมพ์ด้วย f-string\n",
    code='''name = input()
age = int(input())
print(f"Name: {name}, Age: {age}")
''',
),
dict(
    file="04_test.md", answer="04_constant.py",
    title="🔠 Readability — ข้อ 3: ค่าคงที่ ALL_CAPS",
    diff="🟢 Easy", axis="ใช้ค่าคงที่ UPPERCASE",
    scenario="ร้านลดราคา 10%\n\nกำหนด `DISCOUNT_RATE = 0.1` รับราคา แล้วพิมพ์ราคาสุทธิ `price * (1 - DISCOUNT_RATE)` ทศนิยม 2 ตำแหน่ง",
    conditions=["ต้องมีชื่อ ALL_CAPS"],
    input_desc="ราคาจำนวนจริง 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="200\n",
    sample_out="180.00\n",
    hint=None,
    starter="DISCOUNT_RATE = 0.1\nprice = float(input())\n\n# คำนวณราคาสุทธิ\n",
    code='''DISCOUNT_RATE = 0.1
price = float(input())
final_price = price * (1 - DISCOUNT_RATE)
print(f"{final_price:.2f}")
''',
),
dict(
    file="05_easy.md", answer="05_bool_name.py",
    title="☑️ Readability — ข้อ 4: เก็บผลเปรียบเทียบในชื่อดี",
    diff="🟢 Easy", axis="is_x = เงื่อนไข",
    scenario="เก็บผลการเทียบคะแนนไว้ในตัวแปรชื่อดี\n\nรับคะแนน ตั้ง `is_passed = score >= 50` แล้วพิมพ์ `True`/`False` ของตัวแปรนั้น",
    conditions=["ต้องมีตัวแปรขึ้นต้น is_"],
    input_desc="คะแนนจำนวนเต็ม 1 บรรทัด",
    output_desc="True หรือ False",
    sample_in="61\n",
    sample_out="True\n",
    hint=None,
    starter="score = int(input())\n\n# สร้าง is_passed แล้วพิมพ์\n",
    code='''score = int(input())
is_passed = score >= 50
print(is_passed)
''',
),
dict(
    file="06_easy.md", answer="06_function_split.py",
    title="🧱 Readability — ข้อ 5: แยกฟังก์ชันรวมเลข",
    diff="🟢 Easy", axis="ย้ายลูปไปไว้ในฟังก์ชัน",
    scenario="โค้ดรกที่รวมเลข 1..n อยู่ในโปรแกรมหลัก\n\nสร้าง `get_sum(n)` return ผลรวม แล้วรับ n พิมพ์ผล",
    conditions=["มีฟังก์ชัน get_sum"],
    input_desc="n จำนวนเต็ม 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="4\n",
    sample_out="10\n",
    hint=None,
    starter="n = int(input())\n\n# สร้าง get_sum(n) แล้วพิมพ์ผล\n",
    code='''def get_sum(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

n = int(input())
print(get_sum(n))
''',
),
dict(
    file="07_medium.md", answer="07_clean_bill.py",
    title="🧾 Readability — ข้อ 6: บิลที่อ่านง่าย",
    diff="🟡 Medium", axis="ชื่อสื่อ + f-string + ค่าคงที่",
    scenario="รับราคาอาหารและค่าบริการ คิดยอดรวม\n\nใช้ชื่อที่สื่อความหมาย พิมพ์ใบเสร็จ 3 บรรทัด Food / Service / Total",
    conditions=None,
    input_desc="food และ service เป็นจำนวนเต็มอย่างละ 1 บรรทัด",
    output_desc="3 บรรทัด",
    sample_in="120\n20\n",
    sample_out="Food: 120\nService: 20\nTotal: 140\n",
    hint="ตั้งชื่อให้ตรงความหมาย แล้วจัดรูปแบบด้วย f-string",
    starter="food = int(input())\nservice = int(input())\n\n# พิมพ์ใบเสร็จให้อ่านง่าย\n",
    code='''food = int(input())
service = int(input())
total = food + service
print(f"Food: {food}")
print(f"Service: {service}")
print(f"Total: {total}")
''',
),
dict(
    file="08_medium.md", answer="08_less_comment.py",
    title="💬 Readability — ข้อ 7: ลดคอมเมนต์ซ้ำซ้อน",
    diff="🟡 Medium", axis="ชื่อดีแทนคอมเมนต์ทุกบรรทัด",
    scenario="โค้ดเดิมมีคอมเมนต์อธิบายทุกบรรทัดเพราะชื่อตัวแปรแย่\n\nรับจำนวนชิ้นและราคาต่อชิ้น แล้วพิมพ์ยอดรวมโดยใช้ชื่อดี ไม่ต้องมีคอมเมนต์รก",
    conditions=None,
    input_desc="qty และ price เป็นจำนวนเต็มอย่างละ 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="3\n25\n",
    sample_out="Total: 75\n",
    hint="ชื่อที่ดีทำให้ไม่ต้องอธิบายทุกบรรทัด",
    starter="qty = int(input())\nprice = int(input())\n\n# คำนวณยอดรวม\n",
    code='''qty = int(input())
price = int(input())
total = qty * price
print(f"Total: {total}")
''',
),
dict(
    file="09_medium.md", answer="09_indent_func.py",
    title="📐 Readability — ข้อ 8: เยื้องฟังก์ชันทักทาย",
    diff="🟡 Medium", axis="เยื้อง body ของ def ให้ถูก",
    scenario="สร้าง `greet(name)` ที่พิมพ์ `Hello, <name>` ให้เยื้องถูก แล้วเรียกด้วยชื่อจาก input",
    conditions=None,
    input_desc="ชื่อ 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="Bee\n",
    sample_out="Hello, Bee\n",
    hint="บรรทัดในฟังก์ชันต้องเยื้องเข้าไป",
    starter="name = input()\n\n# สร้าง greet(name) ให้เยื้องถูก\n",
    code='''def greet(name):
    print(f"Hello, {name}")

name = input()
greet(name)
''',
),
dict(
    file="10_medium.md", answer="10_vat_constant.py",
    title="🧮 Readability — ข้อ 9: VAT ด้วยค่าคงที่",
    diff="🟡 Medium", axis="ALL_CAPS + ฟังก์ชัน",
    scenario="กำหนด `VAT_RATE = 0.07`\n\nสร้าง `with_vat(price)` return ราคาหลังบวก VAT แล้วพิมพ์ทศนิยม 2 ตำแหน่ง",
    conditions=["ใช้ค่าคงที่ ALL_CAPS"],
    input_desc="ราคาจำนวนจริง 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="100\n",
    sample_out="107.00\n",
    hint="คูณ (1 + VAT_RATE) ในฟังก์ชัน",
    starter="VAT_RATE = 0.07\nprice = float(input())\n\n# สร้าง with_vat(price) แล้วพิมพ์\n",
    code='''VAT_RATE = 0.07

def with_vat(price):
    return price * (1 + VAT_RATE)

price = float(input())
print(f"{with_vat(price):.2f}")
''',
),
dict(
    file="11_medium.md", answer="11_clean_loop.py",
    title="🔁 Readability — ข้อ 10: ลูปชื่อดี",
    diff="🟡 Medium", axis="ชื่อตัวแปรลูปสื่อความหมาย",
    scenario="พิมพ์รายการผลไม้จากลิสต์ด้วยชื่อตัวแปรที่อ่านรู้เรื่อง\n\nใช้ `fruits = [\"Apple\", \"Banana\", \"Mango\"]` พิมพ์ `Fruit: ...` ทีละบรรทัด",
    conditions=["ห้ามใช้ชื่อตัวแปรลูปว่า x"],
    input_desc="ไม่มี",
    output_desc="3 บรรทัด",
    sample_in=None,
    sample_out="Fruit: Apple\nFruit: Banana\nFruit: Mango\n",
    hint="ตั้งชื่อตัวแปรลูปว่า fruit",
    starter='fruits = ["Apple", "Banana", "Mango"]\n\n# วนพิมพ์ให้อ่านง่าย\n',
    code='''fruits = ["Apple", "Banana", "Mango"]
for fruit in fruits:
    print(f"Fruit: {fruit}")
''',
),
dict(
    file="12_medium.md", answer="12_is_open.py",
    title="🚪 Readability — ข้อ 11: สถานะร้านด้วย is_",
    diff="🟡 Medium", axis="bool ชื่อดี + ข้อความสถานะ",
    scenario="รับชั่วโมงปัจจุบัน (0–23) ร้านเปิดเมื่อ `>= 9` และ `< 18`\n\nเก็บใน `is_open` แล้วพิมพ์ `Open`/`Closed`",
    conditions=["ต้องมีตัวแปร is_open"],
    input_desc="ชั่วโมงจำนวนเต็ม 1 บรรทัด",
    output_desc="Open หรือ Closed",
    sample_in="10\n",
    sample_out="Open\n",
    hint="ใช้ and รวมสองเงื่อนไข แล้วเก็บใน is_open",
    starter="hour = int(input())\n\n# สร้าง is_open แล้วพิมพ์สถานะ\n",
    code='''hour = int(input())
is_open = hour >= 9 and hour < 18
if is_open:
    print("Open")
else:
    print("Closed")
''',
),
dict(
    file="13_challenge.md", answer="13_refactor_report.py",
    title="📊 Readability — ข้อ 12: แยกรายงานเป็นฟังก์ชัน",
    diff="🔴 Challenge", axis="แยกฟังก์ชันหัว/ตัว/ท้ายรายงาน",
    scenario="พิมพ์รายงานสั้นๆ ด้วยฟังก์ชันย่อยให้อ่านง่าย\n\nสร้าง `header()`, `body(score)`, `footer()` แล้วเรียกตามลำดับ รับคะแนนจาก input",
    conditions=["มีอย่างน้อย 3 ฟังก์ชัน"],
    input_desc="คะแนนจำนวนเต็ม 1 บรรทัด",
    output_desc="รายงาน 3 ส่วน",
    sample_in="88\n",
    sample_out="=== REPORT ===\nScore: 88\n=== END ===\n",
    hint="แยกส่วนที่ซ้ำหรือเป็นโครงออกเป็นฟังก์ชัน",
    starter="score = int(input())\n\n# แยก header / body / footer\n",
    code='''def header():
    print("=== REPORT ===")

def body(score):
    print(f"Score: {score}")

def footer():
    print("=== END ===")

score = int(input())
header()
body(score)
footer()
''',
),
dict(
    file="14_challenge.md", answer="14_clean_discount.py",
    title="💸 Readability — ข้อ 13: ส่วนลดที่อ่านรู้เรื่อง",
    diff="🔴 Challenge", axis="ค่าคงที่ + ฟังก์ชัน + ชื่อดี",
    scenario="ถ้าซื้อครบ `MIN_SPEND = 300` ลด `DISCOUNT = 30` ไม่งั้นลด 0\n\nสร้าง `get_discount(total)` return ส่วนลด แล้วพิมพ์ยอดจ่าย",
    conditions=["ใช้ค่าคงที่ ALL_CAPS สองตัว"],
    input_desc="ยอดซื้อจำนวนเต็ม 1 บรรทัด",
    output_desc="2 บรรทัด",
    sample_in="350\n",
    sample_out="Discount: 30\nPay: 320\n",
    hint="ตั้งชื่อค่าคงที่ให้ชัด แล้วให้ฟังก์ชันคืนเฉพาะส่วนลด",
    starter="MIN_SPEND = 300\nDISCOUNT = 30\ntotal = int(input())\n\n# สร้าง get_discount(total) แล้วพิมพ์ผล\n",
    code='''MIN_SPEND = 300
DISCOUNT = 30

def get_discount(total):
    if total >= MIN_SPEND:
        return DISCOUNT
    return 0

total = int(input())
discount = get_discount(total)
print(f"Discount: {discount}")
print(f"Pay: {total - discount}")
''',
),
dict(
    file="15_challenge.md", answer="15_student_card.py",
    title="🪪 Readability — ข้อ 14: บัตรนักเรียนสะอาด",
    diff="🔴 Challenge", axis="dict + ชื่อดี + f-string",
    scenario="ข้อมูลนักเรียนเป็น dict ต้องการพิมพ์บัตรให้อ่านง่าย\n\nใช้ `student = {\"name\": \"Mali\", \"room\": 3, \"score\": 91}` พิมพ์ 3 บรรทัดตามตัวอย่าง",
    conditions=["ใช้ f-string", "ห้ามต่อสตริงด้วย +"],
    input_desc="ไม่มี",
    output_desc="3 บรรทัด",
    sample_in=None,
    sample_out="Name : Mali\nRoom : 3\nScore: 91\n",
    hint="จัดช่องว่างหลังชื่อฟิลด์ให้ตรงตัวอย่าง",
    starter='student = {"name": "Mali", "room": 3, "score": 91}\n\n# พิมพ์บัตรให้อ่านง่าย\n',
    code='''student = {"name": "Mali", "room": 3, "score": 91}
print(f"Name : {student['name']}")
print(f"Room : {student['room']}")
print(f"Score: {student['score']}")
''',
),
dict(
    file="16_challenge.md", answer="16_clean_average.py",
    title="📈 Readability — ข้อ 15: ค่าเฉลี่ยแบบแยกฟังก์ชัน",
    diff="🔴 Challenge", axis="ฟังก์ชันสั้น อ่านรู้เรื่อง",
    scenario="ลิสต์คะแนน `[70, 80, 90]`\n\nสร้าง `get_average(scores)` return ค่าเฉลี่ย แล้วพิมพ์ทศนิยม 1 ตำแหน่งพร้อมป้าย Average",
    conditions=["ชื่อฟังก์ชัน/ตัวแปรสื่อความหมาย"],
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="Average: 80.0\n",
    hint="ใช้ sum/len หรือวนบวกเองในฟังก์ชันสั้นๆ",
    starter="scores = [70, 80, 90]\n\n# สร้าง get_average(scores) แล้วพิมพ์\n",
    code='''def get_average(scores):
    return sum(scores) / len(scores)

scores = [70, 80, 90]
print(f"Average: {get_average(scores):.1f}")
''',
),
]


P044 = [
dict(
    file="02_test.md", answer="02_list_total.py",
    title="📋 ทบทวนรวม — ข้อ 1: รวมคะแนนในลิสต์",
    diff="🟢 Easy", axis="list + ฟังก์ชัน",
    scenario="สร้าง `total_of(scores)` return ผลรวมของลิสต์ แล้วพิมพ์ผลจาก `[10, 20, 30]`",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="60\n",
    hint=None,
    starter="scores = [10, 20, 30]\n\n# สร้าง total_of(scores) แล้วพิมพ์\n",
    code='''def total_of(scores):
    total = 0
    for s in scores:
        total = total + s
    return total

scores = [10, 20, 30]
print(total_of(scores))
''',
),
dict(
    file="03_test.md", answer="03_dict_loop.py",
    title="🗂️ ทบทวนรวม — ข้อ 2: วน dict",
    diff="🟢 Easy", axis="dict.items()",
    scenario="พิมพ์คู่ key/value จาก `points = {\"Ann\": 3, \"Ben\": 5}` เป็น `Ann -> 3` รูปแบบ",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="2 บรรทัด",
    sample_in=None,
    sample_out="Ann -> 3\nBen -> 5\n",
    hint=None,
    starter='points = {"Ann": 3, "Ben": 5}\n\n# วนพิมพ์\n',
    code='''points = {"Ann": 3, "Ben": 5}
for name, value in points.items():
    print(f"{name} -> {value}")
''',
),
dict(
    file="04_test.md", answer="04_set_unique.py",
    title="🔁 ทบทวนรวม — ข้อ 3: นับไม่ซ้ำด้วย set",
    diff="🟢 Easy", axis="set + len",
    scenario="จากลิสต์ชื่อที่มีซ้ำ สร้าง set แล้วพิมพ์จำนวนชื่อที่ไม่ซ้ำ",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="Unique: 3\n",
    hint=None,
    starter='names = ["Ann", "Ben", "Ann", "Cat", "Ben"]\n\n# ใช้ set นับไม่ซ้ำ\n',
    code='''names = ["Ann", "Ben", "Ann", "Cat", "Ben"]
unique = set(names)
print(f"Unique: {len(unique)}")
''',
),
dict(
    file="05_easy.md", answer="05_tuple_info.py",
    title="📦 ทบทวนรวม — ข้อ 4: ข้อมูลห้องด้วย tuple",
    diff="🟢 Easy", axis="tuple index",
    scenario="`room = (\"Grade 9\", \"Room 3\")` พิมพ์ทั้งสองค่าตามตัวอย่าง",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="2 บรรทัด",
    sample_in=None,
    sample_out="Grade 9\nRoom 3\n",
    hint=None,
    starter='room = ("Grade 9", "Room 3")\n\n# พิมพ์สมาชิก\n',
    code='''room = ("Grade 9", "Room 3")
print(room[0])
print(room[1])
''',
),
dict(
    file="06_easy.md", answer="06_append_sort.py",
    title="📥 ทบทวนรวม — ข้อ 5: เพิ่มแล้วเรียง",
    diff="🟢 Easy", axis="append + sort",
    scenario="เริ่มจาก `[5, 1, 3]` เพิ่ม 2 แล้ว sort แล้วพิมพ์ลิสต์",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="[1, 2, 3, 5]\n",
    hint=None,
    starter="nums = [5, 1, 3]\n\n# append 2 แล้ว sort\n",
    code='''nums = [5, 1, 3]
nums.append(2)
nums.sort()
print(nums)
''',
),
dict(
    file="07_medium.md", answer="07_dict_of_lists.py",
    title="📚 ทบทวนรวม — ข้อ 6: dict ของ list",
    diff="🟡 Medium", axis="dict values เป็น list",
    scenario="`scores = {\"Ann\": [80, 90], \"Ben\": [70, 75]}` พิมพ์ชื่อและผลรวมคะแนนของแต่ละคน",
    conditions=["ใช้ฟังก์ชันช่วยรวมลิสต์ได้"],
    input_desc="ไม่มี",
    output_desc="2 บรรทัด",
    sample_in=None,
    sample_out="Ann: 170\nBen: 145\n",
    hint="วน .items() แล้วรวมลิสต์คะแนนของแต่ละคน",
    starter='scores = {"Ann": [80, 90], "Ben": [70, 75]}\n\n# พิมพ์ชื่อและผลรวม\n',
    code='''def total_of(values):
    total = 0
    for v in values:
        total = total + v
    return total

scores = {"Ann": [80, 90], "Ben": [70, 75]}
for name, values in scores.items():
    print(f"{name}: {total_of(values)}")
''',
),
dict(
    file="08_medium.md", answer="08_avg_band.py",
    title="🎯 ทบทวนรวม — ข้อ 7: ค่าเฉลี่ยและแบนด์",
    diff="🟡 Medium", axis="ประกอบฟังก์ชัน (ไม่ใช่เกรด A/B/C/F)",
    scenario="จากลิสต์คะแนน คำนวณค่าเฉลี่ย แล้วจัดแบนด์ Ready/Practice/Review ตามเกณฑ์ 80/60",
    conditions=["ห้ามพิมพ์เกรด A/B/C/F"],
    input_desc="ไม่มี",
    output_desc="2 บรรทัด",
    sample_in=None,
    sample_out="Average: 75.0\nBand: Practice\n",
    hint="แยกฟังก์ชันค่าเฉลี่ยกับฟังก์ชันแบนด์",
    starter="scores = [70, 80, 75]\n\n# ค่าเฉลี่ย + แบนด์\n",
    code='''def get_average(scores):
    return sum(scores) / len(scores)

def get_band(avg):
    if avg >= 80:
        return "Ready"
    elif avg >= 60:
        return "Practice"
    else:
        return "Review"

scores = [70, 80, 75]
avg = get_average(scores)
print(f"Average: {avg:.1f}")
print(f"Band: {get_band(avg)}")
''',
),
dict(
    file="09_medium.md", answer="09_inventory.py",
    title="🏪 ทบทวนรวม — ข้อ 8: สต๊อกสินค้า",
    diff="🟡 Medium", axis="dict อัปเดตค่า",
    scenario="`stock = {\"pen\": 5, \"eraser\": 2}` เพิ่ม pen อีก 3 แล้วพิมพ์ทุกคู่",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="2 บรรทัด",
    sample_in=None,
    sample_out="pen: 8\neraser: 2\n",
    hint="อัปเดตค่าใน dict แล้ววน items",
    starter='stock = {"pen": 5, "eraser": 2}\n\n# เพิ่ม pen แล้วพิมพ์\n',
    code='''stock = {"pen": 5, "eraser": 2}
stock["pen"] = stock["pen"] + 3
for item, qty in stock.items():
    print(f"{item}: {qty}")
''',
),
dict(
    file="10_medium.md", answer="10_filter_names.py",
    title="🔎 ทบทวนรวม — ข้อ 9: กรองชื่อสั้น",
    diff="🟡 Medium", axis="list + ฟังก์ชันกรอง",
    scenario="สร้าง `short_names(names)` return ลิสต์ชื่อที่ `len < 4` จาก `[\"Ann\", \"Bobby\", \"Cy\", \"Diana\"]`",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="['Ann', 'Cy']\n",
    hint="สร้างลิสต์ใหม่แล้ว append ชื่อที่ผ่านเงื่อนไข",
    starter='names = ["Ann", "Bobby", "Cy", "Diana"]\n\n# สร้าง short_names(names) แล้วพิมพ์\n',
    code='''def short_names(names):
    result = []
    for name in names:
        if len(name) < 4:
            result.append(name)
    return result

names = ["Ann", "Bobby", "Cy", "Diana"]
print(short_names(names))
''',
),
dict(
    file="11_medium.md", answer="11_while_count.py",
    title="⏳ ทบทวนรวม — ข้อ 10: while นับถอยหลัง",
    diff="🟡 Medium", axis="while + ตัวนับ",
    scenario="เริ่มจาก n ที่รับมา พิมพ์ n ลงไปถึง 1 ด้วย while",
    conditions=["ใช้ while"],
    input_desc="จำนวนเต็มบวก 1 บรรทัด",
    output_desc="นับถอยหลังทีละบรรทัด",
    sample_in="3\n",
    sample_out="3\n2\n1\n",
    hint="ลดค่าตัวนับทุกรอบจนถึง 0",
    starter="n = int(input())\n\n# นับถอยหลังด้วย while\n",
    code='''n = int(input())
while n > 0:
    print(n)
    n = n - 1
''',
),
dict(
    file="12_medium.md", answer="12_merge_unique.py",
    title="🔗 ทบทวนรวม — ข้อ 11: รวมแล้วไม่ซ้ำ",
    diff="🟡 Medium", axis="สอง list → set",
    scenario="รวม `a = [\"Ann\", \"Ben\"]` กับ `b = [\"Ben\", \"Cat\"]` เป็นชุดไม่ซ้ำ แล้วพิมพ์จำนวน",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="3\n",
    hint="รวมลิสต์ก่อน แล้วแปลงเป็น set",
    starter='a = ["Ann", "Ben"]\nb = ["Ben", "Cat"]\n\n# รวมแล้วไม่ซ้ำ\n',
    code='''a = ["Ann", "Ben"]
b = ["Ben", "Cat"]
combined = a + b
unique = set(combined)
print(len(unique))
''',
),
dict(
    file="13_challenge.md", answer="13_class_roster.py",
    title="👩‍🏫 ทบทวนรวม — ข้อ 12: บัญชีรายชื่อห้อง",
    diff="🔴 Challenge", axis="dict ของ list + ค่าเฉลี่ย",
    scenario="`roster = {\"A\": [80, 90, 70], \"B\": [60, 65, 70]}` พิมพ์ห้องและค่าเฉลี่ยทศนิยม 1 ตำแหน่ง",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="2 บรรทัด",
    sample_in=None,
    sample_out="A: 80.0\nB: 65.0\n",
    hint="วน items แล้วหาค่าเฉลี่ยของลิสต์ในแต่ละห้อง",
    starter='roster = {"A": [80, 90, 70], "B": [60, 65, 70]}\n\n# พิมพ์ค่าเฉลี่ยต่อห้อง\n',
    code='''def get_average(scores):
    return sum(scores) / len(scores)

roster = {"A": [80, 90, 70], "B": [60, 65, 70]}
for room, scores in roster.items():
    print(f"{room}: {get_average(scores):.1f}")
''',
),
dict(
    file="14_challenge.md", answer="14_shop_cart.py",
    title="🛍️ ทบทวนรวม — ข้อ 13: ตะกร้าสินค้า",
    diff="🔴 Challenge", axis="dict ราคา × จำนวน",
    scenario="`prices = {\"pen\": 10, \"book\": 40}` รับชื่อสินค้าและจำนวน แล้วพิมพ์ยอดจ่าย",
    conditions=["สินค้าตรงคีย์ใน dict ตามตัวอย่าง"],
    input_desc="ชื่อสินค้า 1 บรรทัด และจำนวน 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="book\n2\n",
    sample_out="Pay: 80\n",
    hint="ใช้ชื่อเป็นคีย์หาราคา แล้วคูณจำนวน",
    starter='prices = {"pen": 10, "book": 40}\nitem = input()\nqty = int(input())\n\n# คิดยอดจ่าย\n',
    code='''prices = {"pen": 10, "book": 40}
item = input()
qty = int(input())
pay = prices[item] * qty
print(f"Pay: {pay}")
''',
),
dict(
    file="15_challenge.md", answer="15_quiz_check.py",
    title="❓ ทบทวนรวม — ข้อ 14: ตรวจคำตอบควิซ",
    diff="🔴 Challenge", axis="dict คำตอบ + นับคะแนน",
    scenario="`answers = {\"q1\": \"A\", \"q2\": \"C\", \"q3\": \"B\"}` รับคำตอบผู้ใช้ 3 ข้อตามลำดับ q1..q3 นับข้อถูก แล้วพิมพ์คะแนน",
    conditions=None,
    input_desc="คำตอบ 3 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="A\nC\nA\n",
    sample_out="Score: 2\n",
    hint="เทียบทีละข้อกับค่าใน dict ตามลำดับคีย์ที่กำหนด",
    starter='answers = {"q1": "A", "q2": "C", "q3": "B"}\n\n# รับคำตอบ 3 ข้อแล้วให้คะแนน\n',
    code='''answers = {"q1": "A", "q2": "C", "q3": "B"}
score = 0
for key in answers:
    user = input()
    if user == answers[key]:
        score = score + 1
print(f"Score: {score}")
''',
),
dict(
    file="16_challenge.md", answer="16_leaderboard.py",
    title="🏁 ทบทวนรวม — ข้อ 15: กระดานผู้นำ",
    diff="🔴 Challenge", axis="หาค่าสูงสุดด้วยมือจาก dict",
    scenario="`board = {\"Ann\": 12, \"Ben\": 18, \"Cat\": 15}` หาคนคะแนนสูงสุดด้วยการวนเอง (ห้าม max) แล้วพิมพ์ชื่อ",
    conditions=["ห้ามใช้ max()"],
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="Ben\n",
    hint="เก็บทั้งชื่อและคะแนนที่ดีที่สุดขณะวน",
    starter='board = {"Ann": 12, "Ben": 18, "Cat": 15}\n\n# หาคนคะแนนสูงสุด\n',
    code='''board = {"Ann": 12, "Ben": 18, "Cat": 15}
best_name = ""
best_score = -1
for name, score in board.items():
    if score > best_score:
        best_score = score
        best_name = name
print(best_name)
''',
),
]
