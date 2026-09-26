# -*- coding: utf-8 -*-
"""Generate gold-standard practice for 017-for-loop. Keeps 01_for_loop.md and 02_range.md."""
import os, shutil

BASE = os.path.join(os.path.dirname(__file__), "..", "..", "slide", "017-for-loop")
ANS = os.path.join(BASE, "answer")

def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text.lstrip("\n") if text.startswith("\n") else text)
        if not text.endswith("\n"):
            f.write("\n")

# Wipe old practice (keep lessons)
for name in os.listdir(BASE):
    if name.endswith(".md") and name not in ("01_for_loop.md", "02_range.md"):
        os.remove(os.path.join(BASE, name))
if os.path.isdir(ANS):
    shutil.rmtree(ANS)
os.makedirs(ANS, exist_ok=True)

PROBLEMS = {}

# ── 02 Easy: stamp Welcome 5 times ─────────────────────────────────
PROBLEMS["02"] = dict(
    file="02_test.md", diff="🟢 Easy", emoji="🎫", title="แสตมป์ Welcome 5 ครั้ง",
    body="""
ห้องสมุดติดแสตมป์ข้อความ `Welcome` บนบัตรเข้าชม ทุกครั้งที่นักท่องเที่ยวเข้ามา
วันนี้มีคิว 5 คน — แสตมป์ซ้ำข้อความเดิม 5 บรรทัด

เขียนโปรแกรมพิมพ์ `Welcome` ทีละบรรทัด รวม 5 ครั้ง
""",
    cond=None,
    inp="ไม่มี (ไม่ต้องรับค่า)",
    out="ข้อความ Welcome 5 บรรทัด",
    sample_in="",
    sample_out="Welcome\nWelcome\nWelcome\nWelcome\nWelcome",
    hint=None,
    starter="# เขียนโค้ดตรงนี้\n",
    answer='for i in range(5):\n    print("Welcome")\n',
)

# ── 03 Easy: print 1..8 ────────────────────────────────────────────
PROBLEMS["03"] = dict(
    file="03_test.md", diff="🟢 Easy", emoji="🔢", title="นับเลขที่นั่ง 1 ถึง 8",
    body="""
โรงหนังมีที่นั่งแถวหน้า 8 ที่ หมายเลข 1 ถึง 8
พนักงานอยากให้โปรแกรมพิมพ์หมายเลขที่นั่งทีละบรรทัด

เขียนโปรแกรมพิมพ์เลข `1` ถึง `8` ทีละบรรทัด
""",
    cond=None,
    inp="ไม่มี",
    out="เลข 1 ถึง 8 ทีละบรรทัด",
    sample_in="",
    sample_out="1\n2\n3\n4\n5\n6\n7\n8",
    hint=None,
    starter="# เขียนโค้ดตรงนี้\n",
    answer="for i in range(1, 9):\n    print(i)\n",
)

# ── 04 Easy: odds with step ────────────────────────────────────────
PROBLEMS["04"] = dict(
    file="04_test.md", diff="🟢 Easy", emoji="🏀", title="หมายเลขผู้เล่นคี่",
    body="""
ทีมบาสมีผู้เล่นหมายเลขคี่เท่านั้น: 1, 3, 5, 7, 9
โค้ชอยากให้พิมพ์รายชื่อหมายเลขบนกระดาน

เขียนโปรแกรมพิมพ์เลขคี่ `1 3 5 7 9` ทีละบรรทัด โดยใช้ `range` ที่มี step
""",
    cond=None,
    inp="ไม่มี",
    out="เลขคี่ 5 ค่า ทีละบรรทัด",
    sample_in="",
    sample_out="1\n3\n5\n7\n9",
    hint=None,
    starter="# เขียนโค้ดตรงนี้\n",
    answer="for i in range(1, 10, 2):\n    print(i)\n",
)

# ── 08 Easy: Day labels ────────────────────────────────────────────
PROBLEMS["08"] = dict(
    file="08_easy.md", diff="🟢 Easy", emoji="📅", title="ป้ายวันฝึกซ้อม 7 วัน",
    body="""
ค่ายกีฬาพิมพ์ป้าย `Day 1` ถึง `Day 7` ติดหน้าห้องฝึก
แต่ละป้ายอยู่คนละบรรทัด

เขียนโปรแกรมพิมพ์ป้ายวันทั้ง 7 วัน
""",
    cond=None,
    inp="ไม่มี",
    out="Day 1 ถึง Day 7 ทีละบรรทัด",
    sample_in="",
    sample_out="Day 1\nDay 2\nDay 3\nDay 4\nDay 5\nDay 6\nDay 7",
    hint=None,
    starter="# เขียนโค้ดตรงนี้\n",
    answer='for i in range(1, 8):\n    print(f"Day {i}")\n',
)

# ── 09 Easy: Beep n times ──────────────────────────────────────────
PROBLEMS["09"] = dict(
    file="09_easy.md", diff="🟢 Easy", emoji="🔔", title="เสียง Beep ตามจำนวนครั้ง",
    body="""
เครื่องแจ้งเตือนดังเสียง `Beep` ตามจำนวนครั้งที่ตั้งไว้
รับจำนวนครั้งแล้วพิมพ์ `Beep` ทีละบรรทัดตามนั้น

เขียนโปรแกรมรับจำนวนเต็ม `n` แล้วพิมพ์ `Beep` จำนวน `n` ครั้ง
""",
    cond=None,
    inp="จำนวนเต็ม n 1 บรรทัด",
    out="ข้อความ Beep n บรรทัด",
    sample_in="4",
    sample_out="Beep\nBeep\nBeep\nBeep",
    hint=None,
    starter="n = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    answer='n = int(input())\nfor i in range(n):\n    print("Beep")\n',
)

# ── 06 Medium: sum 1..n ────────────────────────────────────────────
PROBLEMS["06"] = dict(
    file="06_medium.md", diff="🟡 Medium", emoji="➕", title="รวมแต้มสะสม 1 ถึง n",
    body="""
เกมสะสมแต้มให้คะแนนตามรอบ: รอบที่ 1 ได้ 1 แต้ม รอบที่ 2 ได้ 2 แต้ม …
จนถึงรอบที่ n ได้ n แต้ม

เขียนโปรแกรมรับ `n` แล้วหาผลรวมแต้มทั้งหมด (1+2+…+n)
""",
    cond=None,
    inp="จำนวนเต็ม n 1 บรรทัด",
    out="บรรทัดเดียว แสดงผลรวมในรูปแบบ Total: <ค่า>",
    sample_in="5",
    sample_out="Total: 15",
    hint="สร้างตัวแปร total = 0 ก่อนเข้า loop แล้วบวกค่า i เข้าไปทีละรอบ",
    starter="n = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    answer='n = int(input())\ntotal = 0\nfor i in range(1, n + 1):\n    total = total + i\nprint(f"Total: {total}")\n',
)

# ── 07 Medium: table of 7 ──────────────────────────────────────────
PROBLEMS["07"] = dict(
    file="07_medium.md", diff="🟡 Medium", emoji="7️⃣", title="สูตรคูณแม่ 7",
    body="""
ครูคณิตอยากให้เด็กท่องสูตรคูณแม่ 7 จาก 7×1 ถึง 7×10
แต่ละบรรทัดเป็นรูปแบบ `7 x k = ผล`

เขียนโปรแกรมพิมพ์สูตรคูณแม่ 7 ทั้ง 10 บรรทัด (ไม่ต้องรับ input)
""",
    cond=None,
    inp="ไม่มี",
    out="สูตรคูณ 10 บรรทัด",
    sample_in="",
    sample_out="7 x 1 = 7\n7 x 2 = 14\n7 x 3 = 21\n7 x 4 = 28\n7 x 5 = 35\n7 x 6 = 42\n7 x 7 = 49\n7 x 8 = 56\n7 x 9 = 63\n7 x 10 = 70",
    hint="ใช้ range(1, 11) แล้วพิมพ์บรรทัดละหนึ่งสูตร",
    starter="# เขียนโค้ดตรงนี้\n",
    answer='for k in range(1, 11):\n    print(f"7 x {k} = {7 * k}")\n',
)

# ── 10 Medium: count divisible by 4 ────────────────────────────────
PROBLEMS["10"] = dict(
    file="10_medium.md", diff="🟡 Medium", emoji="📦", title="นับกล่องที่หาร 4 ลงตัว",
    body="""
โกดังติดป้ายหมายเลขกล่อง 1 ถึง n
กล่องที่หมายเลขหารด้วย 4 ลงตัวจะถูกส่งไปแผนกพิเศษ

เขียนโปรแกรมรับ `n` แล้วนับว่ามีกล่องพิเศษกี่ใบ ในช่วง 1 ถึง n
""",
    cond="- ถ้าหมายเลข `i` หารด้วย 4 ลงตัว (`i % 4 == 0`) → นับเพิ่ม 1",
    inp="จำนวนเต็ม n 1 บรรทัด",
    out="บรรทัดเดียว Special Boxes: <จำนวน>",
    sample_in="20",
    sample_out="Special Boxes: 5",
    hint="ใช้ตัวแปรนับ count = 0 แล้ววน for ตรวจด้วย if ทีละหมายเลข",
    starter="n = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    answer='n = int(input())\ncount = 0\nfor i in range(1, n + 1):\n    if i % 4 == 0:\n        count = count + 1\nprint(f"Special Boxes: {count}")\n',
)

# ── 11 Medium: squares ─────────────────────────────────────────────
PROBLEMS["11"] = dict(
    file="11_medium.md", diff="🟡 Medium", emoji="🟪", title="พื้นที่สี่เหลี่ยมจัตุรัส",
    body="""
ช่างก่อสร้างอยากรู้พื้นที่สี่เหลี่ยมจัตุรัสที่ด้านยาว 1 ถึง 6 เมตร
(พื้นที่ = ด้าน × ด้าน)

เขียนโปรแกรมพิมพ์พื้นที่ของด้าน 1 ถึง 6 ทีละบรรทัด ในรูปแบบ `Side k -> Area a`
""",
    cond=None,
    inp="ไม่มี",
    out="6 บรรทัด ตามรูปแบบที่กำหนด",
    sample_in="",
    sample_out="Side 1 -> Area 1\nSide 2 -> Area 4\nSide 3 -> Area 9\nSide 4 -> Area 16\nSide 5 -> Area 25\nSide 6 -> Area 36",
    hint="วน for จาก 1 ถึง 6 แล้วพิมพ์ด้านกับด้าน*ด้าน",
    starter="# เขียนโค้ดตรงนี้\n",
    answer='for k in range(1, 7):\n    print(f"Side {k} -> Area {k * k}")\n',
)

# ── 12 Medium: print from a to b ───────────────────────────────────
PROBLEMS["12"] = dict(
    file="12_medium.md", diff="🟡 Medium", emoji="🚪", title="หมายเลขห้องระหว่างสองชั้น",
    body="""
อาคารมีหมายเลขห้องต่อเนื่อง รับเลขห้องเริ่มต้นและเลขห้องสุดท้าย (ไม่รวมห้องสุดท้าย)
แล้วพิมพ์หมายเลขห้องในช่วงนั้นทีละบรรทัด

เช่น เริ่ม 3 สิ้นสุด 7 → พิมพ์ 3 4 5 6 (ไม่พิมพ์ 7)
""",
    cond=None,
    inp="2 บรรทัด — เลขเริ่ม และเลขสิ้นสุด (stop แบบ range คือไม่รวม)",
    out="หมายเลขห้องทีละบรรทัด",
    sample_in="3\n7",
    sample_out="3\n4\n5\n6",
    hint="ใช้ range(start, stop) โดย stop คือค่าที่รับมาบรรทัดที่สอง",
    starter="start = int(input())\nstop = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    answer="start = int(input())\nstop = int(input())\nfor i in range(start, stop):\n    print(i)\n",
)

# ── 13 Medium: sum of evens ────────────────────────────────────────
PROBLEMS["13"] = dict(
    file="13_medium.md", diff="🟡 Medium", emoji="💰", title="รวมเงินโบนัสเลขคู่",
    body="""
บริษัทจ่ายโบนัสเฉพาะรอบเลขคู่: รอบ 2 ได้ 2 บาท รอบ 4 ได้ 4 บาท …
จนถึงรอบ n (สมมติ n เป็นเลขคู่เสมอในชุดทดสอบ)

เขียนโปรแกรมรับ `n` แล้วหาผลรวมของเลขคู่ตั้งแต่ 2 ถึง n
""",
    cond=None,
    inp="จำนวนเต็ม n (เลขคู่) 1 บรรทัด",
    out="บรรทัดเดียว Bonus: <ผลรวม>",
    sample_in="10",
    sample_out="Bonus: 30",
    hint="ใช้ range(2, n + 1, 2) แล้วสะสมผลรวม",
    starter="n = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    answer='n = int(input())\ntotal = 0\nfor i in range(2, n + 1, 2):\n    total = total + i\nprint(f"Bonus: {total}")\n',
)

# ── 05 Challenge: factors ──────────────────────────────────────────
PROBLEMS["05"] = dict(
    file="05_challenge.md", diff="🔴 Challenge", emoji="🧩", title="หาตัวประกอบของ n",
    body="""
ครูคณิตให้นักเรียนหาตัวประกอบของจำนวนเต็ม n
ตัวประกอบคือเลข i ที่อยู่ระหว่าง 1 ถึง n และ n หารด้วย i ลงตัว

เขียนโปรแกรมรับ `n` แล้วพิมพ์ตัวประกอบทั้งหมดทีละบรรทัด จากน้อยไปมาก
""",
    cond="- ถ้า `n % i == 0` → พิมพ์ i",
    inp="จำนวนเต็ม n 1 บรรทัด",
    out="ตัวประกอบทีละบรรทัด",
    sample_in="12",
    sample_out="1\n2\n3\n4\n6\n12",
    hint="วน i จาก 1 ถึง n แล้วใช้ if ตรวจว่าหารลงตัวหรือไม่ก่อนพิมพ์",
    starter="n = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    answer="n = int(input())\nfor i in range(1, n + 1):\n    if n % i == 0:\n        print(i)\n",
)

# ── 14 Challenge: odds count+sum ───────────────────────────────────
PROBLEMS["14"] = dict(
    file="14_challenge.md", diff="🔴 Challenge", emoji="📊", title="สรุปเลขคี่ในช่วง 1 ถึง n",
    body="""
แผนกสถิติอยากได้รายงานเลขคี่ในช่วง 1 ถึง n
ต้องนับว่ามีเลขคี่กี่ตัว และผลรวมของเลขคี่เหล่านั้นเท่าไร

เขียนโปรแกรมรับ `n` แล้วออกใบสรุปในกรอบ
""",
    cond=None,
    inp="จำนวนเต็ม n 1 บรรทัด",
    out="ใบสรุปในกรอบ แสดง Count และ Sum",
    sample_in="10",
    sample_out="========================\n      ODD REPORT\n========================\nCount : 5\nSum   : 25\n========================",
    hint="ใช้ตัวแปรสองตัว (count กับ total) ใน loop เดียว ตรวจด้วย if i % 2 != 0",
    starter="n = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    answer="""n = int(input())
count = 0
total = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        count = count + 1
        total = total + i
print("========================")
print("      ODD REPORT")
print("========================")
print(f"Count : {count}")
print(f"Sum   : {total}")
print("========================")
""",
)

# ── 15 Challenge: attendance stamps ────────────────────────────────
PROBLEMS["15"] = dict(
    file="15_challenge.md", diff="🔴 Challenge", emoji="✅", title="แสตมป์เข้าเรียน n วัน",
    body="""
ครูประจำชั้นแสตมป์คำว่า `Present` ให้ทุกวันที่มีเรียน
รับจำนวนวัน `n` แล้วพิมพ์รายงานการเข้าเรียนในกรอบ
แสดงบรรทัด `Day k : Present` สำหรับทุกวัน 1 ถึง n
""",
    cond=None,
    inp="จำนวนเต็ม n 1 บรรทัด",
    out="กรอบรายงาน ตามตัวอย่าง",
    sample_in="3",
    sample_out="========================\n     ATTENDANCE\n========================\nDay 1 : Present\nDay 2 : Present\nDay 3 : Present\n========================",
    hint="พิมพ์หัวกรอบก่อน แล้วค่อยวน for พิมพ์แต่ละวัน สุดท้ายปิดกรอบ",
    starter="n = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    answer="""n = int(input())
print("========================")
print("     ATTENDANCE")
print("========================")
for i in range(1, n + 1):
    print(f"Day {i} : Present")
print("========================")
""",
)

# ── 16 Challenge: hot days ─────────────────────────────────────────
PROBLEMS["16"] = dict(
    file="16_challenge.md", diff="🔴 Challenge", emoji="🌡️", title="นับวันที่อากาศร้อน",
    body="""
สถานีอากาศบันทึกอุณหภูมิรายวันเป็นจำนวนเต็ม
วันที่อุณหภูมิ `>= 30` นับเป็นวันร้อน

รับจำนวนวัน `n` แล้วรับอุณหภูมิตามมาอีก n บรรทัด
นับว่ามีวันร้อนกี่วัน แล้วแสดงผล
""",
    cond="- อุณหภูมิ `>= 30` → นับเป็นวันร้อน",
    inp="บรรทัดแรกคือ n ตามด้วยอุณหภูมิ n บรรทัด",
    out="บรรทัดเดียว Hot Days: <จำนวน>",
    sample_in="5\n28\n31\n30\n25\n35",
    sample_out="Hot Days: 3",
    hint="วน for ตามจำนวนวัน ในแต่ละรอบรับอุณหภูมิใหม่ด้วย int(input()) แล้วค่อยตัดสินใจนับ",
    starter="n = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    answer="""n = int(input())
hot = 0
for i in range(n):
    temp = int(input())
    if temp >= 30:
        hot = hot + 1
print(f"Hot Days: {hot}")
""",
)

INDEX = """# 📋 สารบัญโจทย์ — บท 017 for + range

**ขอบเขตของบทนี้:** ความรู้บท 001–016 + **`for i in range(...)`**
(ใช้ได้ทั้ง `range(n)` / `range(a, b)` / `range(a, b, c)`) + `if` ภายใน loop ได้

> ❌ ยังไม่มี list / `for item in list` (บท 018) · ไม่มี `while` (บท 019)
> ❌ ไม่มี `break` / `continue` (บท 020) · ไม่มี nested loop / รูปสามเหลี่ยมดาว (บท 021)
> ❌ ไม่มี `range` นับถอยหลัง (step ติดลบ) ทั้งหลักสูตร

---

## ลำดับที่แนะนำ

| # | ไฟล์ | ระดับ | โจทย์ | แกนการคิด |
|---|------|-------|-------|-----------|
| 1 | `02_test.md` | 🟢 | แสตมป์ Welcome 5 ครั้ง | `range(n)` พิมพ์ซ้ำข้อความ |
| 2 | `03_test.md` | 🟢 | นับเลขที่นั่ง 1 ถึง 8 | `range(start, stop)` |
| 3 | `04_test.md` | 🟢 | หมายเลขผู้เล่นคี่ | `range` แบบมี step |
| 4 | `08_easy.md` | 🟢 | ป้ายวันฝึกซ้อม 7 วัน | ใช้ค่า i ใน f-string |
| 5 | `09_easy.md` | 🟢 | เสียง Beep ตามจำนวนครั้ง | รับ n แล้ววน `range(n)` |
| 6 | `06_medium.md` | 🟡 | รวมแต้มสะสม 1 ถึง n | accumulator รวมเลข |
| 7 | `07_medium.md` | 🟡 | สูตรคูณแม่ 7 | พิมพ์ตารางจาก loop |
| 8 | `10_medium.md` | 🟡 | นับกล่องที่หาร 4 ลงตัว | `if` ภายใน `for` + นับ |
| 9 | `11_medium.md` | 🟡 | พื้นที่สี่เหลี่ยมจัตุรัส | คำนวณใน loop |
| 10 | `12_medium.md` | 🟡 | หมายเลขห้องระหว่างสองชั้น | `range` จาก input 2 ค่า |
| 11 | `13_medium.md` | 🟡 | รวมเงินโบนัสเลขคู่ | `range` + step + สะสม |
| 12 | `05_challenge.md` | 🔴 | หาตัวประกอบของ n | `if` กรองค่าใน loop |
| 13 | `14_challenge.md` | 🔴 | สรุปเลขคี่ในช่วง 1 ถึง n | นับ + รวม ในกรอบ |
| 14 | `15_challenge.md` | 🔴 | แสตมป์เข้าเรียน n วัน | loop + จัดรูปแบบกรอบ |
| 15 | `16_challenge.md` | 🔴 | นับวันที่อากาศร้อน | loop รับ input หลายรอบ |

**สรุป:** 🟢 Easy 5 ข้อ · 🟡 Medium 6 ข้อ · 🔴 Challenge 4 ข้อ = **15 ข้อ**

---

## หมายเหตุสำหรับครู

- ข้อ `02` **ไม่ซ้ำ** ตัวอย่างในบทเรียน (บทเรียนใช้ `Hello` และพิมพ์ค่า `i` จาก `range(5)`)
- เก็บไฟล์บทเรียน `01_for_loop.md` และ `02_range.md` ไว้ตามเดิม (เครื่องตรวจข้าม `*_range*`)
- ห้ามให้นักเรียนทำรูปสามเหลี่ยมดาว — เก็บไว้บท 021
- เฉลยทุกข้ออยู่ใน `answer/` และผ่านการรันเทียบกับตัวอย่างในโจทย์แล้ว
"""

CHAPTER = "for-loop"

def emit():
    write(os.path.join(BASE, "00_index.md"), INDEX)
    for num, p in PROBLEMS.items():
        title_line = f"# {p['emoji']} {CHAPTER} — ข้อ {int(num)}: {p['title']}"
        parts = [title_line, "", f"**Difficulty:** {p['diff']}", "", "---", "", "## โจทย์", "", p["body"].strip(), ""]
        if p.get("cond"):
            parts += ["**เงื่อนไข:**", "", p["cond"], ""]
        parts += ["---", "", "## Input", "", p["inp"], "", "## Output", "", p["out"], "", "---", "", "## ตัวอย่าง", ""]
        if p["sample_in"] == "":
            parts += ["**Input:**", "", "```text", "", "```", ""]
        else:
            parts += ["**Input:**", "", "```text", p["sample_in"], "```", ""]
        parts += ["**Output:**", "", "```text", p["sample_out"], "```", "", "---", ""]
        if p.get("hint"):
            parts += ["## 💡 Hint", "", p["hint"], "", "---", ""]
        parts += ["## Starter Code", "", "```python", p["starter"].rstrip("\n"), "```", ""]
        write(os.path.join(BASE, p["file"]), "\n".join(parts))
        # answer filenames
        slug = {
            "02": "02_welcome_stamp",
            "03": "03_seat_numbers",
            "04": "04_odd_players",
            "05": "05_factors",
            "06": "06_sum_points",
            "07": "07_times_seven",
            "08": "08_day_labels",
            "09": "09_beep_n",
            "10": "10_special_boxes",
            "11": "11_square_areas",
            "12": "12_room_range",
            "13": "13_even_bonus",
            "14": "14_odd_report",
            "15": "15_attendance",
            "16": "16_hot_days",
        }[num]
        write(os.path.join(ANS, slug + ".py"), p["answer"])
    print("017 done:", len(PROBLEMS), "problems")

if __name__ == "__main__":
    emit()
