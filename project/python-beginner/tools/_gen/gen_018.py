# -*- coding: utf-8 -*-
"""Generate gold-standard practice for 018-loop-with-lists."""
import os, shutil

BASE = os.path.join(os.path.dirname(__file__), "..", "..", "slide", "018-loop-with-lists")
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
    file="02_test.md", diff="🟢 Easy", emoji="🥤", title="เมนูเครื่องดื่ม",
    body="ร้านกาแฟมีเมนูเครื่องดื่มเก็บไว้ในลิสต์\nเขียนโปรแกรมพิมพ์ชื่อเครื่องดื่มทีละบรรทัด",
    starter='drinks = ["Latte", "Mocha", "Tea", "Cocoa"]\n\n# เขียนโค้ดตรงนี้\n',
    sample_in="", sample_out="Latte\nMocha\nTea\nCocoa",
    inp="ไม่มี (ลิสต์กำหนดให้แล้ว)", out="ชื่อเครื่องดื่มทีละบรรทัด",
    hint=None,
    answer='drinks = ["Latte", "Mocha", "Tea", "Cocoa"]\nfor drink in drinks:\n    print(drink)\n',
)

PROBLEMS["03"] = dict(
    file="03_test.md", diff="🟢 Easy", emoji="📚", title="รายวิชาในเทอมนี้",
    body="นักเรียนจดรายวิชาไว้ในลิสต์\nเขียนโปรแกรมพิมพ์แต่ละวิชาในรูปแบบ `Subject: <ชื่อ>`",
    starter='subjects = ["Math", "Science", "Art"]\n\n# เขียนโค้ดตรงนี้\n',
    sample_in="", sample_out="Subject: Math\nSubject: Science\nSubject: Art",
    inp="ไม่มี", out="รายวิชาพร้อมป้ายกำกับทีละบรรทัด",
    hint=None,
    answer='subjects = ["Math", "Science", "Art"]\nfor subject in subjects:\n    print(f"Subject: {subject}")\n',
)

PROBLEMS["04"] = dict(
    file="04_test.md", diff="🟢 Easy", emoji="👥", title="นับจำนวนสมาชิกชมรม",
    body="ชมรมหุ่นยนต์เก็บรายชื่อสมาชิกในลิสต์\nเขียนโปรแกรมแสดงจำนวนสมาชิกด้วย `len()`",
    starter='members = ["Ann", "Ben", "Cara", "Dan", "Eve"]\n\n# เขียนโค้ดตรงนี้\n',
    sample_in="", sample_out="Members: 5",
    inp="ไม่มี", out="บรรทัดเดียว Members: <จำนวน>",
    hint=None,
    answer='members = ["Ann", "Ben", "Cara", "Dan", "Eve"]\nprint(f"Members: {len(members)}")\n',
)

PROBLEMS["08"] = dict(
    file="08_easy.md", diff="🟢 Easy", emoji="🛒", title="รวมราคาสินค้าในตะกร้า",
    body="ตะกร้าสินค้ามีราคาเป็นลิสต์จำนวนเต็ม\nเขียนโปรแกรมรวมราคาสินค้าทั้งหมดแล้วแสดงผล",
    starter="prices = [45, 60, 30, 25]\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="", sample_out="Total: 160",
    inp="ไม่มี", out="บรรทัดเดียว Total: <ผลรวม>",
    hint=None,
    answer="prices = [45, 60, 30, 25]\ntotal = 0\nfor price in prices:\n    total = total + price\nprint(f\"Total: {total}\")\n",
)

PROBLEMS["09"] = dict(
    file="09_easy.md", diff="🟢 Easy", emoji="🏷️", title="ติดป้ายสินค้า",
    body="คลังสินค้าอยากพิมพ์ป้าย `Item: <ชื่อ>` ให้ทุกรายการในลิสต์",
    starter='items = ["Soap", "Shampoo", "Tissue"]\n\n# เขียนโค้ดตรงนี้\n',
    sample_in="", sample_out="Item: Soap\nItem: Shampoo\nItem: Tissue",
    inp="ไม่มี", out="ป้ายสินค้าทีละบรรทัด",
    hint=None,
    answer='items = ["Soap", "Shampoo", "Tissue"]\nfor item in items:\n    print(f"Item: {item}")\n',
)

PROBLEMS["06"] = dict(
    file="06_medium.md", diff="🟡 Medium", emoji="📈", title="ค่าเฉลี่ยคะแนนสอบย่อย",
    body="ครูเก็บคะแนนสอบย่อยในลิสต์\nเขียนโปรแกรมหาผลรวมและค่าเฉลี่ย (ทศนิยม 1 ตำแหน่ง) แล้วแสดงทั้งสองค่า",
    starter="scores = [72, 88, 95, 60, 81]\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="", sample_out="Total  : 396\nAverage: 79.2",
    inp="ไม่มี", out="2 บรรทัด — Total และ Average",
    hint="สะสม total ใน loop แล้วหารด้วย len(scores) ใช้ :.1f",
    answer="""scores = [72, 88, 95, 60, 81]
total = 0
for score in scores:
    total = total + score
average = total / len(scores)
print(f"Total  : {total}")
print(f"Average: {average:.1f}")
""",
)

PROBLEMS["07"] = dict(
    file="07_medium.md", diff="🟡 Medium", emoji="🎯", title="นับคนสอบผ่านเกณฑ์ 50",
    body="คะแนนสอบเก็บในลิสต์ คะแนน `>= 50` นับว่าผ่าน\nเขียนโปรแกรมนับจำนวนคนที่ผ่าน",
    starter="scores = [42, 55, 60, 38, 71, 49]\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="", sample_out="Passed: 3",
    inp="ไม่มี", out="บรรทัดเดียว Passed: <จำนวน>",
    hint="ใช้ตัวแปรนับ แล้ว if score >= 50 ภายใน for",
    answer="""scores = [42, 55, 60, 38, 71, 49]
passed = 0
for score in scores:
    if score >= 50:
        passed = passed + 1
print(f"Passed: {passed}")
""",
)

PROBLEMS["10"] = dict(
    file="10_medium.md", diff="🟡 Medium", emoji="🔥", title="รวมแคลอรี่มื้ออาหาร",
    body="แอปสุขภาพเก็บแคลอรี่ของแต่ละเมนูในลิสต์\nเขียนโปรแกรมรวมแคลอรี่ทั้งมื้อ",
    starter="calories = [320, 150, 90, 210]\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="", sample_out="Calories: 770",
    inp="ไม่มี", out="บรรทัดเดียว Calories: <ผลรวม>",
    hint="สะสมค่าใน loop เหมือนการรวมราคา",
    answer="""calories = [320, 150, 90, 210]
total = 0
for cal in calories:
    total = total + cal
print(f"Calories: {total}")
""",
)

PROBLEMS["11"] = dict(
    file="11_medium.md", diff="🟡 Medium", emoji="💸", title="ราคาหลังขึ้นภาษีรายชิ้น",
    body="ร้านต้องแสดงราคาหลังบวกภาษี 10 บาทต่อชิ้น (ราคาเดิม + 10)\nพิมพ์ราคาใหม่ทีละชิ้น แล้วแสดงยอดรวมราคาใหม่ท้ายสุด",
    starter="prices = [100, 250, 80]\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="", sample_out="110\n260\n90\nNew Total: 460",
    inp="ไม่มี", out="ราคาใหม่ทีละบรรทัด แล้วตามด้วย New Total",
    hint="ใน loop พิมพ์ price + 10 และสะสมผลรวมของราคาใหม่ไปด้วย",
    answer="""prices = [100, 250, 80]
total = 0
for price in prices:
    new_price = price + 10
    print(new_price)
    total = total + new_price
print(f"New Total: {total}")
""",
)

PROBLEMS["12"] = dict(
    file="12_medium.md", diff="🟡 Medium", emoji="✏️", title="นับชื่อที่ยาวเกิน 4 ตัวอักษร",
    body="รายชื่อนักเรียนเก็บในลิสต์\nนับว่ามีกี่ชื่อที่ `len(name) > 4`",
    starter='names = ["Ann", "Bobby", "Chris", "Di", "Elena"]\n\n# เขียนโค้ดตรงนี้\n',
    sample_in="", sample_out="Long Names: 3",
    inp="ไม่มี", out="บรรทัดเดียว Long Names: <จำนวน>",
    hint="ใช้ len(name) กับ if ภายใน for — ยังไม่ต้องใช้ indexing",
    answer="""names = ["Ann", "Bobby", "Chris", "Di", "Elena"]
count = 0
for name in names:
    if len(name) > 4:
        count = count + 1
print(f"Long Names: {count}")
""",
)

PROBLEMS["13"] = dict(
    file="13_medium.md", diff="🟡 Medium", emoji="🧾", title="บิลราคากับ VAT 7%",
    body="ร้านพิมพ์บิลโดยแสดงราคาสุทธิของแต่ละชิ้นหลังบวก VAT 7% (`price * 1.07`)\nแล้วแสดงยอดรวมท้ายบิล ทศนิยม 2 ตำแหน่ง",
    starter="prices = [200, 150, 50]\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="", sample_out="214.00\n160.50\n53.50\nGrand Total: 428.00",
    inp="ไม่มี", out="ราคาสุทธิทีละชิ้น แล้ว Grand Total",
    hint="ใน loop คำนวณ price * 1.07 ใช้ :.2f ทั้งตอนพิมพ์รายชิ้นและยอดรวม",
    answer="""prices = [200, 150, 50]
total = 0
for price in prices:
    with_vat = price * 1.07
    print(f"{with_vat:.2f}")
    total = total + with_vat
print(f"Grand Total: {total:.2f}")
""",
)

PROBLEMS["05"] = dict(
    file="05_challenge.md", diff="🔴 Challenge", emoji="🛍️", title="ใบสรุปตะกร้าสินค้า",
    body="ตะกร้ามีราคาสินค้าในลิสต์\nออกใบสรุปในกรอบ แสดงทุกราคา ยอดรวม จำนวนชิ้น และค่าเฉลี่ย (ทศนิยม 1 ตำแหน่ง)",
    starter="prices = [120, 80, 200, 50]\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="",
    sample_out="========================\n        CART\n========================\n120\n80\n200\n50\n------------------------\nItems   : 4\nTotal   : 450\nAverage : 112.5\n========================",
    inp="ไม่มี", out="ใบสรุปในกรอบตามตัวอย่าง",
    hint="พิมพ์หัวกรอบ → วนพิมพ์ราคาและสะสม → ปิดด้วยสถิติจาก total กับ len",
    answer="""prices = [120, 80, 200, 50]
total = 0
print("========================")
print("        CART")
print("========================")
for price in prices:
    print(price)
    total = total + price
print("------------------------")
print(f"Items   : {len(prices)}")
print(f"Total   : {total}")
print(f"Average : {total / len(prices):.1f}")
print("========================")
""",
)

PROBLEMS["14"] = dict(
    file="14_challenge.md", diff="🔴 Challenge", emoji="📝", title="รายงานผลสอบรายคน",
    body="คะแนนสอบเก็บในลิสต์\nพิมพ์แต่ละคนเป็น `Score: xx -> Pass` หรือ `Fail` (เกณฑ์ 50)\nแล้วสรุปจำนวน Pass / Fail ท้ายกรอบ",
    starter="scores = [45, 70, 50, 39, 88]\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="",
    sample_out="========================\n       RESULTS\n========================\nScore: 45 -> Fail\nScore: 70 -> Pass\nScore: 50 -> Pass\nScore: 39 -> Fail\nScore: 88 -> Pass\n------------------------\nPass : 3\nFail : 2\n========================",
    inp="ไม่มี", out="รายงานในกรอบตามตัวอย่าง",
    hint="ใน loop ตัดสิน Pass/Fail เก็บตัวนับสองตัว แล้วพิมพ์สรุปท้ายกรอบ",
    answer="""scores = [45, 70, 50, 39, 88]
passed = 0
failed = 0
print("========================")
print("       RESULTS")
print("========================")
for score in scores:
    if score >= 50:
        print(f"Score: {score} -> Pass")
        passed = passed + 1
    else:
        print(f"Score: {score} -> Fail")
        failed = failed + 1
print("------------------------")
print(f"Pass : {passed}")
print(f"Fail : {failed}")
print("========================")
""",
)

PROBLEMS["15"] = dict(
    file="15_challenge.md", diff="🔴 Challenge", emoji="🌤️", title="สรุปอากาศรายสัปดาห์",
    body="อุณหภูมิรายวันเก็บในลิสต์\nวันร้อนคือ `>= 32` วันเย็นคือ `< 25` ที่เหลือเป็นวันปกติ\nนับจำนวนแต่ละประเภทแล้วแสดงในกรอบ",
    starter="temps = [30, 33, 24, 28, 35, 22, 31]\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="",
    sample_out="========================\n       WEATHER\n========================\nHot    : 2\nNormal : 3\nCool   : 2\n========================",
    inp="ไม่มี", out="ใบสรุปในกรอบ",
    hint="ใช้ if/else เรียงสองชั้น (หรือ if แยก) นับสามตัวแปร — ยังไม่มี elif ก็ใช้ if ซ้อนได้ตามที่เรียนมา",
    answer="""temps = [30, 33, 24, 28, 35, 22, 31]
hot = 0
normal = 0
cool = 0
for temp in temps:
    if temp >= 32:
        hot = hot + 1
    else:
        if temp < 25:
            cool = cool + 1
        else:
            normal = normal + 1
print("========================")
print("       WEATHER")
print("========================")
print(f"Hot    : {hot}")
print(f"Normal : {normal}")
print(f"Cool   : {cool}")
print("========================")
""",
)

PROBLEMS["16"] = dict(
    file="16_challenge.md", diff="🔴 Challenge", emoji="🎒", title="งบซื้อของโรงเรียน",
    body="โรงเรียนมีงบ `budget` และรายการราคาในลิสต์\nรวมราคาสินค้าทั้งหมด แล้วเทียบกับงบ\nถ้าพอซื้อ → `Status: OK` ไม่งั้น → `Status: Over Budget`",
    starter="budget = 500\nprices = [120, 80, 150, 90]\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="",
    sample_out="========================\n       BUDGET\n========================\nBudget : 500\nNeed   : 440\nStatus : OK\n========================",
    inp="ไม่มี", out="ใบสรุปในกรอบ",
    hint="รวมราคาใน loop ก่อน แล้วค่อย if เทียบกับ budget ทีเดียวตอนท้าย",
    answer="""budget = 500
prices = [120, 80, 150, 90]
need = 0
for price in prices:
    need = need + price
print("========================")
print("       BUDGET")
print("========================")
print(f"Budget : {budget}")
print(f"Need   : {need}")
if need <= budget:
    print("Status : OK")
else:
    print("Status : Over Budget")
print("========================")
""",
)

# Wait - elif is taught at 015, so for 018 we CAN use elif! Chapter 018 > 015.
# Let me fix problem 15 to use elif which is cleaner and in scope.
PROBLEMS["15"]["answer"] = """temps = [30, 33, 24, 28, 35, 22, 31]
hot = 0
normal = 0
cool = 0
for temp in temps:
    if temp >= 32:
        hot = hot + 1
    elif temp < 25:
        cool = cool + 1
    else:
        normal = normal + 1
print("========================")
print("       WEATHER")
print("========================")
print(f"Hot    : {hot}")
print(f"Normal : {normal}")
print(f"Cool   : {cool}")
print("========================")
"""
PROBLEMS["15"]["hint"] = "ใช้ if / elif / else นับสามกลุ่มอุณหภูมิใน loop เดียว"

INDEX = """# 📋 สารบัญโจทย์ — บท 018 loop กับ list

**ขอบเขตของบทนี้:** ความรู้บท 001–017 + **list literal** + **`for item in list`** + **`len()`** + accumulator

> ❌ ยังไม่บังคับใช้ indexing `list[0]` (สอนจริงบท 025) · ไม่มี `.append()` (บท 026)
> ❌ ไม่มี `while` (บท 019) · ไม่มี `min()`/`max()`/`sum()` ในหลักสูตรนี้ช่วงนี้

---

## ลำดับที่แนะนำ

| # | ไฟล์ | ระดับ | โจทย์ | แกนการคิด |
|---|------|-------|-------|-----------|
| 1 | `02_test.md` | 🟢 | เมนูเครื่องดื่ม | วนพิมพ์สมาชิกใน list |
| 2 | `03_test.md` | 🟢 | รายวิชาในเทอมนี้ | วนพิมพ์พร้อมป้ายกำกับ |
| 3 | `04_test.md` | 🟢 | นับจำนวนสมาชิกชมรม | ใช้ `len()` อย่างเดียว |
| 4 | `08_easy.md` | 🟢 | รวมราคาสินค้าในตะกร้า | accumulator พื้นฐาน |
| 5 | `09_easy.md` | 🟢 | ติดป้ายสินค้า | วนพิมพ์รูปแบบคงที่ |
| 6 | `06_medium.md` | 🟡 | ค่าเฉลี่ยคะแนนสอบย่อย | รวม + หาร `len` + `:.1f` |
| 7 | `07_medium.md` | 🟡 | นับคนสอบผ่านเกณฑ์ 50 | `if` ใน loop + นับ |
| 8 | `10_medium.md` | 🟡 | รวมแคลอรี่มื้ออาหาร | accumulator สถานการณ์ใหม่ |
| 9 | `11_medium.md` | 🟡 | ราคาหลังขึ้นภาษีรายชิ้น | แปลงค่าทีละชิ้น + รวม |
| 10 | `12_medium.md` | 🟡 | นับชื่อที่ยาวเกิน 4 ตัวอักษร | `len(item)` ใน loop |
| 11 | `13_medium.md` | 🟡 | บิลราคากับ VAT 7% | คูณทศนิยม + `:.2f` |
| 12 | `05_challenge.md` | 🔴 | ใบสรุปตะกร้าสินค้า | พิมพ์รายการ + สถิติในกรอบ |
| 13 | `14_challenge.md` | 🔴 | รายงานผลสอบรายคน | Pass/Fail รายคน + สรุป |
| 14 | `15_challenge.md` | 🔴 | สรุปอากาศรายสัปดาห์ | แยก 3 กลุ่มด้วย elif |
| 15 | `16_challenge.md` | 🔴 | งบซื้อของโรงเรียน | รวมแล้วเทียบเงื่อนไข |

**สรุป:** 🟢 Easy 5 ข้อ · 🟡 Medium 6 ข้อ · 🔴 Challenge 4 ข้อ = **15 ข้อ**

---

## หมายเหตุสำหรับครู

- ข้อ `02` **ไม่ซ้ำ** ตัวอย่างในบทเรียน (บทเรียนใช้ fruits / scores / colors)
- หลีกเลี่ยงการบังคับใช้ `list[0]` — ใช้ `for item in list` และตัวนับแยกถ้าต้องการลำดับ
- เฉลยทุกข้ออยู่ใน `answer/`
"""

CHAPTER = "loop-with-lists"
SLUGS = {
    "02": "02_drink_menu", "03": "03_subjects", "04": "04_member_count",
    "05": "05_cart_summary", "06": "06_score_average", "07": "07_count_pass",
    "08": "08_sum_prices", "09": "09_item_labels", "10": "10_calories",
    "11": "11_taxed_prices", "12": "12_long_names", "13": "13_vat_bill",
    "14": "14_exam_results", "15": "15_weather_summary", "16": "16_school_budget",
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
    print("018 done")

if __name__ == "__main__":
    emit()
