# -*- coding: utf-8 -*-
"""Generate gold-standard practice for 021-nested-loops. Avoid lesson triangle/mult table."""
import os, shutil

BASE = os.path.join(os.path.dirname(__file__), "..", "..", "slide", "021-nested-loops")
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
    file="02_test.md", diff="🟢 Easy", emoji="🧱", title="กำแพงอิฐ 2×5",
    body="สร้างกำแพงจำลองด้วยตัวอักษร `#`\nมี 2 แถว แถวละ 5 ก้อน\nใช้ nested loop และ `end=\"\"` แล้วขึ้นบรรทัดใหม่ด้วย `print()` เปล่า",
    starter="# เขียนโค้ดตรงนี้\n",
    sample_in="", sample_out="#####\n#####",
    inp="ไม่มี", out="กำแพง 2 แถว",
    hint=None,
    answer="""for row in range(2):
    for col in range(5):
        print("#", end="")
    print()
""",
)

PROBLEMS["03"] = dict(
    file="03_test.md", diff="🟢 Easy", emoji="🪑", title="ผังที่นั่งแถวสั้น",
    body="พิมพ์พิกัดที่นั่ง `(r,c)` สำหรับแถว `0..1` และที่นั่ง `0..2`\nแต่ละพิกัดคนละบรรทัด คั่นด้วยช่องว่างในรูปแบบ `r c`",
    starter="# เขียนโค้ดตรงนี้\n",
    sample_in="", sample_out="0 0\n0 1\n0 2\n1 0\n1 1\n1 2",
    inp="ไม่มี", out="พิกัด 6 บรรทัด",
    hint=None,
    answer="""for r in range(2):
    for c in range(3):
        print(r, c)
""",
)

PROBLEMS["04"] = dict(
    file="04_test.md", diff="🟢 Easy", emoji="🅰", title="แถวตัวอักษร AB",
    body="พิมพ์ 3 แถว แต่ละแถวเป็นตัวอักษร `ABAB` (สลับ A/B จำนวน 4 ช่อง)\nใช้ nested loop — ถ้าคอลัมน์เป็นคู่พิมพ์ A ถ้าคี่พิมพ์ B",
    starter="# เขียนโค้ดตรงนี้\n",
    sample_in="", sample_out="ABAB\nABAB\nABAB",
    inp="ไม่มี", out="3 แถวของ ABAB",
    hint=None,
    answer="""for row in range(3):
    for col in range(4):
        if col % 2 == 0:
            print("A", end="")
        else:
            print("B", end="")
    print()
""",
)

PROBLEMS["08"] = dict(
    file="08_easy.md", diff="🟢 Easy", emoji="⭕", title="แผ่นป้ายตัวโอ 3×3",
    body="พิมพ์ตารางตัวอักษร `O` ขนาด 3×3",
    starter="# เขียนโค้ดตรงนี้\n",
    sample_in="", sample_out="OOO\nOOO\nOOO",
    inp="ไม่มี", out="ตาราง O 3×3",
    hint=None,
    answer="""for row in range(3):
    for col in range(3):
        print("O", end="")
    print()
""",
)

PROBLEMS["09"] = dict(
    file="09_easy.md", diff="🟢 Easy", emoji="🎟️", title="ป้ายที่นั่งโรงหนัง",
    body='พิมพ์ป้ายที่นั่ง 2 แถว แถวละ 3 ที่ในรูปแบบ `R{แถว}-S{ที่}`\nแถวและที่เริ่มนับที่ 1\nแต่ละป้ายคนละบรรทัด',
    starter="# เขียนโค้ดตรงนี้\n",
    sample_in="", sample_out="R1-S1\nR1-S2\nR1-S3\nR2-S1\nR2-S2\nR2-S3",
    inp="ไม่มี", out="ป้ายที่นั่ง 6 บรรทัด",
    hint=None,
    answer="""for r in range(1, 3):
    for s in range(1, 4):
        print(f"R{r}-S{s}")
""",
)

PROBLEMS["06"] = dict(
    file="06_medium.md", diff="🟡 Medium", emoji="🪟", title="หน้าต่างขนาดตามสั่ง",
    body="รับจำนวนแถว `rows` และจำนวนคอลัมน์ `cols`\nพิมพ์สี่เหลี่ยมของตัวอักษร `=` ตามขนาดที่รับ",
    starter="rows = int(input())\ncols = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="3\n4", sample_out="====\n====\n====",
    inp="2 บรรทัด — rows และ cols", out="สี่เหลี่ยมของ =",
    hint="ลูปนอกตามแถว ลูปในตามคอลัมน์ พิมพ์ด้วย end แล้วค่อยขึ้นบรรทัดใหม่",
    answer="""rows = int(input())
cols = int(input())
for r in range(rows):
    for c in range(cols):
        print("=", end="")
    print()
""",
)

PROBLEMS["07"] = dict(
    file="07_medium.md", diff="🟡 Medium", emoji="🗺️", title="พิกัดแผนที่ขนาด n",
    body="รับ `n` แล้วพิมพ์พิกัด `r c` สำหรับ `r` และ `c` จาก 1 ถึง n\nแต่ละคู่คนละบรรทัด",
    starter="n = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="2", sample_out="1 1\n1 2\n2 1\n2 2",
    inp="จำนวนเต็ม n 1 บรรทัด", out="พิกัดทั้งหมดทีละบรรทัด",
    hint="ใช้ range(1, n + 1) ทั้งสองชั้น",
    answer="""n = int(input())
for r in range(1, n + 1):
    for c in range(1, n + 1):
        print(r, c)
""",
)

PROBLEMS["10"] = dict(
    file="10_medium.md", diff="🟡 Medium", emoji="♟️", title="กระดานสลับ XO",
    body="พิมพ์กระดาน 4×4 สลับ `X` และ `O`\nช่องที่แถว+คอลัมน์เป็นเลขคู่เป็น X นอกนั้นเป็น O\n(แถว/คอลัมน์เริ่มที่ 0)",
    starter="# เขียนโค้ดตรงนี้\n",
    sample_in="", sample_out="XOXO\nOXOX\nXOXO\nOXOX",
    inp="ไม่มี", out="กระดาน 4 แถว",
    hint="ถ้า (row + col) % 2 == 0 พิมพ์ X นอกนั้น O",
    answer="""for row in range(4):
    for col in range(4):
        if (row + col) % 2 == 0:
            print("X", end="")
        else:
            print("O", end="")
    print()
""",
)

PROBLEMS["11"] = dict(
    file="11_medium.md", diff="🟡 Medium", emoji="✖️", title="ตารางคูณเฉพาะเลขคู่",
    body="พิมพ์ผลคูณของเลขคู่ `2, 4, 6` คูณกันทุกคู่\nแต่ละบรรทัดเป็น `a x b = ผล` โดย a และ b วิ่งใน `[2, 4, 6]`",
    starter="evens = [2, 4, 6]\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="",
    sample_out="2 x 2 = 4\n2 x 4 = 8\n2 x 6 = 12\n4 x 2 = 8\n4 x 4 = 16\n4 x 6 = 24\n6 x 2 = 12\n6 x 4 = 24\n6 x 6 = 36",
    inp="ไม่มี", out="สูตรคูณ 9 บรรทัด",
    hint="nested for บนลิสต์เดียวกัน — ไม่ใช่ตาราง 1..n แบบบทเรียน",
    answer="""evens = [2, 4, 6]
for a in evens:
    for b in evens:
        print(f"{a} x {b} = {a * b}")
""",
)

PROBLEMS["12"] = dict(
    file="12_medium.md", diff="🟡 Medium", emoji="🖼️", title="กรอบสี่เหลี่ยมกลวง",
    body="พิมพ์กรอบขนาด 4×6 ด้วย `*`\nแถวแรกและแถวสุดท้ายเต็มไปด้วยดาว\nแถวกลางมีดาวเฉพาะหัวท้าย ที่เหลือเป็นช่องว่าง",
    starter="# เขียนโค้ดตรงนี้\n",
    sample_in="", sample_out="******\n*    *\n*    *\n******",
    inp="ไม่มี", out="กรอบ 4 แถว กว้าง 6",
    hint="ตรวจว่าเป็นแถวขอบหรือคอลัมน์ขอบ แล้วค่อยเลือกพิมพ์ * หรือช่องว่าง",
    answer="""for row in range(4):
    for col in range(6):
        if row == 0 or row == 3 or col == 0 or col == 5:
            print("*", end="")
        else:
            print(" ", end="")
    print()
""",
)

PROBLEMS["13"] = dict(
    file="13_medium.md", diff="🟡 Medium", emoji="🔢", title="พีระมิดตัวเลข",
    body="รับ `n` แล้วพิมพ์พีระมิดตัวเลข\nแถวที่ 1 พิมพ์ `1` แถวที่ 2 พิมพ์ `1 2` … แถวที่ n พิมพ์ `1..n`\nตัวเลขในแถวเดียวกันคั่นด้วยช่องว่าง (ไม่มีช่องว่างเกินท้ายแถวก็ได้ตามตัวอย่าง)",
    starter="n = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="4", sample_out="1\n1 2\n1 2 3\n1 2 3 4",
    inp="จำนวนเต็ม n 1 บรรทัด", out="พีระมิดตัวเลข",
    hint="ลูปนอกเป็นแถว ลูปในพิมพ์เลข 1 ถึงหมายเลขแถว — ระวังช่องว่างระหว่างเลข",
    answer="""n = int(input())
for row in range(1, n + 1):
    for col in range(1, row + 1):
        if col == row:
            print(col)
        else:
            print(col, end=" ")
""",
)

PROBLEMS["05"] = dict(
    file="05_challenge.md", diff="🔴 Challenge", emoji="🔻", title="สามเหลี่ยมกลับหัวด้วย #",
    body="รับ `n` แล้วพิมพ์สามเหลี่ยมกลับหัวด้วย `#`\nแถวแรกมี n ตัว แถวถัดไปลดลงทีละ 1 จนเหลือ 1\n\n> ไม่ใช่สามเหลี่ยมดาวแบบบทเรียนที่เพิ่มทีละแถว",
    starter="n = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="4", sample_out="####\n###\n##\n#",
    inp="จำนวนเต็ม n 1 บรรทัด", out="สามเหลี่ยมกลับหัว",
    hint="ลูปนอกนับจำนวนดาวในแถวจาก n ลงไป 1 — ใช้ range ที่ลดขนาดลูปใน",
    answer="""n = int(input())
for row in range(n, 0, -1):
    for col in range(row):
        print("#", end="")
    print()
""",
)

# WAIT - negative step in range! SCOPE says: "Negative step / counting down is NEVER shown (range(10, 0, -1) is out of scope for the whole course)"

# I need to fix problem 05 to not use negative step. Alternative:
# for row in range(n):
#     stars = n - row
#     for col in range(stars):
#         print("#", end="")
#     print()

PROBLEMS["05"]["hint"] = "แถวที่ i (เริ่ม 0) มีดาว n - i ดวง — คำนวณจำนวนก่อนเข้าลูปใน"
PROBLEMS["05"]["answer"] = """n = int(input())
for row in range(n):
    stars = n - row
    for col in range(stars):
        print("#", end="")
    print()
"""

PROBLEMS["14"] = dict(
    file="14_challenge.md", diff="🔴 Challenge", emoji="🏟️", title="ผังสนามพร้อมป้ายแถว",
    body="รับจำนวนแถว `rows` และที่นั่งต่อแถว `seats`\nแต่ละแถวขึ้นต้นด้วย `Row X:` แล้วตามด้วยที่นั่ง `A1 A2 ...` ในแถวเดียวกันคั่นด้วยช่องว่าง\nหมายเลขที่นั่งเริ่มที่ 1",
    starter="rows = int(input())\nseats = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="2\n3",
    sample_out="Row 1: A1 A2 A3\nRow 2: A1 A2 A3",
    inp="2 บรรทัด — rows และ seats", out="ผังที่นั่งตามรูปแบบ",
    hint="พิมพ์ป้ายแถวก่อน แล้ววนที่นั่งด้วย end เว้นวรรค ปิดท้ายแถวด้วย print() เปล่า",
    answer="""rows = int(input())
seats = int(input())
for r in range(1, rows + 1):
    print(f"Row {r}:", end="")
    for s in range(1, seats + 1):
        print(f" A{s}", end="")
    print()
""",
)

PROBLEMS["15"] = dict(
    file="15_challenge.md", diff="🔴 Challenge", emoji="🌟", title="แถบดาวคั่นเลข",
    body="รับ `n` แล้วสำหรับแต่ละแถว `i` จาก 1 ถึง n\nพิมพ์เลข `i` ตามด้วยดาว `*` จำนวน i ดวงติดกัน เช่น แถว 3 เป็น `3***`",
    starter="n = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="4", sample_out="1*\n2**\n3***\n4****",
    inp="จำนวนเต็ม n 1 บรรทัด", out="แถบเลข+ดาว",
    hint="พิมพ์เลขก่อนด้วย end=\"\" แล้วค่อยวนพิมพ์ดาว",
    answer="""n = int(input())
for i in range(1, n + 1):
    print(i, end="")
    for j in range(i):
        print("*", end="")
    print()
""",
)

PROBLEMS["16"] = dict(
    file="16_challenge.md", diff="🔴 Challenge", emoji="📅", title="ตารางคาบเรียนคั่นแท็บ",
    body="รับ `n` แล้วพิมพ์ตารางผลคูณขนาด n×n\nแต่ละช่องเป็นค่า `i * j` โดย i, j เริ่มที่ 1\nคั่นคอลัมน์ด้วยแท็บ (`end=\"\\t\"`) และขึ้นบรรทัดใหม่เมื่อจบแถว\n\n> ต่างจากตัวอย่างบทเรียนที่เป็นตาราง 3×3 คงที่ — ข้อนี้รับขนาดจากผู้ใช้",
    starter="n = int(input())\n\n# เขียนโค้ดตรงนี้\n",
    sample_in="3",
    sample_out="1\t2\t3\t\n2\t4\t6\t\n3\t6\t9\t",
    inp="จำนวนเต็ม n 1 บรรทัด", out="ตารางคูณคั่นด้วยแท็บ",
    hint="nested loop พิมพ์ i*j ด้วย end=\"\\t\" แล้ว print() เปล่าเมื่อจบแถว",
    answer="""n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end="\\t")
    print()
""",
)

# Careful with the answer for 16 - I used "\\t" in the string which will be literal \t in the file... 
# In the answer string I have end="\\t" which when written to file becomes end="\t" - wait:
# In Python source """ ... end="\\t" ... """  - the \\t becomes \t in the actual string content written to file.
# So the .py file will contain: print(i * j, end="\t")
# That's correct!

# But sample_out - when I put actual tabs in the string, the checker compares stdout.
# Let me use real tab characters in sample_out.

PROBLEMS["16"]["sample_out"] = "1\t2\t3\t\n2\t4\t6\t\n3\t6\t9\t"
# Actually print with end="\t" then print() adds newline. So each row ends with tab then newline.
# Output of:
# for i in range(1,4):
#   for j in range(1,4):
#     print(i*j, end="\t")
#   print()
# is: "1\t2\t3\t\n2\t4\t6\t\n3\t6\t9\t\n"
# After rstrip("\n") in checker: "1\t2\t3\t\n2\t4\t6\t\n3\t6\t9\t"
# Good.

INDEX = """# 📋 สารบัญโจทย์ — บท 021 nested loops

**ขอบเขตของบทนี้:** ความรู้บท 001–020 + **nested `for`** + **`end=\"\"`** / **`end=\"\\t\"`** + `print()` เปล่า

> ❌ หลีกเลี่ยงการคัดลอกสามเหลี่ยมดาว / ตารางคูณ 3×3 จากบทเรียนเป๊ะๆ

---

## ลำดับที่แนะนำ

| # | ไฟล์ | ระดับ | โจทย์ | แกนการคิด |
|---|------|-------|-------|-----------|
| 1 | `02_test.md` | 🟢 | กำแพงอิฐ 2×5 | สี่เหลี่ยมคงที่ด้วย end |
| 2 | `03_test.md` | 🟢 | ผังที่นั่งแถวสั้น | พิมพ์คู่พิกัด |
| 3 | `04_test.md` | 🟢 | แถวตัวอักษร AB | if ในลูปใน |
| 4 | `08_easy.md` | 🟢 | แผ่นป้ายตัวโอ 3×3 | สี่เหลี่ยมตัวอักษรอื่น |
| 5 | `09_easy.md` | 🟢 | ป้ายที่นั่งโรงหนัง | f-string ใน nested loop |
| 6 | `06_medium.md` | 🟡 | หน้าต่างขนาดตามสั่ง | รับ rows/cols |
| 7 | `07_medium.md` | 🟡 | พิกัดแผนที่ขนาด n | พิกัด 1..n |
| 8 | `10_medium.md` | 🟡 | กระดานสลับ XO | ลายตารางด้วย % |
| 9 | `11_medium.md` | 🟡 | ตารางคูณเฉพาะเลขคู่ | nested บน list |
| 10 | `12_medium.md` | 🟡 | กรอบสี่เหลี่ยมกลวง | เงื่อนไขขอบ |
| 11 | `13_medium.md` | 🟡 | พีระมิดตัวเลข | แถวควบคุมลูปใน |
| 12 | `05_challenge.md` | 🔴 | สามเหลี่ยมกลับหัวด้วย # | ลดจำนวนต่อแถว |
| 13 | `14_challenge.md` | 🔴 | ผังสนามพร้อมป้ายแถว | ป้ายแถว + ที่นั่ง |
| 14 | `15_challenge.md` | 🔴 | แถบดาวคั่นเลข | ผสมเลขกับดาว |
| 15 | `16_challenge.md` | 🔴 | ตารางคาบเรียนคั่นแท็บ | ตารางคูณขนาด n + \\t |

**สรุป:** 🟢 Easy 5 ข้อ · 🟡 Medium 6 ข้อ · 🔴 Challenge 4 ข้อ = **15 ข้อ**
"""

CHAPTER = "nested-loops"
SLUGS = {
    "02": "02_hash_wall", "03": "03_seat_coords", "04": "04_ab_rows",
    "05": "05_invert_triangle", "06": "06_eq_window", "07": "07_map_coords",
    "08": "08_ooo_grid", "09": "09_cinema_seats", "10": "10_xo_board",
    "11": "11_even_mult", "12": "12_hollow_box", "13": "13_number_pyramid",
    "14": "14_stadium_map", "15": "15_number_stars", "16": "16_tab_table",
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
    print("021 done")

if __name__ == "__main__":
    emit()
