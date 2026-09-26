# -*- coding: utf-8 -*-
"""Generate gold-standard practice for 024-midyear-review.
No .append() / empty list building. Hardcoded scores=[...] OK."""
import os, shutil

BASE = os.path.join(os.path.dirname(__file__), "..", "..", "slide", "024-midyear-review")
ANS = os.path.join(BASE, "answer")

def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
        if not text.endswith("\n"):
            f.write("\n")

for name in os.listdir(BASE):
    if name.endswith(".md") and not name.startswith("01_"):
        os.remove(os.path.join(BASE, name))
if os.path.isdir(ANS):
    shutil.rmtree(ANS)
os.makedirs(ANS, exist_ok=True)

PROBLEMS = {}

PROBLEMS["02"] = dict(
    file="02_test.md", diff="🟢 Easy", emoji="🪪", title="ป้ายชื่อพร้อมอายุ",
    body="รับชื่อและปีเกิด แล้วคำนวณอายุโดยใช้ปีปัจจุบัน 2026\nพิมพ์สองบรรทัด: `Name: ...` และ `Age: ...`",
    starter="name = input()\nbirth_year = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="Mina\n2010", sample_out="Name: Mina\nAge: 16",
    inp="2 บรรทัด — ชื่อ และปีเกิด", out="Name และ Age",
    hint=None,
    answer='name = input()\nbirth_year = int(input())\nage = 2026 - birth_year\nprint(f"Name: {name}")\nprint(f"Age: {age}")\n',
)

PROBLEMS["03"] = dict(
    file="03_test.md", diff="🟢 Easy", emoji="➗", title="เครื่องคิดเลขสี่อย่าง",
    body="รับจำนวนเต็มสองตัว `a` และ `b`\nพิมพ์ผลบวก ลบ คูณ หารทศนิยม 2 ตำแหน่ง ตามป้ายกำกับ",
    starter="a = int(input())\nb = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="17\n5",
    sample_out="Sum: 22\nDiff: 12\nProduct: 85\nQuotient: 3.40",
    inp="2 บรรทัด — a และ b", out="ผลลัพธ์สี่บรรทัด",
    hint=None,
    answer="""a = int(input())
b = int(input())
print(f"Sum: {a + b}")
print(f"Diff: {a - b}")
print(f"Product: {a * b}")
print(f"Quotient: {a / b:.2f}")
""",
)

PROBLEMS["04"] = dict(
    file="04_test.md", diff="🟢 Easy", emoji="🎓", title="เกรดจากคะแนนเดียว",
    body="รับคะแนนแล้วจัดเกรด\n`>= 80` → A, `>= 60` → B, `>= 40` → C, น้อยกว่านั้น → F",
    starter="score = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="75", sample_out="Grade: B",
    inp="คะแนน 1 บรรทัด", out="Grade: <ตัวอักษร>",
    hint=None,
    answer="""score = int(input())
if score >= 80:
    print("Grade: A")
elif score >= 60:
    print("Grade: B")
elif score >= 40:
    print("Grade: C")
else:
    print("Grade: F")
""",
)

PROBLEMS["08"] = dict(
    file="08_easy.md", diff="🟢 Easy", emoji="2️⃣", title="พิมพ์เลขคู่ 2 ถึง 20",
    body="พิมพ์เลขคู่ตั้งแต่ 2 ถึง 20 ทีละบรรทัด ด้วย for + range",
    starter="# เขียนโค้ดตรงนี้\n",
    sample_in="", sample_out="2\n4\n6\n8\n10\n12\n14\n16\n18\n20",
    inp="ไม่มี", out="เลขคู่ 2..20",
    hint=None,
    answer="for i in range(2, 21, 2):\n    print(i)\n",
)

PROBLEMS["09"] = dict(
    file="09_easy.md", diff="🟢 Easy", emoji="📚", title="ค่าเฉลี่ยจากลิสต์คะแนน",
    body="มีลิสต์คะแนนกำหนดให้แล้ว\nหาผลรวมและค่าเฉลี่ยทศนิยม 1 ตำแหน่ง แล้วแสดงสองบรรทัด",
    starter="scores = [70, 85, 90, 75]\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="", sample_out="Total: 320\nAverage: 80.0",
    inp="ไม่มี", out="Total และ Average",
    hint=None,
    answer="""scores = [70, 85, 90, 75]
total = 0
for score in scores:
    total = total + score
average = total / len(scores)
print(f"Total: {total}")
print(f"Average: {average:.1f}")
""",
)

PROBLEMS["06"] = dict(
    file="06_medium.md", diff="🟡 Medium", emoji="🧾", title="บิลสองชิ้นพร้อม VAT",
    body="รับราคาสินค้าสองชิ้น รวมกัน แล้วคิด VAT 7%\nแสดงยอดก่อนภาษี ภาษี และยอดสุทธิ ทศนิยม 2 ตำแหน่งในกรอบ",
    starter="price1 = int(input())\nprice2 = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="100\n200",
    sample_out="========================\n        BILL\n========================\nSubtotal : 300.00\nVAT 7%   : 21.00\nTotal    : 321.00\n========================",
    inp="2 บรรทัด — ราคาชิ้นที่ 1 และ 2", out="ใบเสร็จในกรอบ",
    hint="รวมราคาก่อน แล้วค่อยคิด vat = subtotal * 0.07",
    answer="""price1 = int(input())
price2 = int(input())
subtotal = price1 + price2
vat = subtotal * 0.07
total = subtotal + vat
print("========================")
print("        BILL")
print("========================")
print(f"Subtotal : {subtotal:.2f}")
print(f"VAT 7%   : {vat:.2f}")
print(f"Total    : {total:.2f}")
print("========================")
""",
)

PROBLEMS["07"] = dict(
    file="07_medium.md", diff="🟡 Medium", emoji="🎢", title="สิทธิ์เล่นเครื่องเล่น",
    body="รับส่วนสูง (ซม.) และอายุ\nเล่นได้เมื่อส่วนสูง `>= 120` **และ** อายุ `>= 10`\nผ่าน → `Allowed` ไม่ผ่าน → `Denied`",
    starter="height = int(input())\nage = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="130\n12", sample_out="Allowed",
    inp="2 บรรทัด — ส่วนสูง และอายุ", out="Allowed หรือ Denied",
    hint="ใช้ and รวมสองเงื่อนไข",
    answer="""height = int(input())
age = int(input())
if height >= 120 and age >= 10:
    print("Allowed")
else:
    print("Denied")
""",
)

PROBLEMS["10"] = dict(
    file="10_medium.md", diff="🟡 Medium", emoji="🌡️", title="นับวันร้อนจากอุณหภูมิที่รับ",
    body="รับจำนวนวัน `n` แล้วรับอุณหภูมิ n ค่า\nนับวันที่ `>= 32` แล้วแสดงผล\n\n> ไม่ต้องสร้างลิสต์ — นับไปเลยในลูป",
    starter="n = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="4\n30\n33\n28\n35", sample_out="Hot Days: 2",
    inp="บรรทัดแรก n ตามด้วยอุณหภูมิน n บรรทัด", out="Hot Days: <จำนวน>",
    hint="ใช้ for ตาม n รับค่าทีละรอบแล้วตัดสินใจนับทันที",
    answer="""n = int(input())
hot = 0
for i in range(n):
    temp = int(input())
    if temp >= 32:
        hot = hot + 1
print(f"Hot Days: {hot}")
""",
)

PROBLEMS["11"] = dict(
    file="11_medium.md", diff="🟡 Medium", emoji="🔐", title="ล็อกอินจนถูกต้อง",
    body='รหัสถูกต้องคือ `"python"`\nใช้ while True รับรหัส ผิดพิมพ์ `Wrong` ถูกพิมพ์ `Welcome` แล้ว break',
    starter="# เขียนโค้ดตรงนี้\n",
    sample_in="123\npython", sample_out="Wrong\nWelcome",
    inp="รหัสทีละบรรทัดจนถูก", out="Wrong ตามครั้งที่ผิด แล้ว Welcome",
    hint="while True ตรวจรหัสด้วย if/else",
    answer="""while True:
    password = input()
    if password == "python":
        print("Welcome")
        break
    else:
        print("Wrong")
""",
)

PROBLEMS["12"] = dict(
    file="12_medium.md", diff="🟡 Medium", emoji="⭐", title="สามเหลี่ยมดาวจาก input",
    body="รับ `n` แล้วพิมพ์สามเหลี่ยมดาว 1 ถึง n แถว",
    starter="n = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="4", sample_out="*\n**\n***\n****",
    inp="จำนวนเต็ม n 1 บรรทัด", out="สามเหลี่ยมดาว",
    hint="nested for ตามแถว",
    answer="""n = int(input())
for row in range(1, n + 1):
    for col in range(row):
        print("*", end="")
    print()
""",
)

PROBLEMS["13"] = dict(
    file="13_medium.md", diff="🟡 Medium", emoji="🎯", title="สรุปผลสอบจากลิสต์",
    body="มีลิสต์คะแนน\nพิมพ์แต่ละคน Pass/Fail (เกณฑ์ 50) แล้วสรุปจำนวนผ่านในกรอบ",
    starter="scores = [45, 60, 80, 30, 55]\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="",
    sample_out="Fail\nPass\nPass\nFail\nPass\n========================\nPassed: 3\n========================",
    inp="ไม่มี", out="ผลรายคน + สรุป",
    hint="if ใน for แล้วสะสมตัวนับ",
    answer="""scores = [45, 60, 80, 30, 55]
passed = 0
for score in scores:
    if score >= 50:
        print("Pass")
        passed = passed + 1
    else:
        print("Fail")
print("========================")
print(f"Passed: {passed}")
print("========================")
""",
)

PROBLEMS["05"] = dict(
    file="05_challenge.md", diff="🔴 Challenge", emoji="👤", title="โปรไฟล์นักเรียนพร้อมเกรดเฉลี่ย",
    body="รับชื่อ แล้วรับคะแนน 3 วิชาทีละบรรทัด\nคำนวณค่าเฉลี่ยทศนิยม 1 ตำแหน่ง\nจัดเกรดจากเฉลี่ย: `>= 80` A, `>= 60` B, นอกนั้น C\nแสดงในกรอบ\n\n> สะสมผลรวมในลูป — ห้ามใช้ `.append()`",
    starter="name = input()\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="Ann\n70\n80\n90",
    sample_out="========================\n      PROFILE\n========================\nName    : Ann\nAverage : 80.0\nGrade   : A\n========================",
    inp="ชื่อ 1 บรรทัด ตามด้วยคะแนน 3 บรรทัด", out="โปรไฟล์ในกรอบ",
    hint="วนรับคะแนน 3 ครั้งสะสม total แล้วเฉลี่ยและจัดเกรด",
    answer="""name = input()
total = 0
for i in range(3):
    score = int(input())
    total = total + score
average = total / 3
if average >= 80:
    grade = "A"
elif average >= 60:
    grade = "B"
else:
    grade = "C"
print("========================")
print("      PROFILE")
print("========================")
print(f"Name    : {name}")
print(f"Average : {average:.1f}")
print(f"Grade   : {grade}")
print("========================")
""",
)

PROBLEMS["14"] = dict(
    file="14_challenge.md", diff="🔴 Challenge", emoji="🏪", title="ร้านสะดวกรับยอดจน done",
    body='ใช้ while True รับยอดขาย\n- ข้อความ `"done"` → หยุด\n- ยอดเป็นจำนวนเต็ม ถ้า `< 0` ให้ข้าม (continue)\n- นอกนั้นบวกเข้ายอดรวม และนับจำนวนรายการ\nท้ายสุดแสดง Count และ Total ในกรอบ',
    starter="# เขียนโค้ดตรงนี้\n",
    sample_in="100\n-20\n50\ndone",
    sample_out="========================\n       SALES\n========================\nCount : 2\nTotal : 150\n========================",
    inp="ยอดทีละบรรทัด หรือ done", out="สรุปในกรอบ",
    hint="แปลงเป็น int หลังเช็ก done — ค่าติดลบข้ามด้วย continue",
    answer="""count = 0
total = 0
while True:
    text = input()
    if text == "done":
        break
    amount = int(text)
    if amount < 0:
        continue
    count = count + 1
    total = total + amount
print("========================")
print("       SALES")
print("========================")
print(f"Count : {count}")
print(f"Total : {total}")
print("========================")
""",
)

PROBLEMS["15"] = dict(
    file="15_challenge.md", diff="🔴 Challenge", emoji="🚌", title="ค่าโดยสารตามอายุและวัน",
    body="""รับอายุและประเภทวัน (`weekday` / `weekend`)

**ราคาพื้นฐานตามอายุ**
| อายุ | ราคา |
|------|------|
| `< 12` | 15 |
| นอกนั้น | 30 |

**ค่าเพิ่มตามวัน**
| วัน | ค่าเพิ่ม |
|-----|----------|
| `weekend` | +10 |
| `weekday` | 0 |

แสดง Base, Extra, Total ในกรอบ""",
    starter="age = int(input())\nday = input()\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="10\nweekend",
    sample_out="========================\n        FARE\n========================\nBase  : 15\nExtra : 10\nTotal : 25\n========================",
    inp="2 บรรทัด — อายุ และวัน", out="ใบราคาในกรอบ",
    hint="แยก if/else สองชุด คนละเรื่อง แล้วค่อยรวม",
    answer="""age = int(input())
day = input()
if age < 12:
    base = 15
else:
    base = 30
if day == "weekend":
    extra = 10
else:
    extra = 0
total = base + extra
print("========================")
print("        FARE")
print("========================")
print(f"Base  : {base}")
print(f"Extra : {extra}")
print(f"Total : {total}")
print("========================")
""",
)

PROBLEMS["16"] = dict(
    file="16_challenge.md", diff="🔴 Challenge", emoji="🏆", title="สรุปคะแนนชั้นเรียน",
    body="""รับจำนวนนักเรียน `n` แล้วรับคะแนนของแต่ละคน (n บรรทัด)
หา
- ค่าเฉลี่ยทศนิยม 1 ตำแหน่ง
- จำนวนคนที่คะแนน `>= 80` (เรียกว่า Top)
- จำนวนคนที่คะแนน `< 50` (เรียกว่า Risk)

แสดงในกรอบ

> สะสมในลูปทันที ห้ามสร้างลิสต์ด้วย `.append()`""",
    starter="n = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="5\n90\n40\n75\n82\n55",
    sample_out="========================\n     CLASS REPORT\n========================\nStudents : 5\nAverage  : 68.4\nTop      : 2\nRisk     : 1\n========================",
    inp="บรรทัดแรก n ตามด้วยคะแนน n บรรทัด", out="รายงานในกรอบ",
    hint="ตัวแปร total / top / risk อัปเดตในลูปเดียวขณะรับคะแนน",
    answer="""n = int(input())
total = 0
top = 0
risk = 0
for i in range(n):
    score = int(input())
    total = total + score
    if score >= 80:
        top = top + 1
    if score < 50:
        risk = risk + 1
average = total / n
print("========================")
print("     CLASS REPORT")
print("========================")
print(f"Students : {n}")
print(f"Average  : {average:.1f}")
print(f"Top      : {top}")
print(f"Risk     : {risk}")
print("========================")
""",
)

INDEX = """# 📋 สารบัญโจทย์ — บท 024 midyear review

**ขอบเขตของบทนี้:** ทบทวนบท 001–023 ทั้งหมดในขอบเขตที่เรียนมาแล้ว

> ❌ ห้าม `.append()` / สร้างลิสต์ว่างแล้วเติม — สอนบท 026
> ✅ ใช้ list แบบ hardcode `scores = [...]` แล้ววนได้ (เรียนบท 018)
> ✅ รับค่าหลายรอบด้วย loop + สะสมตัวแปรได้โดยไม่ต้องเก็บเป็นลิสต์

---

## ลำดับที่แนะนำ

| # | ไฟล์ | ระดับ | โจทย์ | แกนการคิด |
|---|------|-------|-------|-----------|
| 1 | `02_test.md` | 🟢 | ป้ายชื่อพร้อมอายุ | input + คำนวณ |
| 2 | `03_test.md` | 🟢 | เครื่องคิดเลขสี่อย่าง | ตัวดำเนินการ + f-string |
| 3 | `04_test.md` | 🟢 | เกรดจากคะแนนเดียว | elif |
| 4 | `08_easy.md` | 🟢 | พิมพ์เลขคู่ 2 ถึง 20 | for + range step |
| 5 | `09_easy.md` | 🟢 | ค่าเฉลี่ยจากลิสต์คะแนน | for-in-list + len |
| 6 | `06_medium.md` | 🟡 | บิลสองชิ้นพร้อม VAT | คำนวณ + กรอบ |
| 7 | `07_medium.md` | 🟡 | สิทธิ์เล่นเครื่องเล่น | and |
| 8 | `10_medium.md` | 🟡 | นับวันร้อนจากอุณหภูมิที่รับ | for + input หลายรอบ |
| 9 | `11_medium.md` | 🟡 | ล็อกอินจนถูกต้อง | while True + break |
| 10 | `12_medium.md` | 🟡 | สามเหลี่ยมดาวจาก input | nested loop |
| 11 | `13_medium.md` | 🟡 | สรุปผลสอบจากลิสต์ | if ใน list loop |
| 12 | `05_challenge.md` | 🔴 | โปรไฟล์นักเรียนพร้อมเกรดเฉลี่ย | ผสม input/loop/เกรด |
| 13 | `14_challenge.md` | 🔴 | ร้านสะดวกรับยอดจน done | break + continue |
| 14 | `15_challenge.md` | 🔴 | ค่าโดยสารตามอายุและวัน | if/else สองชุด |
| 15 | `16_challenge.md` | 🔴 | สรุปคะแนนชั้นเรียน | สะสมหลายตัวแปรในลูป |

**สรุป:** 🟢 Easy 5 ข้อ · 🟡 Medium 6 ข้อ · 🔴 Challenge 4 ข้อ = **15 ข้อ**

---

## หมายเหตุสำหรับครู

- โฟลเดอร์ `mid-test/` เป็นข้อสอบแยก ไม่ใช่โจทย์ฝึก 15 ข้อของมาตรฐานนี้
- ข้อ Challenge ยากเพราะผสมหลายบท ไม่ใช่เพราะใช้ของใหม่
"""

CHAPTER = "midyear-review"
SLUGS = {
    "02": "02_name_age", "03": "03_four_ops", "04": "04_letter_grade",
    "05": "05_student_profile", "06": "06_vat_bill", "07": "07_ride_allowed",
    "08": "08_even_numbers", "09": "09_list_average", "10": "10_hot_days",
    "11": "11_login", "12": "12_star_triangle", "13": "13_pass_fail_list",
    "14": "14_sales_until_done", "15": "15_bus_fare", "16": "16_class_report",
}

def emit():
    write(os.path.join(BASE, "00_index.md"), INDEX)
    for num, p in PROBLEMS.items():
        n = int(num)
        lines = [
            f"# {p['emoji']} {CHAPTER} — ข้อ {n}: {p['title']}", "",
            f"**Difficulty:** {p['diff']}", "", "---", "", "## โจทย์", "",
            p["body"], "", "---", "", "## Input", "", p["inp"], "",
            "## Output", "", p["out"], "", "---", "", "## ตัวอย่าง", "",
            "**Input:**", "", "```text", p["sample_in"], "```", "",
            "**Output:**", "", "```text", p["sample_out"], "```", "", "---", "",
        ]
        if p.get("hint"):
            lines += ["## 💡 Hint", "", p["hint"], "", "---", ""]
        lines += ["## Starter Code", "", "```python", p["starter"].rstrip("\n"), "```", ""]
        write(os.path.join(BASE, p["file"]), "\n".join(lines))
        write(os.path.join(ANS, SLUGS[num] + ".py"), p["answer"])
    print("024 done")

if __name__ == "__main__":
    emit()
