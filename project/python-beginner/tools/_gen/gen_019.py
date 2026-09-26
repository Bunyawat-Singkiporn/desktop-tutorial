# -*- coding: utf-8 -*-
"""Generate gold-standard practice for 019-while-loop. NO break/continue/while True."""
import os, shutil

BASE = os.path.join(os.path.dirname(__file__), "..", "..", "slide", "019-while-loop")
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
    file="02_test.md", diff="🟢 Easy", emoji="🚀", title="นับลงจอด 1 ถึง 4",
    body="ยานอวกาศจำลองนับ `1` ถึง `4` ก่อนพร้อมทำงาน\nหลังพิมพ์ครบให้พิมพ์ `Ready!`\n\nเขียนด้วย `while` (ห้ามใช้ for)",
    starter="count = 1\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="", sample_out="1\n2\n3\n4\nReady!",
    inp="ไม่มี", out="เลข 1–4 แล้วตามด้วย Ready!",
    hint=None,
    answer='count = 1\nwhile count <= 4:\n    print(count)\n    count = count + 1\nprint("Ready!")\n',
)

PROBLEMS["03"] = dict(
    file="03_test.md", diff="🟢 Easy", emoji="2️⃣", title="พิมพ์เลขคู่ด้วย while",
    body="พิมพ์เลขคู่ `2 4 6 8 10` ทีละบรรทัด ด้วย `while`\nเริ่มจากตัวแปร `n = 2` แล้วเพิ่มทีละ 2",
    starter="n = 2\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="", sample_out="2\n4\n6\n8\n10",
    inp="ไม่มี", out="เลขคู่ 5 ค่า",
    hint=None,
    answer="n = 2\nwhile n <= 10:\n    print(n)\n    n = n + 2\n",
)

PROBLEMS["04"] = dict(
    file="04_test.md", diff="🟢 Easy", emoji="🔑", title="รหัสผ่านจนถูก",
    body='ระบบล็อกอินรหัสถูกต้องคือ `"ok"`\nรับรหัสซ้ำด้วย `while` จนกว่าจะตรง แล้วพิมพ์ `Access Granted`\n\n> ห้ามใช้ `break` / `while True` — ให้ออกจากลูปด้วยเงื่อนไข while',
    starter='password = input()\n\n# เขียนโค้ดตรงนี้\n',
    sample_in="no\nwait\nok", sample_out="Access Granted",
    inp="รหัสทีละบรรทัด จนถูกต้อง", out="Access Granted เมื่อรหัสถูก",
    hint=None,
    answer='password = input()\nwhile password != "ok":\n    password = input()\nprint("Access Granted")\n',
)

PROBLEMS["08"] = dict(
    file="08_easy.md", diff="🟢 Easy", emoji="⏱️", title="นับถอยหลังเริ่มงาน",
    body='รับจำนวนเต็ม `n` แล้วนับถอยหลังจาก n ถึง 1\nเมื่อจบให้พิมพ์ `Start!`',
    starter="n = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="3", sample_out="3\n2\n1\nStart!",
    inp="จำนวนเต็ม n 1 บรรทัด", out="นับถอยหลังแล้ว Start!",
    hint=None,
    answer='n = int(input())\nwhile n > 0:\n    print(n)\n    n = n - 1\nprint("Start!")\n',
)

PROBLEMS["09"] = dict(
    file="09_easy.md", diff="🟢 Easy", emoji="🔞", title="ตรวจอายุจนครบ 18",
    body="รับอายุซ้ำจนกว่าจะได้ค่า `>= 18`\nแล้วพิมพ์ `Adult`",
    starter="age = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="15\n16\n18", sample_out="Adult",
    inp="อายุทีละบรรทัด จนครบเกณฑ์", out="Adult เมื่ออายุถึงเกณฑ์",
    hint=None,
    answer='age = int(input())\nwhile age < 18:\n    age = int(input())\nprint("Adult")\n',
)

PROBLEMS["06"] = dict(
    file="06_medium.md", diff="🟡 Medium", emoji="📥", title="รวมเลขจนเจอ -1",
    body="รับจำนวนเต็มซ้ำๆ รวมค่าไปเรื่อยๆ\nเมื่อผู้ใช้พิมพ์ `-1` ให้หยุด (ไม่เอามาบวก) แล้วแสดงผลรวม",
    starter="total = 0\nnumber = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="10\n20\n5\n-1", sample_out="Total: 35",
    inp="จำนวนเต็มทีละบรรทัด จบด้วย -1", out="Total: <ผลรวม>",
    hint="ใช้ while number != -1 แล้วรับค่าใหม่ท้ายลูป",
    answer="""total = 0
number = int(input())
while number != -1:
    total = total + number
    number = int(input())
print(f"Total: {total}")
""",
)

PROBLEMS["07"] = dict(
    file="07_medium.md", diff="🟡 Medium", emoji="🎲", title="ทายเลขลับ 10",
    body='เลขลับคือ `10`\nรับคำทายซ้ำ ถ้ายังไม่ถูกพิมพ์ `Wrong`\nเมื่อถูกพิมพ์ `Correct!` แล้วจบ\n\n> ออกจากลูปด้วยเงื่อนไข while เท่านั้น',
    starter="secret = 10\nguess = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="3\n8\n10", sample_out="Wrong\nWrong\nCorrect!",
    inp="คำทายทีละบรรทัด", out="Wrong ทีละครั้งที่ผิด สุดท้าย Correct!",
    hint="พิมพ์ Wrong ในลูป แล้วรับ guess ใหม่ — พิมพ์ Correct! หลังลูป",
    answer="""secret = 10
guess = int(input())
while guess != secret:
    print("Wrong")
    guess = int(input())
print("Correct!")
""",
)

PROBLEMS["10"] = dict(
    file="10_medium.md", diff="🟡 Medium", emoji="💵", title="เงินฝากทบต้นเท่าตัว",
    body="เริ่มเงิน `money = 100`\nทุกเดือนเงินเพิ่มเป็นสองเท่า (`money = money * 2`)\nพิมพ์ยอดเงินแต่ละเดือนจนกว่าจะ `>= 1000`",
    starter="money = 100\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="", sample_out="100\n200\n400\n800\n1600",
    inp="ไม่มี", out="ยอดเงินแต่ละรอบจนถึงหรือเกิน 1000",
    hint="พิมพ์ค่าก่อน แล้วค่อยคูณสอง — ระวังลำดับในลูป",
    answer="""money = 100
while money < 1000:
    print(money)
    money = money * 2
print(money)
""",
)

PROBLEMS["11"] = dict(
    file="11_medium.md", diff="🟡 Medium", emoji="📊", title="นับคะแนนจนเจอศูนย์",
    body="รับคะแนนทีละตัว จนเจอ `0` (ไม่นับ 0)\nนับว่ามีคะแนนกี่ตัว แล้วแสดงจำนวน",
    starter="count = 0\nscore = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="80\n70\n90\n0", sample_out="Count: 3",
    inp="คะแนนทีละบรรทัด จบด้วย 0", out="Count: <จำนวน>",
    hint="คล้ายข้อรวมเลข แต่สะสมตัวนับแทนผลรวม",
    answer="""count = 0
score = int(input())
while score != 0:
    count = count + 1
    score = int(input())
print(f"Count: {count}")
""",
)

PROBLEMS["12"] = dict(
    file="12_medium.md", diff="🟡 Medium", emoji="🏧", title="ใส่ PIN จนถูกต้อง",
    body='PIN ที่ถูกต้องคือ `"1234"`\nรับ PIN ซ้ำจนถูก แล้วพิมพ์ `PIN OK`',
    starter="pin = input()\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="0000\n1111\n1234", sample_out="PIN OK",
    inp="PIN ทีละบรรทัด", out="PIN OK เมื่อถูกต้อง",
    hint="while pin != \"1234\" แล้วรับใหม่",
    answer='pin = input()\nwhile pin != "1234":\n    pin = input()\nprint("PIN OK")\n',
)

PROBLEMS["13"] = dict(
    file="13_medium.md", diff="🟡 Medium", emoji="🚶", title="ก้าวเดินจนถึงเป้าหมาย",
    body="เป้าหมายอยู่ที่ `target` ก้าว เริ่มจาก `steps = 0`\nแต่ละรอบรับจำนวนก้าวที่เดินเพิ่ม แล้วบวกเข้า `steps`\nพิมพ์ยอดก้าวสะสมทุกครั้งหลังบวก จนกว่า `steps >= target`",
    starter="target = int(input())\nsteps = 0\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="20\n5\n8\n7", sample_out="5\n13\n20",
    inp="บรรทัดแรกเป้าหมาย ตามด้วยก้าวที่เดินแต่ละรอบ", out="ยอดก้าวสะสมทีละบรรทัดจนถึงเป้า",
    hint="while steps < target: รับค่า บวก แล้วพิมพ์",
    answer="""target = int(input())
steps = 0
while steps < target:
    walk = int(input())
    steps = steps + walk
    print(steps)
""",
)

PROBLEMS["05"] = dict(
    file="05_challenge.md", diff="🔴 Challenge", emoji="🏦", title="ถอนเงินจนเหลือไม่พอ",
    body="ยอดเงินในบัญชีเริ่มที่ `balance`\nรับจำนวนเงินที่ถอนทีละครั้ง ถ้ายอดคงเหลือพอให้ถอนได้\nถ้าจำนวนที่ขอถอน **มากกว่า** ยอดคงเหลือ ให้หยุดรับและแสดงยอดคงเหลือสุดท้าย\n\n(ใช้เงื่อนไข while เทียบยอด — ห้าม break)",
    starter="balance = int(input())\nwithdraw = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="1000\n200\n300\n600", sample_out="Remaining: 500",
    inp="บรรทัดแรกยอดเงิน ตามด้วยจำนวนถอนทีละบรรทัด",
    out="Remaining: <ยอดคงเหลือเมื่อถอนไม่พอ>",
    hint="while withdraw <= balance: หักยอด แล้วรับจำนวนถอนรอบใหม่ — พิมพ์ Remaining หลังลูป",
    answer="""balance = int(input())
withdraw = int(input())
while withdraw <= balance:
    balance = balance - withdraw
    withdraw = int(input())
print(f"Remaining: {balance}")
""",
)

PROBLEMS["14"] = dict(
    file="14_challenge.md", diff="🔴 Challenge", emoji="📐", title="ค่าเฉลี่ยจนกดศูนย์",
    body="รับจำนวนเต็มซ้ำจนเจอ `0`\nหาผลรวมและจำนวนค่า (ไม่นับ 0) แล้วแสดงค่าเฉลี่ยทศนิยม 1 ตำแหน่งในกรอบ",
    starter="total = 0\ncount = 0\nnumber = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="10\n20\n30\n0",
    sample_out="========================\n      AVERAGE\n========================\nCount   : 3\nTotal   : 60\nAverage : 20.0\n========================",
    inp="จำนวนทีละบรรทัด จบด้วย 0", out="ใบสรุปในกรอบ",
    hint="สะสม total กับ count ในลูป แล้วคำนวณ average หลังจบ",
    answer="""total = 0
count = 0
number = int(input())
while number != 0:
    total = total + number
    count = count + 1
    number = int(input())
average = total / count
print("========================")
print("      AVERAGE")
print("========================")
print(f"Count   : {count}")
print(f"Total   : {total}")
print(f"Average : {average:.1f}")
print("========================")
""",
)

PROBLEMS["15"] = dict(
    file="15_challenge.md", diff="🔴 Challenge", emoji="🔋", title="จำลองแบตหมด",
    body="แบตเริ่มที่เปอร์เซ็นต์ที่รับเข้ามา\nทุกชั่วโมงแบตลดลง 15\nพิมพ์ระดับแบตแต่ละชั่วโมงจนกว่าจะ `<= 0` แล้วพิมพ์ `Dead`",
    starter="battery = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="40", sample_out="40\n25\n10\n-5\nDead",
    inp="ระดับแบตเริ่มต้น 1 บรรทัด", out="ระดับแบตแต่ละรอบ แล้ว Dead",
    hint="พิมพ์ค่าปัจจุบันก่อน แล้วค่อยลบ 15 — รวมรอบที่ติดลบด้วยตามตัวอย่าง",
    answer="""battery = int(input())
while battery > 0:
    print(battery)
    battery = battery - 15
print(battery)
print("Dead")
""",
)

PROBLEMS["16"] = dict(
    file="16_challenge.md", diff="🔴 Challenge", emoji="🎮", title="สะสมแต้มเกมจนถึงเป้า",
    body="เป้าหมายแต้มคือ `goal`\nแต่ละรอบรับแต้มที่ได้บวกสะสม\nพิมพ์ยอดสะสมทุกครั้ง และเมื่อถึงหรือเกินเป้าให้พิมพ์ `Level Up!` ท้ายสุด",
    starter="goal = int(input())\npoints = 0\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="50\n20\n15\n20", sample_out="20\n35\n55\nLevel Up!",
    inp="บรรทัดแรกเป้า ตามด้วยแต้มแต่ละรอบ", out="ยอดสะสมทีละบรรทัด แล้ว Level Up!",
    hint="while points < goal: รับแต้ม บวก พิมพ์ — หลังลูปพิมพ์ Level Up!",
    answer="""goal = int(input())
points = 0
while points < goal:
    gain = int(input())
    points = points + gain
    print(points)
print("Level Up!")
""",
)

INDEX = """# 📋 สารบัญโจทย์ — บท 019 while

**ขอบเขตของบทนี้:** ความรู้บท 001–018 + **`while condition:`** + อัปเดตตัวนับในลูป

> ❌ ห้ามใช้ `break` / `continue` (บท 020)
> ❌ ห้ามใช้ `while True` เป็นเทคนิค — ให้ออกจากลูปด้วยเงื่อนไข while เท่านั้น

---

## ลำดับที่แนะนำ

| # | ไฟล์ | ระดับ | โจทย์ | แกนการคิด |
|---|------|-------|-------|-----------|
| 1 | `02_test.md` | 🟢 | นับลงจอด 1 ถึง 4 | while นับขึ้น + ข้อความท้าย |
| 2 | `03_test.md` | 🟢 | พิมพ์เลขคู่ด้วย while | เพิ่มทีละ 2 |
| 3 | `04_test.md` | 🟢 | รหัสผ่านจนถูก | while ตาม input |
| 4 | `08_easy.md` | 🟢 | นับถอยหลังเริ่มงาน | นับลงจาก input |
| 5 | `09_easy.md` | 🟢 | ตรวจอายุจนครบ 18 | while ตามเงื่อนไขตัวเลข |
| 6 | `06_medium.md` | 🟡 | รวมเลขจนเจอ -1 | sentinel รวมค่า |
| 7 | `07_medium.md` | 🟡 | ทายเลขลับ 10 | ทายซ้ำจนกว่าจะถูก |
| 8 | `10_medium.md` | 🟡 | เงินฝากทบต้นเท่าตัว | คูณค่าในลูป |
| 9 | `11_medium.md` | 🟡 | นับคะแนนจนเจอศูนย์ | sentinel นับจำนวน |
| 10 | `12_medium.md` | 🟡 | ใส่ PIN จนถูกต้อง | เทียบข้อความ |
| 11 | `13_medium.md` | 🟡 | ก้าวเดินจนถึงเป้าหมาย | สะสมจนถึงเป้า |
| 12 | `05_challenge.md` | 🔴 | ถอนเงินจนเหลือไม่พอ | เงื่อนไขเทียบก่อนหัก |
| 13 | `14_challenge.md` | 🔴 | ค่าเฉลี่ยจนกดศูนย์ | นับ+รวม+เฉลี่ยในกรอบ |
| 14 | `15_challenge.md` | 🔴 | จำลองแบตหมด | ลดค่าจนไม่ผ่านเงื่อนไข |
| 15 | `16_challenge.md` | 🔴 | สะสมแต้มเกมจนถึงเป้า | สะสม + ข้อความปิดท้าย |

**สรุป:** 🟢 Easy 5 ข้อ · 🟡 Medium 6 ข้อ · 🔴 Challenge 4 ข้อ = **15 ข้อ**

---

## หมายเหตุสำหรับครู

- ข้อ `02` **ไม่ซ้ำ** ตัวอย่างในบทเรียน (บทเรียนนับ 1–5 และ countdown จาก 5)
- เลขลับ/รหัสผ่านในโจทย์ตั้งคนละค่าจากบทเรียน (`42`, countdown blast off)
- เน้นให้นักเรียนอัปเดตตัวแปรในลูปทุกครั้ง ไม่งั้นจะ infinite loop
"""

CHAPTER = "while-loop"
SLUGS = {
    "02": "02_ready_count", "03": "03_even_while", "04": "04_password_ok",
    "05": "05_atm_withdraw", "06": "06_sum_until_neg1", "07": "07_guess_ten",
    "08": "08_countdown_start", "09": "09_adult_age", "10": "10_double_money",
    "11": "11_count_scores", "12": "12_pin_ok", "13": "13_walk_steps",
    "14": "14_average_until_zero", "15": "15_battery_drain", "16": "16_level_up",
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
    print("019 done")

if __name__ == "__main__":
    emit()
