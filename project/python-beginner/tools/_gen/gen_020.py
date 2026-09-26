# -*- coding: utf-8 -*-
"""Generate gold-standard practice for 020-loop-safety. break/continue/while True OK."""
import os, shutil

BASE = os.path.join(os.path.dirname(__file__), "..", "..", "slide", "020-loop-safety")
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
    file="02_test.md", diff="🟢 Easy", emoji="🛑", title="หยุดที่เลข 7",
    body="วนพิมพ์เลข `1` ถึง `10` แต่เมื่อถึง `7` ให้ `break` ทันที (ไม่พิมพ์ 7)\nแล้วพิมพ์ `Stopped`",
    starter="# เขียนโค้ดตรงนี้\n",
    sample_in="", sample_out="1\n2\n3\n4\n5\n6\nStopped",
    inp="ไม่มี", out="เลข 1–6 แล้ว Stopped",
    hint=None,
    answer="""for i in range(1, 11):
    if i == 7:
        break
    print(i)
print("Stopped")
""",
)

PROBLEMS["03"] = dict(
    file="03_test.md", diff="🟢 Easy", emoji="⏭️", title="ข้ามเลขที่หาร 5 ลงตัว",
    body="วนเลข `1` ถึง `12` ถ้าเลขหารด้วย 5 ลงตัวให้ `continue`\nพิมพ์เฉพาะเลขที่เหลือ",
    starter="# เขียนโค้ดตรงนี้\n",
    sample_in="", sample_out="1\n2\n3\n4\n6\n7\n8\n9\n11\n12",
    inp="ไม่มี", out="เลข 1–12 ที่ไม่หาร 5 ลงตัว",
    hint=None,
    answer="""for i in range(1, 13):
    if i % 5 == 0:
        continue
    print(i)
""",
)

PROBLEMS["04"] = dict(
    file="04_test.md", diff="🟢 Easy", emoji="💬", title="พิมพ์ข้อความจนเจอ stop",
    body='ใช้ `while True` รับข้อความ\nถ้าได้ `"stop"` ให้ `break`\nข้อความอื่นให้พิมพ์กลับในรูปแบบ `Echo: <ข้อความ>`',
    starter="# เขียนโค้ดตรงนี้\n",
    sample_in="hi\npython\nstop", sample_out="Echo: hi\nEcho: python",
    inp="ข้อความทีละบรรทัด จบด้วย stop", out="Echo ของข้อความก่อน stop",
    hint=None,
    answer="""while True:
    word = input()
    if word == "stop":
        break
    print(f"Echo: {word}")
""",
)

PROBLEMS["08"] = dict(
    file="08_easy.md", diff="🟢 Easy", emoji="➕", title="พิมพ์เฉพาะจำนวนบวก",
    body="มีลิสต์ตัวเลขปนบวก-ลบ\nใช้ `continue` ข้ามค่าที่ `< 0` แล้วพิมพ์เฉพาะจำนวนบวกและศูนย์",
    starter="nums = [4, -2, 0, 7, -5, 3]\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="", sample_out="4\n0\n7\n3",
    inp="ไม่มี", out="ค่าที่ไม่ติดลบทีละบรรทัด",
    hint=None,
    answer="""nums = [4, -2, 0, 7, -5, 3]
for n in nums:
    if n < 0:
        continue
    print(n)
""",
)

PROBLEMS["09"] = dict(
    file="09_easy.md", diff="🟢 Easy", emoji="🔎", title="หาเลขคู่แรกแล้วหยุด",
    body="วนเลข `1` ถึง `9` เมื่อเจอเลขคู่ตัวแรกให้พิมพ์เลขนั้น แล้ว `break`",
    starter="# เขียนโค้ดตรงนี้\n",
    sample_in="", sample_out="2",
    inp="ไม่มี", out="เลขคู่ตัวแรกเพียงบรรทัดเดียว",
    hint=None,
    answer="""for i in range(1, 10):
    if i % 2 == 0:
        print(i)
        break
""",
)

PROBLEMS["06"] = dict(
    file="06_medium.md", diff="🟡 Medium", emoji="📇", title="ค้นหาชื่อในรายการ",
    body="มีลิสต์ชื่อ รับชื่อที่ต้องการค้นหา\nวนลิสต์ด้วยตัวนับตำแหน่งเริ่มที่ 1\nเมื่อเจอชื่อตรงกันพิมพ์ `Found at <ตำแหน่ง>` แล้ว `break`\nถ้าวนจบแล้วยังไม่เจอพิมพ์ `Not Found`",
    starter='names = ["Ann", "Ben", "Cara", "Dan"]\ntarget = input()\n\n# เขียนโค้ดตรงนี้\n',
    sample_in="Cara", sample_out="Found at 3",
    inp="ชื่อที่ค้นหา 1 บรรทัด", out="Found at ... หรือ Not Found",
    hint="ใช้ตัวแปร found เป็นข้อความเริ่มต้น Not Found ถ้าเจอให้เปลี่ยนแล้ว break",
    answer="""names = ["Ann", "Ben", "Cara", "Dan"]
target = input()
pos = 1
result = "Not Found"
for name in names:
    if name == target:
        result = f"Found at {pos}"
        break
    pos = pos + 1
print(result)
""",
)

PROBLEMS["07"] = dict(
    file="07_medium.md", diff="🟡 Medium", emoji="📆", title="ข้ามวันหยุดสุดสัปดาห์",
    body='มีลิสต์วันในสัปดาห์\nถ้าเป็น `"Sat"` หรือ `"Sun"` ให้ `continue`\nวันที่เหลือพิมพ์ `Work: <วัน>`',
    starter='days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]\n\n# เขียนโค้ดตรงนี้\n',
    sample_in="", sample_out="Work: Mon\nWork: Tue\nWork: Wed\nWork: Thu\nWork: Fri",
    inp="ไม่มี", out="เฉพาะวันทำงาน",
    hint="ใช้ if ตรวจ Sat/Sun ด้วย or แล้ว continue",
    answer="""days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for day in days:
    if day == "Sat" or day == "Sun":
        continue
    print(f"Work: {day}")
""",
)

PROBLEMS["10"] = dict(
    file="10_medium.md", diff="🟡 Medium", emoji="💰", title="รวมเฉพาะยอดบวกจนเจอ 0",
    body="ใช้ `while True` รับจำนวน\nถ้าได้ `0` ให้ `break`\nถ้าได้ค่าน้อยกว่า 0 ให้ `continue` (ไม่บวก)\nนอกนั้นบวกเข้า total แล้วท้ายสุดพิมพ์ผลรวม",
    starter="total = 0\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="10\n-3\n5\n0", sample_out="Total: 15",
    inp="จำนวนทีละบรรทัด จบด้วย 0", out="Total: <ผลรวมค่าบวก>",
    hint="ลำดับในลูป: รับค่า → ถ้า 0 break → ถ้าติดลบ continue → ค่อยบวก",
    answer="""total = 0
while True:
    number = int(input())
    if number == 0:
        break
    if number < 0:
        continue
    total = total + number
print(f"Total: {total}")
""",
)

PROBLEMS["11"] = dict(
    file="11_medium.md", diff="🟡 Medium", emoji="🔐", title="ล็อกอินด้วย while True",
    body='รหัสถูกต้องคือ `"secret"`\nใช้ `while True` รับรหัส\nถูกรหัสพิมพ์ `Welcome` แล้ว break\nผิดพิมพ์ `Try again` แล้ววนต่อ',
    starter="# เขียนโค้ดตรงนี้\n",
    sample_in="123\npass\nsecret", sample_out="Try again\nTry again\nWelcome",
    inp="รหัสทีละบรรทัดจนถูก", out="Try again ตามครั้งที่ผิด แล้ว Welcome",
    hint="if/else ใน while True — ถูกแล้ว break",
    answer="""while True:
    password = input()
    if password == "secret":
        print("Welcome")
        break
    else:
        print("Try again")
""",
)

PROBLEMS["12"] = dict(
    file="12_medium.md", diff="🟡 Medium", emoji="🎓", title="แสดงเฉพาะคะแนนผ่าน",
    body="มีลิสต์คะแนน ใช้ `continue` ข้ามคะแนน `< 50`\nพิมพ์เฉพาะคะแนนที่ผ่านในรูปแบบ `Pass: <คะแนน>`",
    starter="scores = [40, 55, 62, 48, 90]\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="", sample_out="Pass: 55\nPass: 62\nPass: 90",
    inp="ไม่มี", out="เฉพาะคะแนนที่ผ่าน",
    hint="if score < 50: continue",
    answer="""scores = [40, 55, 62, 48, 90]
for score in scores:
    if score < 50:
        continue
    print(f"Pass: {score}")
""",
)

PROBLEMS["13"] = dict(
    file="13_medium.md", diff="🟡 Medium", emoji="📋", title="เมนูคำสั่งจน exit",
    body='ใช้ `while True` รับคำสั่ง\nถ้าได้ `"exit"` พิมพ์ `Bye` แล้ว break\nคำสั่งอื่นพิมพ์ `CMD: <คำสั่ง>`',
    starter="# เขียนโค้ดตรงนี้\n",
    sample_in="help\nlist\nexit", sample_out="CMD: help\nCMD: list\nBye",
    inp="คำสั่งทีละบรรทัด จบด้วย exit", out="CMD ของคำสั่งก่อน exit แล้ว Bye",
    hint="คล้ายข้อ Echo แต่ข้อความปิดท้ายต่างกัน",
    answer="""while True:
    cmd = input()
    if cmd == "exit":
        print("Bye")
        break
    print(f"CMD: {cmd}")
""",
)

PROBLEMS["05"] = dict(
    file="05_challenge.md", diff="🔴 Challenge", emoji="🎯", title="ทายเลขพร้อมคำใบ้",
    body='เลขลับคือ `25`\nใช้ `while True` รับคำทาย\n- ถูก → พิมพ์ `Correct!` แล้ว break\n- น้อยเกินไป → พิมพ์ `Too low` แล้ว continue\n- มากเกินไป → พิมพ์ `Too high` แล้ว continue',
    starter="secret = 25\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="10\n40\n25", sample_out="Too low\nToo high\nCorrect!",
    inp="คำทายทีละบรรทัด", out="คำใบ้จนถูก",
    hint="เทียบ guess กับ secret ด้วย if / elif / else ใน while True",
    answer="""secret = 25
while True:
    guess = int(input())
    if guess == secret:
        print("Correct!")
        break
    elif guess < secret:
        print("Too low")
        continue
    else:
        print("Too high")
        continue
""",
)

PROBLEMS["14"] = dict(
    file="14_challenge.md", diff="🔴 Challenge", emoji="📦", title="รับออเดอร์ข้ามรายการยกเลิก",
    body='ใช้ `while True` รับชื่อสินค้า\n- `"done"` → break\n- `"cancel"` → continue (ไม่พิมพ์)\n- อื่นๆ → พิมพ์ `Order: <ชื่อ>`\nท้ายสุดพิมพ์ `End of orders`',
    starter="# เขียนโค้ดตรงนี้\n",
    sample_in="pen\ncancel\nbook\ndone", sample_out="Order: pen\nOrder: book\nEnd of orders",
    inp="ชื่อสินค้าทีละบรรทัด จบด้วย done", out="Order ที่ไม่ถูกยกเลิก แล้ว End of orders",
    hint="ตรวจ done ก่อน แล้วค่อยตรวจ cancel แล้วค่อยพิมพ์",
    answer="""while True:
    item = input()
    if item == "done":
        break
    if item == "cancel":
        continue
    print(f"Order: {item}")
print("End of orders")
""",
)

PROBLEMS["15"] = dict(
    file="15_challenge.md", diff="🔴 Challenge", emoji="🏫", title="นับคนเข้าเรียนข้าม Absent",
    body='มีลิสต์สถานะนักเรียน\n- ค่า `"END"` → break (ไม่นับ)\n- ค่า `"Absent"` → continue\n- อื่นๆ → นับเป็นคนมาเรียน\nแสดงจำนวนคนมาเรียน',
    starter='status = ["Present", "Absent", "Present", "Present", "END", "Present"]\n\n# เขียนโค้ดตรงนี้\n',
    sample_in="", sample_out="Present Count: 3",
    inp="ไม่มี", out="Present Count: <จำนวน>",
    hint="for + if END break + if Absent continue + นับ",
    answer="""status = ["Present", "Absent", "Present", "Present", "END", "Present"]
count = 0
for s in status:
    if s == "END":
        break
    if s == "Absent":
        continue
    count = count + 1
print(f"Present Count: {count}")
""",
)

PROBLEMS["16"] = dict(
    file="16_challenge.md", diff="🔴 Challenge", emoji="🏦", title="ตู้ฝาก-ถอนจน quit",
    body='เริ่มยอดเงิน `balance = 1000`\nใช้ `while True` รับคำสั่ง\n- `"quit"` → พิมพ์ยอดคงเหลือในกรอบแล้ว break\n- `"deposit"` → รับจำนวนบวกเข้า balance\n- `"withdraw"` → รับจำนวน ถ้ามากกว่า balance ให้พิมพ์ `Denied` แล้ว continue (ไม่หัก)\n  ถ้าน้อยกว่าหรือเท่าให้หักได้\n- คำสั่งอื่น → พิมพ์ `Unknown` แล้ว continue',
    starter="balance = 1000\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="deposit\n200\nwithdraw\n1500\nwithdraw\n300\nquit",
    sample_out="Denied\n========================\nBalance: 900\n========================",
    inp="คำสั่งและจำนวนตามลำดับ จบด้วย quit",
    out="Denied ถ้ามี และกรอบยอดคงเหลือท้ายสุด",
    hint="แยก if ตามชนิดคำสั่ง — withdraw ที่เกินให้ continue ก่อนหัก",
    answer="""balance = 1000
while True:
    cmd = input()
    if cmd == "quit":
        print("========================")
        print(f"Balance: {balance}")
        print("========================")
        break
    elif cmd == "deposit":
        amount = int(input())
        balance = balance + amount
    elif cmd == "withdraw":
        amount = int(input())
        if amount > balance:
            print("Denied")
            continue
        balance = balance - amount
    else:
        print("Unknown")
        continue
""",
)

INDEX = """# 📋 สารบัญโจทย์ — บท 020 loop safety

**ขอบเขตของบทนี้:** ความรู้บท 001–019 + **`break`** + **`continue`** + **`while True` + break**

---

## ลำดับที่แนะนำ

| # | ไฟล์ | ระดับ | โจทย์ | แกนการคิด |
|---|------|-------|-------|-----------|
| 1 | `02_test.md` | 🟢 | หยุดที่เลข 7 | break ใน for |
| 2 | `03_test.md` | 🟢 | ข้ามเลขที่หาร 5 ลงตัว | continue ใน for |
| 3 | `04_test.md` | 🟢 | พิมพ์ข้อความจนเจอ stop | while True + break |
| 4 | `08_easy.md` | 🟢 | พิมพ์เฉพาะจำนวนบวก | continue กับ list |
| 5 | `09_easy.md` | 🟢 | หาเลขคู่แรกแล้วหยุด | break เมื่อเจอเงื่อนไข |
| 6 | `06_medium.md` | 🟡 | ค้นหาชื่อในรายการ | หาค่า + ตำแหน่ง + break |
| 7 | `07_medium.md` | 🟡 | ข้ามวันหยุดสุดสัปดาห์ | continue + or |
| 8 | `10_medium.md` | 🟡 | รวมเฉพาะยอดบวกจนเจอ 0 | break + continue คู่กัน |
| 9 | `11_medium.md` | 🟡 | ล็อกอินด้วย while True | ข้อความตอบกลับในลูป |
| 10 | `12_medium.md` | 🟡 | แสดงเฉพาะคะแนนผ่าน | continue กรอง list |
| 11 | `13_medium.md` | 🟡 | เมนูคำสั่งจน exit | while True เมนูสั้น |
| 12 | `05_challenge.md` | 🔴 | ทายเลขพร้อมคำใบ้ | break + continue + ใบ้ |
| 13 | `14_challenge.md` | 🔴 | รับออเดอร์ข้ามรายการยกเลิก | สองเงื่อนไขพิเศษในลูป |
| 14 | `15_challenge.md` | 🔴 | นับคนเข้าเรียนข้าม Absent | break + continue ใน list |
| 15 | `16_challenge.md` | 🔴 | ตู้ฝาก-ถอนจน quit | เมนูหลายคำสั่ง + ตรวจยอด |

**สรุป:** 🟢 Easy 5 ข้อ · 🟡 Medium 6 ข้อ · 🔴 Challenge 4 ข้อ = **15 ข้อ**

---

## หมายเหตุสำหรับครู

- ข้อ `02` ไม่ซ้ำบทเรียน (บทเรียน break ที่ i == 5 และ continue ข้ามคู่/`i == 3`)
- ข้อ Echo/quit ในบทเรียนใช้คำว่า quit — โจทย์ใช้ stop / exit / done แทน
"""

CHAPTER = "loop-safety"
SLUGS = {
    "02": "02_stop_at_seven", "03": "03_skip_div5", "04": "04_echo_stop",
    "05": "05_guess_hints", "06": "06_find_name", "07": "07_skip_weekend",
    "08": "08_positive_only", "09": "09_first_even", "10": "10_sum_positives",
    "11": "11_login_loop", "12": "12_pass_scores", "13": "13_cmd_menu",
    "14": "14_orders", "15": "15_attendance_skip", "16": "16_bank_menu",
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
    print("020 done")

if __name__ == "__main__":
    emit()
