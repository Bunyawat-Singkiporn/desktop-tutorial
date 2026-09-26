# -*- coding: utf-8 -*-
"""Expand weeks 029-032 to 15-problem standard."""
from _expand_helpers import write_week

NO_IN = "ไม่มี (กำหนดค่าในโปรแกรม)"


def p(n, title, slug, body, out_desc, sample_out, starter, answer, hint=None, sample_in=None, in_desc=None):
    return {
        "n": n, "title": title, "slug": slug, "body": body,
        "input_desc": in_desc if in_desc is not None else (NO_IN if sample_in is None else "ดูตัวอย่าง"),
        "output_desc": out_desc, "sample_input": sample_in, "sample_output": sample_out,
        "hint": hint, "starter": starter, "answer": answer,
    }


def idx(title, scope, bans, rows, notes=""):
    table = "\n".join(f"| {i} | `{a}` | {b} | {c} | {d} |" for i, (a, b, c, d) in enumerate(rows, 1))
    return f"""# 📋 สารบัญโจทย์ — {title}

**ขอบเขตของบทนี้:** {scope}

> ❌ {bans}

---

## ลำดับที่แนะนำ

| # | ไฟล์ | ระดับ | โจทย์ | แกนการคิด |
|---|------|-------|-------|-----------|
{table}

**สรุป:** 🟢 Easy 5 ข้อ · 🟡 Medium 6 ข้อ · 🔴 Challenge 4 ข้อ = **15 ข้อ**

---

## หมายเหตุสำหรับครู

{notes}
"""


# ─── 029 tuples ──────────────────────────────────────────────────────────────

write_week(
    "029-tuples",
    chapter="Tuples",
    emoji="📦",
    index_md=idx(
        "บท 029 Tuples",
        "tuple `()` · indexing · `len()` · `for x in tuple` · อ่านอย่างเดียว (immutable)",
        "ห้ามแก้ค่า tuple · ไม่มี unpacking · ไม่มี list methods บน tuple",
        [
            ("02_test.md", "🟢", "ป้ายวันทำการหัวท้าย", "index แรก/ท้าย"),
            ("03_test.md", "🟢", "พิกัดจุดบนแผนที่", "อ่านสองค่าจาก tuple"),
            ("04_test.md", "🟢", "นับจำนวนวันในสัปดาห์เรียน", "len ของ tuple"),
            ("08_easy.md", "🟢", "วนพิมพ์สีธง", "for ใน tuple"),
            ("09_easy.md", "🟢", "รหัสห้องเรียน", "index กลาง"),
            ("06_medium.md", "🟡", "บัตรนักเรียนสั้น", "พิมพ์ฟิลด์จาก tuple"),
            ("07_medium.md", "🟡", "สรุปพิกัดพร้อมจำนวน", "index + len"),
            ("10_medium.md", "🟡", "เมนูคงที่พร้อมเลข", "นับเองขณะวน"),
            ("11_medium.md", "🟡", "เปรียบเทียบสองพิกัด", "อ่านหลาย tuple"),
            ("12_medium.md", "🟡", "บันทึกผลการแข่ง", "tuple ของตัวเลข + รวม"),
            ("13_medium.md", "🟡", "ป้ายเที่ยวบิน", "หลายฟิลด์ + กล่อง"),
            ("05_challenge.md", "🔴", "โปรไฟล์นักกีฬา", "tuple หลายค่า + สรุป"),
            ("14_challenge.md", "🔴", "ตารางเวลาเรียนคงที่", "วน + หัวท้าย"),
            ("15_challenge.md", "🔴", "ใบเสร็จพิกัดส่งของ", "สอง tuple + คำนวณ"),
            ("16_challenge.md", "🔴", "กล่องข้อมูลชั้นเรียน", "tuple ผสม + กรอบ"),
        ],
        "- ข้อ 02 ไม่ซ้ำตัวอย่าง days/student ในบทเรียนแบบเดิม\n"
        "- tuple อ่านได้อย่างเดียว ห้าม assignment\n"
        "- ไม่สอน unpacking",
    ),
    problems=[
        p(2, "ป้ายวันทำการหัวท้าย", "workdays_ends",
          "ออฟฟิศอยากโชว์วันทำการวันแรกและวันสุดท้าย\n\n"
          "กำหนด `workdays = (\"Mon\", \"Tue\", \"Wed\", \"Thu\", \"Fri\")`\n\n"
          "แสดงวันแรกและวันสุดท้ายคนละบรรทัด",
          "2 บรรทัด", "Mon\nFri",
          'workdays = ("Mon", "Tue", "Wed", "Thu", "Fri")\n\n# เขียนโค้ดตรงนี้',
          'workdays = ("Mon", "Tue", "Wed", "Thu", "Fri")\nprint(workdays[0])\nprint(workdays[-1])'),
        p(3, "พิกัดจุดบนแผนที่", "map_point",
          "แอปแผนที่เก็บพิกัดจุดหนึ่งไว้ใน tuple\n\n"
          "กำหนด `point = (12, 45)`\n\n"
          "แสดง `X: 12` และ `Y: 45`",
          "2 บรรทัด", "X: 12\nY: 45",
          "point = (12, 45)\n\n# เขียนโค้ดตรงนี้",
          'point = (12, 45)\nprint(f"X: {point[0]}")\nprint(f"Y: {point[1]}")'),
        p(4, "นับจำนวนวันในสัปดาห์เรียน", "school_days_len",
          "นับจำนวนวันเรียนในสัปดาห์\n\n"
          "กำหนด `days = (\"Mon\", \"Tue\", \"Wed\", \"Thu\", \"Fri\")`\n\n"
          "แสดง `Days: 5`",
          "บรรทัดเดียว", "Days: 5",
          'days = ("Mon", "Tue", "Wed", "Thu", "Fri")\n\n# เขียนโค้ดตรงนี้',
          'days = ("Mon", "Tue", "Wed", "Thu", "Fri")\nprint(f"Days: {len(days)}")'),
        p(8, "วนพิมพ์สีธง", "flag_colors",
          "พิมพ์สีของธงทีละบรรทัด\n\n"
          "กำหนด `colors = (\"Red\", \"White\", \"Blue\")`\n\n"
          "วนพิมพ์ทุกสี",
          "3 บรรทัด", "Red\nWhite\nBlue",
          'colors = ("Red", "White", "Blue")\n\n# เขียนโค้ดตรงนี้',
          'colors = ("Red", "White", "Blue")\nfor color in colors:\n    print(color)'),
        p(9, "รหัสห้องเรียน", "room_code",
          "รหัสห้องเก็บเป็น tuple สามส่วน อยากได้ส่วนกลาง\n\n"
          "กำหนด `room = (\"B\", \"204\", \"Lab\")`\n\n"
          "แสดงส่วนกลาง `204`",
          "บรรทัดเดียว", "204",
          'room = ("B", "204", "Lab")\n\n# เขียนโค้ดตรงนี้',
          'room = ("B", "204", "Lab")\nprint(room[1])'),
        p(6, "บัตรนักเรียนสั้น", "student_card",
          "พิมพ์บัตรนักเรียนจากข้อมูลคงที่\n\n"
          "กำหนด `student = (\"Nida\", 13, \"M1\")`\n\n"
          "แสดง Name / Age / Grade ตามตัวอย่าง",
          "3 บรรทัด", "Name : Nida\nAge  : 13\nGrade: M1",
          'student = ("Nida", 13, "M1")\n\n# เขียนโค้ดตรงนี้',
          'student = ("Nida", 13, "M1")\nprint(f"Name : {student[0]}")\nprint(f"Age  : {student[1]}")\nprint(f"Grade: {student[2]}")',
          "อ่านทีละตำแหน่งด้วย index"),
        p(7, "สรุปพิกัดพร้อมจำนวน", "point_summary",
          "สรุปพิกัดและจำนวนค่าใน tuple\n\n"
          "กำหนด `point = (8, 15, 3)`\n\n"
          "แสดงค่าแรก ค่าสุดท้าย และจำนวนสมาชิก",
          "3 บรรทัด", "Start: 8\nEnd  : 3\nSize : 3",
          "point = (8, 15, 3)\n\n# เขียนโค้ดตรงนี้",
          'point = (8, 15, 3)\nprint(f"Start: {point[0]}")\nprint(f"End  : {point[-1]}")\nprint(f"Size : {len(point)}")',
          "ใช้ [0] [-1] และ len"),
        p(10, "เมนูคงที่พร้อมเลข", "fixed_menu",
          "เมนูอาหารชุดพิเศษเปลี่ยนไม่ได้ อยากพิมพ์พร้อมเลขที่\n\n"
          "กำหนด `menu = (\"Rice\", \"Soup\", \"Fruit\")`\n\n"
          "แสดง `1. Rice` โดยเพิ่มตัวนับเอง",
          "3 บรรทัด", "1. Rice\n2. Soup\n3. Fruit",
          'menu = ("Rice", "Soup", "Fruit")\n\n# เขียนโค้ดตรงนี้',
          'menu = ("Rice", "Soup", "Fruit")\nnum = 1\nfor item in menu:\n    print(f"{num}. {item}")\n    num += 1',
          "tuple วนได้เหมือน list"),
        p(11, "เปรียบเทียบสองพิกัด", "compare_points",
          "เปรียบเทียบพิกัด X ของจุดสองจุด\n\n"
          "กำหนด `a = (10, 20)` และ `b = (7, 25)`\n\n"
          "ถ้า X ของ a มากกว่าหรือเท่ากับ b แสดง `A` ไม่เช่นนั้นแสดง `B`",
          "บรรทัดเดียว", "A",
          "a = (10, 20)\nb = (7, 25)\n\n# เขียนโค้ดตรงนี้",
          'a = (10, 20)\nb = (7, 25)\nif a[0] >= b[0]:\n    print("A")\nelse:\n    print("B")',
          "เทียบเฉพาะค่า index 0"),
        p(12, "บันทึกผลการแข่ง", "match_scores",
          "ผลการแข่งเก็บเป็นคะแนนคงที่\n\n"
          "กำหนด `scores = (2, 1, 3, 0)`\n\n"
          "รวมคะแนนแล้วแสดง `Total: ...` และจำนวนเกม",
          "2 บรรทัด", "Total: 6\nGames: 4",
          "scores = (2, 1, 3, 0)\n\n# เขียนโค้ดตรงนี้",
          'scores = (2, 1, 3, 0)\ntotal = 0\nfor s in scores:\n    total += s\nprint(f"Total: {total}")\nprint(f"Games: {len(scores)}")',
          "วนรวมได้เหมือน list"),
        p(13, "ป้ายเที่ยวบิน", "flight_tag",
          "พิมพ์ป้ายเที่ยวบินจากข้อมูลคงที่\n\n"
          "กำหนด `flight = (\"TG\", 305, \"BKK\")`\n\n"
          "แสดงตามตัวอย่าง",
          "3 บรรทัด", "Airline: TG\nNumber : 305\nCity   : BKK",
          'flight = ("TG", 305, "BKK")\n\n# เขียนโค้ดตรงนี้',
          'flight = ("TG", 305, "BKK")\nprint(f"Airline: {flight[0]}")\nprint(f"Number : {flight[1]}")\nprint(f"City   : {flight[2]}")',
          "จัดคอลัมน์ป้ายกำกับให้ตรง"),
        p(5, "โปรไฟล์นักกีฬา", "athlete_profile",
          "พิมพ์โปรไฟล์นักกีฬาจาก tuple\n\n"
          "กำหนด `athlete = (\"Beam\", 16, \"Swim\", 3)`\n\n"
          "แสดงชื่อ อายุ กีฬา และจำนวนเหรียญ ตามตัวอย่าง",
          "4 บรรทัด",
          "Name  : Beam\nAge   : 16\nSport : Swim\nMedals: 3",
          'athlete = ("Beam", 16, "Swim", 3)\n\n# เขียนโค้ดตรงนี้',
          'athlete = ("Beam", 16, "Swim", 3)\nprint(f"Name  : {athlete[0]}")\nprint(f"Age   : {athlete[1]}")\nprint(f"Sport : {athlete[2]}")\nprint(f"Medals: {athlete[3]}")',
          "อ่านทีละฟิลด์ตามลำดับ"),
        p(14, "ตารางเวลาเรียนคงที่", "timetable",
          "ตารางคาบเช้าเปลี่ยนไม่ได้\n\n"
          "กำหนด `periods = (\"Math\", \"Thai\", \"Science\", \"PE\")`\n\n"
          "พิมพ์ทุกคาบทีละบรรทัด แล้วปิดท้ายด้วยคาบแรก คาบสุดท้าย และจำนวนคาบ",
          "รายการ + สรุป",
          "Math\nThai\nScience\nPE\nFirst: Math\nLast : PE\nCount: 4",
          'periods = ("Math", "Thai", "Science", "PE")\n\n# เขียนโค้ดตรงนี้',
          'periods = ("Math", "Thai", "Science", "PE")\nfor p in periods:\n    print(p)\nprint(f"First: {periods[0]}")\nprint(f"Last : {periods[-1]}")\nprint(f"Count: {len(periods)}")',
          "วนพิมพ์ก่อน แล้วค่อยสรุป"),
        p(15, "ใบเสร็จพิกัดส่งของ", "delivery_points",
          "ระบบส่งของมีจุดรับและจุดส่ง\n\n"
          "กำหนด `pickup = (10, 20)` และ `drop = (40, 50)`\n\n"
          "แสดงพิกัดทั้งสอง และผลต่างของ X กับ Y (drop - pickup)",
          "สรุป 4 บรรทัด",
          "Pickup: (10, 20)\nDrop  : (40, 50)\nDX    : 30\nDY    : 30",
          "pickup = (10, 20)\ndrop = (40, 50)\n\n# เขียนโค้ดตรงนี้",
          'pickup = (10, 20)\ndrop = (40, 50)\nprint(f"Pickup: ({pickup[0]}, {pickup[1]})")\nprint(f"Drop  : ({drop[0]}, {drop[1]})")\nprint(f"DX    : {drop[0] - pickup[0]}")\nprint(f"DY    : {drop[1] - pickup[1]}")',
          "คำนวณจากค่าที่อ่านจาก tuple"),
        p(16, "กล่องข้อมูลชั้นเรียน", "class_tuple_box",
          "แสดงข้อมูลชั้นเรียนแบบมีกรอบ\n\n"
          "กำหนด `info = (\"M2/1\", 32, \"Building A\")`\n\n"
          "แสดงตามตัวอย่าง",
          "กล่องสรุป",
          "====================\nClass : M2/1\nSize  : 32\nPlace : Building A\n====================",
          'info = ("M2/1", 32, "Building A")\n\n# เขียนโค้ดตรงนี้',
          'info = ("M2/1", 32, "Building A")\nprint("====================")\nprint(f"Class : {info[0]}")\nprint(f"Size  : {info[1]}")\nprint(f"Place : {info[2]}")\nprint("====================")',
          "กรอบยาวเท่ากันทุกบรรทัด"),
    ],
)


# ─── 030 sets ────────────────────────────────────────────────────────────────
# Careful: set print order is non-deterministic — convert to list + sort when showing contents

write_week(
    "030-sets",
    chapter="Sets",
    emoji="🔤",
    index_md=idx(
        "บท 030 Sets",
        "set `{}` · `set(list)` · `.add()` · `.remove()` · **`in`** · `|` · `&`",
        "ห้ามพึ่งพาลำดับตอน print(set) — แปลงเป็น list แล้ว `.sort()` ก่อนแสดง · ไม่มี set difference",
        [
            ("02_test.md", "🟢", "เช็คชื่อในกลุ่มเพื่อน", "in สมาชิก"),
            ("03_test.md", "🟢", "เพิ่มเมืองที่เคยไป", "add"),
            ("04_test.md", "🟢", "ลบเมนูที่เลิกขาย", "remove"),
            ("08_easy.md", "🟢", "ตัดชื่อซ้ำจากรายชื่อ", "set(list) + เรียง"),
            ("09_easy.md", "🟢", "เช็คว่ามีรหัสหรือยัง", "in + ข้อความ"),
            ("06_medium.md", "🟡", "เพื่อนร่วมและสหภาพ", "| และ &"),
            ("07_medium.md", "🟡", "นับสมาชิกไม่ซ้ำ", "set + len ผ่าน list"),
            ("10_medium.md", "🟡", "เพิ่มแล้วเช็คของในคลัง", "add + in"),
            ("11_medium.md", "🟡", "ลบแล้วหาส่วนร่วม", "remove + &"),
            ("12_medium.md", "🟡", "รวมสองรายการไม่ซ้ำ", "| แล้วเรียง"),
            ("13_medium.md", "🟡", "วิชาที่เรียนร่วมกัน", "& แล้วเรียง"),
            ("05_challenge.md", "🔴", "บัตรเข้างานพร้อมเช็ค", "in + ข้อความสองทาง"),
            ("14_challenge.md", "🔴", "อัปเดตชมรมแล้วสรุป", "add/remove + |"),
            ("15_challenge.md", "🔴", "เพื่อนเก่าเพื่อนใหม่", "| & และจำนวน"),
            ("16_challenge.md", "🔴", "คลังรหัสสินค้า", "ครบชุด set skills"),
        ],
        "- ข้อ 02 ไม่ซ้ำตัวอย่าง fruits membership แบบเดิมทุกตัวอักษร\n"
        "- เมื่อต้องแสดงสมาชิก set ให้แปลงเป็น list แล้ว sort เสมอ\n"
        "- `in` สอนครั้งแรกในบทนี้",
    ),
    problems=[
        p(2, "เช็คชื่อในกลุ่มเพื่อน", "friend_check",
          "แอปเช็คว่ามีเพื่อนชื่อนี้ในกลุ่มหรือไม่\n\n"
          "กำหนด `friends = {\"Mew\", \"Pim\", \"Ohm\"}`\n\n"
          "ถ้า `\"Pim\"` อยู่ในกลุ่ม แสดง `Found` ไม่เช่นนั้นแสดง `Missing`",
          "บรรทัดเดียว", "Found",
          'friends = {"Mew", "Pim", "Ohm"}\n\n# เขียนโค้ดตรงนี้',
          'friends = {"Mew", "Pim", "Ohm"}\nif "Pim" in friends:\n    print("Found")\nelse:\n    print("Missing")'),
        p(3, "เพิ่มเมืองที่เคยไป", "city_add",
          "นักท่องเที่ยวเพิ่มเมืองใหม่เข้า set\n\n"
          "กำหนด `cities = {\"Bangkok\", \"Chiang Mai\"}` แล้ว `.add(\"Phuket\")`\n\n"
          "แปลงเป็น list เรียงชื่อ แล้วแสดง",
          "list หนึ่งบรรทัด", "['Bangkok', 'Chiang Mai', 'Phuket']",
          'cities = {"Bangkok", "Chiang Mai"}\n\n# เขียนโค้ดตรงนี้',
          'cities = {"Bangkok", "Chiang Mai"}\ncities.add("Phuket")\nresult = list(cities)\nresult.sort()\nprint(result)'),
        p(4, "ลบเมนูที่เลิกขาย", "menu_set_remove",
          "ร้านลบเมนูที่เลิกขายออกจาก set\n\n"
          "กำหนด `menu = {\"Soup\", \"Salad\", \"Steak\"}` แล้ว remove `Salad`\n\n"
          "แปลงเป็น list เรียงแล้วแสดง",
          "list หนึ่งบรรทัด", "['Soup', 'Steak']",
          'menu = {"Soup", "Salad", "Steak"}\n\n# เขียนโค้ดตรงนี้',
          'menu = {"Soup", "Salad", "Steak"}\nmenu.remove("Salad")\nresult = list(menu)\nresult.sort()\nprint(result)'),
        p(8, "ตัดชื่อซ้ำจากรายชื่อ", "dedup_names",
          "รายชื่อมีชื่อซ้ำ อยากได้ชุดไม่ซ้ำ\n\n"
          "กำหนด `names = [\"Ann\", \"Ben\", \"Ann\", \"Cara\", \"Ben\"]`\n\n"
          "แปลงเป็น set แล้วกลับเป็น list เรียงชื่อ และแสดง",
          "list หนึ่งบรรทัด", "['Ann', 'Ben', 'Cara']",
          'names = ["Ann", "Ben", "Ann", "Cara", "Ben"]\n\n# เขียนโค้ดตรงนี้',
          'names = ["Ann", "Ben", "Ann", "Cara", "Ben"]\nunique = list(set(names))\nunique.sort()\nprint(unique)'),
        p(9, "เช็คว่ามีรหัสหรือยัง", "code_check",
          "ระบบเช็ครหัสคูปอง\n\n"
          "กำหนด `codes = {\"A1\", \"B2\", \"C3\"}`\n\n"
          "เช็ค `\"B2\"` ถ้ามีแสดง `Valid` ไม่มีแสดง `Invalid`",
          "บรรทัดเดียว", "Valid",
          'codes = {"A1", "B2", "C3"}\n\n# เขียนโค้ดตรงนี้',
          'codes = {"A1", "B2", "C3"}\nif "B2" in codes:\n    print("Valid")\nelse:\n    print("Invalid")'),
        p(6, "เพื่อนร่วมและสหภาพ", "friend_ops",
          "หาเพื่อนที่อยู่ทั้งสองกลุ่ม และเพื่อนทั้งหมด\n\n"
          "กำหนด `a = {\"Ann\", \"Ben\", \"Cara\"}` และ `b = {\"Ben\", \"Dan\", \"Cara\"}`\n\n"
          "แสดงส่วนร่วมและสหภาพ (เรียงชื่อ) คนละบรรทัด",
          "2 บรรทัด",
          "['Ben', 'Cara']\n['Ann', 'Ben', 'Cara', 'Dan']",
          'a = {"Ann", "Ben", "Cara"}\nb = {"Ben", "Dan", "Cara"}\n\n# เขียนโค้ดตรงนี้',
          'a = {"Ann", "Ben", "Cara"}\nb = {"Ben", "Dan", "Cara"}\nboth = list(a & b)\nboth.sort()\nall_friends = list(a | b)\nall_friends.sort()\nprint(both)\nprint(all_friends)',
          "& คือส่วนร่วม | คือรวมทั้งหมด"),
        p(7, "นับสมาชิกไม่ซ้ำ", "unique_count",
          "นับจำนวนรหัสไม่ซ้ำจาก list\n\n"
          "กำหนด `ids = [10, 20, 10, 30, 20, 40]`\n\n"
          "แสดง `Unique: N`",
          "บรรทัดเดียว", "Unique: 4",
          "ids = [10, 20, 10, 30, 20, 40]\n\n# เขียนโค้ดตรงนี้",
          'ids = [10, 20, 10, 30, 20, 40]\nunique = set(ids)\nprint(f"Unique: {len(unique)}")',
          "set ตัดซ้ำ แล้วใช้ len"),
        p(10, "เพิ่มแล้วเช็คของในคลัง", "stock_add_check",
          "คลังเพิ่มสินค้าแล้วเช็คว่ามีหรือยัง\n\n"
          "กำหนด `stock = {\"Rice\", \"Oil\"}` แล้ว add `Salt`\n\n"
          "ถ้ามี `Salt` แสดง `In stock` ไม่เช่นนั้น `Out`",
          "บรรทัดเดียว", "In stock",
          'stock = {"Rice", "Oil"}\n\n# เขียนโค้ดตรงนี้',
          'stock = {"Rice", "Oil"}\nstock.add("Salt")\nif "Salt" in stock:\n    print("In stock")\nelse:\n    print("Out")',
          "add ก่อน แล้วค่อย in"),
        p(11, "ลบแล้วหาส่วนร่วม", "remove_then_and",
          "ลบสมาชิกแล้วหาส่วนร่วมกับอีกกลุ่ม\n\n"
          "กำหนด `a = {\"A\", \"B\", \"C\", \"D\"}` และ `b = {\"B\", \"C\", \"E\"}`\n\n"
          "ลบ `D` จาก a แล้วแสดง `a & b` แบบ list เรียง",
          "list หนึ่งบรรทัด", "['B', 'C']",
          'a = {"A", "B", "C", "D"}\nb = {"B", "C", "E"}\n\n# เขียนโค้ดตรงนี้',
          'a = {"A", "B", "C", "D"}\nb = {"B", "C", "E"}\na.remove("D")\nresult = list(a & b)\nresult.sort()\nprint(result)',
          "remove ก่อนคำนวณส่วนร่วม"),
        p(12, "รวมสองรายการไม่ซ้ำ", "union_sorted",
          "รวมรายชื่อสองห้องให้ไม่ซ้ำ\n\n"
          "กำหนด `room1 = {\"Ann\", \"Ben\"}` และ `room2 = {\"Ben\", \"Cara\", \"Dan\"}`\n\n"
          "ใช้ `|` แล้วแสดง list เรียง",
          "list หนึ่งบรรทัด", "['Ann', 'Ben', 'Cara', 'Dan']",
          'room1 = {"Ann", "Ben"}\nroom2 = {"Ben", "Cara", "Dan"}\n\n# เขียนโค้ดตรงนี้',
          'room1 = {"Ann", "Ben"}\nroom2 = {"Ben", "Cara", "Dan"}\nresult = list(room1 | room2)\nresult.sort()\nprint(result)',
          "| รวมแล้วตัดซ้ำอัตโนมัติ"),
        p(13, "วิชาที่เรียนร่วมกัน", "shared_subjects",
          "หาวิชาที่ทั้งสองคนเรียนร่วมกัน\n\n"
          "กำหนด `ann = {\"Math\", \"Thai\", \"PE\"}` และ `ben = {\"Thai\", \"Art\", \"PE\"}`\n\n"
          "แสดงส่วนร่วมแบบ list เรียง",
          "list หนึ่งบรรทัด", "['PE', 'Thai']",
          'ann = {"Math", "Thai", "PE"}\nben = {"Thai", "Art", "PE"}\n\n# เขียนโค้ดตรงนี้',
          'ann = {"Math", "Thai", "PE"}\nben = {"Thai", "Art", "PE"}\nshared = list(ann & ben)\nshared.sort()\nprint(shared)',
          "& ให้เฉพาะตัวที่มีทั้งสองฝั่ง"),
        p(5, "บัตรเข้างานพร้อมเช็ค", "badge_check",
          "ระบบสแกนบัตรเข้างาน\n\n"
          "กำหนด `badges = {\"E01\", \"E02\", \"E03\"}`\n\n"
          "เช็ค `\"E04\"` ถ้ามีแสดง `Welcome` ไม่มีแสดง `Denied`",
          "บรรทัดเดียว", "Denied",
          'badges = {"E01", "E02", "E03"}\n\n# เขียนโค้ดตรงนี้',
          'badges = {"E01", "E02", "E03"}\nif "E04" in badges:\n    print("Welcome")\nelse:\n    print("Denied")',
          "กรณีไม่พบก็ต้องมี else"),
        p(14, "อัปเดตชมรมแล้วสรุป", "club_update",
          "ชมรมอัปเดตรายชื่อสมาชิก\n\n"
          "กำหนด `club = {\"Ann\", \"Ben\", \"Cara\"}`\n\n"
          "เพิ่ม `Dan` ลบ `Ben` แล้วแสดงสมาชิกเรียงและจำนวน",
          "2 บรรทัด", "['Ann', 'Cara', 'Dan']\nMembers: 3",
          'club = {"Ann", "Ben", "Cara"}\n\n# เขียนโค้ดตรงนี้',
          'club = {"Ann", "Ben", "Cara"}\nclub.add("Dan")\nclub.remove("Ben")\nmembers = list(club)\nmembers.sort()\nprint(members)\nprint(f"Members: {len(members)}")',
          "add/remove แล้วค่อยแปลงเป็น list"),
        p(15, "เพื่อนเก่าเพื่อนใหม่", "old_new_friends",
          "เปรียบเทียบเพื่อนปีที่แล้วกับปีนี้\n\n"
          "กำหนด `old = {\"Ann\", \"Ben\", \"Cara\"}` และ `new = {\"Ben\", \"Cara\", \"Dan\", \"Ed\"}`\n\n"
          "แสดงจำนวนเพื่อนทั้งหมด (union) และจำนวนเพื่อนร่วม (intersection)",
          "2 บรรทัด", "All  : 5\nBoth : 2",
          'old = {"Ann", "Ben", "Cara"}\nnew = {"Ben", "Cara", "Dan", "Ed"}\n\n# เขียนโค้ดตรงนี้',
          'old = {"Ann", "Ben", "Cara"}\nnew = {"Ben", "Cara", "Dan", "Ed"}\nprint(f"All  : {len(old | new)}")\nprint(f"Both : {len(old & new)}")',
          "ใช้ len กับผลของ | และ &"),
        p(16, "คลังรหัสสินค้า", "sku_warehouse",
          "คลังจัดการรหัสสินค้า\n\n"
          "กำหนด `warehouse = {\"S01\", \"S02\", \"S03\"}` และ `incoming = {\"S03\", \"S04\"}`\n\n"
          "เพิ่ม `S05` เข้า warehouse ลบ `S01` แล้วแสดง\n"
          "รหัสทั้งหมดหลังรวมกับ incoming (เรียง) ส่วนร่วมกับ incoming (เรียง) และจำนวนทั้งหมด",
          "3 บรรทัด",
          "['S02', 'S03', 'S04', 'S05']\n['S03']\nTotal: 4",
          'warehouse = {"S01", "S02", "S03"}\nincoming = {"S03", "S04"}\n\n# เขียนโค้ดตรงนี้',
          'warehouse = {"S01", "S02", "S03"}\nincoming = {"S03", "S04"}\nwarehouse.add("S05")\nwarehouse.remove("S01")\nall_codes = list(warehouse | incoming)\nall_codes.sort()\nboth = list(warehouse & incoming)\nboth.sort()\nprint(all_codes)\nprint(both)\nprint(f"Total: {len(all_codes)}")',
          "อัปเดต warehouse ก่อนค่อย | และ &"),
    ],
)


# ─── 031 choosing-data-types ─────────────────────────────────────────────────

write_week(
    "031-choosing-data-types",
    chapter="Choosing Types",
    emoji="🧭",
    index_md=idx(
        "บท 031 Choosing Data Types",
        "เลือกใช้ list / tuple / set ตามสถานการณ์ (ไม่เพิ่ม syntax ใหม่)",
        "ห้ามใช้ dict (บท 033) · ห้าม insert/pop/sorted/min/max",
        [
            ("02_test.md", "🟢", "รายการซื้อที่แก้ได้", "เลือก list + append"),
            ("03_test.md", "🟢", "วันในสัปดาห์คงที่", "เลือก tuple"),
            ("04_test.md", "🟢", "ผู้เข้าชมไม่ซ้ำ", "เลือก set"),
            ("08_easy.md", "🟢", "พิกัดจุดคงที่", "tuple สองค่า"),
            ("09_easy.md", "🟢", "ตัดรหัสซ้ำ", "set จาก list"),
            ("06_medium.md", "🟡", "คิวงานที่เรียงได้", "list + sort"),
            ("07_medium.md", "🟡", "เพื่อนร่วมสองกลุ่ม", "set &"),
            ("10_medium.md", "🟡", "โปรไฟล์คงที่", "tuple หลายฟิลด์"),
            ("11_medium.md", "🟡", "ตะกร้าแล้วตัดซ้ำ", "list → set"),
            ("12_medium.md", "🟡", "เมนูคงที่กับของเพิ่ม", "tuple อ่าน + list แก้"),
            ("13_medium.md", "🟡", "เช็คสมาชิกชมรม", "set + in"),
            ("05_challenge.md", "🔴", "เลือกโครงสร้างสามแบบ", "list+tuple+set คู่กัน"),
            ("14_challenge.md", "🔴", "งานบ้านกับวันคงที่", "list งาน + tuple วัน"),
            ("15_challenge.md", "🔴", "แขกงานกับรายชื่อซ้ำ", "list + set สรุป"),
            ("16_challenge.md", "🔴", "คลังผสมสามชนิด", "ครบ list/tuple/set"),
        ],
        "- ข้อ 02 ไม่ซ้ำตัวอย่าง shopping/weekdays/visitors ในบทเรียนแบบเดิม\n"
        "- เน้นการเลือกชนิดข้อมูลให้เหมาะกับงาน\n"
        "- ยังไม่มี dict",
    ),
    problems=[
        p(2, "รายการซื้อที่แก้ได้", "mutable_cart",
          "รายการซื้อต้องเพิ่มของได้ทีหลัง เลยใช้ list\n\n"
          "เริ่ม `cart = [\"Milk\", \"Bread\"]` แล้ว append `Eggs`\n\n"
          "แสดง list",
          "list หนึ่งบรรทัด", "['Milk', 'Bread', 'Eggs']",
          'cart = ["Milk", "Bread"]\n\n# เขียนโค้ดตรงนี้\n\nprint(cart)',
          'cart = ["Milk", "Bread"]\ncart.append("Eggs")\nprint(cart)'),
        p(3, "วันในสัปดาห์คงที่", "fixed_week",
          "ชื่อวันเปลี่ยนไม่ได้ ใช้ tuple\n\n"
          "กำหนด `week = (\"Mon\", \"Tue\", \"Wed\")`\n\n"
          "แสดงวันแรกและจำนวนวัน",
          "2 บรรทัด", "Mon\nDays: 3",
          'week = ("Mon", "Tue", "Wed")\n\n# เขียนโค้ดตรงนี้',
          'week = ("Mon", "Tue", "Wed")\nprint(week[0])\nprint(f"Days: {len(week)}")'),
        p(4, "ผู้เข้าชมไม่ซ้ำ", "unique_visitors",
          "นับผู้เข้าชมไม่ซ้ำด้วย set\n\n"
          "กำหนด `visitors = {\"Ann\", \"Ben\", \"Ann\", \"Cara\"}`\n\n"
          "แสดงจำนวนสมาชิกใน set",
          "บรรทัดเดียว", "Visitors: 3",
          'visitors = {"Ann", "Ben", "Ann", "Cara"}\n\n# เขียนโค้ดตรงนี้',
          'visitors = {"Ann", "Ben", "Ann", "Cara"}\nprint(f"Visitors: {len(visitors)}")'),
        p(8, "พิกัดจุดคงที่", "fixed_point",
          "พิกัดจุดบนแผนที่ไม่ควรแก้ ใช้ tuple\n\n"
          "กำหนด `point = (5, 9)` แสดง `X` และ `Y`",
          "2 บรรทัด", "X: 5\nY: 9",
          "point = (5, 9)\n\n# เขียนโค้ดตรงนี้",
          'point = (5, 9)\nprint(f"X: {point[0]}")\nprint(f"Y: {point[1]}")'),
        p(9, "ตัดรหัสซ้ำ", "dedup_codes",
          "ตัดรหัสซ้ำจาก list ด้วย set\n\n"
          "กำหนด `codes = [1, 2, 2, 3, 1, 4]`\n\n"
          "แสดง list ไม่ซ้ำแบบเรียง",
          "list หนึ่งบรรทัด", "[1, 2, 3, 4]",
          "codes = [1, 2, 2, 3, 1, 4]\n\n# เขียนโค้ดตรงนี้",
          "codes = [1, 2, 2, 3, 1, 4]\nunique = list(set(codes))\nunique.sort()\nprint(unique)"),
        p(6, "คิวงานที่เรียงได้", "sortable_jobs",
          "คิวงานต้องเรียงชื่อได้ ใช้ list\n\n"
          "กำหนด `jobs = [\"Clean\", \"Cook\", \"Buy\"]` แล้ว sort และแสดง",
          "list หนึ่งบรรทัด", "['Buy', 'Clean', 'Cook']",
          'jobs = ["Clean", "Cook", "Buy"]\n\n# เขียนโค้ดตรงนี้\n\nprint(jobs)',
          'jobs = ["Clean", "Cook", "Buy"]\njobs.sort()\nprint(jobs)',
          "list เรียงได้ด้วย .sort()"),
        p(7, "เพื่อนร่วมสองกลุ่ม", "shared_group",
          "หาเพื่อนร่วมด้วย set\n\n"
          "กำหนด `g1 = {\"Ann\", \"Ben\"}` และ `g2 = {\"Ben\", \"Cara\"}`\n\n"
          "แสดงส่วนร่วมแบบ list เรียง",
          "list หนึ่งบรรทัด", "['Ben']",
          'g1 = {"Ann", "Ben"}\ng2 = {"Ben", "Cara"}\n\n# เขียนโค้ดตรงนี้',
          'g1 = {"Ann", "Ben"}\ng2 = {"Ben", "Cara"}\nshared = list(g1 & g2)\nshared.sort()\nprint(shared)',
          "set เหมาะกับส่วนร่วม"),
        p(10, "โปรไฟล์คงที่", "fixed_profile",
          "ข้อมูลโปรไฟล์สั้นๆ ไม่ควรแก้ ใช้ tuple\n\n"
          "กำหนด `profile = (\"Ohm\", 14, \"Bangkok\")`\n\n"
          "แสดงตามตัวอย่าง",
          "3 บรรทัด", "Name: Ohm\nAge : 14\nCity: Bangkok",
          'profile = ("Ohm", 14, "Bangkok")\n\n# เขียนโค้ดตรงนี้',
          'profile = ("Ohm", 14, "Bangkok")\nprint(f"Name: {profile[0]}")\nprint(f"Age : {profile[1]}")\nprint(f"City: {profile[2]}")',
          "tuple อ่านด้วย index"),
        p(11, "ตะกร้าแล้วตัดซ้ำ", "cart_unique",
          "ตะกร้าเป็น list มีของซ้ำ อยากได้ชุดไม่ซ้ำ\n\n"
          "กำหนด `cart = [\"Pen\", \"Book\", \"Pen\", \"Glue\"]`\n\n"
          "แสดงของไม่ซ้ำแบบเรียง",
          "list หนึ่งบรรทัด", "['Book', 'Glue', 'Pen']",
          'cart = ["Pen", "Book", "Pen", "Glue"]\n\n# เขียนโค้ดตรงนี้',
          'cart = ["Pen", "Book", "Pen", "Glue"]\nunique = list(set(cart))\nunique.sort()\nprint(unique)',
          "list เก็บลำดับซื้อ set ตัดซ้ำ"),
        p(12, "เมนูคงที่กับของเพิ่ม", "menu_and_extra",
          "เมนูหลักเป็น tuple ส่วนของเพิ่มเป็น list\n\n"
          "กำหนด `menu = (\"Rice\", \"Soup\")` และ `extra = [\"Egg\"]` แล้ว append `Pork`\n\n"
          "แสดงเมนูหลักทีละบรรทัด และของเพิ่มทั้ง list",
          "3 บรรทัด", "Rice\nSoup\n['Egg', 'Pork']",
          'menu = ("Rice", "Soup")\nextra = ["Egg"]\n\n# เขียนโค้ดตรงนี้',
          'menu = ("Rice", "Soup")\nextra = ["Egg"]\nextra.append("Pork")\nfor item in menu:\n    print(item)\nprint(extra)',
          "tuple อ่านอย่างเดียว list แก้ได้"),
        p(13, "เช็คสมาชิกชมรม", "club_member",
          "เช็คสมาชิกด้วย set เพราะต้องการ in ที่เร็วและไม่ซ้ำ\n\n"
          "กำหนด `club = {\"Ann\", \"Ben\", \"Cara\"}`\n\n"
          "เช็ค `\"Dan\"` แสดง `Member` หรือ `Guest`",
          "บรรทัดเดียว", "Guest",
          'club = {"Ann", "Ben", "Cara"}\n\n# เขียนโค้ดตรงนี้',
          'club = {"Ann", "Ben", "Cara"}\nif "Dan" in club:\n    print("Member")\nelse:\n    print("Guest")',
          "set + in เหมาะกับเช็คสมาชิก"),
        p(5, "เลือกโครงสร้างสามแบบ", "three_types",
          "โปรแกรมเก็บข้อมูลสามอย่างคนละชนิด\n\n"
          "- `tasks` เป็น list ของงาน 2 อย่าง แล้ว append งานที่สาม\n"
          "- `days` เป็น tuple วันทำการ 3 วัน\n"
          "- `tags` เป็น set ของแท็ก แล้วตัดซ้ำอัตโนมัติ\n\n"
          "แสดง tasks, วันแรกของ days, และจำนวน tags",
          "3 บรรทัด",
          "['Wash', 'Cook', 'Shop']\nMon\nTags: 2",
          'tasks = ["Wash", "Cook"]\ndays = ("Mon", "Tue", "Wed")\ntags = {"home", "home", "school"}\n\n# เขียนโค้ดตรงนี้',
          'tasks = ["Wash", "Cook"]\ndays = ("Mon", "Tue", "Wed")\ntags = {"home", "home", "school"}\ntasks.append("Shop")\nprint(tasks)\nprint(days[0])\nprint(f"Tags: {len(tags)}")',
          "เลือกชนิดตามว่าแก้ได้ / คงที่ / ไม่ซ้ำ"),
        p(14, "งานบ้านกับวันคงที่", "chores_days",
          "งานบ้านเป็น list วันเป็น tuple\n\n"
          "กำหนด `chores = [\"Sweep\", \"Mop\"]` append `Dust`\n"
          "และ `days = (\"Sat\", \"Sun\")`\n\n"
          "แสดงงานพร้อมเลขที่ด้วย range(len) และแสดงทุกวันจาก tuple",
          "รายการผสม",
          "1) Sweep\n2) Mop\n3) Dust\nSat\nSun",
          'chores = ["Sweep", "Mop"]\ndays = ("Sat", "Sun")\n\n# เขียนโค้ดตรงนี้',
          'chores = ["Sweep", "Mop"]\ndays = ("Sat", "Sun")\nchores.append("Dust")\nfor i in range(len(chores)):\n    print(f"{i + 1}) {chores[i]}")\nfor day in days:\n    print(day)',
          "list แก้ได้ tuple วนอย่างเดียว"),
        p(15, "แขกงานกับรายชื่อซ้ำ", "party_guests",
          "รายชื่อแขกเป็น list มีซ้ำ อยากสรุปด้วย set\n\n"
          "กำหนด `guests = [\"Ann\", \"Ben\", \"Ann\", \"Cara\", \"Ben\", \"Dan\"]`\n\n"
          "แสดงจำนวนชื่อใน list และจำนวนไม่ซ้ำ",
          "2 บรรทัด", "Listed : 6\nUnique : 4",
          'guests = ["Ann", "Ben", "Ann", "Cara", "Ben", "Dan"]\n\n# เขียนโค้ดตรงนี้',
          'guests = ["Ann", "Ben", "Ann", "Cara", "Ben", "Dan"]\nprint(f"Listed : {len(guests)}")\nprint(f"Unique : {len(set(guests))}")',
          "list นับทั้งหมด set นับไม่ซ้ำ"),
        p(16, "คลังผสมสามชนิด", "mixed_warehouse",
          "คลังใช้สามชนิดข้อมูลร่วมกัน\n\n"
          "- `stock` list เริ่ม `[\"Rice\", \"Oil\"]` append `Salt` แล้ว sort\n"
          "- `location` tuple `(\"Zone\", \"A\")`\n"
          "- `codes` set จาก `[101, 102, 101, 103]`\n\n"
          "แสดง stock, รหัสโซน (ค่าท้ายของ location), และรหัสไม่ซ้ำเรียง",
          "3 บรรทัด",
          "['Oil', 'Rice', 'Salt']\nA\n[101, 102, 103]",
          'stock = ["Rice", "Oil"]\nlocation = ("Zone", "A")\nraw_codes = [101, 102, 101, 103]\n\n# เขียนโค้ดตรงนี้',
          'stock = ["Rice", "Oil"]\nlocation = ("Zone", "A")\nraw_codes = [101, 102, 101, 103]\nstock.append("Salt")\nstock.sort()\ncodes = list(set(raw_codes))\ncodes.sort()\nprint(stock)\nprint(location[-1])\nprint(codes)',
          "ใช้คนละชนิดตามหน้าที่"),
    ],
)


# ─── 032 collection-review ───────────────────────────────────────────────────

write_week(
    "032-collection-review",
    chapter="Collection Review",
    emoji="📚",
    index_md=idx(
        "บท 032 Collection Review",
        "ทบทวน list / tuple / set ควบคู่กัน (ไม่มี syntax ใหม่)",
        "ห้าม dict (บท 033) · ห้าม insert/pop/sorted/min/max",
        [
            ("02_test.md", "🟢", "อ่าน list กับ tuple", "index คู่กัน"),
            ("03_test.md", "🟢", "ตัดซ้ำจากรายชื่อ", "list → set"),
            ("04_test.md", "🟢", "เช็คสมาชิก set", "in"),
            ("08_easy.md", "🟢", "เพิ่มงานใน list", "append"),
            ("09_easy.md", "🟢", "วนพิมพ์ tuple", "for ใน tuple"),
            ("06_medium.md", "🟡", "สหภาพสองชมรม", "|"),
            ("07_medium.md", "🟡", "ค่าเฉลี่ยจาก list", "รวม / len"),
            ("10_medium.md", "🟡", "โปรไฟล์ tuple สั้น", "หลายฟิลด์"),
            ("11_medium.md", "🟡", "กรองคะแนนแล้วตัดซ้ำ", "filter + set"),
            ("12_medium.md", "🟡", "คิว list กับวัน tuple", "สองชนิดร่วม"),
            ("13_medium.md", "🟡", "ส่วนร่วมรายวิชา", "&"),
            ("05_challenge.md", "🔴", "สรุปสามชนิดข้อมูล", "list+tuple+set"),
            ("14_challenge.md", "🔴", "รายงานผลสอบทบทวน", "list skills"),
            ("15_challenge.md", "🔴", "งานอีเวนต์ผสม", "list/set/tuple"),
            ("16_challenge.md", "🔴", "กล่องสรุปคอลเลกชัน", "ครบชุดทบทวน"),
        ],
        "- ข้อ 02 ไม่ซ้ำตัวอย่าง students/days ในบทเรียนแบบเดิม\n"
        "- ทบทวนความต่าง mutable / immutable / unique\n"
        "- ยังไม่มี dictionary",
    ),
    problems=[
        p(2, "อ่าน list กับ tuple", "list_tuple_read",
          "อ่านค่าแรกจาก list และค่าท้ายจาก tuple\n\n"
          "กำหนด `names = [\"Ann\", \"Ben\", \"Cara\"]` และ `codes = (101, 102, 103)`\n\n"
          "แสดงตามตัวอย่าง",
          "2 บรรทัด", "Ann\n103",
          'names = ["Ann", "Ben", "Cara"]\ncodes = (101, 102, 103)\n\n# เขียนโค้ดตรงนี้',
          'names = ["Ann", "Ben", "Cara"]\ncodes = (101, 102, 103)\nprint(names[0])\nprint(codes[-1])'),
        p(3, "ตัดซ้ำจากรายชื่อ", "review_dedup",
          "ตัดชื่อซ้ำจาก list\n\n"
          "กำหนด `names = [\"Ed\", \"Ann\", \"Ed\", \"Ben\"]`\n\n"
          "แสดงไม่ซ้ำแบบเรียง",
          "list หนึ่งบรรทัด", "['Ann', 'Ben', 'Ed']",
          'names = ["Ed", "Ann", "Ed", "Ben"]\n\n# เขียนโค้ดตรงนี้',
          'names = ["Ed", "Ann", "Ed", "Ben"]\nunique = list(set(names))\nunique.sort()\nprint(unique)'),
        p(4, "เช็คสมาชิก set", "set_member",
          "เช็คว่ามีแท็กนี้หรือไม่\n\n"
          "กำหนด `tags = {\"food\", \"travel\", \"sport\"}`\n\n"
          "เช็ค `\"music\"` แสดง `Yes` หรือ `No`",
          "บรรทัดเดียว", "No",
          'tags = {"food", "travel", "sport"}\n\n# เขียนโค้ดตรงนี้',
          'tags = {"food", "travel", "sport"}\nif "music" in tags:\n    print("Yes")\nelse:\n    print("No")'),
        p(8, "เพิ่มงานใน list", "add_task",
          "เพิ่มงานใหม่เข้า list\n\n"
          "กำหนด `tasks = [\"Read\", \"Write\"]` append `Review` แล้วแสดง",
          "list หนึ่งบรรทัด", "['Read', 'Write', 'Review']",
          'tasks = ["Read", "Write"]\n\n# เขียนโค้ดตรงนี้\n\nprint(tasks)',
          'tasks = ["Read", "Write"]\ntasks.append("Review")\nprint(tasks)'),
        p(9, "วนพิมพ์ tuple", "loop_tuple",
          "วนพิมพ์สถานีรถไฟจาก tuple\n\n"
          "กำหนด `stops = (\"A\", \"B\", \"C\")`",
          "3 บรรทัด", "A\nB\nC",
          'stops = ("A", "B", "C")\n\n# เขียนโค้ดตรงนี้',
          'stops = ("A", "B", "C")\nfor stop in stops:\n    print(stop)'),
        p(6, "สหภาพสองชมรม", "club_union",
          "รวมสมาชิกสองชมรม\n\n"
          "กำหนด `art = {\"Ann\", \"Ben\"}` และ `music = {\"Ben\", \"Cara\"}`\n\n"
          "แสดงสหภาพเรียงชื่อ",
          "list หนึ่งบรรทัด", "['Ann', 'Ben', 'Cara']",
          'art = {"Ann", "Ben"}\nmusic = {"Ben", "Cara"}\n\n# เขียนโค้ดตรงนี้',
          'art = {"Ann", "Ben"}\nmusic = {"Ben", "Cara"}\nall_members = list(art | music)\nall_members.sort()\nprint(all_members)',
          "| รวมสมาชิกไม่ซ้ำ"),
        p(7, "ค่าเฉลี่ยจาก list", "list_average",
          "หาค่าเฉลี่ยคะแนน\n\n"
          "กำหนด `scores = [70, 80, 90]`\n\n"
          "แสดง `Average: 80.0`",
          "บรรทัดเดียว", "Average: 80.0",
          "scores = [70, 80, 90]\n\n# เขียนโค้ดตรงนี้",
          'scores = [70, 80, 90]\ntotal = 0\nfor score in scores:\n    total += score\nprint(f"Average: {total / len(scores):.1f}")',
          "รวมแล้วหาร len"),
        p(10, "โปรไฟล์ tuple สั้น", "tuple_profile",
          "พิมพ์โปรไฟล์จาก tuple\n\n"
          "กำหนด `user = (\"Pim\", 15, \"M3\")`",
          "3 บรรทัด", "Pim\n15\nM3",
          'user = ("Pim", 15, "M3")\n\n# เขียนโค้ดตรงนี้',
          'user = ("Pim", 15, "M3")\nprint(user[0])\nprint(user[1])\nprint(user[2])',
          "อ่านทีละตำแหน่ง"),
        p(11, "กรองคะแนนแล้วตัดซ้ำ", "filter_dedup",
          "กรองคะแนน >= 50 แล้วตัดค่าซ้ำ\n\n"
          "กำหนด `scores = [40, 70, 70, 90, 40, 55]`\n\n"
          "แสดงค่าที่ผ่านแบบไม่ซ้ำเรียง",
          "list หนึ่งบรรทัด", "[55, 70, 90]",
          "scores = [40, 70, 70, 90, 40, 55]\n\n# เขียนโค้ดตรงนี้",
          "scores = [40, 70, 70, 90, 40, 55]\npassed = []\nfor score in scores:\n    if score >= 50:\n        passed.append(score)\nunique = list(set(passed))\nunique.sort()\nprint(unique)",
          "กรองด้วย list ก่อน แล้วค่อย set"),
        p(12, "คิว list กับวัน tuple", "queue_day",
          "คิวเป็น list วันเปิดเป็น tuple\n\n"
          "กำหนด `queue = [\"A1\", \"A2\"]` append `A3`\n"
          "และ `open_days = (\"Mon\", \"Wed\", \"Fri\")`\n\n"
          "แสดงคิวและวันเปิดวันแรก",
          "2 บรรทัด", "['A1', 'A2', 'A3']\nMon",
          'queue = ["A1", "A2"]\nopen_days = ("Mon", "Wed", "Fri")\n\n# เขียนโค้ดตรงนี้',
          'queue = ["A1", "A2"]\nopen_days = ("Mon", "Wed", "Fri")\nqueue.append("A3")\nprint(queue)\nprint(open_days[0])',
          "list แก้ได้ tuple คงที่"),
        p(13, "ส่วนร่วมรายวิชา", "subject_and",
          "หารายวิชาร่วมกัน\n\n"
          "กำหนด `a = {\"Math\", \"PE\", \"Art\"}` และ `b = {\"PE\", \"Thai\", \"Art\"}`\n\n"
          "แสดงส่วนร่วมเรียง",
          "list หนึ่งบรรทัด", "['Art', 'PE']",
          'a = {"Math", "PE", "Art"}\nb = {"PE", "Thai", "Art"}\n\n# เขียนโค้ดตรงนี้',
          'a = {"Math", "PE", "Art"}\nb = {"PE", "Thai", "Art"}\nshared = list(a & b)\nshared.sort()\nprint(shared)',
          "& คือส่วนร่วม"),
        p(5, "สรุปสามชนิดข้อมูล", "three_summary",
          "สรุปข้อมูลสามชนิดในโปรแกรมเดียว\n\n"
          "กำหนด `scores = [80, 70, 90]` , `info = (\"M2\", 30)` , `clubs = {\"Art\", \"Music\", \"Art\"}`\n\n"
          "แสดงผลรวมคะแนน ชื่อชั้นจาก info และจำนวนชมรมไม่ซ้ำ",
          "3 บรรทัด", "Total : 240\nClass : M2\nClubs : 2",
          'scores = [80, 70, 90]\ninfo = ("M2", 30)\nclubs = {"Art", "Music", "Art"}\n\n# เขียนโค้ดตรงนี้',
          'scores = [80, 70, 90]\ninfo = ("M2", 30)\nclubs = {"Art", "Music", "Art"}\ntotal = 0\nfor score in scores:\n    total += score\nprint(f"Total : {total}")\nprint(f"Class : {info[0]}")\nprint(f"Clubs : {len(clubs)}")',
          "ใช้คนละชนิดตามหน้าที่"),
        p(14, "รายงานผลสอบทบทวน", "exam_collection",
          "รายงานผลสอบจาก list คะแนน\n\n"
          "กำหนด `scores = [45, 80, 60, 30]`\n\n"
          "พิมพ์ Pass/Fail ทีละคน (>=50) แล้วแสดงจำนวนผ่าน",
          "รายงาน + สรุป",
          "Fail\nPass\nPass\nFail\nPassed: 2",
          "scores = [45, 80, 60, 30]\n\n# เขียนโค้ดตรงนี้",
          'scores = [45, 80, 60, 30]\npassed = 0\nfor score in scores:\n    if score >= 50:\n        print("Pass")\n        passed += 1\n    else:\n        print("Fail")\nprint(f"Passed: {passed}")',
          "ทบทวน if ใน loop กับ list"),
        p(15, "งานอีเวนต์ผสม", "event_mix",
          "งานอีเวนต์ใช้หลายชนิดข้อมูล\n\n"
          "กำหนด `staff = [\"Ann\", \"Ben\"]` append `Cara`\n"
          "`rooms = (\"Hall\", \"Garden\")`\n"
          "`guests = [\"Ed\", \"Ann\", \"Ed\", \"Ben\"]`\n\n"
          "แสดง staff, ห้องแรก, และแขกไม่ซ้ำเรียง",
          "3 บรรทัด",
          "['Ann', 'Ben', 'Cara']\nHall\n['Ann', 'Ben', 'Ed']",
          'staff = ["Ann", "Ben"]\nrooms = ("Hall", "Garden")\nguests = ["Ed", "Ann", "Ed", "Ben"]\n\n# เขียนโค้ดตรงนี้',
          'staff = ["Ann", "Ben"]\nrooms = ("Hall", "Garden")\nguests = ["Ed", "Ann", "Ed", "Ben"]\nstaff.append("Cara")\nunique_guests = list(set(guests))\nunique_guests.sort()\nprint(staff)\nprint(rooms[0])\nprint(unique_guests)',
          "list แก้ / tuple คงที่ / set ตัดซ้ำ"),
        p(16, "กล่องสรุปคอลเลกชัน", "collection_box",
          "สรุปคอลเลกชันสามชนิดแบบมีกรอบ\n\n"
          "กำหนด `nums = [5, 2, 9]` sort แล้ว\n"
          "`point = (3, 4)`\n"
          "`labels = {\"A\", \"B\", \"A\"}`\n\n"
          "แสดงตามตัวอย่าง",
          "กล่องสรุป",
          "====================\nList : [2, 5, 9]\nTuple: (3, 4)\nSet  : 2\n====================",
          "nums = [5, 2, 9]\npoint = (3, 4)\nlabels = {\"A\", \"B\", \"A\"}\n\n# เขียนโค้ดตรงนี้",
          'nums = [5, 2, 9]\npoint = (3, 4)\nlabels = {"A", "B", "A"}\nnums.sort()\nprint("====================")\nprint(f"List : {nums}")\nprint(f"Tuple: ({point[0]}, {point[1]})")\nprint(f"Set  : {len(labels)}")\nprint("====================")',
          "แสดงตัวแทนของทั้งสามชนิด"),
    ],
)

print("done 029-032")
