# -*- coding: utf-8 -*-
"""Generate gold-standard practice for 023-debugging-loops."""
import os, shutil

BASE = os.path.join(os.path.dirname(__file__), "..", "..", "slide", "023-debugging-loops")
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

def problem(num, file, diff, emoji, title, body, starter, sample_in, sample_out, inp, out, hint, answer):
    return dict(file=file, diff=diff, emoji=emoji, title=title, body=body,
                starter=starter, sample_in=sample_in, sample_out=sample_out,
                inp=inp, out=out, hint=hint, answer=answer)

PROBLEMS = {}

PROBLEMS["02"] = problem(
    "02", "02_test.md", "🟢 Easy", "1️⃣", "แก้ off-by-one ให้ครบ 1–10",
    """โค้ดด้านล่างตั้งใจพิมพ์เลข 1 ถึง 10 แต่พิมพ์แค่ 1 ถึง 9

```python
for i in range(1, 10):
    print(i)
```

เขียนโปรแกรมที่ถูกต้องให้พิมพ์ 1 ถึง 10""",
    "# เขียนโค้ดที่ถูกต้องตรงนี้\n",
    "", "1\n2\n3\n4\n5\n6\n7\n8\n9\n10",
    "ไม่มี", "เลข 1 ถึง 10",
    None,
    "for i in range(1, 11):\n    print(i)\n",
)

PROBLEMS["03"] = problem(
    "03", "03_test.md", "🟢 Easy", "♾️", "แก้ while วนไม่จบ",
    """โค้ดนี้วนไม่จบเพราะลืมอัปเดตตัวนับ

```python
count = 1
while count <= 5:
    print(count)
```

เขียนเวอร์ชันที่พิมพ์ 1 ถึง 5 แล้วจบอย่างถูกต้อง""",
    "# เขียนโค้ดที่ถูกต้องตรงนี้\n",
    "", "1\n2\n3\n4\n5",
    "ไม่มี", "เลข 1 ถึง 5",
    None,
    "count = 1\nwhile count <= 5:\n    print(count)\n    count = count + 1\n",
)

PROBLEMS["04"] = problem(
    "04", "04_test.md", "🟢 Easy", "📦", "แก้พิมพ์ชื่อ list ผิดตัว",
    """โค้ดนี้พิมพ์ทั้งลิสต์ซ้ำทุกครั้ง แทนที่จะพิมพ์ทีละชื่อ

```python
names = ["Ann", "Ben", "Cara"]
for name in names:
    print(names)
```

เขียนโปรแกรมที่พิมพ์ชื่อทีละบรรทัดให้ถูก""",
    'names = ["Ann", "Ben", "Cara"]\n\n# เขียนโค้ดที่ถูกต้องตรงนี้\n',
    "", "Ann\nBen\nCara",
    "ไม่มี", "ชื่อทีละบรรทัด",
    None,
    'names = ["Ann", "Ben", "Cara"]\nfor name in names:\n    print(name)\n',
)

PROBLEMS["08"] = problem(
    "08", "08_easy.md", "🟢 Easy", "🔧", "แก้ range ให้ได้ 1–4",
    """ต้องการพิมพ์ 1 2 3 4 แต่ใช้ `range(1, 4)` จึงขาด 4

เขียนโปรแกรมที่พิมพ์ 1 ถึง 4 ให้ครบ""",
    "# เขียนโค้ดที่ถูกต้องตรงนี้\n",
    "", "1\n2\n3\n4",
    "ไม่มี", "เลข 1 ถึง 4",
    None,
    "for i in range(1, 5):\n    print(i)\n",
)

PROBLEMS["09"] = problem(
    "09", "09_easy.md", "🟢 Easy", "📉", "แก้ countdown ให้ถึง 1",
    """โค้ดนับถอยหลังจาก 3 แต่เงื่อนไขผิดจึงไม่พิมพ์อะไร

```python
count = 3
while count < 1:
    print(count)
    count = count - 1
```

เขียน countdown จาก 3 ถึง 1 ให้ถูก""",
    "# เขียนโค้ดที่ถูกต้องตรงนี้\n",
    "", "3\n2\n1",
    "ไม่มี", "3 ถึง 1",
    None,
    "count = 3\nwhile count >= 1:\n    print(count)\n    count = count - 1\n",
)

PROBLEMS["06"] = problem(
    "06", "06_medium.md", "🟡 Medium", "📌", "แก้ indent ให้ผลรวมถูก",
    """โค้ดนี้เยื้องผิด ทำให้พิมพ์ total ทุกครั้งในลูป และค่าสุดท้ายอาจงง

ต้องการ: รวมเลขในลิสต์ แล้วพิมพ์ผลรวม **ครั้งเดียว** ท้ายสุด เป็น `Total: 60`

```python
nums = [10, 20, 30]
total = 0
for n in nums:
    total = total + n
    print(f"Total: {total}")
```

เขียนเวอร์ชันที่ถูกต้อง""",
    "nums = [10, 20, 30]\n\n# เขียนโค้ดที่ถูกต้องตรงนี้\n",
    "", "Total: 60",
    "ไม่มี", "Total: 60 บรรทัดเดียว",
    "ย้ายคำสั่งพิมพ์ให้อยู่นอก for — เยื้องให้ตรงกับ for ไม่ใช่ข้างใน",
    "nums = [10, 20, 30]\ntotal = 0\nfor n in nums:\n    total = total + n\nprint(f\"Total: {total}\")\n",
)

PROBLEMS["07"] = problem(
    "07", "07_medium.md", "🟡 Medium", "⏭️", "แก้ continue ให้ข้ามศูนย์",
    """ต้องการพิมพ์เฉพาะค่าในลิสต์ที่ **ไม่ใช่ 0** แต่โค้ดเดิม break ผิด

```python
nums = [3, 0, 5, 0, 2]
for n in nums:
    if n == 0:
        break
    print(n)
```

เขียนใหม่ให้ข้ามเลข 0 ด้วย continue แล้วพิมพ์ค่าที่เหลือ""",
    "nums = [3, 0, 5, 0, 2]\n\n# เขียนโค้ดที่ถูกต้องตรงนี้\n",
    "", "3\n5\n2",
    "ไม่มี", "ค่าที่ไม่ใช่ 0",
    "ใช้ continue เมื่อเจอ 0 แทน break เพื่อไม่ให้หยุดทั้งลูป",
    "nums = [3, 0, 5, 0, 2]\nfor n in nums:\n    if n == 0:\n        continue\n    print(n)\n",
)

PROBLEMS["10"] = problem(
    "10", "10_medium.md", "🟡 Medium", "🔢", "แก้ off-by-one ของผลรวม 1..n",
    """รับ `n` ต้องการผลรวม 1 ถึง n แต่โค้ดเดิมใช้ `range(n)` จึงรวม 0..(n-1) ผิด

เขียนโปรแกรมรับ n แล้วพิมพ์ `Sum: <ผลรวมที่ถูก>`""",
    "n = int(input())\n\n# เขียนโค้ดที่ถูกต้องตรงนี้\n",
    "5", "Sum: 15",
    "จำนวนเต็ม n 1 บรรทัด", "Sum: <ผลรวม>",
    "range สำหรับรวม 1 ถึง n ต้องเริ่มที่ 1 และจบที่ n",
    "n = int(input())\ntotal = 0\nfor i in range(1, n + 1):\n    total = total + i\nprint(f\"Sum: {total}\")\n",
)

PROBLEMS["11"] = problem(
    "11", "11_medium.md", "🟡 Medium", "🔐", "แก้รหัสผ่านที่ลืมรับค่าใหม่",
    """โค้ดตรวจรหัส `"go"` แต่ลืมรับ input ใหม่ในลูป จึงอาจวนค้าง

เขียนโปรแกรมรับรหัสซ้ำจนกว่าจะได้ `go` แล้วพิมพ์ `OK`
(ใช้ while ตามเงื่อนไขได้ หรือ while True + break ก็ได้)""",
    "# เขียนโค้ดที่ถูกต้องตรงนี้\n",
    "no\nwait\ngo", "OK",
    "รหัสทีละบรรทัดจนถูก", "OK",
    "ในลูปต้องมีบรรทัดรับค่าใหม่ทุกครั้งหลังตรวจว่ายังไม่ถูก",
    'password = input()\nwhile password != "go":\n    password = input()\nprint("OK")\n',
)

PROBLEMS["12"] = problem(
    "12", "12_medium.md", "🟡 Medium", "🧱", "แก้สี่เหลี่ยมดาวให้ขึ้นบรรทัดใหม่",
    """โค้ดพิมพ์ดาว 3×3 แต่ลืม `print()` เปล่าหลังจบแถว จึงติดกันเป็นบรรทัดเดียว

เขียนโปรแกรมพิมพ์

```text
***
***
***
```""",
    "# เขียนโค้ดที่ถูกต้องตรงนี้\n",
    "", "***\n***\n***",
    "ไม่มี", "สี่เหลี่ยมดาว 3×3",
    "หลังลูปในแต่ละแถว ต้องมี print() เพื่อขึ้นบรรทัดใหม่",
    'for row in range(3):\n    for col in range(3):\n        print("*", end="")\n    print()\n',
)

PROBLEMS["13"] = problem(
    "13", "13_medium.md", "🟡 Medium", "📊", "แก้นับคนผ่านที่นับผิด",
    """ต้องการนับคะแนน `>= 50` แต่เงื่อนไขเขียนกลับเป็น `< 50`

ลิสต์: `[40, 55, 60, 30]` ต้องได้ `Passed: 2`

เขียนโปรแกรมที่นับถูกต้อง""",
    "scores = [40, 55, 60, 30]\n\n# เขียนโค้ดที่ถูกต้องตรงนี้\n",
    "", "Passed: 2",
    "ไม่มี", "Passed: 2",
    "ตรวจเงื่อนไขเครื่องหมายเปรียบเทียบให้ตรงกับคำว่าผ่าน",
    "scores = [40, 55, 60, 30]\npassed = 0\nfor score in scores:\n    if score >= 50:\n        passed = passed + 1\nprint(f\"Passed: {passed}\")\n",
)

PROBLEMS["05"] = problem(
    "05", "05_challenge.md", "🔴 Challenge", "🐛", "แก้บั๊กสามจุดในรายงานผลรวม",
    """โปรแกรมด้านล่างมีบั๊กอย่างน้อย 3 จุด
ต้องการรับตัวเลขจนเจอ `0` แล้วแสดงจำนวนค่าและผลรวม

```python
count = 0
total = 0
number = int(input())
while number != 0
    total = total + number
    count = count + 1
print(f"Count: {count}, Total: {total}")
```

ปัญหาที่ต้องแก้ เช่น ขาดเครื่องหมาย `:` และลืมรับค่าใหม่ในลูป

เขียนโปรแกรมที่ทำงานถูกต้องตามตัวอย่าง""",
    "# เขียนโค้ดที่ถูกต้องตรงนี้\n",
    "5\n10\n0", "Count: 2, Total: 15",
    "จำนวนทีละบรรทัด จบด้วย 0", "Count และ Total",
    "เช็กเครื่องหมายหลัง while และอย่าลืมรับค่าใหม่ท้ายลูป",
    "count = 0\ntotal = 0\nnumber = int(input())\nwhile number != 0:\n    total = total + number\n    count = count + 1\n    number = int(input())\nprint(f\"Count: {count}, Total: {total}\")\n",
)

PROBLEMS["14"] = problem(
    "14", "14_challenge.md", "🔴 Challenge", "🌡️", "แก้รายงานอุณหภูมิที่บั๊ก",
    """ต้องการนับวันร้อน (`>= 30`) จากลิสต์ แต่โค้ดเดิมใช้ผิดตัวแปรและเงื่อนไข

ลิสต์: `[28, 31, 30, 25]` ต้องได้ `Hot Days: 2`

เขียนโปรแกรมที่ถูกต้อง""",
    "temps = [28, 31, 30, 25]\n\n# เขียนโค้ดที่ถูกต้องตรงนี้\n",
    "", "Hot Days: 2",
    "ไม่มี", "Hot Days: 2",
    "วนด้วยตัวแปรลูปทีละค่า แล้วเทียบกับ 30",
    "temps = [28, 31, 30, 25]\nhot = 0\nfor temp in temps:\n    if temp >= 30:\n        hot = hot + 1\nprint(f\"Hot Days: {hot}\")\n",
)

PROBLEMS["15"] = problem(
    "15", "15_challenge.md", "🔴 Challenge", "🔁", "แก้ตารางพิกัดที่ลูปซ้อนผิด",
    """ต้องการพิมพ์พิกัดสำหรับ `n = 2` เป็น

```text
1 1
1 2
2 1
2 2
```

แต่โค้ดเดิมลูปในใช้ `range(n)` เริ่ม 0 และพิมพ์ผิดรูปแบบ

รับ `n` แล้วพิมพ์พิกัด 1..n ให้ถูก""",
    "n = int(input())\n\n# เขียนโค้ดที่ถูกต้องตรงนี้\n",
    "2", "1 1\n1 2\n2 1\n2 2",
    "จำนวนเต็ม n 1 บรรทัด", "พิกัด 1..n",
    "ทั้งสองลูปควรเริ่มที่ 1 ถึง n",
    "n = int(input())\nfor r in range(1, n + 1):\n    for c in range(1, n + 1):\n        print(r, c)\n",
)

PROBLEMS["16"] = problem(
    "16", "16_challenge.md", "🔴 Challenge", "🎮", "แก้เกมสะสมแต้มที่เงื่อนไขกลับ",
    """ต้องการสะสมแต้มจน `>= goal` แต่เงื่อนไข while เขียนกลับทำให้ไม่เข้าลูป

รับ goal แล้วรับแต้มทีละรอบ บวกสะสม พิมพ์ยอดหลังบวกทุกครั้ง
เมื่อจบพิมพ์ `Done`

ตัวอย่าง goal = 10 แล้วได้แต้ม 4 และ 7""",
    "goal = int(input())\npoints = 0\n\n# เขียนโค้ดที่ถูกต้องตรงนี้\n",
    "10\n4\n7", "4\n11\nDone",
    "บรรทัดแรกเป้า ตามด้วยแต้มแต่ละรอบ", "ยอดสะสมแล้ว Done",
    "เงื่อนไขควรทำงานขณะที่ยังน้อยกว่าเป้า และต้องรับแต้มภายในลูป",
    'goal = int(input())\npoints = 0\nwhile points < goal:\n    gain = int(input())\n    points = points + gain\n    print(points)\nprint("Done")\n',
)

INDEX = """# 📋 สารบัญโจทย์ — บท 023 debugging loops

**ขอบเขตของบทนี้:** ไม่มี syntax ใหม่ — ฝึกหาและแก้บั๊ก loop จากบท 017–022

ประเภทบั๊กหลัก: off-by-one · infinite while · indent ผิด · ใช้ชื่อ list แทนตัวแปรลูป

---

## ลำดับที่แนะนำ

| # | ไฟล์ | ระดับ | โจทย์ | แกนการคิด |
|---|------|-------|-------|-----------|
| 1 | `02_test.md` | 🟢 | แก้ off-by-one ให้ครบ 1–10 | range stop |
| 2 | `03_test.md` | 🟢 | แก้ while วนไม่จบ | ลืมอัปเดตตัวนับ |
| 3 | `04_test.md` | 🟢 | แก้พิมพ์ชื่อ list ผิดตัว | ใช้ตัวแปรลูป |
| 4 | `08_easy.md` | 🟢 | แก้ range ให้ได้ 1–4 | off-by-one สั้น |
| 5 | `09_easy.md` | 🟢 | แก้ countdown ให้ถึง 1 | เงื่อนไข while กลับ |
| 6 | `06_medium.md` | 🟡 | แก้ indent ให้ผลรวมถูก | พิมพ์นอก loop |
| 7 | `07_medium.md` | 🟡 | แก้ continue ให้ข้ามศูนย์ | break vs continue |
| 8 | `10_medium.md` | 🟡 | แก้ off-by-one ของผลรวม 1..n | range กับ accumulator |
| 9 | `11_medium.md` | 🟡 | แก้รหัสผ่านที่ลืมรับค่าใหม่ | อัปเดต input ในลูป |
| 10 | `12_medium.md` | 🟡 | แก้สี่เหลี่ยมดาวให้ขึ้นบรรทัดใหม่ | ลืม print() เปล่า |
| 11 | `13_medium.md` | 🟡 | แก้นับคนผ่านที่นับผิด | เงื่อนไขเปรียบเทียบกลับ |
| 12 | `05_challenge.md` | 🔴 | แก้บั๊กสามจุดในรายงานผลรวม | หลายบั๊กในโปรแกรมเดียว |
| 13 | `14_challenge.md` | 🔴 | แก้รายงานอุณหภูมิที่บั๊ก | นับตามเงื่อนไข |
| 14 | `15_challenge.md` | 🔴 | แก้ตารางพิกัดที่ลูปซ้อนผิด | nested range |
| 15 | `16_challenge.md` | 🔴 | แก้เกมสะสมแต้มที่เงื่อนไขกลับ | while สะสมจนถึงเป้า |

**สรุป:** 🟢 Easy 5 ข้อ · 🟡 Medium 6 ข้อ · 🔴 Challenge 4 ข้อ = **15 ข้อ**
"""

CHAPTER = "debugging-loops"
SLUGS = {
    "02": "02_fix_offbyone_ten", "03": "03_fix_infinite", "04": "04_fix_loop_var",
    "05": "05_fix_sum_report", "06": "06_fix_indent_total", "07": "07_fix_continue_zero",
    "08": "08_fix_range_four", "09": "09_fix_countdown", "10": "10_fix_sum_range",
    "11": "11_fix_password", "12": "12_fix_star_grid", "13": "13_fix_pass_count",
    "14": "14_fix_hot_days", "15": "15_fix_coords", "16": "16_fix_points",
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
    print("023 done")

if __name__ == "__main__":
    emit()
