# -*- coding: utf-8 -*-
"""Generate gold-standard practice for 022-loop-review. Rebuild to exactly 15."""
import os, shutil

BASE = os.path.join(os.path.dirname(__file__), "..", "..", "slide", "022-loop-review")
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
    file="02_test.md", diff="🟢 Easy", emoji="➕", title="ผลรวม 1 ถึง n",
    body="รับ `n` แล้วหาผลรวม 1 ถึง n ด้วย `for`\nใช้ `+=` ได้",
    starter="n = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="6", sample_out="Sum: 21",
    inp="จำนวนเต็ม n 1 บรรทัด", out="Sum: <ผลรวม>",
    hint=None,
    answer="""n = int(input())
total = 0
for i in range(1, n + 1):
    total += i
print(f"Sum: {total}")
""",
)

PROBLEMS["03"] = dict(
    file="03_test.md", diff="🟢 Easy", emoji="🔟", title="พิมพ์พหุคูณของ n",
    body="รับ `n` แล้วพิมพ์ `n*1` ถึง `n*5` ทีละบรรทัด",
    starter="n = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="4", sample_out="4\n8\n12\n16\n20",
    inp="จำนวนเต็ม n 1 บรรทัด", out="พหุคูณ 5 ค่า",
    hint=None,
    answer="""n = int(input())
for i in range(1, 6):
    print(n * i)
""",
)

PROBLEMS["04"] = dict(
    file="04_test.md", diff="🟢 Easy", emoji="📋", title="รายการคะแนนพร้อมลำดับ",
    body="มีลิสต์คะแนน พิมพ์เป็น `1. 80` `2. 90` … โดยใช้ตัวนับแยก (ยังไม่บังคับ indexing)",
    starter="scores = [80, 90, 75]\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="", sample_out="1. 80\n2. 90\n3. 75",
    inp="ไม่มี", out="คะแนนพร้อมลำดับ",
    hint=None,
    answer="""scores = [80, 90, 75]
num = 1
for score in scores:
    print(f"{num}. {score}")
    num += 1
""",
)

PROBLEMS["08"] = dict(
    file="08_easy.md", diff="🟢 Easy", emoji="⏳", title="นับถอยหลังแล้ว Go",
    body='รับ `n` นับถอยหลังถึง 1 ด้วย while แล้วพิมพ์ `"Go!"`',
    starter="n = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="3", sample_out="3\n2\n1\nGo!",
    inp="จำนวนเต็ม n 1 บรรทัด", out="นับถอยหลังแล้ว Go!",
    hint=None,
    answer="""n = int(input())
while n > 0:
    print(n)
    n -= 1
print("Go!")
""",
)

PROBLEMS["09"] = dict(
    file="09_easy.md", diff="🟢 Easy", emoji="🔊", title="Echo จนเจอ 0",
    body="ใช้ `while True` รับจำนวน ถ้าได้ `0` ให้ break\nนอกนั้นพิมพ์จำนวนนั้นกลับไป",
    starter="# เขียนโค้ดตรงนี้\n",
    sample_in="5\n8\n0", sample_out="5\n8",
    inp="จำนวนทีละบรรทัด จบด้วย 0", out="Echo ค่าก่อน 0",
    hint=None,
    answer="""while True:
    number = int(input())
    if number == 0:
        break
    print(number)
""",
)

PROBLEMS["06"] = dict(
    file="06_medium.md", diff="🟡 Medium", emoji="🛒", title="ยอดสะสมราคาสินค้า",
    body="มีลิสต์ราคา พิมพ์ยอดสะสมหลังบวกแต่ละชิ้น (running total)",
    starter="prices = [50, 30, 20]\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="", sample_out="50\n80\n100",
    inp="ไม่มี", out="ยอดสะสมทีละชิ้น",
    hint="เก็บ total แล้วบวกทีละราคา พิมพ์หลังบวกทุกครั้ง",
    answer="""prices = [50, 30, 20]
total = 0
for price in prices:
    total += price
    print(total)
""",
)

PROBLEMS["07"] = dict(
    file="07_medium.md", diff="🟡 Medium", emoji="🔍", title="นับค่าที่ตรงเป้าหมาย",
    body="มีลิสต์ตัวเลข รับค่า `target` แล้วนับว่ามีกี่ตัวที่เท่ากับ target",
    starter="nums = [2, 5, 2, 7, 2, 9]\ntarget = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="2", sample_out="Count: 3",
    inp="ค่า target 1 บรรทัด", out="Count: <จำนวน>",
    hint="วน list แล้ว if เท่ากับ target ให้นับเพิ่ม",
    answer="""nums = [2, 5, 2, 7, 2, 9]
target = int(input())
count = 0
for n in nums:
    if n == target:
        count += 1
print(f"Count: {count}")
""",
)

PROBLEMS["10"] = dict(
    file="10_medium.md", diff="🟡 Medium", emoji="✅", title="ตรวจว่าทุกคนผ่านไหม",
    body="มีลิสต์คะแนน ถ้าทุกคน `>= 60` พิมพ์ `All Pass`\nถ้ามีคนใดคนหนึ่งไม่ถึง พิมพ์ `Has Fail`\nใช้ loop ตรวจได้ (พบ fail แล้ว break ก็ได้)",
    starter="scores = [70, 65, 80, 90]\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="", sample_out="All Pass",
    inp="ไม่มี", out="All Pass หรือ Has Fail",
    hint="สมมติว่าผ่านไว้ก่อน ถ้าเจอคนไม่ผ่านให้เปลี่ยนสถานะแล้วหยุดได้",
    answer="""scores = [70, 65, 80, 90]
result = "All Pass"
for score in scores:
    if score < 60:
        result = "Has Fail"
        break
print(result)
""",
)

PROBLEMS["11"] = dict(
    file="11_medium.md", diff="🟡 Medium", emoji="🎯", title="กรองคะแนนด้วย continue",
    body="รับจำนวนรอบ `k` แล้วรับคะแนน k ค่า\nพิมพ์เฉพาะคะแนนที่เป็นเลขคู่ (ใช้ continue ข้ามคี่)",
    starter="k = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="5\n3\n8\n1\n4\n7", sample_out="8\n4",
    inp="บรรทัดแรก k ตามด้วยคะแนน k บรรทัด", out="เฉพาะคะแนนคู่",
    hint="วน range(k) รับคะแนน ถ้าเป็นคี่ให้ continue",
    answer="""k = int(input())
for i in range(k):
    score = int(input())
    if score % 2 != 0:
        continue
    print(score)
""",
)

PROBLEMS["12"] = dict(
    file="12_medium.md", diff="🟡 Medium", emoji="⭐", title="สามเหลี่ยมดาวขนาด n",
    body="รับ `n` แล้วพิมพ์สามเหลี่ยมดาวแถวที่ 1 มี 1 ดาว … แถวที่ n มี n ดาว",
    starter="n = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="3", sample_out="*\n**\n***",
    inp="จำนวนเต็ม n 1 บรรทัด", out="สามเหลี่ยมดาว",
    hint="ลูปนอกเป็นแถว ลูปในพิมพ์ดาวตามหมายเลขแถว",
    answer="""n = int(input())
for row in range(1, n + 1):
    for col in range(row):
        print("*", end="")
    print()
""",
)

PROBLEMS["13"] = dict(
    file="13_medium.md", diff="🟡 Medium", emoji="🧮", title="รวมเลขจนเจอศูนย์แล้วรายงาน",
    body="ใช้ while True รับเลขจนเจอ 0\nแสดงจำนวนค่าที่รับ (ไม่นับ 0) และผลรวมในบรรทัดเดียว",
    starter="# เขียนโค้ดตรงนี้\n",
    sample_in="4\n6\n0", sample_out="Count: 2, Total: 10",
    inp="จำนวนทีละบรรทัด จบด้วย 0", out="Count และ Total",
    hint="สะสม count กับ total ในลูป พิมพ์หลัง break",
    answer="""count = 0
total = 0
while True:
    number = int(input())
    if number == 0:
        break
    count += 1
    total += number
print(f"Count: {count}, Total: {total}")
""",
)

PROBLEMS["05"] = dict(
    file="05_challenge.md", diff="🔴 Challenge", emoji="buzz", title="FizzBuzz 1 ถึง n",
    body="""รับ `n` แล้วพิมพ์เลข 1 ถึง n ตามกติกา
- หาร 15 ลงตัว → `FizzBuzz`
- หาร 3 ลงตัว → `Fizz`
- หาร 5 ลงตัว → `Buzz`
- นอกนั้น → พิมพ์เลขนั้น""",
    starter="n = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="15",
    sample_out="1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz",
    inp="จำนวนเต็ม n 1 บรรทัด", out="FizzBuzz 1 ถึง n",
    hint="ตรวจหาร 15 ก่อน แล้วค่อย 3 และ 5 — ลำดับ if สำคัญ",
    answer="""n = int(input())
for i in range(1, n + 1):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
""",
)
# Fix emoji - "buzz" is invalid, use a real emoji
PROBLEMS["05"]["emoji"] = "🐝"

PROBLEMS["14"] = dict(
    file="14_challenge.md", diff="🔴 Challenge", emoji="📊", title="รายงานเกรดจากลิสต์",
    body="มีลิสต์คะแนน 5 ค่า\nแต่ละคน: `>= 80` → A, `>= 50` → B, นอกนั้น → C\nพิมพ์เกรดทีละคน แล้วนับจำนวน A ในกรอบสรุป",
    starter="scores = [85, 42, 70, 90, 55]\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="",
    sample_out="A\nC\nB\nA\nB\n========================\nA Count: 2\n========================",
    inp="ไม่มี", out="เกรดรายคน + สรุปจำนวน A",
    hint="ใช้ elif จัดเกรด และสะสมตัวนับ A",
    answer="""scores = [85, 42, 70, 90, 55]
a_count = 0
for score in scores:
    if score >= 80:
        print("A")
        a_count += 1
    elif score >= 50:
        print("B")
    else:
        print("C")
print("========================")
print(f"A Count: {a_count}")
print("========================")
""",
)

PROBLEMS["15"] = dict(
    file="15_challenge.md", diff="🔴 Challenge", emoji="🔁", title="for รวมแล้ว while ลด",
    body="รับ `n`\nขั้น 1: ใช้ for รวม 1 ถึง n เก็บใน `total`\nขั้น 2: ใช้ while ลด `total` ทีละ 1 พิมพ์ค่าหลังลดทุกครั้งจนเหลือ 0",
    starter="n = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="3", sample_out="6\n5\n4\n3\n2\n1\n0",
    # Wait: sum 1+2+3=6, then while decrease printing each time until 0.
    # If we print after each decrement starting from 6: 5,4,3,2,1,0 — missing initial 6?
    # Or print total first then decrease?
    # User sample intent: show 6 then countdown to 0.
    # total=6; while total >= 0: print(total); total -= 1  → 6..0
    # Or: print sum first somehow. Let me use while total >= 0.
    inp="จำนวนเต็ม n 1 บรรทัด", out="ผลรวม แล้วลดทีละ 1 ถึง 0",
    hint="รวมด้วย for ก่อน แล้ว while พิมพ์และลดค่าจนถึง 0",
    answer="""n = int(input())
total = 0
for i in range(1, n + 1):
    total += i
while total >= 0:
    print(total)
    total -= 1
""",
)

PROBLEMS["16"] = dict(
    file="16_challenge.md", diff="🔴 Challenge", emoji="🏁", title="รวมแต้มบวกข้ามค่าลบจน done",
    body='ใช้ while True รับข้อความ\n- `"done"` → break\n- แปลงเป็นจำนวนด้วย int — ถ้าติดลบให้ continue\n- ค่าบวกหรือศูนย์ให้บวกเข้า total\nท้ายสุดพิมพ์ยอดรวม',
    starter="# เขียนโค้ดตรงนี้\n",
    sample_in="10\n-5\n7\ndone", sample_out="Total: 17",
    inp="ค่าทีละบรรทัด (ตัวเลขหรือ done)", out="Total: <ผลรวมค่าที่ไม่ติดลบ>",
    hint="ตรวจ done ก่อน แล้วแปลงเป็น int — ค่าติดลบข้ามด้วย continue",
    answer="""total = 0
while True:
    text = input()
    if text == "done":
        break
    number = int(text)
    if number < 0:
        continue
    total += number
print(f"Total: {total}")
""",
)

INDEX = """# 📋 สารบัญโจทย์ — บท 022 loop review

**ขอบเขตของบทนี้:** ทบทวน loop ทั้ง fore / while / break / continue / nested + ใช้ `+=` ได้

> ไม่มี syntax ใหม่นอกจาก `+=` ที่ปรากฏในบทเรียน

---

## ลำดับที่แนะนำ

| # | ไฟล์ | ระดับ | โจทย์ | แกนการคิด |
|---|------|-------|-------|-----------|
| 1 | `02_test.md` | 🟢 | ผลรวม 1 ถึง n | for + += |
| 2 | `03_test.md` | 🟢 | พิมพ์พหุคูณของ n | for คูณค่า |
| 3 | `04_test.md` | 🟢 | รายการคะแนนพร้อมลำดับ | ตัวนับคู่ for-list |
| 4 | `08_easy.md` | 🟢 | นับถอยหลังแล้ว Go | while นับลง |
| 5 | `09_easy.md` | 🟢 | Echo จนเจอ 0 | while True + break |
| 6 | `06_medium.md` | 🟡 | ยอดสะสมราคาสินค้า | running total |
| 7 | `07_medium.md` | 🟡 | นับค่าที่ตรงเป้าหมาย | นับใน list |
| 8 | `10_medium.md` | 🟡 | ตรวจว่าทุกคนผ่านไหม | ตรวจครบ + break |
| 9 | `11_medium.md` | 🟡 | กรองคะแนนด้วย continue | continue + input หลายรอบ |
| 10 | `12_medium.md` | 🟡 | สามเหลี่ยมดาวขนาด n | nested ทบทวน |
| 11 | `13_medium.md` | 🟡 | รวมเลขจนเจอศูนย์แล้วรายงาน | while True สะสมสองค่า |
| 12 | `05_challenge.md` | 🔴 | FizzBuzz 1 ถึง n | หลายเงื่อนไขใน loop |
| 13 | `14_challenge.md` | 🔴 | รายงานเกรดจากลิสต์ | elif + สรุป |
| 14 | `15_challenge.md` | 🔴 | for รวมแล้ว while ลด | ผสม for + while |
| 15 | `16_challenge.md` | 🔴 | รวมแต้มบวกข้ามค่าลบจน done | break + continue + แปลงค่า |

**สรุป:** 🟢 Easy 5 ข้อ · 🟡 Medium 6 ข้อ · 🔴 Challenge 4 ข้อ = **15 ข้อ**
"""

CHAPTER = "loop-review"
SLUGS = {
    "02": "02_sum_to_n", "03": "03_multiples", "04": "04_numbered_scores",
    "05": "05_fizzbuzz", "06": "06_running_total", "07": "07_count_target",
    "08": "08_countdown_go", "09": "09_echo_zero", "10": "10_all_pass",
    "11": "11_even_filter", "12": "12_star_triangle", "13": "13_count_total",
    "14": "14_grade_report", "15": "15_for_then_while", "16": "16_sum_until_done",
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
    print("022 done")

if __name__ == "__main__":
    emit()
