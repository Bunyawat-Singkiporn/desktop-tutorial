#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from _gen_lib import emit

def gen_029():
    probs = [
    dict(file="02_test.md", answer="02_city_info.py", diff="🟢 Easy",
         name="ข้อมูลเมืองอ่านอย่างเดียว", axis="tuple index",
         title="🏙️ Tuples — ข้อ 1: ข้อมูลเมือง",
         scenario='ข้อมูลเมืองเก็บเป็น tuple\n\n```python\ncity = ("Chiang Mai", "North", 120)\n```\n\nแสดงชื่อเมืองและภูมิภาค คนละบรรทัด',
         conditions=None, inp="ไม่มี input", out="2 บรรทัด ชื่อและภูมิภาค",
         hint="ใช้ `city[0]` และ `city[1]`",
         starter='city = ("Chiang Mai", "North", 120)\n\n# เขียนโค้ดตรงนี้',
         code='city = ("Chiang Mai", "North", 120)\nprint(city[0])\nprint(city[1])'),
    dict(file="03_test.md", answer="03_weekend.py", diff="🟢 Easy",
         name="วันหยุดสุดสัปดาห์", axis="negative index บน tuple",
         title="📅 Tuples — ข้อ 2: วันหยุดสุดสัปดาห์",
         scenario='```python\ndays = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")\n```\n\nแสดงสองวันสุดท้ายของสัปดาห์ คนละบรรทัด',
         conditions=None, inp="ไม่มี input", out="2 บรรทัด Sat และ Sun",
         hint="ใช้ `[-2]` และ `[-1]`",
         starter='days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")\n\n# เขียนโค้ดตรงนี้',
         code='days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")\nprint(days[-2])\nprint(days[-1])'),
    dict(file="04_test.md", answer="04_rgb.py", diff="🟢 Easy",
         name="ค่าสี RGB", axis="len + index",
         title="🎨 Tuples — ข้อ 3: ค่าสี RGB",
         scenario="```python\nrgb = (255, 128, 0)\n```\n\nแสดงจำนวนช่องสี และค่า Red (ช่องแรก)",
         conditions=None, inp="ไม่มี input", out="2 บรรทัด Channels / Red",
         hint="`len(rgb)` และ `rgb[0]`",
         starter="rgb = (255, 128, 0)\n\n# เขียนโค้ดตรงนี้",
         code='rgb = (255, 128, 0)\nprint(f"Channels: {len(rgb)}")\nprint(f"Red: {rgb[0]}")'),
    dict(file="05_easy.md", answer="05_print_levels.py", diff="🟢 Easy",
         name="พิมพ์ด่านเกม", axis="for ใน tuple",
         title="🕹️ Tuples — ข้อ 4: พิมพ์ด่านเกม",
         scenario='```python\nlevels = ("Tutorial", "Forest", "Castle", "Boss")\n```\n\nพิมพ์ชื่อด่านทุกด่าน คนละบรรทัด',
         conditions=None, inp="ไม่มี input", out="ชื่อด่านทีละบรรทัด",
         hint="`for level in levels:`",
         starter='levels = ("Tutorial", "Forest", "Castle", "Boss")\n\n# เขียนโค้ดตรงนี้',
         code='levels = ("Tutorial", "Forest", "Castle", "Boss")\nfor level in levels:\n    print(level)'),
    dict(file="06_easy.md", answer="06_ lat_long.py", diff="🟢 Easy",
         name="พิกัดร้านกาแฟ", axis="อ่าน tuple สองค่า",
         title="📍 Tuples — ข้อ 5: พิกัดร้านกาแฟ",
         scenario="```python\npoint = (13.75, 100.50)\n```\n\nแสดง `Lat: ...` และ `Lng: ...`",
         conditions=None, inp="ไม่มี input", out="2 บรรทัดพิกัด",
         hint="อย่า unpack — ใช้ index ทีละช่อง",
         starter="point = (13.75, 100.50)\n\n# เขียนโค้ดตรงนี้",
         code='point = (13.75, 100.50)\nprint(f"Lat: {point[0]}")\nprint(f"Lng: {point[1]}")'),
    ]
    # fix filename typo
    probs[4]["answer"] = "06_lat_long.py"
    probs += [
    dict(file="07_medium.md", answer="07_student_card.py", diff="🟡 Medium",
         name="บัตรนักเรียนจาก tuple", axis="พิมพ์ป้ายจากหลาย index",
         title="🎓 Tuples — ข้อ 6: บัตรนักเรียน",
         scenario='```python\nstudent = ("Mali", 14, "Grade 8")\n```\n\nแสดง Name / Age / Grade คนละบรรทัด',
         conditions=None, inp="ไม่มี input", out="3 บรรทัดข้อมูลนักเรียน",
         hint="เข้าถึง `[0]` `[1]` `[2]` แยกกัน — ห้าม unpack",
         starter='student = ("Mali", 14, "Grade 8")\n\n# เขียนโค้ดตรงนี้',
         code='''student = ("Mali", 14, "Grade 8")
print(f"Name: {student[0]}")
print(f"Age: {student[1]}")
print(f"Grade: {student[2]}")'''),
    dict(file="08_medium.md", answer="08_flight.py", diff="🟡 Medium",
         name="ข้อมูลเที่ยวบิน", axis="first/last + len",
         title="✈️ Tuples — ข้อ 7: ข้อมูลเที่ยวบิน",
         scenario='```python\nflight = ("BKK", "CNX", "PG210", 75)\n```\n\nแสดงต้นทาง ปลายทาง และจำนวนฟิลด์',
         conditions=None, inp="ไม่มี input", out="3 บรรทัด From / To / Fields",
         hint="ต้นทางคือตัวแรก ปลายทางคือตัวถัดไป",
         starter='flight = ("BKK", "CNX", "PG210", 75)\n\n# เขียนโค้ดตรงนี้',
         code='''flight = ("BKK", "CNX", "PG210", 75)
print(f"From: {flight[0]}")
print(f"To: {flight[1]}")
print(f"Fields: {len(flight)}")'''),
    dict(file="09_medium.md", answer="09_labeled_days.py", diff="🟡 Medium",
         name="วันทำการมีหมายเลข", axis="tuple + range(len)",
         title="🗓️ Tuples — ข้อ 8: วันทำการมีหมายเลข",
         scenario='```python\nworkdays = ("Mon", "Tue", "Wed", "Thu", "Fri")\n```\n\nพิมพ์ `1. Mon` แบบมีหมายเลข',
         conditions=None, inp="ไม่มี input", out="วันทำการมีหมายเลข",
         hint="tuple วนด้วย `range(len(...))` ได้เหมือน list",
         starter='workdays = ("Mon", "Tue", "Wed", "Thu", "Fri")\n\n# เขียนโค้ดตรงนี้',
         code='''workdays = ("Mon", "Tue", "Wed", "Thu", "Fri")
for i in range(len(workdays)):
    print(f"{i + 1}. {workdays[i]}")'''),
    dict(file="10_medium.md", answer="10_match_score.py", diff="🟡 Medium",
         name="ผลสกอร์แมตช์", axis="เทียบค่าใน tuple",
         title="⚽ Tuples — ข้อ 9: ผลสกอร์แมตช์",
         scenario="```python\nscore = (2, 1)\n```\n\nเทียบประตูทีมเหย้า `[0]` กับทีมเยือน `[1]`",
         conditions=["ถ้าเหย้ามากกว่า → `Home Win`", "ถ้าไม่ใช่ → `Home Not Win`"],
         inp="ไม่มี input", out="ข้อความผลแมตช์ 1 บรรทัด",
         hint="อ่านสองช่องมาเทียบด้วย if/else",
         starter="score = (2, 1)\n\n# เขียนโค้ดตรงนี้",
         code='''score = (2, 1)
if score[0] > score[1]:
    print("Home Win")
else:
    print("Home Not Win")'''),
    dict(file="11_medium.md", answer="11_product_tuple.py", diff="🟡 Medium",
         name="ราคาสินค้าคงที่", axis="คำนวณจากฟิลด์ tuple",
         title="🛍️ Tuples — ข้อ 10: ราคาสินค้าคงที่",
         scenario='```python\nproduct = ("USB Cable", 79, 3)\n```\n\nชื่ออยู่ช่อง 0 ราคาช่อง 1 จำนวนช่อง 2 — คำนวณยอด `ราคา * จำนวน` แสดงชื่อและยอด',
         conditions=None, inp="ไม่มี input", out="2 บรรทัด Item / Total",
         hint="คูณ `product[1] * product[2]`",
         starter='product = ("USB Cable", 79, 3)\n\n# เขียนโค้ดตรงนี้',
         code='''product = ("USB Cable", 79, 3)
print(f"Item: {product[0]}")
print(f"Total: {product[1] * product[2]}")'''),
    dict(file="12_medium.md", answer="12_time_parts.py", diff="🟡 Medium",
         name="แยกชั่วโมงนาทีวินาที", axis="อ่านสามช่อง + จัดรูปแบบ",
         title="⏰ Tuples — ข้อ 11: แยกเวลา",
         scenario="```python\ntime = (9, 5, 30)\n```\n\nแสดงเวลาในรูป `09:05:30` โดยแปะ 0 นำหน้าถ้าค่าน้อยกว่า 10",
         conditions=None, inp="ไม่มี input", out="เวลา 1 บรรทัด",
         hint="ใช้ f-string จัดรูปแบบ `{value:02d}` หรือต่อเงื่อนไขเอง — ที่นี่ใช้ `:02d` ได้จากความรู้ format ที่มีในหลักสูตรหรือพิมพ์เองแบบง่าย",
         starter="time = (9, 5, 30)\n\n# เขียนโค้ดตรงนี้",
         code='''time = (9, 5, 30)
h = time[0]
m = time[1]
s = time[2]
print(f"{h:02d}:{m:02d}:{s:02d}")'''),
    dict(file="13_challenge.md", answer="13_itinerary.py", diff="🔴 Challenge",
         name="แผนเที่ยวอ่านอย่างเดียว", axis="หลาย tuple + สรุป",
         title="🧳 Tuples — ข้อ 12: แผนเที่ยว",
         scenario='```python\nday1 = ("Ayutthaya", 2)\nday2 = ("Pattaya", 3)\nday3 = ("Hua Hin", 2)\n```\n\nพิมพ์แผนแต่ละวันเป็น `Day N: <ที่> (<คืน> nights)` แล้วนับรวมจำนวนคืน',
         conditions=None, inp="ไม่มี input", out="3 บรรทัดแผน + Total nights",
         hint="สร้าง list ของ tuple หรือพิมพ์ทีละวันก็ได้ แล้วบวกคืนรวม",
         starter='day1 = ("Ayutthaya", 2)\nday2 = ("Pattaya", 3)\nday3 = ("Hua Hin", 2)\n\n# เขียนโค้ดตรงนี้',
         code='''day1 = ("Ayutthaya", 2)
day2 = ("Pattaya", 3)
day3 = ("Hua Hin", 2)

print(f"Day 1: {day1[0]} ({day1[1]} nights)")
print(f"Day 2: {day2[0]} ({day2[1]} nights)")
print(f"Day 3: {day3[0]} ({day3[1]} nights)")
print(f"Total nights: {day1[1] + day2[1] + day3[1]}")'''),
    dict(file="14_challenge.md", answer="14_team_roster.py", diff="🔴 Challenge",
         name="รายชื่อทีมคงที่", axis="tuple ของชื่อ + วนสรุป",
         title="🏀 Tuples — ข้อ 13: รายชื่อทีม",
         scenario='```python\nteam = ("Amy", "Ben", "Cara", "Dan", "Eve")\n```\n\nพิมพ์รายชื่อมีหมายเลข แสดงจำนวนสมาชิก และชื่อกัปตัน (ตัวแรก) กับตัวสำรองคนสุดท้าย',
         conditions=None, inp="ไม่มี input", out="รายชื่อมีหมายเลข ตามด้วย Count/Captain/Bench",
         hint="ใช้ range(len) สำหรับหมายเลข แล้วอ่าน `[0]` / `[-1]`",
         starter='team = ("Amy", "Ben", "Cara", "Dan", "Eve")\n\n# เขียนโค้ดตรงนี้',
         code='''team = ("Amy", "Ben", "Cara", "Dan", "Eve")
for i in range(len(team)):
    print(f"{i + 1}. {team[i]}")
print(f"Count: {len(team)}")
print(f"Captain: {team[0]}")
print(f"Bench: {team[-1]}")'''),
    dict(file="15_challenge.md", answer="15_receipt_lines.py", diff="🔴 Challenge",
         name="ใบเสร็จจาก tuple คงที่", axis="tuple ของราคา + รวม + กรอบ",
         title="🧾 Tuples — ข้อ 14: ใบเสร็จคงที่",
         scenario='ราคาในออเดอร์ล็อกแล้ว\n\n```python\nprices = (49, 79, 29, 99)\n```\n\nพิมพ์แต่ละราคาแบบมีหมายเลข รวมยอด แสดงกรอบสรุปจำนวนรายการและยอด',
         conditions=None, inp="ไม่มี input", out="รายการมีหมายเลข + กล่องสรุป",
         hint="tuple วนได้เหมือน list แต่แก้ค่าไม่ได้",
         starter="prices = (49, 79, 29, 99)\n\n# เขียนโค้ดตรงนี้",
         code='''prices = (49, 79, 29, 99)
for i in range(len(prices)):
    print(f"{i + 1}. {prices[i]}")

total = 0
for price in prices:
    total += price

print("========================")
print(f"Items      : {len(prices)}")
print(f"Total      : {total}")
print("========================")'''),
    dict(file="16_challenge.md", answer="16_exam_slot.py", diff="🔴 Challenge",
         name="ตารางสอบอ่านอย่างเดียว", axis="เทียบเวลา + แสดงรายละเอียด",
         title="📌 Tuples — ข้อ 15: ตารางสอบ",
         scenario='```python\nexam = ("Math", 9, 11)\n```\n\nวิชาช่อง 0 เริ่มช่อง 1 จบช่อง 2 — คำนวณชั่วโมงที่ใช้ ถ้ามากกว่า 2 ชม. สถานะ `Long` ไม่งั้น `Normal` แสดงกรอบสรุป',
         conditions=None, inp="ไม่มี input", out="กล่องสรุปตารางสอบ",
         hint="ชั่วโมง = จบ - เริ่ม แล้วค่อยตัดสินสถานะ",
         starter='exam = ("Math", 9, 11)\n\n# เขียนโค้ดตรงนี้',
         code='''exam = ("Math", 9, 11)
hours = exam[2] - exam[1]
if hours > 2:
    status = "Long"
else:
    status = "Normal"

print("========================")
print("       EXAM SLOT")
print("========================")
print(f"Subject    : {exam[0]}")
print(f"Start      : {exam[1]}")
print(f"End        : {exam[2]}")
print(f"Hours      : {hours}")
print(f"Status     : {status}")
print("========================")'''),
    ]
    emit("029-tuples", probs, "บท 029 Tuples",
         ["tuple literal `(...)`", "indexing / negative index", "`len(tuple)`", "`for x in tuple:`", "อ่านอย่างเดียว"],
         ["ห้าม tuple unpacking (`a, b = point`)", "ห้ามแก้ค่าใน tuple"],
         ["ข้อ `02` ไม่ซ้ำตัวอย่างนักเรียน Bob / days Mon-Fri จากบทเรียนตรงๆ",
          "เน้นว่า tuple เหมาะกับข้อมูลคงที่"])


def gen_030():
    # For set outputs: never print(set) — use membership / ordered candidate loops
    probs = [
    dict(file="02_test.md", answer="02_has_member.py", diff="🟢 Easy",
         name="เช็คสมาชิกในคลับ", axis="in กับ set",
         title="🎯 Sets — ข้อ 1: เช็คสมาชิกในคลับ",
         scenario='```python\nclub = {"Ann", "Ben", "Cara"}\n```\n\nตรวจว่า `"Ben"` อยู่ในคลับหรือไม่ แสดง `True` หรือ `False`',
         conditions=None, inp="ไม่มี input", out="True หรือ False 1 บรรทัด",
         hint='พิมพ์ผลของ `"Ben" in club` โดยตรง',
         starter='club = {"Ann", "Ben", "Cara"}\n\n# เขียนโค้ดตรงนี้',
         code='club = {"Ann", "Ben", "Cara"}\nprint("Ben" in club)'),
    dict(file="03_test.md", answer="03_dedup_tags.py", diff="🟢 Easy",
         name="ตัดแท็กซ้ำ", axis="set(list)",
         title="🏷️ Sets — ข้อ 2: ตัดแท็กซ้ำ",
         scenario='```python\ntags = ["food", "travel", "food", "cat", "travel"]\n```\n\nแปลงเป็น set แล้วตรวจทีละแท็กในลำดับ `food` / `travel` / `cat` / `dog` ว่ามีหรือไม่ พิมพ์ `tag: True/False`',
         conditions=None, inp="ไม่มี input", out="4 บรรทัดผลการมีอยู่ของแต่ละแท็ก",
         hint="ใช้ `set(tags)` แล้วเช็ค `in` ตามลำดับที่กำหนด เพื่อไม่พึ่งลำดับของ set",
         starter='tags = ["food", "travel", "food", "cat", "travel"]\n\n# เขียนโค้ดตรงนี้',
         code='''tags = ["food", "travel", "food", "cat", "travel"]
unique = set(tags)
for tag in ["food", "travel", "cat", "dog"]:
    print(f"{tag}: {tag in unique}")'''),
    dict(file="04_test.md", answer="04_add_guest.py", diff="🟢 Easy",
         name="เพิ่มแขกลงชุดชื่อ", axis=".add()",
         title="➕ Sets — ข้อ 3: เพิ่มแขก",
         scenario='```python\nguests = {"Ann", "Ben"}\n```\n\nเพิ่ม `"Cara"` แล้วเช็คว่ามี Cara และ Dan หรือไม่',
         conditions=None, inp="ไม่มี input", out="2 บรรทัด True/False",
         hint="`.add` ก่อน แล้วพิมพ์ผล `in`",
         starter='guests = {"Ann", "Ben"}\n\n# เขียนโค้ดตรงนี้',
         code='''guests = {"Ann", "Ben"}
guests.add("Cara")
print("Cara" in guests)
print("Dan" in guests)'''),
    dict(file="05_easy.md", answer="05_remove_player.py", diff="🟢 Easy",
         name="ลบผู้เล่นออกจากล็อบบี้", axis=".remove()",
         title="🎮 Sets — ข้อ 4: ลบผู้เล่น",
         scenario='```python\nlobby = {"Ash", "Brook", "Cody"}\n```\n\nลบ `"Brook"` แล้วเช็ค Ash / Brook',
         conditions=None, inp="ไม่มี input", out="2 บรรทัด True/False",
         hint="`.remove` แล้วใช้ `in`",
         starter='lobby = {"Ash", "Brook", "Cody"}\n\n# เขียนโค้ดตรงนี้',
         code='''lobby = {"Ash", "Brook", "Cody"}
lobby.remove("Brook")
print("Ash" in lobby)
print("Brook" in lobby)'''),
    dict(file="06_easy.md", answer="06_union_check.py", diff="🟢 Easy",
         name="รวมสองกลุ่มชมรม", axis="union |",
         title="🤝 Sets — ข้อ 5: รวมสองกลุ่มชมรม",
         scenario='```python\nart = {"Ann", "Ben", "Cara"}\nmusic = {"Ben", "Dan"}\n```\n\nหาสมาชิกรวมด้วย `|` แล้วเช็คทีละชื่อ Ann/Ben/Cara/Dan/Eve',
         conditions=None, inp="ไม่มี input", out="5 บรรทัดผลการเป็นสมาชิก",
         hint="`all_members = art | music`",
         starter='art = {"Ann", "Ben", "Cara"}\nmusic = {"Ben", "Dan"}\n\n# เขียนโค้ดตรงนี้',
         code='''art = {"Ann", "Ben", "Cara"}
music = {"Ben", "Dan"}
all_members = art | music
for name in ["Ann", "Ben", "Cara", "Dan", "Eve"]:
    print(f"{name}: {name in all_members}")'''),
    dict(file="07_medium.md", answer="07_common_skills.py", diff="🟡 Medium",
         name="สกิลร่วมของสองคน", axis="intersection &",
         title="🧩 Sets — ข้อ 6: สกิลร่วม",
         scenario='```python\nalice = {"python", "html", "css"}\nbob = {"python", "java", "css"}\n```\n\nหาสกิลร่วมด้วย `&` แล้วเช็ค python/html/css/java',
         conditions=None, inp="ไม่มี input", out="4 บรรทัด",
         hint="`shared = alice & bob`",
         starter='alice = {"python", "html", "css"}\nbob = {"python", "java", "css"}\n\n# เขียนโค้ดตรงนี้',
         code='''alice = {"python", "html", "css"}
bob = {"python", "java", "css"}
shared = alice & bob
for skill in ["python", "html", "css", "java"]:
    print(f"{skill}: {skill in shared}")'''),
    dict(file="08_medium.md", answer="08_rsvp.py", diff="🟡 Medium",
         name="ระบบ RSVP", axis="add + in + ข้อความ",
         title="🎉 Sets — ข้อ 7: ระบบ RSVP",
         scenario='```python\nrsvp = {"Ann", "Ben"}\n```\n\nเพิ่ม `"Cara"` รับชื่อจาก input หนึ่งบรรทัด ถ้าอยู่ใน rsvp แสดง `Registered` ไม่งั้น `Walk-in`',
         conditions=None, inp="ชื่อ 1 บรรทัด", out="สถานะ 1 บรรทัด",
         stdin="Ben\n",
         hint="เพิ่ม Cara ก่อน แล้วค่อยเช็คชื่อที่รับมา",
         starter='rsvp = {"Ann", "Ben"}\nname = input()\n\n# เขียนโค้ดตรงนี้',
         code='''rsvp = {"Ann", "Ben"}
rsvp.add("Cara")
name = input()
if name in rsvp:
    print("Registered")
else:
    print("Walk-in")'''),
    dict(file="09_medium.md", answer="09_unique_orders.py", diff="🟡 Medium",
         name="นับเมนูไม่ซ้ำ", axis="set(list) + วนเช็ค",
         title="🍜 Sets — ข้อ 8: นับเมนูไม่ซ้ำ",
         scenario='```python\norders = ["pad thai", "rice", "pad thai", "soup", "rice"]\n```\n\nแปลงเป็น set แล้วตรวจเมนูในลำดับ pad thai/rice/soup/salad พร้อมนับว่ามีกี่เมนูที่พบ (True)',
         conditions=None, inp="ไม่มี input", out="บรรทัดเมนู + Found count",
         hint="อย่าพิมพ์ set ตรงๆ — วนรายการคงที่แล้วเช็ค in",
         starter='orders = ["pad thai", "rice", "pad thai", "soup", "rice"]\n\n# เขียนโค้ดตรงนี้',
         code='''orders = ["pad thai", "rice", "pad thai", "soup", "rice"]
unique = set(orders)
found = 0
for item in ["pad thai", "rice", "soup", "salad"]:
    ok = item in unique
    print(f"{item}: {ok}")
    if ok:
        found += 1
print(f"Found: {found}")'''),
    dict(file="10_medium.md", answer="10_class_overlap.py", diff="🟡 Medium",
         name="ห้องเรียนซ้อนกัน", axis="| และ & คู่กัน",
         title="🏫 Sets — ข้อ 9: ห้องเรียนซ้อนกัน",
         scenario='```python\nmorning = {"Ann", "Ben", "Cara"}\nafternoon = {"Cara", "Dan", "Eve"}\n```\n\nแสดงว่าใครเรียนอย่างน้อยหนึ่งรอบ (union) และใครเรียนทั้งสองรอบ (intersection) โดยเช็คชื่อ Ann..Eve',
         conditions=None, inp="ไม่มี input", out="สองบล็อก Either / Both",
         hint="คำนวณ `|` กับ `&` แยกกัน แล้ววนพิมพ์",
         starter='morning = {"Ann", "Ben", "Cara"}\nafternoon = {"Cara", "Dan", "Eve"}\n\n# เขียนโค้ดตรงนี้',
         code='''morning = {"Ann", "Ben", "Cara"}
afternoon = {"Cara", "Dan", "Eve"}
either = morning | afternoon
both = morning & afternoon
print("Either:")
for name in ["Ann", "Ben", "Cara", "Dan", "Eve"]:
    print(f"{name}: {name in either}")
print("Both:")
for name in ["Ann", "Ben", "Cara", "Dan", "Eve"]:
    print(f"{name}: {name in both}")'''),
    dict(file="11_medium.md", answer="11_inventory_tags.py", diff="🟡 Medium",
         name="แท็กคลังสินค้า", axis="add/remove + in",
         title="📦 Sets — ข้อ 10: แท็กคลังสินค้า",
         scenario='```python\ntags = {"fragile", "cold"}\n```\n\nเพิ่ม `"express"` ลบ `"cold"` แล้วตอบคำถามมี fragile/cold/express หรือไม่',
         conditions=None, inp="ไม่มี input", out="3 บรรทัด True/False",
         hint="add → remove → เช็คสามค่า",
         starter='tags = {"fragile", "cold"}\n\n# เขียนโค้ดตรงนี้',
         code='''tags = {"fragile", "cold"}
tags.add("express")
tags.remove("cold")
print("fragile:", "fragile" in tags)
print("cold:", "cold" in tags)
print("express:", "express" in tags)'''),
    dict(file="12_medium.md", answer="12_access_list.py", diff="🟡 Medium",
         name="รายชื่อเข้างานอีเวนต์", axis="set จาก list + input เช็ค",
         title="🎫 Sets — ข้อ 11: เช็คเข้างาน",
         scenario='```python\npasses = ["A1", "B2", "A1", "C3", "B2"]\n```\n\nตัดรหัสซ้ำด้วย set รับรหัสจาก input ถ้ามีสิทธิ์แสดง `Access granted` ไม่งั้น `Access denied`',
         conditions=None, inp="รหัสผ่าน 1 บรรทัด", out="ข้อความสิทธิ์ 1 บรรทัด",
         stdin="B2\n",
         hint="`allowed = set(passes)` แล้วเช็ค `in`",
         starter='passes = ["A1", "B2", "A1", "C3", "B2"]\ncode = input()\n\n# เขียนโค้ดตรงนี้',
         code='''passes = ["A1", "B2", "A1", "C3", "B2"]
allowed = set(passes)
code = input()
if code in allowed:
    print("Access granted")
else:
    print("Access denied")'''),
    dict(file="13_challenge.md", answer="13_project_teams.py", diff="🔴 Challenge",
         name="ทีมโปรเจกต์สองทีม", axis="union/intersection + รายงาน",
         title="👥 Sets — ข้อ 12: ทีมโปรเจกต์",
         scenario='```python\nteam_a = {"Ann", "Ben", "Cara", "Dan"}\nteam_b = {"Cara", "Dan", "Eve", "Finn"}\n```\n\nรายงานว่าใครอยู่ทีม A อย่างเดียวโดยเช็คจากรายชื่อคงที่ (อยู่ใน A แต่ไม่อยู่ใน intersection) และใครอยู่ทั้งสองทีม',
         conditions=None, inp="ไม่มี input", out="สองบล็อก Only A / Both",
         hint="หา `both = team_a & team_b` แล้ว Only A คืออยู่ใน A แต่ไม่อยู่ทั้งสองทีม",
         starter='team_a = {"Ann", "Ben", "Cara", "Dan"}\nteam_b = {"Cara", "Dan", "Eve", "Finn"}\n\n# เขียนโค้ดตรงนี้',
         code='''team_a = {"Ann", "Ben", "Cara", "Dan"}
team_b = {"Cara", "Dan", "Eve", "Finn"}
both = team_a & team_b
print("Only A:")
for name in ["Ann", "Ben", "Cara", "Dan", "Eve", "Finn"]:
    only_a = (name in team_a) and not (name in both)
    print(f"{name}: {only_a}")
print("Both:")
for name in ["Ann", "Ben", "Cara", "Dan", "Eve", "Finn"]:
    print(f"{name}: {name in both}")'''),
    dict(file="14_challenge.md", answer="14_course_enroll.py", diff="🔴 Challenge",
         name="ลงทะเบียนคอร์ส", axis="add/remove + union รายงาน",
         title="📘 Sets — ข้อ 13: ลงทะเบียนคอร์ส",
         scenario='```python\npython = {"Ann", "Ben"}\nexcel = {"Ben", "Cara"}\n```\n\nเพิ่ม `"Dan"` ใน python ลบ `"Cara"` จาก excel\nแสดงสถานะสมาชิกของคอร์สรวม (union) สำหรับ Ann/Ben/Cara/Dan',
         conditions=None, inp="ไม่มี input", out="4 บรรทัดสมาชิกรวมหลังอัปเดต",
         hint="อัปเดตแต่ละ set ก่อน แล้วค่อย `|`",
         starter='python = {"Ann", "Ben"}\nexcel = {"Ben", "Cara"}\n\n# เขียนโค้ดตรงนี้',
         code='''python = {"Ann", "Ben"}
excel = {"Ben", "Cara"}
python.add("Dan")
excel.remove("Cara")
all_students = python | excel
for name in ["Ann", "Ben", "Cara", "Dan"]:
    print(f"{name}: {name in all_students}")'''),
    dict(file="15_challenge.md", answer="15_allergy_filter.py", diff="🔴 Challenge",
         name="กรองเมนูแพ้อาหาร", axis="intersection เมนูกับ allergy",
         title="🥗 Sets — ข้อ 14: กรองเมนูแพ้",
         scenario='```python\nmenu = {"noodle", "salad", "steak", "soup"}\nallergy = {"noodle", "soup", "milk"}\n```\n\nหาเมนูที่ชนกับ allergy ด้วย `&` พิมพ์ผลเช็คทีละเมนูใน menu ตามลำดับ แล้วถ้ามีเมนูชนแสดง `Warning: allergy conflict` ไม่งั้น `Safe menu`',
         conditions=None, inp="ไม่มี input", out="ผลเช็คเมนู + สถานะ",
         hint="`conflict = menu & allergy` แล้ววนเมนูคงที่",
         starter='menu = {"noodle", "salad", "steak", "soup"}\nallergy = {"noodle", "soup", "milk"}\n\n# เขียนโค้ดตรงนี้',
         code='''menu = {"noodle", "salad", "steak", "soup"}
allergy = {"noodle", "soup", "milk"}
conflict = menu & allergy
for item in ["noodle", "salad", "steak", "soup"]:
    print(f"{item}: {item in conflict}")
if "noodle" in conflict:
    print("Warning: allergy conflict")
else:
    print("Safe menu")'''),
    dict(file="16_challenge.md", answer="16_visitor_log.py", diff="🔴 Challenge",
         name="บันทึกผู้เข้าชมร้าน", axis="set จาก log + เพิ่ม/ลบ + สรุป",
         title="🧾 Sets — ข้อ 15: บันทึกผู้เข้าชม",
         scenario='```python\nlog = ["Ann", "Ben", "Ann", "Cara", "Ben", "Dan"]\n```\n\nตัดชื่อซ้ำด้วย set เพิ่ม `"Eve"` ลบ `"Ben"`\nเช็คสถานะ Ann/Ben/Cara/Dan/Eve\nรับชื่อจาก input แล้วบอกว่า `Inside` หรือ `Outside`',
         conditions=None, inp="ชื่อ 1 บรรทัด", out="สถานะห้าคน + ผลการเช็คชื่อ",
         stdin="Cara\n",
         hint="set(log) → add → remove → วนเช็ค → รับ input",
         starter='log = ["Ann", "Ben", "Ann", "Cara", "Ben", "Dan"]\nname = input()\n\n# เขียนโค้ดตรงนี้',
         code='''log = ["Ann", "Ben", "Ann", "Cara", "Ben", "Dan"]
visitors = set(log)
visitors.add("Eve")
visitors.remove("Ben")
for person in ["Ann", "Ben", "Cara", "Dan", "Eve"]:
    print(f"{person}: {person in visitors}")
name = input()
if name in visitors:
    print("Inside")
else:
    print("Outside")'''),
    ]
    emit("030-sets", probs, "บท 030 Sets",
         ["set literal `{...}`", "`set(list)`", "`.add()` / `.remove()`", "`in`", "union `|` / intersection `&`"],
         ["ห้ามพิมพ์ set ตรงๆ ในเฉลย (ลำดับไม่คงที่)", "ห้าม set difference / discard"],
         ["ข้อ `02` ไม่ซ้ำตัวอย่าง fruits / A|B จากบทเรียนตรงๆ",
          "ทุกข้อที่ต้องแสดงสมาชิกให้วนรายการคงที่แล้วใช้ `in`"])


def gen_031():
    probs = [
    dict(file="02_test.md", answer="02_shopping_list.py", diff="🟢 Easy",
         name="ตะกร้าช้อปต้องแก้ได้", axis="เลือก list",
         title="🛒 Choosing Types — ข้อ 1: ตะกร้าช้อป",
         scenario="ลูกค้าจะเพิ่มของในตะกร้าทีหลังได้ ต้องเก็บลำดับด้วย\n\nสร้าง list เริ่มต้น `milk` / `eggs` แล้ว `.append(\"bread\")` พิมพ์ list",
         conditions=None, inp="ไม่มี input", out="list หลังเพิ่มของ",
         hint="ของที่แก้ได้และมีลำดับ → list",
         starter="# เขียนโค้ดตรงนี้",
         code='shopping = ["milk", "eggs"]\nshopping.append("bread")\nprint(shopping)'),
    dict(file="03_test.md", answer="03_weekdays_tuple.py", diff="🟢 Easy",
         name="วันในสัปดาห์คงที่", axis="เลือก tuple",
         title="📅 Choosing Types — ข้อ 2: วันในสัปดาห์",
         scenario='วันทำงานไม่ควรแก้ สร้าง tuple `("Mon", "Tue", "Wed", "Thu", "Fri")` แล้วพิมพ์วันแรกกับวันสุดท้าย',
         conditions=None, inp="ไม่มี input", out="2 บรรทัด",
         hint="ข้อมูลคงที่และมีลำดับ → tuple",
         starter="# เขียนโค้ดตรงนี้",
         code='weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri")\nprint(weekdays[0])\nprint(weekdays[-1])'),
    dict(file="04_test.md", answer="04_unique_visitors.py", diff="🟢 Easy",
         name="ผู้เข้าชมไม่ซ้ำ", axis="เลือก set",
         title="🚪 Choosing Types — ข้อ 3: ผู้เข้าชมไม่ซ้ำ",
         scenario='ล็อกชื่อซ้ำได้\n\n```python\nlog = ["Ann", "Ben", "Ann", "Cara", "Ben"]\n```\n\nเก็บเป็น set แล้วเช็คว่ามี Ann/Ben/Dan หรือไม่',
         conditions=None, inp="ไม่มี input", out="3 บรรทัด True/False",
         hint="ต้องการค่าไม่ซ้ำ ไม่สนลำดับ → set",
         starter='log = ["Ann", "Ben", "Ann", "Cara", "Ben"]\n\n# เขียนโค้ดตรงนี้',
         code='''log = ["Ann", "Ben", "Ann", "Cara", "Ben"]
visitors = set(log)
print("Ann:", "Ann" in visitors)
print("Ben:", "Ben" in visitors)
print("Dan:", "Dan" in visitors)'''),
    dict(file="05_easy.md", answer="05_coordinates.py", diff="🟢 Easy",
         name="พิกัดจุดบนแผนที่", axis="tuple สองค่า",
         title="🗺️ Choosing Types — ข้อ 4: พิกัดจุด",
         scenario="พิกัดไม่ควรแก้ สร้าง `point = (10, 20)` แสดง X และ Y",
         conditions=None, inp="ไม่มี input", out="2 บรรทัด",
         hint="คู่ค่าคงที่ → tuple",
         starter="# เขียนโค้ดตรงนี้",
         code='point = (10, 20)\nprint(f"X: {point[0]}")\nprint(f"Y: {point[1]}")'),
    dict(file="06_easy.md", answer="06_player_inventory.py", diff="🟢 Easy",
         name="กระเป๋าไอเท็มในเกม", axis="list ที่แก้ได้",
         title="🎒 Choosing Types — ข้อ 5: กระเป๋าไอเท็ม",
         scenario='เริ่มด้วย `["potion", "map"]` เพิ่ม `"key"` ลบ `"map"` พิมพ์ผล',
         conditions=None, inp="ไม่มี input", out="list หลังอัปเดต",
         hint="เพิ่ม/ลบได้ → list",
         starter="# เขียนโค้ดตรงนี้",
         code='''bag = ["potion", "map"]
bag.append("key")
bag.remove("map")
print(bag)'''),
    dict(file="07_medium.md", answer="07_dedup_then_sort.py", diff="🟡 Medium",
         name="ตัดซ้ำแล้วเรียงชื่อ", axis="set → list → sort",
         title="🔤 Choosing Types — ข้อ 6: ตัดซ้ำแล้วเรียง",
         scenario='```python\nnames = ["Bee", "Ann", "Cara", "Ann", "Bee"]\n```\n\nตัดซ้ำด้วย set แปลงกลับเป็น list เรียง A→Z พิมพ์ผล',
         conditions=None, inp="ไม่มี input", out="list ชื่อไม่ซ้ำเรียงแล้ว",
         hint="set ตัดซ้ำ → `list(...)` → `.sort()` เพราะ set เรียงเองไม่ได้",
         starter='names = ["Bee", "Ann", "Cara", "Ann", "Bee"]\n\n# เขียนโค้ดตรงนี้',
         code='''names = ["Bee", "Ann", "Cara", "Ann", "Bee"]
unique = list(set(names))
unique.sort()
print(unique)'''),
    dict(file="08_medium.md", answer="08_seat_tuple.py", diff="🟡 Medium",
         name="ที่นั่งโรงหนังคงที่", axis="tuple + แสดงหมายเลข",
         title="🎬 Choosing Types — ข้อ 7: ที่นั่งโรงหนัง",
         scenario='แถวที่นั่งล็อกแล้ว\n\n```python\nrow = ("A1", "A2", "A3", "A4")\n```\n\nพิมพ์แบบมีหมายเลข และจำนวนที่นั่ง',
         conditions=None, inp="ไม่มี input", out="ที่นั่งมีหมายเลข + Count",
         hint="ลำดับสำคัญแต่แก้ไม่ได้ → tuple",
         starter='row = ("A1", "A2", "A3", "A4")\n\n# เขียนโค้ดตรงนี้',
         code='''row = ("A1", "A2", "A3", "A4")
for i in range(len(row)):
    print(f"{i + 1}. {row[i]}")
print(f"Count: {len(row)}")'''),
    dict(file="09_medium.md", answer="09_tags_vs_list.py", diff="🟡 Medium",
         name="แท็กโพสต์ vs ลำดับสไลด์", axis="set และ list คนละงาน",
         title="🧾 Choosing Types — ข้อ 8: แท็กกับลำดับสไลด์",
         scenario='แท็กโพสต์ไม่สนลำดับและไม่ซ้ำ: สร้าง set จาก `["cat", "food", "cat"]`\nลำดับสไลด์ต้องเรียงได้: list `["intro", "demo"]` แล้ว append `"end"`\nเช็คว่ามีแท็ก food หรือไม่ และพิมพ์ list สไลด์',
         conditions=None, inp="ไม่มี input", out="2 บรรทัด — มีแท็กหรือไม่ และ list สไลด์",
         hint="คนละงานคนละชนิดข้อมูล",
         starter="# เขียนโค้ดตรงนี้",
         code='''tags = set(["cat", "food", "cat"])
slides = ["intro", "demo"]
slides.append("end")
print("food" in tags)
print(slides)'''),
    dict(file="10_medium.md", answer="10_highscore_board.py", diff="🟡 Medium",
         name="บอร์ดคะแนนต้องเรียง", axis="list + sort reverse",
         title="🏆 Choosing Types — ข้อ 9: บอร์ดคะแนน",
         scenario="คะแนนต้องเรียงอันดับได้\n\n```python\nscores = [120, 90]\n```\n\nเพิ่ม 150 เรียงมาก→น้อย แสดง Top เป็นตัวแรก",
         conditions=None, inp="ไม่มี input", out="list หลังเรียง + Top",
         hint="ต้องการลำดับที่เปลี่ยนได้ → list",
         starter="scores = [120, 90]\n\n# เขียนโค้ดตรงนี้",
         code='''scores = [120, 90]
scores.append(150)
scores.sort(reverse=True)
print(scores)
print(f"Top: {scores[0]}")'''),
    dict(file="11_medium.md", answer="11_allowed_ids.py", diff="🟡 Medium",
         name="ชุดรหัสผ่านประตู", axis="set + in จาก input",
         title="🔐 Choosing Types — ข้อ 10: รหัสผ่านประตู",
         scenario='รหัสที่ผ่านได้ไม่ซ้ำ\n\n```python\nraw = ["X1", "Y2", "X1", "Z3"]\n```\n\nเก็บเป็น set รับรหัสจาก input แล้วตอบ Allowed/Denied',
         conditions=None, inp="รหัส 1 บรรทัด", out="Allowed หรือ Denied",
         stdin="Y2\n",
         hint="เช็คสมาชิกเร็วๆ ไม่สนลำดับ → set",
         starter='raw = ["X1", "Y2", "X1", "Z3"]\ncode = input()\n\n# เขียนโค้ดตรงนี้',
         code='''raw = ["X1", "Y2", "X1", "Z3"]
allowed = set(raw)
code = input()
if code in allowed:
    print("Allowed")
else:
    print("Denied")'''),
    dict(file="12_medium.md", answer="12_rewrite_tuple.py", diff="🟡 Medium",
         name="เปลี่ยนข้อมูลนักเรียนเป็น tuple", axis="เก็บ record คงที่",
         title="🎓 Choosing Types — ข้อ 11: ระเบียนนักเรียน",
         scenario='ข้อมูลนักเรียนไม่ควรแก้ชื่อ/อายุมั่ว สร้าง tuple `("Nok", 13, "M.1")` แสดงสามบรรทัด Name/Age/Class',
         conditions=None, inp="ไม่มี input", out="3 บรรทัด",
         hint="record คงที่ → tuple",
         starter="# เขียนโค้ดตรงนี้",
         code='''student = ("Nok", 13, "M.1")
print(f"Name: {student[0]}")
print(f"Age: {student[1]}")
print(f"Class: {student[2]}")'''),
    dict(file="13_challenge.md", answer="13_event_system.py", diff="🔴 Challenge",
         name="ระบบอีเวนต์ผสมสามชนิด", axis="list+tuple+set ในโปรแกรมเดียว",
         title="🎪 Choosing Types — ข้อ 12: ระบบอีเวนต์",
         scenario='กำหนด:\n- ลำดับกิจกรรมทั้งวันเป็น list เริ่ม `["open", "talk"]` แล้ว append `"close"`\n- สถานที่เป็น tuple คงที่ `("Hall A", 100)`\n- แขกไม่ซ้ำเป็น set จาก `["Ann", "Ben", "Ann"]` แล้ว add `"Cara"`\n\nพิมพ์ list กิจกรรม, ชื่อสถานที่, ความจุ, และสถานะมี Ben/Dan',
         conditions=None, inp="ไม่มี input", out="หลายบรรทัดสรุประบบ",
         hint="เลือกชนิดตามหน้าที่ของข้อมูลแต่ละส่วน",
         starter="# เขียนโค้ดตรงนี้",
         code='''schedule = ["open", "talk"]
schedule.append("close")
venue = ("Hall A", 100)
guests = set(["Ann", "Ben", "Ann"])
guests.add("Cara")

print(schedule)
print(f"Venue: {venue[0]}")
print(f"Capacity: {venue[1]}")
print("Ben:", "Ben" in guests)
print("Dan:", "Dan" in guests)'''),
    dict(file="14_challenge.md", answer="14_order_pipeline.py", diff="🔴 Challenge",
         name="ไปป์ไลน์ออเดอร์ร้านอาหาร", axis="list แก้ได้ + set เมนูพิเศษ",
         title="🍽️ Choosing Types — ข้อ 13: ไปป์ไลน์ออเดอร์",
         scenario='คิวออเดอร์เป็น list `["A", "B"]` เพิ่ม `"C"` ลบ `"A"`\nเมนูพิเศษวันนี้เป็น set `{"B", "C", "D"}`\nพิมพ์คิวสุดท้าย แล้วเช็คว่าออเดอร์แต่ละตัวในคิวเป็นเมนูพิเศษหรือไม่',
         conditions=None, inp="ไม่มี input", out="คิว + ผลเช็คเมนูพิเศษ",
         hint="คิวมีลำดับและเปลี่ยนได้=list / เมนูพิเศษไม่ซ้ำ=set",
         starter="# เขียนโค้ดตรงนี้",
         code='''queue = ["A", "B"]
queue.append("C")
queue.remove("A")
special = {"B", "C", "D"}
print(queue)
for order in queue:
    print(f"{order}: {order in special}")'''),
    dict(file="15_challenge.md", answer="15_match_config.py", diff="🔴 Challenge",
         name="คอนฟิกแมตช์กีฬา", axis="tuple คงที่ + list สกอร์",
         title="🏅 Choosing Types — ข้อ 14: คอนฟิกแมตช์",
         scenario='คู่แข่งล็อกเป็น tuple `("Tigers", "Bears")`\nสกอร์เป็น list เริ่ม `[0, 0]` แล้วตั้งเป็น `[3, 2]` ด้วย assignment\nแสดงทีมเหย้า ทีมเยือน และผู้ชนะ (ถ้าเหย้ามากกว่าหรือเท่า → Home)',
         conditions=None, inp="ไม่มี input", out="Home/Away/Winner",
         hint="ชื่อทีมคงที่=tuple / สกอร์เปลี่ยนได้=list",
         starter="# เขียนโค้ดตรงนี้",
         code='''teams = ("Tigers", "Bears")
scores = [0, 0]
scores[0] = 3
scores[1] = 2
print(f"Home: {teams[0]}")
print(f"Away: {teams[1]}")
if scores[0] >= scores[1]:
    print("Winner: Home")
else:
    print("Winner: Away")'''),
    dict(file="16_challenge.md", answer="16_best_type_lab.py", diff="🔴 Challenge",
         name="แล็บเลือกชนิดข้อมูล", axis="สามสถานการณ์ในข้อเดียว",
         title="🧪 Choosing Types — ข้อ 15: แล็บเลือกชนิด",
         scenario='สร้างสามตัวแปรให้เหมาะงาน:\n1) `colors` — ลำดับสีธีมที่เรียงได้: list `["red", "blue"]` แล้ว sort\n2) `origin` — จุดกำเนิดคงที่: tuple `(0, 0)`\n3) `badges` — เหรียญไม่ซ้ำ: set จาก list ที่มีซ้ำ แล้วเช็ค `"gold"`\n\nพิมพ์ colors, X ของ origin, และผลเช็ค gold',
         conditions=None, inp="ไม่มี input", out="3 บรรทัด",
         hint="ถามตัวเอง: แก้ได้ไหม? มีลำดับไหม? ซ้ำได้ไหม?",
         starter="# เขียนโค้ดตรงนี้",
         code='''colors = ["red", "blue"]
colors.sort()
origin = (0, 0)
badges = set(["gold", "silver", "gold"])
print(colors)
print(f"X: {origin[0]}")
print("gold:", "gold" in badges)'''),
    ]
    emit("031-choosing-data-types", probs, "บท 031 Choosing Data Types",
         ["ตัดสินใจเลือก list / tuple / set", "ใช้ของที่เรียนใน 025 / 029 / 030"],
         ["ไม่มี syntax ใหม่"],
         ["โจทย์เป็นสถานการณ์จริงที่ต้องเลือกชนิดข้อมูลให้ถูก",
          "ข้อ `02` ไม่ใช่ตารางสถานการณ์ในบทเรียนลอกมาตรงๆ"])


def gen_032():
    probs = [
    dict(file="02_test.md", answer="02_three_boxes.py", diff="🟢 Easy",
         name="สามกล่องข้อมูล", axis="ประกาศ list/tuple/set",
         title="🗂️ Collection Review — ข้อ 1: สามกล่องข้อมูล",
         scenario='สร้าง\n- list `students` มี `"Ann"` สองครั้งกับ `"Ben"`\n- tuple `days` เป็น `("Mon", "Tue")`\n- set `unique` จาก students\n\nพิมพ์ students, days[0], และผล `"Ann" in unique`',
         conditions=None, inp="ไม่มี input", out="3 บรรทัด",
         hint="list ซ้ำได้ / tuple มีลำดับ / set ตัดซ้ำ",
         starter="# เขียนโค้ดตรงนี้",
         code='''students = ["Ann", "Ben", "Ann"]
days = ("Mon", "Tue")
unique = set(students)
print(students)
print(days[0])
print("Ann" in unique)'''),
    dict(file="03_test.md", answer="03_tuple_readonly.py", diff="🟢 Easy",
         name="อ่าน tuple อย่างเดียว", axis="index + for",
         title="🔒 Collection Review — ข้อ 2: อ่าน tuple",
         scenario='```python\nprize = ("Gold", "Silver", "Bronze")\n```\n\nพิมพ์ทุกอันดับ และอันดับสุดท้ายซ้ำอีกครั้ง',
         conditions=None, inp="ไม่มี input", out="4 บรรทัด",
         hint="วน for แล้วพิมพ์ `[-1]`",
         starter='prize = ("Gold", "Silver", "Bronze")\n\n# เขียนโค้ดตรงนี้',
         code='''prize = ("Gold", "Silver", "Bronze")
for p in prize:
    print(p)
print(prize[-1])'''),
    dict(file="04_test.md", answer="04_list_set_combo.py", diff="🟢 Easy",
         name="list ตัดซ้ำด้วย set", axis="list → set → เช็ค",
         title="🔁 Collection Review — ข้อ 3: ตัดซ้ำจาก list",
         scenario='```python\nvotes = ["A", "B", "A", "C", "B"]\n```\n\nตัดซ้ำ แล้วเช็ค A/B/D',
         conditions=None, inp="ไม่มี input", out="3 บรรทัด",
         hint="`set(votes)`",
         starter='votes = ["A", "B", "A", "C", "B"]\n\n# เขียนโค้ดตรงนี้',
         code='''votes = ["A", "B", "A", "C", "B"]
unique = set(votes)
print("A:", "A" in unique)
print("B:", "B" in unique)
print("D:", "D" in unique)'''),
    dict(file="05_easy.md", answer="05_update_list_keep_tuple.py", diff="🟢 Easy",
         name="แก้ list แต่ไม่แตะ tuple", axis="แยกหน้าที่ชนิดข้อมูล",
         title="🛠️ Collection Review — ข้อ 4: แก้ list ไม่แตะ tuple",
         scenario='```python\nitems = ["pen", "ink"]\nshop = ("Stationery Hub", "Floor 2")\n```\n\nเพิ่ม `"ruler"` ใน items พิมพ์ items และชื่อร้านจาก tuple',
         conditions=None, inp="ไม่มี input", out="2 บรรทัด",
         hint="tuple ใช้แค่อ่าน",
         starter='items = ["pen", "ink"]\nshop = ("Stationery Hub", "Floor 2")\n\n# เขียนโค้ดตรงนี้',
         code='''items = ["pen", "ink"]
shop = ("Stationery Hub", "Floor 2")
items.append("ruler")
print(items)
print(shop[0])'''),
    dict(file="06_easy.md", answer="06_membership_gate.py", diff="🟢 Easy",
         name="ประตูสมาชิก set", axis="in + if",
         title="🚪 Collection Review — ข้อ 5: ประตูสมาชิก",
         scenario='```python\nmembers = {"Ann", "Ben", "Cara"}\n```\n\nรับชื่อ แล้วตอบ Member/Guest',
         conditions=None, inp="ชื่อ 1 บรรทัด", out="Member หรือ Guest",
         stdin="Dan\n",
         hint="ใช้ `in` กับ set",
         starter='members = {"Ann", "Ben", "Cara"}\nname = input()\n\n# เขียนโค้ดตรงนี้',
         code='''members = {"Ann", "Ben", "Cara"}
name = input()
if name in members:
    print("Member")
else:
    print("Guest")'''),
    dict(file="07_medium.md", answer="07_class_stats.py", diff="🟡 Medium",
         name="สถิติห้องจาก list", axis="len list vs len set",
         title="📊 Collection Review — ข้อ 6: สถิติห้อง",
         scenario='```python\nall_students = ["Ann", "Ben", "Ann", "Cara", "Ben", "Dan"]\n```\n\nแสดงจำนวนรายการทั้งหมด และจำนวนชื่อไม่ซ้ำ (ผ่าน set) พร้อมรหัสห้องเป็น tuple `("M.2", "Room 4")`',
         conditions=None, inp="ไม่มี input", out="Total / Unique / Grade / Room",
         hint="นับจาก list และจาก set แยกกัน",
         starter='all_students = ["Ann", "Ben", "Ann", "Cara", "Ben", "Dan"]\ngrade_info = ("M.2", "Room 4")\n\n# เขียนโค้ดตรงนี้',
         code='''all_students = ["Ann", "Ben", "Ann", "Cara", "Ben", "Dan"]
grade_info = ("M.2", "Room 4")
unique_students = set(all_students)
print(f"Total: {len(all_students)}")
print(f"Unique: {len(unique_students)}")
print(f"Grade: {grade_info[0]}")
print(f"Room: {grade_info[1]}")'''),
    dict(file="08_medium.md", answer="08_schedule_board.py", diff="🟡 Medium",
         name="กระดานตารางเรียน", axis="tuple วัน + list วิชา",
         title="🗓️ Collection Review — ข้อ 7: กระดานตารางเรียน",
         scenario='```python\ndays = ("Mon", "Tue", "Wed")\nsubjects = ["Math", "Thai"]\n```\n\nเพิ่ม `"English"` เรียงวิชา แล้วพิมพ์วันทุกวันและวิชาทุกวิชา',
         conditions=None, inp="ไม่มี input", out="วันและวิชาทีละบรรทัด",
         hint="วันคงที่=tuple / วิชาแก้ได้=list",
         starter='days = ("Mon", "Tue", "Wed")\nsubjects = ["Math", "Thai"]\n\n# เขียนโค้ดตรงนี้',
         code='''days = ("Mon", "Tue", "Wed")
subjects = ["Math", "Thai"]
subjects.append("English")
subjects.sort()
print("Days:")
for day in days:
    print(day)
print("Subjects:")
for subject in subjects:
    print(subject)'''),
    dict(file="09_medium.md", answer="09_party_overlap.py", diff="🟡 Medium",
         name="แขกซ้ำสองงานเลี้ยง", axis="& และ |",
         title="🥳 Collection Review — ข้อ 8: แขกซ้ำสองงาน",
         scenario='```python\nparty1 = {"Ann", "Ben", "Cara"}\nparty2 = {"Cara", "Dan"}\n```\n\nเช็คชื่อในรายการคงที่ว่าใครไปได้อย่างน้อยหนึ่งงาน และใครไปทั้งสองงาน',
         conditions=None, inp="ไม่มี input", out="สองบล็อก",
         hint="ใช้ `|` และ `&`",
         starter='party1 = {"Ann", "Ben", "Cara"}\nparty2 = {"Cara", "Dan"}\n\n# เขียนโค้ดตรงนี้',
         code='''party1 = {"Ann", "Ben", "Cara"}
party2 = {"Cara", "Dan"}
either = party1 | party2
both = party1 & party2
print("Either:")
for name in ["Ann", "Ben", "Cara", "Dan"]:
    print(f"{name}: {name in either}")
print("Both:")
for name in ["Ann", "Ben", "Cara", "Dan"]:
    print(f"{name}: {name in both}")'''),
    dict(file="10_medium.md", answer="10_cart_and_coupon.py", diff="🟡 Medium",
         name="ตะกร้ากับคูปอง", axis="list + set สิทธิ์",
         title="🛍️ Collection Review — ข้อ 9: ตะกร้ากับคูปอง",
         scenario='```python\ncart = ["book", "pen"]\ncoupons = {"SAVE10", "FREESHIP"}\n```\n\nเพิ่ม `"bag"` ในตะกร้า รับรหัสคูปอง ถ้ามีใน set แสดง `Coupon OK` ไม่งั้น `Coupon invalid` พร้อมพิมพ์ cart',
         conditions=None, inp="รหัสคูปอง 1 บรรทัด", out="สถานะคูปอง + cart",
         stdin="SAVE10\n",
         hint="ของในตะกร้า=list / รหัสคูปอง=set",
         starter='cart = ["book", "pen"]\ncoupons = {"SAVE10", "FREESHIP"}\ncode = input()\n\n# เขียนโค้ดตรงนี้',
         code='''cart = ["book", "pen"]
coupons = {"SAVE10", "FREESHIP"}
code = input()
cart.append("bag")
if code in coupons:
    print("Coupon OK")
else:
    print("Coupon invalid")
print(cart)'''),
    dict(file="11_medium.md", answer="11_index_both.py", diff="🟡 Medium",
         name="เข้าถึง list และ tuple ด้วย index", axis="เปรียบเทียบการเข้าถึง",
         title="📍 Collection Review — ข้อ 10: index สองชนิด",
         scenario='```python\ncolors = ["red", "green", "blue"]\nrgb = (255, 0, 128)\n```\n\nแสดงสีสุดท้ายและค่าช่องกลางของ rgb',
         conditions=None, inp="ไม่มี input", out="2 บรรทัด",
         hint="ทั้ง list และ tuple ใช้ index ได้",
         starter='colors = ["red", "green", "blue"]\nrgb = (255, 0, 128)\n\n# เขียนโค้ดตรงนี้',
         code='''colors = ["red", "green", "blue"]
rgb = (255, 0, 128)
print(colors[-1])
print(rgb[1])'''),
    dict(file="12_medium.md", answer="12_clean_roster.py", diff="🟡 Medium",
         name="ทำความสะอาดรายชื่อ", axis="list แก้ + set สรุป",
         title="🧹 Collection Review — ข้อ 11: ทำความสะอาดรายชื่อ",
         scenario='```python\nroster = ["Ann", "Ben", "Cara", "Ben"]\n```\n\nลบ `"Cara"` เพิ่ม `"Dan"` สร้าง set จาก roster แล้วเช็ค Ben/Cara/Dan',
         conditions=None, inp="ไม่มี input", out="list + 3 บรรทัดเช็ค",
         hint="อัปเดต list ก่อน แล้วค่อย set",
         starter='roster = ["Ann", "Ben", "Cara", "Ben"]\n\n# เขียนโค้ดตรงนี้',
         code='''roster = ["Ann", "Ben", "Cara", "Ben"]
roster.remove("Cara")
roster.append("Dan")
unique = set(roster)
print(roster)
print("Ben:", "Ben" in unique)
print("Cara:", "Cara" in unique)
print("Dan:", "Dan" in unique)'''),
    dict(file="13_challenge.md", answer="13_student_tracker.py", diff="🔴 Challenge",
         name="ตัวติดตามนักเรียน", axis="list+set+tuple สรุปกรอบ",
         title="🏫 Collection Review — ข้อ 12: ตัวติดตามนักเรียน",
         scenario='```python\nall_students = ["Ann", "Ben", "Ann", "Cara", "Dan", "Ben"]\ngrade_info = ("Grade 9", "Room 3")\n```\n\nสร้าง set ชื่อไม่ซ้ำ แสดงกรอบ Total / Unique / Grade / Room และรายชื่อไม่ซ้ำเรียงแล้ว (แปลงเป็น list แล้ว sort)',
         conditions=None, inp="ไม่มี input", out="กล่องสรุป + รายชื่อเรียง",
         hint="อย่าพิมพ์ set ตรงๆ — แปลงเป็น list แล้ว sort",
         starter='all_students = ["Ann", "Ben", "Ann", "Cara", "Dan", "Ben"]\ngrade_info = ("Grade 9", "Room 3")\n\n# เขียนโค้ดตรงนี้',
         code='''all_students = ["Ann", "Ben", "Ann", "Cara", "Dan", "Ben"]
grade_info = ("Grade 9", "Room 3")
unique_students = set(all_students)
names = list(unique_students)
names.sort()

print("========================")
print("    STUDENT TRACKER")
print("========================")
print(f"Total      : {len(all_students)}")
print(f"Unique     : {len(unique_students)}")
print(f"Grade      : {grade_info[0]}")
print(f"Room       : {grade_info[1]}")
print("========================")
for name in names:
    print(name)'''),
    dict(file="14_challenge.md", answer="14_store_front.py", diff="🔴 Challenge",
         name="หน้าร้านผสมสามชนิด", axis="หลายโครงสร้าง + input",
         title="🏪 Collection Review — ข้อ 13: หน้าร้าน",
         scenario='เมนูคงที่ tuple `("latte", "mocha", "tea")`\nคิวลูกค้า list เริ่ม `["Ann"]` แล้ว append ชื่อจาก input\nสมาชิก VIP set `{"Ann", "Ben"}`\nพิมพ์เมนูมีหมายเลข คิวสุดท้าย และว่าคนล่าสุดในคิวเป็น VIP หรือไม่',
         conditions=None, inp="ชื่อลูกค้าใหม่ 1 บรรทัด", out="เมนู + คิว + VIP status",
         stdin="Cara\n",
         hint="อ่านเมนูจาก tuple / ต่อคิวด้วย list / เช็ค VIP ด้วย set",
         starter='menu = ("latte", "mocha", "tea")\nqueue = ["Ann"]\nvip = {"Ann", "Ben"}\nname = input()\n\n# เขียนโค้ดตรงนี้',
         code='''menu = ("latte", "mocha", "tea")
queue = ["Ann"]
vip = {"Ann", "Ben"}
name = input()
queue.append(name)

for i in range(len(menu)):
    print(f"{i + 1}. {menu[i]}")
print(queue)
last = queue[-1]
if last in vip:
    print("VIP: Yes")
else:
    print("VIP: No")'''),
    dict(file="15_challenge.md", answer="15_match_day.py", diff="🔴 Challenge",
         name="วันแข่งขันกีฬาสี", axis="tuple ทีม + list คะแนน + set ใบเหลือง",
         title="🎽 Collection Review — ข้อ 14: วันแข่งขัน",
         scenario='ทีม tuple `("Red", "Blue")`\nสกอร์ list `[1, 1]` แล้วเพิ่มประตูให้ Red (`scores[0] = 2`)\nใบเหลือง set จาก `["Red", "Blue", "Red"]`\nแสดงทีม สกอร์ และว่า Red มีใบเหลืองไหม',
         conditions=None, inp="ไม่มี input", out="สรุปแมตช์หลายบรรทัด",
         hint="แยกชนิดตามหน้าที่",
         starter="# เขียนโค้ดตรงนี้",
         code='''teams = ("Red", "Blue")
scores = [1, 1]
scores[0] = 2
yellow = set(["Red", "Blue", "Red"])
print(f"Home: {teams[0]} {scores[0]}")
print(f"Away: {teams[1]} {scores[1]}")
print("Red yellow:", "Red" in yellow)'''),
    dict(file="16_challenge.md", answer="16_final_mix.py", diff="🔴 Challenge",
         name="คลังรวมท้ายบท", axis="ผสมทุกทักษะ collection",
         title="📦 Collection Review — ข้อ 15: คลังรวมท้ายบท",
         scenario='```python\nskus = ["A1", "B2", "A1", "C3", "B2"]\nwarehouse = ("Bangkok", "Zone 2")\n```\n\nตัดรหัสซ้ำเป็น set แปลงเป็น list แล้ว sort\nลบ `"B2"` จาก list ที่เรียงแล้ว (ถ้ามี) เพิ่ม `"D4"`\nแสดงกรอบที่อยู่คลัง จำนวนรหัสสุดท้าย และรายการรหัส',
         conditions=None, inp="ไม่มี input", out="กล่องสรุป + รายการรหัส",
         hint="set ตัดซ้ำ → list+sort เพื่อมีลำดับคงที่ → แก้ด้วย remove/append",
         starter='skus = ["A1", "B2", "A1", "C3", "B2"]\nwarehouse = ("Bangkok", "Zone 2")\n\n# เขียนโค้ดตรงนี้',
         code='''skus = ["A1", "B2", "A1", "C3", "B2"]
warehouse = ("Bangkok", "Zone 2")
codes = list(set(skus))
codes.sort()
codes.remove("B2")
codes.append("D4")
codes.sort()

print("========================")
print("      WAREHOUSE")
print("========================")
print(f"City       : {warehouse[0]}")
print(f"Zone       : {warehouse[1]}")
print(f"Count      : {len(codes)}")
print("========================")
for code in codes:
    print(code)'''),
    ]
    emit("032-collection-review", probs, "บท 032 Collection Review",
         ["ทบทวน list / tuple / set เคียงข้างกัน", "เลือกชนิดให้ถูกงาน"],
         ["ไม่มี syntax ใหม่", "ห้ามพิมพ์ set ตรงๆ"],
         ["ข้อ Challenge ผสมหลายชนิดในโปรแกรมเดียว",
          "หลีกเลี่ยงตัวอย่าง students/days จากบทเรียนแบบลอกตรง"])


if __name__ == "__main__":
    gen_029()
    gen_030()
    gen_031()
    gen_032()
    print("029-032 complete")
