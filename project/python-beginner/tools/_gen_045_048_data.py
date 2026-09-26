# -*- coding: utf-8 -*-
"""Problem data for weeks 045-048."""

P045 = [
dict(
    file="02_test.md", answer="02_collect_names.py",
    title="🧠 รวมตรรกะ — ข้อ 1: เก็บชื่อ 3 คน",
    diff="🟢 Easy", axis="loop + append จาก input",
    scenario="รับชื่อ 3 คนเก็บในลิสต์ แล้วพิมพ์ทีละชื่อ",
    conditions=["ใช้ for + append"],
    input_desc="ชื่อ 3 บรรทัด",
    output_desc="3 บรรทัด",
    sample_in="Ann\nBen\nCat\n",
    sample_out="Ann\nBen\nCat\n",
    hint=None,
    starter="names = []\n\n# รับ 3 ชื่อแล้วพิมพ์\n",
    code='''names = []
for i in range(3):
    names.append(input())
for name in names:
    print(name)
''',
),
dict(
    file="03_test.md", answer="03_sum_n.py",
    title="➕ รวมตรรกะ — ข้อ 2: รวม n จำนวน",
    diff="🟢 Easy", axis="รับ n แล้วสะสมผลรวม",
    scenario="รับ n แล้วรับจำนวนจริง/เต็ม n ตัว รวมยอดแล้วพิมพ์",
    conditions=None,
    input_desc="n แล้วตามด้วย n จำนวนเต็ม",
    output_desc="1 บรรทัด",
    sample_in="3\n10\n20\n30\n",
    sample_out="60\n",
    hint=None,
    starter="n = int(input())\n\n# รวม n จำนวน\n",
    code='''n = int(input())
total = 0
for i in range(n):
    total = total + int(input())
print(total)
''',
),
dict(
    file="04_test.md", answer="04_first_letter.py",
    title="🔤 รวมตรรกะ — ข้อ 3: ชื่อขึ้นต้นด้วย A",
    diff="🟢 Easy", axis="เทียบตัวอักษรแรกด้วย index (ไม่ใช้ startswith)",
    scenario="รับชื่อ 1 คำ ถ้าตัวอักษรแรกเป็น `A` พิมพ์ `Yes` ไม่งั้น `No`\n\nห้ามใช้ `.startswith()`",
    conditions=["ใช้ `name[0]`"],
    input_desc="ชื่อ 1 บรรทัด",
    output_desc="Yes หรือ No",
    sample_in="Ann\n",
    sample_out="Yes\n",
    hint=None,
    starter="name = input()\n\n# ตรวจตัวอักษรแรกโดยไม่ใช้ startswith\n",
    code='''name = input()
if name[0] == "A":
    print("Yes")
else:
    print("No")
''',
),
dict(
    file="05_easy.md", answer="05_tool_pick.py",
    title="🧰 รวมตรรกะ — ข้อ 4: เลือกเครื่องมือ",
    diff="🟢 Easy", axis="แม็พโจทย์ → โครงสร้างข้อมูล",
    scenario="รับคำอธิบายสั้น แล้วแนะนำเครื่องมือ\n\n`unique names` → set, `lookup price` → dict, `ordered scores` → list, อื่นๆ → other",
    conditions=None,
    input_desc="ข้อความ 1 บรรทัด",
    output_desc="ชื่อเครื่องมือ",
    sample_in="lookup price\n",
    sample_out="dict\n",
    hint=None,
    starter="need = input()\n\n# แนะนำเครื่องมือ\n",
    code='''need = input()
if need == "unique names":
    print("set")
elif need == "lookup price":
    print("dict")
elif need == "ordered scores":
    print("list")
else:
    print("other")
''',
),
dict(
    file="06_easy.md", answer="06_even_list.py",
    title="2️⃣ รวมตรรกะ — ข้อ 5: กรองเลขคู่",
    diff="🟢 Easy", axis="สร้างลิสต์ผลลัพธ์",
    scenario="จาก `[1, 2, 3, 4, 5, 6]` สร้างลิสต์เลขคู่แล้วพิมพ์",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="[2, 4, 6]\n",
    hint=None,
    starter="nums = [1, 2, 3, 4, 5, 6]\n\n# กรองเลขคู่\n",
    code='''nums = [1, 2, 3, 4, 5, 6]
evens = []
for n in nums:
    if n % 2 == 0:
        evens.append(n)
print(evens)
''',
),
dict(
    file="07_medium.md", answer="07_filter_a_names.py",
    title="📝 รวมตรรกะ — ข้อ 6: เก็บแล้วกรองชื่อ A",
    diff="🟡 Medium", axis="รับหลายชื่อ + กรองตัวอักษรแรก",
    scenario="รับชื่อ 5 คน เก็บในลิสต์ แล้วพิมพ์เฉพาะชื่อที่ขึ้นต้นด้วย `A` (ใช้ index ห้าม startswith)",
    conditions=["ห้าม `.startswith()`"],
    input_desc="ชื่อ 5 บรรทัด",
    output_desc="เฉพาะชื่อที่ขึ้นต้นด้วย A",
    sample_in="Ann\nBen\nAmy\nCat\nAda\n",
    sample_out="Ann\nAmy\nAda\n",
    hint="เก็บครบก่อน แล้วค่อยวนกรองด้วย name[0]",
    starter="names = []\n\n# รับ 5 ชื่อ แล้วพิมพ์ที่ขึ้นต้นด้วย A\n",
    code='''names = []
for i in range(5):
    names.append(input())
for name in names:
    if name[0] == "A":
        print(name)
''',
),
dict(
    file="08_medium.md", answer="08_steps_checklist.py",
    title="🧭 รวมตรรกะ — ข้อ 7: เช็กลิสต์ขั้นตอน",
    diff="🟡 Medium", axis="พิมพ์ลำดับคิดโจทย์",
    scenario="รับประเภทงาน `sum` / `lookup` / `unique` แล้วพิมพ์ขั้นตอนสั้นๆ ตามตัวอย่าง",
    conditions=None,
    input_desc="ประเภทงาน 1 บรรทัด",
    output_desc="2 บรรทัดขั้นตอน",
    sample_in="lookup\n",
    sample_out="1) choose dict\n2) use key\n",
    hint="แต่ละประเภทงานมีเครื่องมือคนละแบบ",
    starter="task = input()\n\n# พิมพ์ขั้นตอนตามประเภทงาน\n",
    code='''task = input()
if task == "sum":
    print("1) choose list")
    print("2) loop add")
elif task == "lookup":
    print("1) choose dict")
    print("2) use key")
else:
    print("1) choose set")
    print("2) convert list")
''',
),
dict(
    file="09_medium.md", answer="09_score_map.py",
    title="🗺️ รวมตรรกะ — ข้อ 8: แผนที่คะแนน",
    diff="🟡 Medium", axis="สร้าง dict จาก input",
    scenario="รับ n แล้วรับคู่ชื่อ/คะแนน n รอบ เก็บใน dict แล้วพิมพ์ทุกคู่",
    conditions=None,
    input_desc="n แล้วตามด้วยชื่อและคะแนนสลับกัน 2n บรรทัด",
    output_desc="คู่ชื่อคะแนน",
    sample_in="2\nAnn\n80\nBen\n90\n",
    sample_out="Ann: 80\nBen: 90\n",
    hint="วน n ครั้ง รับชื่อแล้วรับคะแนน เก็บลง dict",
    starter="n = int(input())\nscores = {}\n\n# สร้าง dict แล้วพิมพ์\n",
    code='''n = int(input())
scores = {}
for i in range(n):
    name = input()
    score = int(input())
    scores[name] = score
for name, score in scores.items():
    print(f"{name}: {score}")
''',
),
dict(
    file="10_medium.md", answer="10_threshold.py",
    title="🎚️ รวมตรรกะ — ข้อ 9: นับผ่านเกณฑ์",
    diff="🟡 Medium", axis="รับลิสต์ตัวเลข + นับ",
    scenario="รับ n แล้วรับคะแนน n ตัว นับว่ากี่ตัว `>= 50`",
    conditions=None,
    input_desc="n แล้วตามด้วย n คะแนน",
    output_desc="1 บรรทัด",
    sample_in="4\n40\n55\n70\n49\n",
    sample_out="Passed: 2\n",
    hint="สะสมตัวนับขณะวนรับค่า",
    starter="n = int(input())\n\n# นับคะแนนที่ >= 50\n",
    code='''n = int(input())
count = 0
for i in range(n):
    score = int(input())
    if score >= 50:
        count = count + 1
print(f"Passed: {count}")
''',
),
dict(
    file="11_medium.md", answer="11_menu_system.py",
    title="🎛️ รวมตรรกะ — ข้อ 10: เมนูเล็กๆ",
    diff="🟡 Medium", axis="เลือกการทำงานจากเมนู",
    scenario="รับคำสั่ง `add` หรือ `mul` และเลขสองตัว แล้วพิมพ์ผล",
    conditions=None,
    input_desc="คำสั่ง 1 บรรทัด แล้วเลข 2 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="add\n2\n5\n",
    sample_out="7\n",
    hint="แตกโจทย์: อ่านคำสั่งก่อน แล้วค่อยคำนวณ",
    starter="cmd = input()\na = int(input())\nb = int(input())\n\n# คำนวณตามคำสั่ง\n",
    code='''cmd = input()
a = int(input())
b = int(input())
if cmd == "add":
    print(a + b)
else:
    print(a * b)
''',
),
dict(
    file="12_medium.md", answer="12_word_len_list.py",
    title="📏 รวมตรรกะ — ข้อ 11: ความยาวคำ",
    diff="🟡 Medium", axis="list ความยาวจาก list คำ",
    scenario="จาก `words = [\"hi\", \"python\", \"go\"]` สร้างลิสต์ความยาวแล้วพิมพ์",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="[2, 6, 2]\n",
    hint="append len ของแต่ละคำ",
    starter='words = ["hi", "python", "go"]\n\n# สร้างลิสต์ความยาว\n',
    code='''words = ["hi", "python", "go"]
lengths = []
for w in words:
    lengths.append(len(w))
print(lengths)
''',
),
dict(
    file="13_challenge.md", answer="13_prefix_report.py",
    title="📊 รวมตรรกะ — ข้อ 12: รายงานกลุ่มตัวอักษรแรก",
    diff="🔴 Challenge", axis="จัดกลุ่มด้วย dict โดยไม่ใช้ startswith",
    scenario="รับชื่อ 4 คน นับว่ามีกี่คนที่ขึ้นต้นด้วย `A` และ `B` (ตัวอื่นไม่นับ) พิมพ์ตามตัวอย่าง",
    conditions=["ห้าม `.startswith()`", "ใช้ name[0]"],
    input_desc="ชื่อ 4 บรรทัด",
    output_desc="2 บรรทัด",
    sample_in="Ann\nBen\nAmy\nCat\n",
    sample_out="A: 2\nB: 1\n",
    hint="ใช้ตัวนับสองตัวหรือ dict นับจากตัวอักษรแรก",
    starter="# รับ 4 ชื่อ แล้วนับที่ขึ้นต้นด้วย A และ B\n",
    code='''count_a = 0
count_b = 0
for i in range(4):
    name = input()
    if name[0] == "A":
        count_a = count_a + 1
    elif name[0] == "B":
        count_b = count_b + 1
print(f"A: {count_a}")
print(f"B: {count_b}")
''',
),
dict(
    file="14_challenge.md", answer="14_checkout.py",
    title="💳 รวมตรรกะ — ข้อ 13: เช็คเอาต์หลายชิ้น",
    diff="🔴 Challenge", axis="list ราคา + ส่วนลดตามยอด",
    scenario="รับ n แล้วรับราคาสินค้า n ชิ้น รวมยอด ถ้า `>= 200` ลด 20 แล้วพิมพ์ยอดจ่าย",
    conditions=None,
    input_desc="n แล้วตามด้วย n ราคา",
    output_desc="1 บรรทัด",
    sample_in="3\n80\n70\n60\n",
    sample_out="Pay: 190\n",
    hint="รวมก่อน แล้วค่อยตัดสินใจส่วนลด",
    starter="n = int(input())\n\n# รวมยอด แล้วคิดส่วนลด\n",
    code='''n = int(input())
total = 0
for i in range(n):
    total = total + int(input())
if total >= 200:
    total = total - 20
print(f"Pay: {total}")
''',
),
dict(
    file="15_challenge.md", answer="15_attendance.py",
    title="📅 รวมตรรกะ — ข้อ 14: เช็กชื่อเข้าคลาส",
    diff="🔴 Challenge", axis="list + ค้นหา",
    scenario="รายชื่อในคลาส `roster = [\"Ann\", \"Ben\", \"Cat\"]` รับชื่อ แล้วพิมพ์ `Present` หรือ `Absent`",
    conditions=None,
    input_desc="ชื่อ 1 บรรทัด",
    output_desc="Present หรือ Absent",
    sample_in="Ben\n",
    sample_out="Present\n",
    hint="วนเทียบทีละชื่อ หรือใช้ in",
    starter='roster = ["Ann", "Ben", "Cat"]\nname = input()\n\n# ตรวจว่าอยู่ในคลาสไหม\n',
    code='''roster = ["Ann", "Ben", "Cat"]
name = input()
found = False
for student in roster:
    if student == name:
        found = True
if found:
    print("Present")
else:
    print("Absent")
''',
),
dict(
    file="16_challenge.md", answer="16_mini_system.py",
    title="🖥️ รวมตรรกะ — ข้อ 15: ระบบเล็กเก็บคะแนน",
    diff="🔴 Challenge", axis="รวม input/dict/function",
    scenario="สร้างระบบเล็ก: รับชื่อและคะแนน 3 คน เก็บใน dict สร้าง `average(scores_dict)` return ค่าเฉลี่ยของทุกคน แล้วพิมพ์ค่าเฉลี่ยทศนิยม 1 ตำแหน่ง",
    conditions=["มีฟังก์ชัน average"],
    input_desc="ชื่อและคะแนนสลับกัน 6 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="Ann\n80\nBen\n70\nCat\n90\n",
    sample_out="Average: 80.0\n",
    hint="เก็บครบใน dict ก่อน แล้วส่ง values ไปคิดค่าเฉลี่ย",
    starter="scores = {}\n\n# รับ 3 คน แล้วคิดค่าเฉลี่ยรวม\n",
    code='''def average(scores_dict):
    total = 0
    count = 0
    for value in scores_dict.values():
        total = total + value
        count = count + 1
    return total / count

scores = {}
for i in range(3):
    name = input()
    score = int(input())
    scores[name] = score
print(f"Average: {average(scores):.1f}")
''',
),
]


P046 = [
dict(
    file="02_test.md", answer="02_trace_max.py",
    title="👀 อ่านโค้ด — ข้อ 1: หาค่ามากสุด",
    diff="🟢 Easy", axis="ไล่หาค่ามากสุดด้วยมือ",
    scenario="เขียนโปรแกรมหาค่ามากสุดจาก `[3, 7, 2, 9, 4]` ด้วยการวนเอง แล้วพิมพ์ผล",
    conditions=["ห้าม max()"],
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="9\n",
    hint=None,
    starter="numbers = [3, 7, 2, 9, 4]\n\n# หาค่ามากสุดด้วยการวน\n",
    code='''numbers = [3, 7, 2, 9, 4]
result = numbers[0]
for num in numbers:
    if num > result:
        result = num
print(result)
''',
),
dict(
    file="03_test.md", answer="03_double_list.py",
    title="✖️ อ่านโค้ด — ข้อ 2: คูณสองทุกตัว",
    diff="🟢 Easy", axis="ฟังก์ชันเรียกฟังก์ชัน สร้าง list ใหม่",
    scenario="สร้าง `double(x)` และ `apply_all(lst)` ที่คืนลิสต์ค่าคูณสอง จาก `[1, 2, 3]`",
    conditions=["apply_all เรียก double"],
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="[2, 4, 6]\n",
    hint=None,
    starter="nums = [1, 2, 3]\n\n# สร้าง double และ apply_all\n",
    code='''def double(x):
    return x * 2

def apply_all(lst):
    result = []
    for item in lst:
        result.append(double(item))
    return result

nums = [1, 2, 3]
print(apply_all(nums))
''',
),
dict(
    file="04_test.md", answer="04_count_steps.py",
    title="🧮 อ่านโค้ด — ข้อ 3: นับรอบลูป",
    diff="🟢 Easy", axis="เข้าใจว่า range ทำงานกี่รอบ",
    scenario="พิมพ์จำนวนรอบของ `for i in range(5):` โดยให้โปรแกรมนับเองแล้วพิมพ์",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="5\n",
    hint=None,
    starter="count = 0\n\n# นับรอบ range(5)\n",
    code='''count = 0
for i in range(5):
    count = count + 1
print(count)
''',
),
dict(
    file="05_easy.md", answer="05_running_total.py",
    title="🏃 อ่านโค้ด — ข้อ 4: ยอดสะสมทีละขั้น",
    diff="🟢 Easy", axis="พิมพ์ยอดสะสมระหว่างทาง",
    scenario="จาก `[5, 10, 15]` พิมพ์ยอดสะสมหลังบวกแต่ละตัว",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="3 บรรทัด",
    sample_in=None,
    sample_out="5\n15\n30\n",
    hint=None,
    starter="nums = [5, 10, 15]\n\n# พิมพ์ยอดสะสมทีละขั้น\n",
    code='''nums = [5, 10, 15]
total = 0
for n in nums:
    total = total + n
    print(total)
''',
),
dict(
    file="06_easy.md", answer="06_compose.py",
    title="🔗 อ่านโค้ด — ข้อ 5: ประกอบฟังก์ชัน",
    diff="🟢 Easy", axis="อ่านลำดับการเรียก",
    scenario="สร้าง `inc(n)` return n+1 และ `square(n)` return n*n แล้วพิมพ์ `square(inc(3))`",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="16\n",
    hint=None,
    starter="# สร้าง inc และ square แล้วประกอบกันกับ 3\n",
    code='''def inc(n):
    return n + 1

def square(n):
    return n * n

print(square(inc(3)))
''',
),
dict(
    file="07_medium.md", answer="07_trace_dict.py",
    title="🗂️ อ่านโค้ด — ข้อ 6: ไล่ค่าใน dict",
    diff="🟡 Medium", axis="สะสมจาก values",
    scenario="จาก `data = {\"a\": 2, \"b\": 5, \"c\": 3}` รวม values แล้วพิมพ์",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="10\n",
    hint="วน .values() แล้วบวก",
    starter='data = {"a": 2, "b": 5, "c": 3}\n\n# รวม values\n',
    code='''data = {"a": 2, "b": 5, "c": 3}
total = 0
for value in data.values():
    total = total + value
print(total)
''',
),
dict(
    file="08_medium.md", answer="08_build_squares.py",
    title="🟦 อ่านโค้ด — ข้อ 7: สร้างลิสต์กำลังสอง",
    diff="🟡 Medium", axis="ฟังก์ชันคืน list",
    scenario="สร้าง `squares(n)` return ลิสต์กำลังสองของ 1..n แล้วพิมพ์ `squares(4)`",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="[1, 4, 9, 16]\n",
    hint="append i*i ในลูป 1..n",
    starter="# สร้าง squares(n) แล้วพิมพ์ squares(4)\n",
    code='''def squares(n):
    result = []
    for i in range(1, n + 1):
        result.append(i * i)
    return result

print(squares(4))
''',
),
dict(
    file="09_medium.md", answer="09_filter_map.py",
    title="🧭 อ่านโค้ด — ข้อ 8: กรองแล้วแปลง",
    diff="🟡 Medium", axis="สองขั้นในฟังก์ชัน",
    scenario="จาก `[1, 2, 3, 4, 5]` คืนลิสต์เลขคี่ที่คูณสองแล้ว `[2, 6, 10]`",
    conditions=["มีฟังก์ชันอย่างน้อย 1 ตัว"],
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="[2, 6, 10]\n",
    hint="เลือกเฉพาะคี่ แล้วคูณสองก่อน append",
    starter="nums = [1, 2, 3, 4, 5]\n\n# กรองคี่แล้วคูณสอง\n",
    code='''def odd_doubled(nums):
    result = []
    for n in nums:
        if n % 2 != 0:
            result.append(n * 2)
    return result

nums = [1, 2, 3, 4, 5]
print(odd_doubled(nums))
''',
),
dict(
    file="10_medium.md", answer="10_nested_call.py",
    title="📞 อ่านโค้ด — ข้อ 9: เรียกซ้อนในลูป",
    diff="🟡 Medium", axis="เรียกฟังก์ชันในลูป",
    scenario="สร้าง `label(n)` return ข้อความ `N=<n>` แล้วพิมพ์สำหรับทุกค่าใน `[1, 2, 3]`",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="3 บรรทัด",
    sample_in=None,
    sample_out="N=1\nN=2\nN=3\n",
    hint="ในลูปเรียกฟังก์ชันแล้วพิมพ์ผล",
    starter="nums = [1, 2, 3]\n\n# สร้าง label แล้วใช้ในลูป\n",
    code='''def label(n):
    return f"N={n}"

nums = [1, 2, 3]
for n in nums:
    print(label(n))
''',
),
dict(
    file="11_medium.md", answer="11_min_trace.py",
    title="📉 อ่านโค้ด — ข้อ 10: หาค่าน้อยสุด",
    diff="🟡 Medium", axis="กลับเงื่อนไขจาก max",
    scenario="หาค่าน้อยสุดจาก `[8, 3, 5, 2, 9]` ด้วยมือ แล้วพิมพ์",
    conditions=["ห้าม min()"],
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="2\n",
    hint="เริ่มจากตัวแรก แล้วอัปเดตเมื่อเจอค่าน้อยกว่า",
    starter="nums = [8, 3, 5, 2, 9]\n\n# หาค่าน้อยสุด\n",
    code='''nums = [8, 3, 5, 2, 9]
result = nums[0]
for n in nums:
    if n < result:
        result = n
print(result)
''',
),
dict(
    file="12_medium.md", answer="12_pair_sum.py",
    title="🤝 อ่านโค้ด — ข้อ 11: รวมคู่ขนาน",
    diff="🟡 Medium", axis="ใช้ index เดินสองลิสต์",
    scenario="`a = [1, 2, 3]` และ `b = [4, 5, 6]` สร้างลิสต์ผลบวกทีละคู่",
    conditions=["ห้าม zip()"],
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="[5, 7, 9]\n",
    hint="วนด้วย range(len(a)) แล้วบวก a[i]+b[i]",
    starter="a = [1, 2, 3]\nb = [4, 5, 6]\n\n# รวมทีละคู่\n",
    code='''a = [1, 2, 3]
b = [4, 5, 6]
result = []
for i in range(len(a)):
    result.append(a[i] + b[i])
print(result)
''',
),
dict(
    file="13_challenge.md", answer="13_pipeline.py",
    title="🏭 อ่านโค้ด — ข้อ 12: ท่อแปลงข้อมูล",
    diff="🔴 Challenge", axis="หลายฟังก์ชันต่อกันคืน list",
    scenario="สร้าง `add_one_all(lst)` และ `only_even(lst)` แล้วนำ `[1, 2, 3, 4]` ผ่าน add_one_all ก่อน แล้ว only_even",
    conditions=["ผลสุดท้าย [2, 4]"],
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="[2, 4]\n",
    hint="ไล่ลำดับ: +1 ทั้งลิสต์ก่อน แล้วค่อยกรองเลขคู่",
    starter="nums = [1, 2, 3, 4]\n\n# สร้าง add_one_all และ only_even แล้วต่อกัน\n",
    code='''def add_one_all(lst):
    result = []
    for n in lst:
        result.append(n + 1)
    return result

def only_even(lst):
    result = []
    for n in lst:
        if n % 2 == 0:
            result.append(n)
    return result

nums = [1, 2, 3, 4]
print(only_even(add_one_all(nums)))
''',
),
dict(
    file="14_challenge.md", answer="14_freq.py",
    title="📊 อ่านโค้ด — ข้อ 13: นับความถี่",
    diff="🔴 Challenge", axis="สร้าง dict นับจาก list",
    scenario="จาก `words = [\"a\", \"b\", \"a\", \"c\", \"b\", \"a\"]` สร้าง dict ความถี่แล้วพิมพ์ตามลำดับคีย์ที่พบครั้งแรก a/b/c",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="3 บรรทัด",
    sample_in=None,
    sample_out="a: 3\nb: 2\nc: 1\n",
    hint="ถ้าคีย์ยังไม่มีให้ตั้ง 1 ถ้ามีแล้วบวกเพิ่ม",
    starter='words = ["a", "b", "a", "c", "b", "a"]\n\n# นับความถี่แล้วพิมพ์\n',
    code='''words = ["a", "b", "a", "c", "b", "a"]
freq = {}
for w in words:
    if w in freq:
        freq[w] = freq[w] + 1
    else:
        freq[w] = 1
for key, value in freq.items():
    print(f"{key}: {value}")
''',
),
dict(
    file="15_challenge.md", answer="15_matrix_sum.py",
    title="▦ อ่านโค้ด — ข้อ 14: รวมลิสต์ซ้อน",
    diff="🔴 Challenge", axis="nested list รวมทุกค่า",
    scenario="`rows = [[1, 2], [3, 4], [5]]` รวมทุกจำนวนแล้วพิมพ์",
    conditions=["ใช้ลูปซ้อน"],
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="15\n",
    hint="ลูปแถวก่อน แล้วลูปสมาชิกในแถว",
    starter="rows = [[1, 2], [3, 4], [5]]\n\n# รวมทุกค่า\n",
    code='''rows = [[1, 2], [3, 4], [5]]
total = 0
for row in rows:
    for n in row:
        total = total + n
print(total)
''',
),
dict(
    file="16_challenge.md", answer="16_explain_flow.py",
    title="🧾 อ่านโค้ด — ข้อ 15: สรุปผลหลังไล่โค้ด",
    diff="🔴 Challenge", axis="จำลองผลโปรแกรมสั้นๆ",
    scenario="จำลองโปรแกรม: เริ่ม `n = 1` แล้วทำ `n = n * 2` สามครั้ง พิมพ์ค่าสุดท้าย",
    conditions=["ใช้ลูป"],
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="8\n",
    hint="คูณสองสามครั้งจาก 1 ได้ 8",
    starter="n = 1\n\n# คูณสองสามครั้ง\n",
    code='''n = 1
for i in range(3):
    n = n * 2
print(n)
''',
),
]


P047 = [
dict(
    file="02_test.md", answer="02_basics_mix.py",
    title="🧩 ทบทวนปิด — ข้อ 1: input คำนวณพิมพ์",
    diff="🟢 Easy", axis="สูตรพื้นฐาน Phase 1",
    scenario="รับราคาและจำนวน คิดยอดรวมแล้วพิมพ์",
    conditions=None,
    input_desc="ราคาและจำนวน เป็นจำนวนเต็มอย่างละ 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="25\n4\n",
    sample_out="Total: 100\n",
    hint=None,
    starter="price = int(input())\nqty = int(input())\n\n# คิดยอดรวม\n",
    code='''price = int(input())
qty = int(input())
print(f"Total: {price * qty}")
''',
),
dict(
    file="03_test.md", answer="03_branch_loop.py",
    title="🔀 ทบทวนปิด — ข้อ 2: เงื่อนไขในลูป",
    diff="🟢 Easy", axis="for + if",
    scenario="พิมพ์เลข 1 ถึง 10 เฉพาะเลขคู่",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="เลขคู่ทีละบรรทัด",
    sample_in=None,
    sample_out="2\n4\n6\n8\n10\n",
    hint=None,
    starter="# พิมพ์เลขคู่ 1..10\n",
    code='''for i in range(1, 11):
    if i % 2 == 0:
        print(i)
''',
),
dict(
    file="04_test.md", answer="04_list_dict.py",
    title="📚 ทบทวนปิด — ข้อ 3: list กับ dict",
    diff="🟢 Easy", axis="collections พื้นฐาน",
    scenario="สร้าง dict จากสองลิสต์คู่กัน `keys=[\"a\",\"b\"]` `vals=[1,2]` แล้วพิมพ์",
    conditions=["ห้าม zip"],
    input_desc="ไม่มี",
    output_desc="2 บรรทัด",
    sample_in=None,
    sample_out="a: 1\nb: 2\n",
    hint=None,
    starter='keys = ["a", "b"]\nvals = [1, 2]\n\n# สร้าง dict แล้วพิมพ์\n',
    code='''keys = ["a", "b"]
vals = [1, 2]
data = {}
for i in range(len(keys)):
    data[keys[i]] = vals[i]
for key, value in data.items():
    print(f"{key}: {value}")
''',
),
dict(
    file="05_easy.md", answer="05_function_return.py",
    title="🔁 ทบทวนปิด — ข้อ 4: ฟังก์ชันคืนค่า",
    diff="🟢 Easy", axis="def + return",
    scenario="สร้าง `area(w, h)` return พื้นที่ แล้วพิมพ์จาก input",
    conditions=None,
    input_desc="w และ h จำนวนเต็มอย่างละ 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="3\n7\n",
    sample_out="21\n",
    hint=None,
    starter="w = int(input())\nh = int(input())\n\n# สร้าง area(w, h) แล้วพิมพ์\n",
    code='''def area(w, h):
    return w * h

w = int(input())
h = int(input())
print(area(w, h))
''',
),
dict(
    file="06_easy.md", answer="06_ready_check.py",
    title="✅ ทบทวนปิด — ข้อ 5: เช็กความพร้อมสั้นๆ",
    diff="🟢 Easy", axis="คะแนน readiness ง่ายๆ",
    scenario="รับจำนวนหัวข้อที่มั่นใจ (0–10) ถ้า `>= 7` พิมพ์ `Ready` ไม่งั้น `Review`",
    conditions=None,
    input_desc="จำนวนเต็ม 1 บรรทัด",
    output_desc="Ready หรือ Review",
    sample_in="8\n",
    sample_out="Ready\n",
    hint=None,
    starter="confident = int(input())\n\n# ประเมินความพร้อม\n",
    code='''confident = int(input())
if confident >= 7:
    print("Ready")
else:
    print("Review")
''',
),
dict(
    file="07_medium.md", answer="07_student_avg.py",
    title="🎓 ทบทวนปิด — ข้อ 6: ค่าเฉลี่ยนักเรียน",
    diff="🟡 Medium", axis="dict ของ list + ฟังก์ชัน",
    scenario="`data = {\"Ann\": [80, 90], \"Ben\": [70, 80]}` พิมพ์ค่าเฉลี่ยแต่ละคนทศนิยม 1 ตำแหน่ง",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="2 บรรทัด",
    sample_in=None,
    sample_out="Ann: 85.0\nBen: 75.0\n",
    hint="ใช้ฟังก์ชันค่าเฉลี่ยกับลิสต์ของแต่ละคน",
    starter='data = {"Ann": [80, 90], "Ben": [70, 80]}\n\n# พิมพ์ค่าเฉลี่ย\n',
    code='''def get_average(scores):
    return sum(scores) / len(scores)

data = {"Ann": [80, 90], "Ben": [70, 80]}
for name, scores in data.items():
    print(f"{name}: {get_average(scores):.1f}")
''',
),
dict(
    file="08_medium.md", answer="08_unique_visitors.py",
    title="👥 ทบทวนปิด — ข้อ 7: ผู้เข้าชมไม่ซ้ำ",
    diff="🟡 Medium", axis="set จาก list",
    scenario="รับ n แล้วรับชื่อ n คน พิมพ์จำนวนชื่อไม่ซ้ำ",
    conditions=None,
    input_desc="n แล้วตามด้วย n ชื่อ",
    output_desc="1 บรรทัด",
    sample_in="5\nAnn\nBen\nAnn\nCat\nBen\n",
    sample_out="Unique: 3\n",
    hint="เก็บในลิสต์หรือเพิ่มเข้า set ทีละชื่อ",
    starter="n = int(input())\n\n# นับชื่อไม่ซ้ำ\n",
    code='''n = int(input())
names = []
for i in range(n):
    names.append(input())
print(f"Unique: {len(set(names))}")
''',
),
dict(
    file="09_medium.md", answer="09_budget.py",
    title="💵 ทบทวนปิด — ข้อ 8: งบประมาณ",
    diff="🟡 Medium", axis="รวมรายจ่าย + เทียบงบ",
    scenario="รับงบประมาณ แล้วรับรายจ่าย 3 รายการ ถ้าเหลือเงินพิมพ์ `OK` พร้อมเงินเหลือ ไม่งั้น `Over`",
    conditions=None,
    input_desc="งบ 1 บรรทัด และรายจ่าย 3 บรรทัด",
    output_desc="OK พร้อมยอด หรือ Over",
    sample_in="100\n20\n30\n40\n",
    sample_out="OK 10\n",
    hint="รวมรายจ่ายก่อนเทียบกับงบ",
    starter="budget = int(input())\n\n# รับรายจ่าย 3 รายการแล้วสรุป\n",
    code='''budget = int(input())
spent = 0
for i in range(3):
    spent = spent + int(input())
if spent <= budget:
    print(f"OK {budget - spent}")
else:
    print("Over")
''',
),
dict(
    file="10_medium.md", answer="10_word_filter.py",
    title="✂️ ทบทวนปิด — ข้อ 9: กรองคำยาว",
    diff="🟡 Medium", axis="list + len",
    scenario="รับ n คำ แล้วพิมพ์เฉพาะคำที่ยาวอย่างน้อย 4 ตัวอักษร",
    conditions=None,
    input_desc="n แล้วตามด้วย n คำ",
    output_desc="คำที่ผ่านเกณฑ์",
    sample_in="4\nhi\ncode\ngo\npython\n",
    sample_out="code\npython\n",
    hint="ตรวจ len ก่อนพิมพ์",
    starter="n = int(input())\n\n# พิมพ์คำที่ยาว >= 4\n",
    code='''n = int(input())
for i in range(n):
    word = input()
    if len(word) >= 4:
        print(word)
''',
),
dict(
    file="11_medium.md", answer="11_inventory_value.py",
    title="📦 ทบทวนปิด — ข้อ 10: มูลค่าสต๊อก",
    diff="🟡 Medium", axis="dict ราคา × จำนวน",
    scenario="`qty = {\"pen\": 3, \"book\": 2}` และ `price = {\"pen\": 10, \"book\": 40}` คิดมูลค่ารวม",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="1 บรรทัด",
    sample_in=None,
    sample_out="Value: 110\n",
    hint="วนคีย์ร่วมแล้วคูณจำนวนกับราคา",
    starter='qty = {"pen": 3, "book": 2}\nprice = {"pen": 10, "book": 40}\n\n# คิดมูลค่ารวม\n',
    code='''qty = {"pen": 3, "book": 2}
price = {"pen": 10, "book": 40}
total = 0
for item in qty:
    total = total + qty[item] * price[item]
print(f"Value: {total}")
''',
),
dict(
    file="12_medium.md", answer="12_login_attempts.py",
    title="🔐 ทบทวนปิด — ข้อ 11: จำกัดครั้ง login",
    diff="🟡 Medium", axis="while + เงื่อนไข",
    scenario="รหัสผ่านที่ถูกคือ `python` ผู้ใช้มี 3 ครั้ง ถ้ารหัสถูกพิมพ์ `Welcome` และหยุด ถ้าครบ 3 ครั้งยังผิดพิมพ์ `Locked`",
    conditions=["ใช้ while หรือ for"],
    input_desc="รหัสผ่านทีละบรรทัดจนกว่าจะถูกหรือครบ 3 ครั้ง",
    output_desc="Welcome หรือ Locked",
    sample_in="hi\ncode\npython\n",
    sample_out="Welcome\n",
    hint="นับครั้งที่ลอง และหยุดทันทีเมื่อถูก",
    starter="secret = \"python\"\n\n# ให้ลองได้ 3 ครั้ง\n",
    code='''secret = "python"
attempts = 0
success = False
while attempts < 3 and success == False:
    pw = input()
    if pw == secret:
        success = True
    attempts = attempts + 1
if success:
    print("Welcome")
else:
    print("Locked")
''',
),
dict(
    file="13_challenge.md", answer="13_gradebook.py",
    title="📒 ทบทวนปิด — ข้อ 12: สมุดคะแนนห้อง",
    diff="🔴 Challenge", axis="รับข้อมูลหลายคน + สรุป",
    scenario="รับ n นักเรียน แต่ละคนมีชื่อและคะแนน 2 วิชา เก็บเป็น dict ของ list แล้วพิมพ์ชื่อพร้อมผลรวม",
    conditions=None,
    input_desc="n แล้วสำหรับแต่ละคน: ชื่อ, คะแนนวิชา1, คะแนนวิชา2",
    output_desc="ชื่อและผลรวมทีละคน",
    sample_in="2\nAnn\n40\n50\nBen\n30\n60\n",
    sample_out="Ann: 90\nBen: 90\n",
    hint="เก็บเป็น dict ของ list สองคะแนน แล้วรวมตอนพิมพ์",
    starter="n = int(input())\nbook = {}\n\n# รับข้อมูลแล้วพิมพ์ผลรวม\n",
    code='''n = int(input())
book = {}
for i in range(n):
    name = input()
    s1 = int(input())
    s2 = int(input())
    book[name] = [s1, s2]
for name, scores in book.items():
    print(f"{name}: {scores[0] + scores[1]}")
''',
),
dict(
    file="14_challenge.md", answer="14_shop_system.py",
    title="🛒 ทบทวนปิด — ข้อ 13: ระบบร้านค้าย่อ",
    diff="🔴 Challenge", axis="เมนู + dict สต๊อก",
    scenario="สต๊อกเริ่ม `{\"apple\": 5}` รับคำสั่ง `buy` พร้อมจำนวน หรือ `show`\n\nถ้า buy ให้ลดสต๊อกแล้วพิมพ์คงเหลือ ถ้า show พิมพ์จำนวน apple",
    conditions=["รองรับสองคำสั่งตามตัวอย่าง"],
    input_desc="คำสั่ง 1 บรรทัด และถ้าเป็น buy มีจำนวนอีก 1 บรรทัด",
    output_desc="ตามคำสั่ง",
    sample_in="buy\n2\n",
    sample_out="apple: 3\n",
    hint="อ่านคำสั่งก่อน แล้วค่อยอ่านจำนวนเมื่อจำเป็น",
    starter='stock = {"apple": 5}\ncmd = input()\n\n# ทำงานตามคำสั่ง\n',
    code='''stock = {"apple": 5}
cmd = input()
if cmd == "buy":
    qty = int(input())
    stock["apple"] = stock["apple"] - qty
    print(f"apple: {stock['apple']}")
else:
    print(f"apple: {stock['apple']}")
''',
),
dict(
    file="15_challenge.md", answer="15_phase1_score.py",
    title="🏁 ทบทวนปิด — ข้อ 14: คะแนนรวม Phase 1",
    diff="🔴 Challenge", axis="หลายหมวด + สรุปความพร้อม",
    scenario="รับคะแนน 3 หมวด (basics, collections, functions) อย่างละ 0–10\n\nคิดผลรวม ถ้า `>= 24` พิมพ์ `Phase2 Ready` ถ้า `>= 18` พิมพ์ `Almost` ไม่งั้น `Keep Practice`",
    conditions=None,
    input_desc="คะแนน 3 บรรทัด",
    output_desc="สถานะ 1 บรรทัด",
    sample_in="9\n8\n8\n",
    sample_out="Phase2 Ready\n",
    hint="รวมก่อน แล้วค่อยจัดช่วงสถานะ",
    starter="basics = int(input())\ncollections = int(input())\nfunctions = int(input())\n\n# สรุปความพร้อม\n",
    code='''basics = int(input())
collections = int(input())
functions = int(input())
total = basics + collections + functions
if total >= 24:
    print("Phase2 Ready")
elif total >= 18:
    print("Almost")
else:
    print("Keep Practice")
''',
),
dict(
    file="16_challenge.md", answer="16_capstone.py",
    title="🏆 ทบทวนปิด — ข้อ 15: โปรเจ็กต์ย่อสรุปคลาส",
    diff="🔴 Challenge", axis="รวม list/dict/function/เงื่อนไข",
    scenario="รับจำนวนคน n สร้าง dict ชื่อ→คะแนน แล้วใช้ฟังก์ชันหาค่าเฉลี่ยและคนคะแนนสูงสุด (ห้าม max) พิมพ์ตามตัวอย่าง",
    conditions=["มีฟังก์ชันอย่างน้อย 2 ตัว"],
    input_desc="n แล้วชื่อ/คะแนนสลับกัน",
    output_desc="ค่าเฉลี่ยและชื่อผู้นำ",
    sample_in="3\nAnn\n70\nBen\n90\nCat\n80\n",
    sample_out="Average: 80.0\nTop: Ben\n",
    hint="แยกฟังก์ชันค่าเฉลี่ยกับฟังก์ชันหาชื่อคะแนนสูงสุด",
    starter="n = int(input())\nscores = {}\n\n# สร้างระบบสรุปคะแนนห้อง\n",
    code='''def get_average(scores):
    total = 0
    count = 0
    for value in scores.values():
        total = total + value
        count = count + 1
    return total / count

def get_top(scores):
    top_name = ""
    top_score = -1
    for name, score in scores.items():
        if score > top_score:
            top_score = score
            top_name = name
    return top_name

n = int(input())
scores = {}
for i in range(n):
    name = input()
    score = int(input())
    scores[name] = score
print(f"Average: {get_average(scores):.1f}")
print(f"Top: {get_top(scores)}")
''',
),
]


P048 = [
dict(
    file="02_test.md", answer="02_count_checks.py",
    title="✅ Transition — ข้อ 1: นับข้อที่ติ๊กได้",
    diff="🟢 Easy", axis="นับความพร้อมจากคะแนน",
    scenario="รับจำนวนข้อที่ติ๊กได้ใน checklist (0–22) แล้วพิมพ์จำนวนนั้นพร้อมป้าย Checked",
    conditions=None,
    input_desc="จำนวนเต็ม 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="18\n",
    sample_out="Checked: 18\n",
    hint=None,
    starter="checked = int(input())\n\n# พิมพ์จำนวนที่ติ๊กได้\n",
    code='''checked = int(input())
print(f"Checked: {checked}")
''',
),
dict(
    file="03_test.md", answer="03_ready_band.py",
    title="🟢 Transition — ข้อ 2: แปลผล checklist",
    diff="🟢 Easy", axis="ช่วงคะแนนความพร้อม",
    scenario="ตามตาราง readiness: 18–22 พร้อมมาก, 12–17 พร้อมปานกลาง, น้อยกว่า 12 ควรทบทวน\n\nรับจำนวนข้อที่ติ๊ก แล้วพิมพ์ `High` / `Medium` / `Low`",
    conditions=None,
    input_desc="จำนวนเต็ม 1 บรรทัด",
    output_desc="High / Medium / Low",
    sample_in="15\n",
    sample_out="Medium\n",
    hint=None,
    starter="checked = int(input())\n\n# แปลผลตามตาราง readiness\n",
    code='''checked = int(input())
if checked >= 18:
    print("High")
elif checked >= 12:
    print("Medium")
else:
    print("Low")
''',
),
dict(
    file="04_test.md", answer="04_topic_flag.py",
    title="📌 Transition — ข้อ 3: หัวข้อที่มั่นใจ",
    diff="🟢 Easy", axis="รับคำตอบ yes/no",
    scenario="รับคำตอบว่ามั่นใจ functions หรือไม่ (`yes`/`no`) แล้วพิมพ์ `Functions OK` หรือ `Review Functions`",
    conditions=None,
    input_desc="yes หรือ no 1 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="yes\n",
    sample_out="Functions OK\n",
    hint=None,
    starter="answer = input()\n\n# แปลคำตอบ\n",
    code='''answer = input()
if answer == "yes":
    print("Functions OK")
else:
    print("Review Functions")
''',
),
dict(
    file="05_easy.md", answer="05_section_scores.py",
    title="📊 Transition — ข้อ 4: คะแนนรายหมวด",
    diff="🟢 Easy", axis="รับ 3 หมวดแล้วพิมพ์สรุป",
    scenario="รับคะแนนหมวด basics / collections / functions (0–10) แล้วพิมพ์ผลรวม",
    conditions=None,
    input_desc="คะแนน 3 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="8\n7\n9\n",
    sample_out="Total: 24\n",
    hint=None,
    starter="basics = int(input())\ncollections = int(input())\nfunctions = int(input())\n\n# พิมพ์ผลรวม\n",
    code='''basics = int(input())
collections = int(input())
functions = int(input())
print(f"Total: {basics + collections + functions}")
''',
),
dict(
    file="06_easy.md", answer="06_map_topic.py",
    title="🗺️ Transition — ข้อ 5: แม็พ Phase1→Phase2",
    diff="🟢 Easy", axis="ตาราง mapping เป็นโปรแกรม",
    scenario="รับหัวข้อ Phase 1 แล้วพิมพ์หัวข้อ Phase 2 ที่เชื่อม\n\n`Functions`→`OOP`, `Dictionaries`→`JSON`, `Lists`→`Files`, `Debugging`→`Error Handling`, อื่นๆ→`TBD`",
    conditions=["ห้าม import / class / open"],
    input_desc="ชื่อหัวข้อ Phase 1 หนึ่งบรรทัด",
    output_desc="หัวข้อ Phase 2",
    sample_in="Dictionaries\n",
    sample_out="JSON\n",
    hint=None,
    starter="topic = input()\n\n# แม็พไป Phase 2\n",
    code='''topic = input()
if topic == "Functions":
    print("OOP")
elif topic == "Dictionaries":
    print("JSON")
elif topic == "Lists":
    print("Files")
elif topic == "Debugging":
    print("Error Handling")
else:
    print("TBD")
''',
),
dict(
    file="07_medium.md", answer="07_checklist_list.py",
    title="📋 Transition — ข้อ 6: เก็บ checklist เป็น list",
    diff="🟡 Medium", axis="list ของ 0/1",
    scenario="รับสถานะ 5 ข้อเป็น `1` (ติ๊กได้) หรือ `0` เก็บในลิสต์ แล้วพิมพ์จำนวนที่ติ๊กได้",
    conditions=None,
    input_desc="0 หรือ 1 จำนวน 5 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="1\n1\n0\n1\n0\n",
    sample_out="Done: 3\n",
    hint="สะสมผลรวมของค่า 0/1",
    starter="flags = []\n\n# รับ 5 ค่า แล้วนับที่ติ๊กได้\n",
    code='''flags = []
for i in range(5):
    flags.append(int(input()))
done = 0
for f in flags:
    done = done + f
print(f"Done: {done}")
''',
),
dict(
    file="08_medium.md", answer="08_skill_dict.py",
    title="🗂️ Transition — ข้อ 7: บันทึกทักษะเป็น dict",
    diff="🟡 Medium", axis="dict ทักษะ → คะแนน",
    scenario="สร้าง dict ทักษะจาก input 3 คู่ (ชื่อทักษะ, คะแนน 0–10) แล้วพิมพ์ทุกคู่",
    conditions=None,
    input_desc="ชื่อและคะแนนสลับกัน 6 บรรทัด",
    output_desc="คู่ทักษะ",
    sample_in="list\n8\ndict\n7\nfunction\n9\n",
    sample_out="list: 8\ndict: 7\nfunction: 9\n",
    hint="เก็บใน dict แล้ววน items",
    starter="skills = {}\n\n# รับ 3 ทักษะแล้วพิมพ์\n",
    code='''skills = {}
for i in range(3):
    name = input()
    score = int(input())
    skills[name] = score
for name, score in skills.items():
    print(f"{name}: {score}")
''',
),
dict(
    file="09_medium.md", answer="09_weak_topics.py",
    title="⚠️ Transition — ข้อ 8: หาหัวข้อที่ต้องทบทวน",
    diff="🟡 Medium", axis="กรองจาก dict ตามเกณฑ์",
    scenario="`skills = {\"list\": 8, \"dict\": 5, \"function\": 9, \"scope\": 4}` พิมพ์ชื่อทักษะที่คะแนน `< 6`",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="หัวข้อที่ต้องทบทวน",
    sample_in=None,
    sample_out="dict\nscope\n",
    hint="วน items แล้วพิมพ์เฉพาะที่ต่ำกว่า 6",
    starter='skills = {"list": 8, "dict": 5, "function": 9, "scope": 4}\n\n# พิมพ์หัวข้อที่ต้องทบทวน\n',
    code='''skills = {"list": 8, "dict": 5, "function": 9, "scope": 4}
for name, score in skills.items():
    if score < 6:
        print(name)
''',
),
dict(
    file="10_medium.md", answer="10_phase_gate.py",
    title="🚧 Transition — ข้อ 9: ประตูเข้า Phase 2",
    diff="🟡 Medium", axis="หลายเงื่อนไขความพร้อม",
    scenario="รับคะแนน collections และ functions\n\nผ่านประตูเมื่อ collections `>= 7` และ functions `>= 7` พิมพ์ `Enter Phase 2` ไม่งั้น `Not yet`",
    conditions=["ใช้ and"],
    input_desc="คะแนน 2 บรรทัด",
    output_desc="Enter Phase 2 หรือ Not yet",
    sample_in="8\n6\n",
    sample_out="Not yet\n",
    hint="ต้องผ่านทั้งสองหมวดพร้อมกัน",
    starter="collections = int(input())\nfunctions = int(input())\n\n# ตรวจประตู Phase 2\n",
    code='''collections = int(input())
functions = int(input())
if collections >= 7 and functions >= 7:
    print("Enter Phase 2")
else:
    print("Not yet")
''',
),
dict(
    file="11_medium.md", answer="11_review_plan.py",
    title="📅 Transition — ข้อ 10: แผนทบทวน",
    diff="🟡 Medium", axis="สร้างลิสต์แผนจากคะแนนต่ำ",
    scenario="รับชื่อหัวข้อ 4 อันและคะแนนสลับกัน สร้างลิสต์เฉพาะหัวข้อที่ `< 7` แล้วพิมพ์ลิสต์แผนทบทวน",
    conditions=None,
    input_desc="ชื่อ/คะแนนสลับกัน 8 บรรทัด",
    output_desc="1 บรรทัด (ลิสต์)",
    sample_in="list\n8\ndict\n5\nloop\n9\nscope\n6\n",
    sample_out="['dict', 'scope']\n",
    hint="append เฉพาะหัวข้อที่คะแนนต่ำกว่า 7",
    starter="plan = []\n\n# รับ 4 หัวข้อ สร้างแผนทบทวน\n",
    code='''plan = []
for i in range(4):
    topic = input()
    score = int(input())
    if score < 7:
        plan.append(topic)
print(plan)
''',
),
dict(
    file="12_medium.md", answer="12_self_score.py",
    title="🪞 Transition — ข้อ 11: คะแนนประเมินตนเอง",
    diff="🟡 Medium", axis="ฟังก์ชันแปลผลรวม",
    scenario="สร้าง `band(total)` return High/Medium/Low ตามเกณฑ์ 18/12 จากผลรวมที่รับมา 3 หมวด",
    conditions=["มีฟังก์ชัน band"],
    input_desc="คะแนน 3 บรรทัด",
    output_desc="1 บรรทัด",
    sample_in="6\n6\n5\n",
    sample_out="Medium\n",
    hint="รวมก่อน แล้วส่งเข้าฟังก์ชันแปลผล",
    starter="# สร้าง band(total)\n# รับ 3 หมวดแล้วพิมพ์ผล\n",
    code='''def band(total):
    if total >= 18:
        return "High"
    elif total >= 12:
        return "Medium"
    else:
        return "Low"

a = int(input())
b = int(input())
c = int(input())
print(band(a + b + c))
''',
),
dict(
    file="13_challenge.md", answer="13_readiness_report.py",
    title="📑 Transition — ข้อ 12: รายงานความพร้อม",
    diff="🔴 Challenge", axis="กล่องสรุปจากหลายหมวด",
    scenario="รับคะแนน 4 หมวด: basics, collections, functions, quality\n\nพิมพ์รายงานกล่องตามตัวอย่าง พร้อมสถานะ Ready ถ้าผลรวม `>= 28` ไม่งั้น Review",
    conditions=None,
    input_desc="คะแนน 4 บรรทัด (0–10)",
    output_desc="กล่องรายงาน",
    sample_in="8\n8\n7\n6\n",
    sample_out="====================\nBasics      : 8\nCollections : 8\nFunctions   : 7\nQuality     : 6\nStatus      : Ready\n====================\n",
    hint="จัดคอลัมน์ : ให้ตรงกัน และคิดสถานะจากผลรวม",
    starter="basics = int(input())\ncollections = int(input())\nfunctions = int(input())\nquality = int(input())\n\n# พิมพ์รายงานความพร้อม\n",
    code='''basics = int(input())
collections = int(input())
functions = int(input())
quality = int(input())
total = basics + collections + functions + quality
if total >= 28:
    status = "Ready"
else:
    status = "Review"
print("====================")
print(f"Basics      : {basics}")
print(f"Collections : {collections}")
print(f"Functions   : {functions}")
print(f"Quality     : {quality}")
print(f"Status      : {status}")
print("====================")
''',
),
dict(
    file="14_challenge.md", answer="14_gap_finder.py",
    title="🔍 Transition — ข้อ 13: หาช่องว่างทักษะ",
    diff="🔴 Challenge", axis="เปรียบเทียบเป้าหมายกับคะแนนจริง",
    scenario="เป้าหมายทุกทักษะคือ 8 จาก `skills = {\"list\": 9, \"dict\": 6, \"function\": 8, \"debug\": 5}`\n\nพิมพ์ทักษะที่ต่ำกว่าเป้าหมายพร้อมส่วนต่าง เช่น `dict needs 2`",
    conditions=None,
    input_desc="ไม่มี",
    output_desc="รายการช่องว่าง",
    sample_in=None,
    sample_out="dict needs 2\ndebug needs 3\n",
    hint="เป้าหมายคงที่ 8 ลบด้วยคะแนนจริง",
    starter='TARGET = 8\nskills = {"list": 9, "dict": 6, "function": 8, "debug": 5}\n\n# พิมพ์ช่องว่างทักษะ\n',
    code='''TARGET = 8
skills = {"list": 9, "dict": 6, "function": 8, "debug": 5}
for name, score in skills.items():
    if score < TARGET:
        need = TARGET - score
        print(f"{name} needs {need}")
''',
),
dict(
    file="15_challenge.md", answer="15_study_queue.py",
    title="📚 Transition — ข้อ 14: คิวทบทวนก่อน Phase 2",
    diff="🔴 Challenge", axis="เรียงลำดับทบทวนด้วย list",
    scenario="รับ n หัวข้อที่ต้องทบทวน เก็บในลิสต์ แล้วพิมพ์เป็นคิวหมายเลข `1. ...`",
    conditions=None,
    input_desc="n แล้วตามด้วย n ชื่อหัวข้อ",
    output_desc="คิวหมายเลข",
    sample_in="3\nscope\ndebug\ndict\n",
    sample_out="1. scope\n2. debug\n3. dict\n",
    hint="ใช้ตัวนับหรือ range ตอนพิมพ์คิว",
    starter="n = int(input())\nqueue = []\n\n# สร้างคิวทบทวนแล้วพิมพ์\n",
    code='''n = int(input())
queue = []
for i in range(n):
    queue.append(input())
number = 1
for topic in queue:
    print(f"{number}. {topic}")
    number = number + 1
''',
),
dict(
    file="16_challenge.md", answer="16_final_gate.py",
    title="🚀 Transition — ข้อ 15: ประตูสุดท้ายเข้า Phase 2",
    diff="🔴 Challenge", axis="รวม checklist + mapping + สถานะ",
    scenario="รับจำนวนข้อที่ติ๊ก (0–22) และหัวข้อ Phase 1 ที่อยากไปต่อ\n\nถ้า checked `>= 18` พิมพ์ `GO` ในบรรทัดแรก และพิมพ์หัวข้อ Phase 2 ตามแม็พเดียวกับข้อ 5 ในบรรทัดสอง ไม่งั้นพิมพ์แค่ `WAIT`",
    conditions=["ห้ามใช้ของ Phase 2 จริง (class/import/open/try)"],
    input_desc="จำนวนข้อที่ติ๊ก 1 บรรทัด และหัวข้อ Phase 1 1 บรรทัด",
    output_desc="GO + หัวข้อ Phase 2 หรือ WAIT",
    sample_in="20\nFunctions\n",
    sample_out="GO\nOOP\n",
    hint="ตรวจเกณฑ์ checked ก่อน แล้วค่อยแม็พหัวข้อ",
    starter="checked = int(input())\ntopic = input()\n\n# ประตูสุดท้าย\n",
    code='''checked = int(input())
topic = input()
if checked >= 18:
    print("GO")
    if topic == "Functions":
        print("OOP")
    elif topic == "Dictionaries":
        print("JSON")
    elif topic == "Lists":
        print("Files")
    elif topic == "Debugging":
        print("Error Handling")
    else:
        print("TBD")
else:
    print("WAIT")
''',
),
]
