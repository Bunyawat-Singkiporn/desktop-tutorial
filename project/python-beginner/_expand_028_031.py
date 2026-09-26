# -*- coding: utf-8 -*-
"""Expand weeks 028-036."""
from _expand_helpers import write_week

def p(n, title, slug, body, out_desc, sample_out, starter, answer, hint=None, sample_in=None):
    return dict(
        n=n, title=title, slug=slug, body=body,
        input_desc="ดูตัวอย่าง" if sample_in is not None else "ไม่มี",
        output_desc=out_desc, sample_input=sample_in, sample_output=sample_out,
        hint=hint, starter=starter, answer=answer,
    )


def idx(title, scope, bans, names):
    files = [
        ("02_test.md", "🟢"), ("03_test.md", "🟢"), ("04_test.md", "🟢"),
        ("08_easy.md", "🟢"), ("09_easy.md", "🟢"),
        ("06_medium.md", "🟡"), ("07_medium.md", "🟡"), ("10_medium.md", "🟡"),
        ("11_medium.md", "🟡"), ("12_medium.md", "🟡"), ("13_medium.md", "🟡"),
        ("05_challenge.md", "🔴"), ("14_challenge.md", "🔴"),
        ("15_challenge.md", "🔴"), ("16_challenge.md", "🔴"),
    ]
    rows = "\n".join(
        f"| {i} | `{f}` | {lv} | {names[i-1][0]} | {names[i-1][1]} |"
        for i, (f, lv) in enumerate(files, 1)
    )
    return f"""# 📋 สารบัญโจทย์ — {title}

**ขอบเขต:** {scope}

> ❌ {bans}

---

## ลำดับที่แนะนำ

| # | ไฟล์ | ระดับ | โจทย์ | แกนการคิด |
|---|------|-------|-------|-----------|
{rows}

**สรุป:** 15 ข้อ
"""


def week_028():
    names = [("เข้าถึงขอบ", "0/-1"), ("วนสองแบบ", "for และ range len"), ("เมธอดสั้น", "append+sort"),
             ("เฉลี่ย", "total/len"), ("แก้ค่า", "index assign"),
             ("ลบแล้วเรียง", "remove+sort"), ("นับผ่าน", "count"), ("กรอง", "new list"),
             ("รายงานเลขที่", "range len"), ("สต็อก", "หลายขั้น"), ("ทบทวน len", "len"),
             ("คลังรวม", "ผสม"), ("คะแนนจัดอันดับ", "sort reverse"), ("ของใช้", "CRUD เบา"), ("ปิดบทลิสต์", "สรุป")]
    index = idx("บท 028 Review Lists", "ทบทวนลิสต์ทั้งหมดถึง 027", "ไม่เกินเมธอดที่สอน", names)
    probs = [
        p(2, "เข้าถึงขอบ", "edges", 'a = ["x", "y", "z"] แสดงแรกและท้าย', "2 บรรทัด", "x\nz",
          'a = ["x", "y", "z"]\n# ขอบ', 'a = ["x", "y", "z"]\nprint(a[0])\nprint(a[-1])'),
        p(3, "วนสองแบบ", "two_loops", 'colors = ["Red", "Blue"] พิมพ์ด้วย for-in แล้วพิมพ์ index:value',
          "4 บรรทัด", "Red\nBlue\n0:Red\n1:Blue",
          'colors = ["Red", "Blue"]\n# สองแบบ',
          'colors = ["Red", "Blue"]\nfor c in colors:\n    print(c)\nfor i in range(len(colors)):\n    print(f"{i}:{colors[i]}")'),
        p(4, "เมธอดสั้น", "append_sort_r", "n = [3, 1] append 2 แล้ว sort", "1 บรรทัด", "[1, 2, 3]",
          "n = [3, 1]\n# ", "n = [3, 1]\nn.append(2)\nn.sort()\nprint(n)"),
        p(8, "เฉลี่ย", "avg_r", "s = [80, 70, 90] แสดงเฉลี่ยทศนิยม 1 ตำแหน่ง", "1 บรรทัด", "80.0",
          "s = [80, 70, 90]\nt = 0\n# ",
          's = [80, 70, 90]\nt = 0\nfor x in s:\n    t = t + x\nprint(f"{t / len(s):.1f}")'),
        p(9, "แก้ค่า", "assign_r", "d = [1, 9, 3] แก้กลางเป็น 2", "1 บรรทัด", "[1, 2, 3]",
          "d = [1, 9, 3]\n# ", "d = [1, 9, 3]\nd[1] = 2\nprint(d)"),
        p(6, "ลบแล้วเรียง", "rm_sort", 'f = ["c", "a", "b"] ลบ c แล้ว sort', "1 บรรทัด", "['a', 'b']",
          'f = ["c", "a", "b"]\n# ', 'f = ["c", "a", "b"]\nf.remove("c")\nf.sort()\nprint(f)', "ลบก่อนเรียง"),
        p(7, "นับผ่าน", "count_r", "s = [40, 60, 80] นับ >=50", "1 บรรทัด", "2",
          "s = [40, 60, 80]\nc = 0\n# ", "s = [40, 60, 80]\nc = 0\nfor x in s:\n    if x >= 50:\n        c = c + 1\nprint(c)"),
        p(10, "กรอง", "filter_r", "n = [2, 11, 4, 15] เก็บ >10", "1 บรรทัด", "[11, 15]",
          "n = [2, 11, 4, 15]\nb = []\n# ", "n = [2, 11, 4, 15]\nb = []\nfor x in n:\n    if x > 10:\n        b.append(x)\nprint(b)"),
        p(11, "รายงานเลขที่", "num_r", 't = ["A", "B"] พิมพ์ 1 . A', "2 บรรทัด", "1 . A\n2 . B",
          't = ["A", "B"]\n# ', 't = ["A", "B"]\nfor i in range(len(t)):\n    print(i + 1, ".", t[i])'),
        p(12, "สต็อก", "stock_r", "s = [5, 0, 3] append 2 แล้ว remove 0", "1 บรรทัด", "[5, 3, 2]",
          "s = [5, 0, 3]\n# ", "s = [5, 0, 3]\ns.append(2)\ns.remove(0)\nprint(s)"),
        p(13, "ทบทวน len", "len_r", "a = [1, 2, 3, 4] แสดง Len", "1 บรรทัด", "Len: 4",
          "a = [1, 2, 3, 4]\n# ", 'a = [1, 2, 3, 4]\nprint(f"Len: {len(a)}")'),
        p(5, "คลังรวม", "combo_r", "nums = [4, 1, 3] append 2, sort, แสดงแรกและท้าย",
          "3 บรรทัด", "[1, 2, 3, 4]\n1\n4",
          "nums = [4, 1, 3]\n# ", "nums = [4, 1, 3]\nnums.append(2)\nnums.sort()\nprint(nums)\nprint(nums[0])\nprint(nums[-1])", "เรียงก่อนอ่านขอบ"),
        p(14, "คะแนนจัดอันดับ", "rank_r", "s = [70, 95, 80] เรียงมาก→น้อย แล้วพิมพ์", "3 บรรทัด", "95\n80\n70",
          "s = [70, 95, 80]\n# ", "s = [70, 95, 80]\ns.sort(reverse=True)\nfor x in s:\n    print(x)"),
        p(15, "ของใช้", "items_r", 'items = ["pen"] append book, แก้ pen เป็น pencil', "1 บรรทัด", "['pencil', 'book']",
          'items = ["pen"]\n# ', 'items = ["pen"]\nitems.append("book")\nitems[0] = "pencil"\nprint(items)'),
        p(16, "ปิดบทลิสต์", "finale_r", "data = [9, 2, 7] รวมค่าด้วยลูป แสดง Total", "1 บรรทัด", "Total: 18",
          "data = [9, 2, 7]\nt = 0\n# ", 'data = [9, 2, 7]\nt = 0\nfor x in data:\n    t = t + x\nprint(f"Total: {t}")'),
    ]
    write_week("028-review-lists", chapter="Review Lists", emoji="📦", index_md=index, problems=probs)


def week_029():
    names = [("วันแรก", "t[0]"), ("วันท้าย", "t[-1]"), ("ความยาว", "len"),
             ("วนวัน", "for"), ("พิกัด x", "tuple[0]"),
             ("นักเรียน", "หลายฟิลด์"), ("จุดสองค่า", "x y"), ("นับสมาชิก", "len ป้าย"),
             ("วนพิกัด", "for print"), ("ระเบียน", "Name/Age"), ("หัวท้าย", "0/-1"),
             ("โปรไฟล์", "3 ฟิลด์"), ("ตารางวัน", "วน"), ("คงที่", "อ่านอย่างเดียว"), ("สรุปทูเพิล", "ผสม")]
    index = idx("บท 029 Tuples", "tuple () / index / len / for — อ่านอย่างเดียว", "ห้ามแก้ค่าทูเพิล / unpacking", names)
    probs = [
        p(2, "วันแรก", "day0", 'days = ("Mon", "Tue", "Wed") แสดงวันแรก', "1 บรรทัด", "Mon",
          'days = ("Mon", "Tue", "Wed")\n# ', 'days = ("Mon", "Tue", "Wed")\nprint(days[0])'),
        p(3, "วันท้าย", "day_last", 'days = ("Mon", "Tue", "Wed") แสดงท้าย', "1 บรรทัด", "Wed",
          'days = ("Mon", "Tue", "Wed")\n# ', 'days = ("Mon", "Tue", "Wed")\nprint(days[-1])'),
        p(4, "ความยาว", "tup_len", 'days = ("Mon", "Tue", "Wed", "Thu", "Fri") แสดง len', "1 บรรทัด", "5",
          'days = ("Mon", "Tue", "Wed", "Thu", "Fri")\n# ', 'days = ("Mon", "Tue", "Wed", "Thu", "Fri")\nprint(len(days))'),
        p(8, "วนวัน", "for_days", 'days = ("Mon", "Tue") พิมพ์ทีละวัน', "2 บรรทัด", "Mon\nTue",
          'days = ("Mon", "Tue")\n# ', 'days = ("Mon", "Tue")\nfor d in days:\n    print(d)'),
        p(9, "พิกัด x", "point_x", "point = (10, 20) แสดง x", "1 บรรทัด", "10",
          "point = (10, 20)\n# ", "point = (10, 20)\nprint(point[0])"),
        p(6, "นักเรียน", "student_t", 'student = ("Bob", 14, "Grade 8") แสดง Name/Age/Grade',
          "3 บรรทัด", "Name: Bob\nAge: 14\nGrade: Grade 8",
          'student = ("Bob", 14, "Grade 8")\n# ',
          'student = ("Bob", 14, "Grade 8")\nprint("Name:", student[0])\nprint("Age:", student[1])\nprint("Grade:", student[2])', "อ่านทีละช่อง"),
        p(7, "จุดสองค่า", "point_xy", "point = (3, 4) แสดง X และ Y", "2 บรรทัด", "X: 3\nY: 4",
          "point = (3, 4)\n# ", 'point = (3, 4)\nprint(f"X: {point[0]}")\nprint(f"Y: {point[1]}")'),
        p(10, "นับสมาชิก", "tup_count", 'rgb = ("r", "g", "b") แสดง Count', "1 บรรทัด", "Count: 3",
          'rgb = ("r", "g", "b")\n# ', 'rgb = ("r", "g", "b")\nprint(f"Count: {len(rgb)}")'),
        p(11, "วนพิกัด", "for_pair", "pair = (1, 2) พิมพ์ทีละค่า", "2 บรรทัด", "1\n2",
          "pair = (1, 2)\n# ", "pair = (1, 2)\nfor v in pair:\n    print(v)"),
        p(12, "ระเบียน", "record", 'info = ("Ann", 12) แสดงสองบรรทัด', "2 บรรทัด", "Ann\n12",
          'info = ("Ann", 12)\n# ', 'info = ("Ann", 12)\nprint(info[0])\nprint(info[1])'),
        p(13, "หัวท้าย", "head_tail_t", 't = ("a", "b", "c", "d") แสดงหัวท้าย', "2 บรรทัด", "a\nd",
          't = ("a", "b", "c", "d")\n# ', 't = ("a", "b", "c", "d")\nprint(t[0])\nprint(t[-1])'),
        p(5, "โปรไฟล์", "profile_t", 'p = ("Nova", 3, True) แสดง Player/Level/Active',
          "3 บรรทัด", "Player: Nova\nLevel: 3\nActive: True",
          'p = ("Nova", 3, True)\n# ',
          'p = ("Nova", 3, True)\nprint(f"Player: {p[0]}")\nprint(f"Level: {p[1]}")\nprint(f"Active: {p[2]}")'),
        p(14, "ตารางวัน", "week_table", 'days = ("Mon", "Tue", "Wed") พิมพ์ Day: ...',
          "3 บรรทัด", "Day: Mon\nDay: Tue\nDay: Wed",
          'days = ("Mon", "Tue", "Wed")\n# ',
          'days = ("Mon", "Tue", "Wed")\nfor d in days:\n    print(f"Day: {d}")'),
        p(15, "คงที่", "const_msg", 'msg = ("Hello", "World") แสดงประโยคด้วยช่องว่าง', "1 บรรทัด", "Hello World",
          'msg = ("Hello", "World")\n# ', 'msg = ("Hello", "World")\nprint(msg[0], msg[1])'),
        p(16, "สรุปทูเพิล", "tuple_summary", 's = ("Kim", 15, "A") แสดงความยาวและชื่อ',
          "2 บรรทัด", "Fields: 3\nName: Kim",
          's = ("Kim", 15, "A")\n# ',
          's = ("Kim", 15, "A")\nprint(f"Fields: {len(s)}")\nprint(f"Name: {s[0]}")'),
    ]
    write_week("029-tuples", chapter="Tuples", emoji="🧩", index_md=index, problems=probs)


def week_030():
    names = [("สร้างเซต", "literal"), ("ตัดซ้ำ", "dedupe"), ("แปลงจากลิสต์", "set(list)"),
             ("เพิ่ม", "add"), ("ลบ", "remove"),
             ("สมาชิก?", "in"), ("ยูเนียน", "|"), ("อินเตอร์เซกชัน", "&"),
             ("ไม่ซ้ำชื่อ", "set names"), ("เช็กของ", "in print"), ("รวมเซต", "| ป้าย"),
             ("คลังไม่ซ้ำ", "ผสม"), ("ตัดรายการ", "set+len"), ("สองกลุ่ม", "&"), ("สรุปเซต", "หลายขั้น")]
    index = idx("บท 030 Sets", "set / add / remove / in / | / & / set(list)", "ไม่มี difference/discard", names)
    probs = [
        p(2, "สร้างเซต", "make_set", 'แสดงเซต fruits = {"apple", "banana"} โดยพิมพ์ทั้งเซต (ลำดับอาจต่าง — ใช้เซตเดียวกับตัวอย่างที่มีสมาชิก 2)',
          "1 บรรทัด", "2",
          'fruits = {"apple", "banana"}\n# แสดงจำนวนแทนเพื่อเลี่ยงลำดับ',
          'fruits = {"apple", "banana"}\nprint(len(fruits))'),
        p(3, "ตัดซ้ำ", "dedupe", "nums = {1, 2, 2, 3, 3, 3} แสดงจำนวนสมาชิกหลังตัดซ้ำ", "1 บรรทัด", "3",
          "nums = {1, 2, 2, 3, 3, 3}\n# ", "nums = {1, 2, 2, 3, 3, 3}\nprint(len(nums))"),
        p(4, "แปลงจากลิสต์", "list_to_set", "data = [1, 2, 2, 3] แปลงเป็นเซตแล้วแสดงจำนวน", "1 บรรทัด", "3",
          "data = [1, 2, 2, 3]\n# ", "data = [1, 2, 2, 3]\nprint(len(set(data)))"),
        p(8, "เพิ่ม", "set_add", 's = {"a"} แล้ว add "b" แสดงจำนวน', "1 บรรทัด", "2",
          's = {"a"}\n# ', 's = {"a"}\ns.add("b")\nprint(len(s))'),
        p(9, "ลบ", "set_remove", 's = {"a", "b"} ลบ "a" แสดงจำนวน', "1 บรรทัด", "1",
          's = {"a", "b"}\n# ', 's = {"a", "b"}\ns.remove("a")\nprint(len(s))'),
        p(6, "สมาชิก?", "membership", 'fruits = {"apple", "banana"} แสดงผล "apple" in fruits และ "grape" in fruits',
          "2 บรรทัด", "True\nFalse",
          'fruits = {"apple", "banana"}\n# ',
          'fruits = {"apple", "banana"}\nprint("apple" in fruits)\nprint("grape" in fruits)', "ใช้ in"),
        p(7, "ยูเนียน", "union", 'a = {"A", "B"} b = {"B", "C"} แสดงจำนวน a|b', "1 บรรทัด", "3",
          'a = {"A", "B"}\nb = {"B", "C"}\n# ', 'a = {"A", "B"}\nb = {"B", "C"}\nprint(len(a | b))'),
        p(10, "อินเตอร์เซกชัน", "intersect", 'a = {"A", "B"} b = {"B", "C"} แสดงจำนวน a&b', "1 บรรทัด", "1",
          'a = {"A", "B"}\nb = {"B", "C"}\n# ', 'a = {"A", "B"}\nb = {"B", "C"}\nprint(len(a & b))'),
        p(11, "ไม่ซ้ำชื่อ", "unique_names", 'names = ["Ann", "Ben", "Ann"] แสดงจำนวนชื่อไม่ซ้ำ', "1 บรรทัด", "2",
          'names = ["Ann", "Ben", "Ann"]\n# ', 'names = ["Ann", "Ben", "Ann"]\nprint(len(set(names)))'),
        p(12, "เช็กของ", "check_item", 'bag = {"pen", "book"} รับคำ แล้วแสดงผลว่ามีใน bag หรือไม่ (True/False)',
          "1 บรรทัด", "True",
          'bag = {"pen", "book"}\nword = input()\n# ',
          'bag = {"pen", "book"}\nword = input()\nprint(word in bag)', sample_in="pen"),
        p(13, "รวมเซต", "union_label", 'a = {1, 2} b = {2, 3} แสดง Size ของ union', "1 บรรทัด", "Size: 3",
          "a = {1, 2}\nb = {2, 3}\n# ", 'a = {1, 2}\nb = {2, 3}\nprint(f"Size: {len(a | b)}")'),
        p(5, "คลังไม่ซ้ำ", "warehouse_set", 'items = ["nail", "screw", "nail"] แปลงเป็นเซต add "bolt" แสดงจำนวน',
          "1 บรรทัด", "3",
          'items = ["nail", "screw", "nail"]\n# ',
          'items = ["nail", "screw", "nail"]\ns = set(items)\ns.add("bolt")\nprint(len(s))', "set แล้ว add"),
        p(14, "ตัดรายการ", "dedupe_len", "data = [5, 5, 6, 6, 6] แสดง Unique count", "1 บรรทัด", "Unique: 2",
          "data = [5, 5, 6, 6, 6]\n# ", 'data = [5, 5, 6, 6, 6]\nprint(f"Unique: {len(set(data))}")'),
        p(15, "สองกลุ่ม", "two_groups", 'math = {"Ann", "Ben"} art = {"Ben", "Cat"} แสดงจำนวนคนที่เรียนทั้งสอง',
          "1 บรรทัด", "Both: 1",
          'math = {"Ann", "Ben"}\nart = {"Ben", "Cat"}\n# ',
          'math = {"Ann", "Ben"}\nart = {"Ben", "Cat"}\nprint(f"Both: {len(math & art)}")'),
        p(16, "สรุปเซต", "set_finale", 's = {"x"} add "y" remove "x" แสดง "y" in s',
          "1 บรรทัด", "True",
          's = {"x"}\n# ', 's = {"x"}\ns.add("y")\ns.remove("x")\nprint("y" in s)'),
    ]
    write_week("030-sets", chapter="Sets", emoji="🔵", index_md=index, problems=probs)


def week_031():
    names = [("เลือก list", "mutable"), ("เลือก tuple", "fixed"), ("เลือก set", "unique"),
             ("สร้างตามโจทย์", "list"), ("วันในสัปดาห์", "tuple"),
             ("ผู้เยี่ยมไม่ซ้ำ", "set"), ("ตะกร้า", "list append"), ("พิกัด", "tuple"),
             ("แท็ก", "set"), ("เปรียบเทียบจำนวน", "len"), ("สถานการณ์ผสม", "3 ชนิด"),
             ("ของใช้ประจำ", "list"), ("รหัสคงที่", "tuple"), ("บัตรเข้างาน", "set"), ("สรุปเลือกชนิด", "ตัดสินใจ")]
    index = idx("บท 031 Choosing Data Types", "เลือก list/tuple/set ตามสถานการณ์ (ไม่มี syntax ใหม่)", "ใช้ของที่สอนแล้ว", names)
    probs = [
        p(2, "เลือก list", "use_list", 'สร้าง shopping = ["milk", "eggs"] แล้ว append "bread" แสดงลิสต์',
          "1 บรรทัด", "['milk', 'eggs', 'bread']",
          "# list", 'shopping = ["milk", "eggs"]\nshopping.append("bread")\nprint(shopping)'),
        p(3, "เลือก tuple", "use_tuple", 'weekdays = ("Mon", "Tue", "Wed") แสดงความยาว', "1 บรรทัด", "3",
          "# tuple", 'weekdays = ("Mon", "Tue", "Wed")\nprint(len(weekdays))'),
        p(4, "เลือก set", "use_set", 'visitors = {"Alice", "Bob", "Alice"} แสดงจำนวนไม่ซ้ำ', "1 บรรทัด", "2",
          "# set", 'visitors = {"Alice", "Bob", "Alice"}\nprint(len(visitors))'),
        p(8, "สร้างตามโจทย์", "make_roster", 'roster นักเรียนแบบแก้ได้: ["Ann", "Ben"] แสดง', "1 บรรทัด", "['Ann', 'Ben']",
          "# ", 'roster = ["Ann", "Ben"]\nprint(roster)'),
        p(9, "วันในสัปดาห์", "fixed_days", 'days = ("Sat", "Sun") แสดงวันแรก', "1 บรรทัด", "Sat",
          "# ", 'days = ("Sat", "Sun")\nprint(days[0])'),
        p(6, "ผู้เยี่ยมไม่ซ้ำ", "unique_visitors", 'raw = ["A", "B", "A"] แปลงเป็นเซตแสดงจำนวน', "1 บรรทัด", "2",
          'raw = ["A", "B", "A"]\n# ', 'raw = ["A", "B", "A"]\nprint(len(set(raw)))', "ใช้ set เมื่อไม่เอาซ้ำ"),
        p(7, "ตะกร้า", "cart", 'cart = ["apple"] append "banana"', "1 บรรทัด", "['apple', 'banana']",
          'cart = ["apple"]\n# ', 'cart = ["apple"]\ncart.append("banana")\nprint(cart)'),
        p(10, "พิกัด", "coords", "point = (0, 0) แสดง Y", "1 บรรทัด", "0",
          "point = (0, 0)\n# ", "point = (0, 0)\nprint(point[1])"),
        p(11, "แท็ก", "tags", 'tags = {"math", "fun"} add "code" แสดงจำนวน', "1 บรรทัด", "3",
          'tags = {"math", "fun"}\n# ', 'tags = {"math", "fun"}\ntags.add("code")\nprint(len(tags))'),
        p(12, "เปรียบเทียบจำนวน", "compare_sizes",
          'lst = ["A", "A"] และ st = set(lst) แสดงความยาว list และ set',
          "2 บรรทัด", "List: 2\nSet: 1",
          'lst = ["A", "A"]\n# ',
          'lst = ["A", "A"]\nst = set(lst)\nprint(f"List: {len(lst)}")\nprint(f"Set: {len(st)}")'),
        p(13, "สถานการณ์ผสม", "three_types",
          'สร้าง list L=[1, 2], tuple T=(9, 8), set S={3} แสดงความยาวทั้งสาม',
          "3 บรรทัด", "2\n2\n1",
          "# สามชนิด", "L = [1, 2]\nT = (9, 8)\nS = {3}\nprint(len(L))\nprint(len(T))\nprint(len(S))"),
        p(5, "ของใช้ประจำ", "daily_items", 'items = ["brush", "towel"] แก้ตัวแรกเป็น "comb" แสดง',
          "1 บรรทัด", "['comb', 'towel']",
          'items = ["brush", "towel"]\n# ', 'items = ["brush", "towel"]\nitems[0] = "comb"\nprint(items)', "list เพราะต้องแก้"),
        p(14, "รหัสคงที่", "fixed_code", 'code = ("TH", "BKK") แสดง Country', "1 บรรทัด", "Country: TH",
          'code = ("TH", "BKK")\n# ', 'code = ("TH", "BKK")\nprint(f"Country: {code[0]}")'),
        p(15, "บัตรเข้างาน", "badges", 'seen = set() add "A" add "A" แสดงจำนวน', "1 บรรทัด", "1",
          "seen = set()\n# ", 'seen = set()\nseen.add("A")\nseen.add("A")\nprint(len(seen))'),
        p(16, "สรุปเลือกชนิด", "choose_finale",
          'มีรายชื่อซ้ำ names=["X","Y","X"] แสดงจำนวนสมาชิกแบบ list และแบบไม่ซ้ำ',
          "2 บรรทัด", "All: 3\nUnique: 2",
          'names = ["X", "Y", "X"]\n# ',
          'names = ["X", "Y", "X"]\nprint(f"All: {len(names)}")\nprint(f"Unique: {len(set(names))}")'),
    ]
    write_week("031-choosing-data-types", chapter="Choosing Types", emoji="⚖️", index_md=index, problems=probs)


if __name__ == "__main__":
    week_028()
    week_029()
    week_030()
    week_031()
    print("028-031 done")
