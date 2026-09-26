# -*- coding: utf-8 -*-
"""Expand 022-024 loop review / debug / midyear."""
from _expand_helpers import write_week

def p(n, title, slug, body, out_desc, sample_out, starter, answer, hint=None, sample_in=None):
    return dict(
        n=n, title=title, slug=slug, body=body,
        input_desc="ดูตัวอย่าง" if sample_in is not None else "ไม่มี",
        output_desc=out_desc, sample_input=sample_in, sample_output=sample_out,
        hint=hint, starter=starter, answer=answer,
    )


def week_022():
    index = """
# 📋 สารบัญโจทย์ — บท 022 Loop Review

**ขอบเขต:** for / while / list loop / break / continue / nested — ไม่มี `.append()` / `sum()`

---

## ลำดับที่แนะนำ

| # | ไฟล์ | ระดับ | โจทย์ | แกนการคิด |
|---|------|-------|-------|-----------|
| 1 | `02_test.md` | 🟢 | นับด้วย for | range |
| 2 | `03_test.md` | 🟢 | นับด้วย while | while |
| 3 | `04_test.md` | 🟢 | วนลิสต์ | for-in-list |
| 4 | `08_easy.md` | 🟢 | หยุดที่ 2 | break |
| 5 | `09_easy.md` | 🟢 | ข้ามค่ากลาง | continue |
| 6 | `06_medium.md` | 🟡 | รวม range | accumulator |
| 7 | `07_medium.md` | 🟡 | รวมลิสต์ | for list |
| 8 | `10_medium.md` | 🟡 | while จน 0 | while True+break |
| 9 | `11_medium.md` | 🟡 | นับคู่ในลิสต์ | % ในลูป |
| 10 | `12_medium.md` | 🟡 | กริดเล็ก | nested |
| 11 | `13_medium.md` | 🟡 | เฉลี่ยลิสต์ | total/len |
| 12 | `05_challenge.md` | 🔴 | กรองแล้วรวม | continue+sum pattern |
| 13 | `14_challenge.md` | 🔴 | สามเหลี่ยมตาม n | nested+input |
| 14 | `15_challenge.md` | 🔴 | นับจนกว่าจะเจอ | while |
| 15 | `16_challenge.md` | 🔴 | สรุปหลายทักษะ | ผสม |

**สรุป:** 15 ข้อ
"""
    probs = [
        p(2, "นับด้วย for", "for_count", "พิมพ์ 0 1 2 ด้วย for-range", "3 บรรทัด", "0\n1\n2",
          "# for", "for i in range(3):\n    print(i)"),
        p(3, "นับด้วย while", "while_count", "พิมพ์ 1 และ 2 ด้วย while", "2 บรรทัด", "1\n2",
          "i = 1\n# while", "i = 1\nwhile i <= 2:\n    print(i)\n    i = i + 1"),
        p(4, "วนลิสต์", "list_walk", "วน [5, 6] แสดงทีละค่า", "2 บรรทัด", "5\n6",
          "nums = [5, 6]\n# วน", "nums = [5, 6]\nfor n in nums:\n    print(n)"),
        p(8, "หยุดที่ 2", "break_at_two", "วน range(5) พิมพ์แล้วหยุดหลังพิมพ์ 2", "3 บรรทัด", "0\n1\n2",
          "# break", "for i in range(5):\n    print(i)\n    if i == 2:\n        break"),
        p(9, "ข้ามค่ากลาง", "skip_one", "วน range(4) ข้ามเมื่อ i==1", "3 บรรทัด", "0\n2\n3",
          "# continue", "for i in range(4):\n    if i == 1:\n        continue\n    print(i)"),
        p(6, "รวม range", "sum_range", "รวม 1+2+3 ด้วย for แสดงผลรวม", "1 บรรทัด", "6",
          "total = 0\n# รวม", "total = 0\nfor i in range(1, 4):\n    total = total + i\nprint(total)", "สะสมใน total"),
        p(7, "รวมลิสต์", "sum_list", "รวม [10, 20, 30]", "1 บรรทัด", "60",
          "nums = [10, 20, 30]\ntotal = 0\n# รวม", "nums = [10, 20, 30]\ntotal = 0\nfor n in nums:\n    total = total + n\nprint(total)", "อย่าใช้ sum()"),
        p(10, "while จน 0", "until_zero", "รับจำนวนซ้ำ รวมค่าที่ไม่ใช่ 0 เมื่อเจอ 0 หยุดแล้วแสดงผลรวม",
          "1 บรรทัด", "9", "total = 0\n# อ่านจนเจอ 0",
          "total = 0\nwhile True:\n    n = int(input())\n    if n == 0:\n        break\n    total = total + n\nprint(total)",
          sample_in="4\n5\n0", hint="while True + break"),
        p(11, "นับคู่ในลิสต์", "count_evens", "นับเลขคู่ใน [1,2,3,4] แสดงจำนวน", "1 บรรทัด", "2",
          "nums = [1, 2, 3, 4]\ncount = 0\n# นับคู่",
          "nums = [1, 2, 3, 4]\ncount = 0\nfor n in nums:\n    if n % 2 == 0:\n        count = count + 1\nprint(count)", "ใช้ %"),
        p(12, "กริดเล็ก", "tiny_grid", "พิมพ์ ## สองแถวด้วยลูปซ้อน", "2 บรรทัด", "##\n##",
          "# กริด", 'for i in range(2):\n    for j in range(2):\n        print("#", end="")\n    print()'),
        p(13, "เฉลี่ยลิสต์", "list_avg", "ลิสต์ [10, 20] แสดงค่าเฉลี่ยทศนิยม 1 ตำแหน่ง", "1 บรรทัด", "15.0",
          "nums = [10, 20]\ntotal = 0\n# เฉลี่ย",
          'nums = [10, 20]\ntotal = 0\nfor n in nums:\n    total = total + n\nprint(f"{total / len(nums):.1f}")', "total / len"),
        p(5, "กรองแล้วรวม", "filter_sum", "จาก [3, 10, 7, 12] รวมเฉพาะค่า > 8", "1 บรรทัด", "22",
          "nums = [3, 10, 7, 12]\ntotal = 0\n# กรองรวม",
          "nums = [3, 10, 7, 12]\ntotal = 0\nfor n in nums:\n    if n <= 8:\n        continue\n    total = total + n\nprint(total)", "continue เมื่อไม่เข้าเกณฑ์"),
        p(14, "สามเหลี่ยมตาม n", "tri_n", "รับ n พิมพ์ดาวเป็นสามเหลี่ยมสูง n", "สามเหลี่ยม", "*\n**\n***",
          "n = int(input())\n# วาด",
          'n = int(input())\nfor row in range(1, n + 1):\n    for c in range(row):\n        print("*", end="")\n    print()',
          sample_in="3", hint="ลูปในตามหมายเลขแถว"),
        p(15, "นับจนกว่าจะเจอ", "count_until", "รับตัวเลขเป้าหมาย แล้ววน for range(1, 20) พิมพ์ค่าจนเจอเป้าแล้ว break (พิมพ์เป้าด้วย)",
          "หลายบรรทัด", "1\n2\n3\n4\n5",
          "target = int(input())\n# หา",
          "target = int(input())\nfor i in range(1, 20):\n    print(i)\n    if i == target:\n        break",
          sample_in="5"),
        p(16, "สรุปหลายทักษะ", "mixed_review",
          "รับ n พิมพ์เลข 1..n ที่ไม่ใช่พหุคูณของ 3",
          "หลายบรรทัด", "1\n2\n4\n5",
          "n = int(input())\n# กรอง",
          "n = int(input())\nfor i in range(1, n + 1):\n    if i % 3 == 0:\n        continue\n    print(i)",
          sample_in="5", hint="continue เมื่อหาร 3 ลงตัว"),
    ]
    write_week("022-loop-review", chapter="Loop Review", emoji="🔁", index_md=index, problems=probs)


def week_023():
    index = """
# 📋 สารบัญโจทย์ — บท 023 Debugging Loops

**ขอบเขต:** แก้บั๊กลูปด้วย range/while/indent ที่ถูกต้อง — ไม่มี min/max/append ใหม่

---

## ลำดับที่แนะนำ

| # | ไฟล์ | ระดับ | โจทย์ | แกนการคิด |
|---|------|-------|-------|-----------|
| 1 | `02_test.md` | 🟢 | range ให้ครบ 1..3 | off-by-one |
| 2 | `03_test.md` | 🟢 | อัปเดต while | กัน infinite |
| 3 | `04_test.md` | 🟢 | เยื้องใน for | indent |
| 4 | `08_easy.md` | 🟢 | พิมพ์สมาชิก | ตัวแปรวน |
| 5 | `09_easy.md` | 🟢 | debug(4) | 0..3 |
| 6 | `06_medium.md` | 🟡 | debug(1,n+1) | inclusive |
| 7 | `07_medium.md` | 🟡 | debug i= | debug print |
| 8 | `10_medium.md` | 🟡 | while i<3 | เงื่อนไข |
| 9 | `11_medium.md` | 🟡 | while True+break | ทางออก |
| 10 | `12_medium.md` | 🟡 | ข้ามศูนย์ | continue |
| 11 | `13_medium.md` | 🟡 | รวมไม่พลาด | accumulator |
| 12 | `05_challenge.md` | 🔴 | แก้รายงานคะแนน | หลายจุด |
| 13 | `14_challenge.md` | 🔴 | นับคู่ถูก | % |
| 14 | `15_challenge.md` | 🔴 | ลิสต์ไม่พิมพ์ทั้งก้อน | loop var |
| 15 | `16_challenge.md` | 🔴 | countdown ถูก | while |

**สรุป:** 15 ข้อ
"""
    probs = [
        p(2, "range ให้ครบ 1..3", "fix_range_13", "พิมพ์ 1 ถึง 3 ด้วย range ที่ถูกต้อง", "3 บรรทัด", "1\n2\n3",
          "# range", "for i in range(1, 4):\n    print(i)"),
        p(3, "อัปเดต while", "fix_while_update", "พิมพ์ Hi สองครั้งด้วย while ที่มีตัวนับ", "2 บรรทัด", "Hi\nHi",
          "i = 0\n# while", 'i = 0\nwhile i < 2:\n    print("Hi")\n    i = i + 1'),
        p(4, "เยื้องใน for", "fix_indent", "ใช้ for พิมพ์ 0 1 2 โดยเยื้องถูก", "3 บรรทัด", "0\n1\n2",
          "# for", "for i in range(3):\n    print(i)"),
        p(8, "พิมพ์สมาชิก", "print_items", 'วน ["A","B"] พิมพ์ทีละตัว', "2 บรรทัด", "A\nB",
          'names = ["A", "B"]\n# วน', 'names = ["A", "B"]\nfor name in names:\n    print(name)'),
        p(9, "range(4)", "range_four", "พิมพ์ 0 ถึง 3", "4 บรรทัด", "0\n1\n2\n3",
          "# range", "for i in range(4):\n    print(i)"),
        p(6, "range(1,n+1)", "range_to_n", "รับ n พิมพ์ 1..n", "3 บรรทัด", "1\n2\n3",
          "n = int(input())\n# พิมพ์", "n = int(input())\nfor i in range(1, n + 1):\n    print(i)",
          sample_in="3", hint="range(1, n+1)"),
        p(7, "debug i=", "debug_print", "วน range(2) แสดง i=0 และ i=1", "2 บรรทัด", "i=0\ni=1",
          "# debug", 'for i in range(2):\n    print(f"i={i}")', "f-string ช่วยไล่บั๊ก"),
        p(10, "while i<3", "while_lt3", "พิมพ์ 0 1 2 ด้วย while i < 3", "3 บรรทัด", "0\n1\n2",
          "i = 0\n# while", "i = 0\nwhile i < 3:\n    print(i)\n    i = i + 1"),
        p(11, "while True+break", "while_break_end", "พิมพ์ End แล้ว break", "1 บรรทัด", "End",
          "# while True", 'while True:\n    print("End")\n    break'),
        p(12, "ข้ามศูนย์", "skip_zero", "วน range(3) ข้าม 0 เหลือ 1 2", "2 บรรทัด", "1\n2",
          "# continue", "for i in range(3):\n    if i == 0:\n        continue\n    print(i)"),
        p(13, "รวมไม่พลาด", "sum_careful", "รวม range(1,5) ให้ได้ 10", "1 บรรทัด", "10",
          "total = 0\n# รวม", "total = 0\nfor i in range(1, 5):\n    total = total + i\nprint(total)", "อย่าเขียน total = i"),
        p(5, "แก้รายงานคะแนน", "fix_score_report", "ลิสต์ [80, 70, 90] แสดงแต่ละคะแนนและผลรวมท้าย",
          "4 บรรทัด", "80\n70\n90\nTotal: 240",
          "scores = [80, 70, 90]\ntotal = 0\n# รายงาน",
          'scores = [80, 70, 90]\ntotal = 0\nfor s in scores:\n    print(s)\n    total = total + s\nprint(f"Total: {total}")',
          "สะสมทุกค่าในลูป"),
        p(14, "นับคู่ถูก", "count_evens_fix", "นับคู่ใน [2, 3, 4, 5, 6]", "1 บรรทัด", "3",
          "nums = [2, 3, 4, 5, 6]\ncount = 0\n# นับ",
          "nums = [2, 3, 4, 5, 6]\ncount = 0\nfor n in nums:\n    if n % 2 == 0:\n        count = count + 1\nprint(count)"),
        p(15, "ลิสต์ไม่พิมพ์ทั้งก้อน", "print_each_name", 'วน ["Ann","Ben"] พิมพ์ทีละชื่อ', "2 บรรทัด", "Ann\nBen",
          'names = ["Ann", "Ben"]\n# ระวังอย่า print(names)',
          'names = ["Ann", "Ben"]\nfor name in names:\n    print(name)', "พิมพ์ตัวแปรวน"),
        p(16, "countdown ถูก", "countdown_fix", "นับถอยหลัง 3 2 1 แล้ว Blast off!", "4 บรรทัด", "3\n2\n1\nBlast off!",
          "c = 3\n# countdown",
          'c = 3\nwhile c > 0:\n    print(c)\n    c = c - 1\nprint("Blast off!")', "อัปเดต c ทุกครั้ง"),
    ]
    write_week("023-debugging-loops", chapter="Debugging Loops", emoji="🐛", index_md=index, problems=probs)


def week_024():
    index = """
# 📋 สารบัญโจทย์ — บท 024 Midyear Review

**ขอบเขต:** ความรู้ถึงลูป/เงื่อนไข — ห้าม `.append()` / `sum()` / สร้างลิสต์จาก input

---

## ลำดับที่แนะนำ

| # | ไฟล์ | ระดับ | โจทย์ | แกนการคิด |
|---|------|-------|-------|-----------|
| 1 | `02_test.md` | 🟢 | ทักทาย | input |
| 2 | `03_test.md` | 🟢 | ผ่านเกณฑ์ | if |
| 3 | `04_test.md` | 🟢 | คู่คี่ | % |
| 4 | `08_easy.md` | 🟢 | เกรด elif | elif |
| 5 | `09_easy.md` | 🟢 | นับ 1..n | for |
| 6 | `06_medium.md` | 🟡 | รวมลิสต์ | for list |
| 7 | `07_medium.md` | 🟡 | while นับ | while |
| 8 | `10_medium.md` | 🟡 | and เงื่อนไข | logical |
| 9 | `11_medium.md` | 🟡 | break | safety |
| 10 | `12_medium.md` | 🟡 | เฉลี่ย | len |
| 11 | `13_medium.md` | 🟡 | ซ้อนเล็ก | nested |
| 12 | `05_challenge.md` | 🔴 | รายงานคะแนน | หลายขั้น |
| 13 | `14_challenge.md` | 🔴 | กรองลิสต์ | continue |
| 14 | `15_challenge.md` | 🔴 | เมนู while | while True |
| 15 | `16_challenge.md` | 🔴 | สรุป midyear | ผสม |

**สรุป:** 15 ข้อ
"""
    probs = [
        p(2, "ทักทาย", "my_hello", "รับชื่อ แสดง Hello, ชื่อ", "1 บรรทัด", "Hello, Lee",
          "name = input()\n# ทัก", 'name = input()\nprint(f"Hello, {name}")', sample_in="Lee"),
        p(3, "ผ่านเกณฑ์", "pass_fail", "รับคะแนน >=50 Pass ไม่เช่นนั้น Fail", "1 บรรทัด", "Pass",
          "score = int(input())\n# ตัดสิน",
          'score = int(input())\nif score >= 50:\n    print("Pass")\nelse:\n    print("Fail")', sample_in="50"),
        p(4, "คู่คี่", "even_odd_rev", "รับจำนวน แสดง Even/Odd", "1 บรรทัด", "Odd",
          "n = int(input())\n# คู่คี่",
          'n = int(input())\nif n % 2 == 0:\n    print("Even")\nelse:\n    print("Odd")', sample_in="3"),
        p(8, "เกรด elif", "grade_elif", ">=80 A, >=60 B, else C", "1 บรรทัด", "B",
          "s = int(input())\n# เกรด",
          's = int(input())\nif s >= 80:\n    print("A")\nelif s >= 60:\n    print("B")\nelse:\n    print("C")', sample_in="75"),
        p(9, "นับ 1..n", "count_n", "รับ n พิมพ์ 1..n", "3 บรรทัด", "1\n2\n3",
          "n = int(input())\n# นับ", "n = int(input())\nfor i in range(1, n + 1):\n    print(i)", sample_in="3"),
        p(6, "รวมลิสต์", "sum_fixed", "รวม [2,2,2]", "1 บรรทัด", "6",
          "nums = [2, 2, 2]\nt = 0\n# รวม", "nums = [2, 2, 2]\nt = 0\nfor x in nums:\n    t = t + x\nprint(t)"),
        p(7, "while นับ", "while_123", "พิมพ์ 1 2 3 ด้วย while", "3 บรรทัด", "1\n2\n3",
          "i = 1\n# while", "i = 1\nwhile i <= 3:\n    print(i)\n    i = i + 1"),
        p(10, "and เงื่อนไข", "and_pass", "รับ age และ score ถ้า age>=12 และ score>=50 แสดง Pass นอกนั้น No",
          "1 บรรทัด", "Pass",
          "age = int(input())\nscore = int(input())\n# ตรวจ",
          'age = int(input())\nscore = int(input())\nif age >= 12 and score >= 50:\n    print("Pass")\nelse:\n    print("No")',
          sample_in="15\n80", hint="ใช้ and"),
        p(11, "break", "break_demo", "วน range(10) พิมพ์จนถึง 3 แล้วหยุด", "4 บรรทัด", "0\n1\n2\n3",
          "# break", "for i in range(10):\n    print(i)\n    if i == 3:\n        break"),
        p(12, "เฉลี่ย", "avg_list", "ลิสต์ [10,20,30] แสดงเฉลี่ยทศนิยม 1 ตำแหน่ง", "1 บรรทัด", "20.0",
          "nums = [10, 20, 30]\nt = 0\n# เฉลี่ย",
          'nums = [10, 20, 30]\nt = 0\nfor n in nums:\n    t = t + n\nprint(f"{t / len(nums):.1f}")'),
        p(13, "ซ้อนเล็ก", "nest_hash", "พิมพ์ ## สองแถว", "2 บรรทัด", "##\n##",
          "# nested", 'for i in range(2):\n    for j in range(2):\n        print("#", end="")\n    print()'),
        p(5, "รายงานคะแนน", "score_report", "ลิสต์ [85, 60, 40] สำหรับแต่ละค่า แสดงคะแนนและ Pass/Fail (>=50)",
          "6 บรรทัด", "85\nPass\n60\nPass\n40\nFail",
          "scores = [85, 60, 40]\n# รายงาน",
          'scores = [85, 60, 40]\nfor s in scores:\n    print(s)\n    if s >= 50:\n        print("Pass")\n    else:\n        print("Fail")',
          "ลูป + if"),
        p(14, "กรองลิสต์", "filter_big", "จาก [5, 15, 8, 20] พิมพ์เฉพาะ >10", "2 บรรทัด", "15\n20",
          "nums = [5, 15, 8, 20]\n# กรอง",
          "nums = [5, 15, 8, 20]\nfor n in nums:\n    if n <= 10:\n        continue\n    print(n)"),
        p(15, "เมนู while", "menu_quit", 'รับคำสั่งซ้ำ พิมพ์ You typed: ... จนเจอ quit แล้ว Goodbye!',
          "หลายบรรทัด", "You typed: hi\nYou typed: go\nGoodbye!",
          "# เมนู",
          'while True:\n    word = input()\n    if word == "quit":\n        print("Goodbye!")\n        break\n    print(f"You typed: {word}")',
          sample_in="hi\ngo\nquit"),
        p(16, "สรุป midyear", "midyear_mix",
          "รับ n พิมพ์เลขคู่ตั้งแต่ 2 ถึง n inclusive",
          "หลายบรรทัด", "2\n4\n6",
          "n = int(input())\n# เลขคู่",
          "n = int(input())\nfor i in range(2, n + 1, 2):\n    print(i)",
          sample_in="6", hint="range step 2"),
    ]
    write_week("024-midyear-review", chapter="Midyear Review", emoji="📚", index_md=index, problems=probs)


if __name__ == "__main__":
    week_022()
    week_023()
    week_024()
    print("done 022-024")
