#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from _gen_lib import emit

def gen_033():
    # NO .keys/.get/.items/.values/del — use for key in dict / dict[key] / in / add by assignment
    probs = [
    dict(file="02_test.md", answer="02_pet_card.py", diff="🟢 Easy",
         name="การ์ดสัตว์เลี้ยง", axis="อ่านค่าด้วย key",
         title="🐾 Dictionaries — ข้อ 1: การ์ดสัตว์เลี้ยง",
         scenario='```python\npet = {"name": "Mochi", "type": "cat", "age": 2}\n```\n\nแสดงชื่อและชนิดสัตว์',
         conditions=None, inp="ไม่มี input", out="2 บรรทัด Name / Type",
         hint='ใช้ `pet["name"]` และ `pet["type"]`',
         starter='pet = {"name": "Mochi", "type": "cat", "age": 2}\n\n# เขียนโค้ดตรงนี้',
         code='''pet = {"name": "Mochi", "type": "cat", "age": 2}
print(f"Name: {pet['name']}")
print(f"Type: {pet['type']}")'''),
    dict(file="03_test.md", answer="03_add_score.py", diff="🟢 Easy",
         name="เพิ่มคะแนนลงบัตร", axis="เพิ่ม key ด้วย assignment",
         title="➕ Dictionaries — ข้อ 2: เพิ่มคะแนน",
         scenario='```python\nplayer = {"name": "Bee", "level": 3}\n```\n\nเพิ่ม `"score"` = 1200 แล้วพิมพ์ค่า score',
         conditions=None, inp="ไม่มี input", out="1 บรรทัดคะแนน",
         hint='`player["score"] = 1200`',
         starter='player = {"name": "Bee", "level": 3}\n\n# เขียนโค้ดตรงนี้',
         code='''player = {"name": "Bee", "level": 3}
player["score"] = 1200
print(f"Score: {player['score']}")'''),
    dict(file="04_test.md", answer="04_has_key.py", diff="🟢 Easy",
         name="มีเบอร์โทรไหม", axis="in ตรวจ key",
         title="📞 Dictionaries — ข้อ 3: มีเบอร์โทรไหม",
         scenario='```python\ncontact = {"name": "Ann", "city": "Bangkok"}\n```\n\nถ้ามี key `"phone"` แสดง `Has phone` ไม่งั้น `No phone`',
         conditions=None, inp="ไม่มี input", out="ข้อความ 1 บรรทัด",
         hint='ใช้ `if "phone" in contact:`',
         starter='contact = {"name": "Ann", "city": "Bangkok"}\n\n# เขียนโค้ดตรงนี้',
         code='''contact = {"name": "Ann", "city": "Bangkok"}
if "phone" in contact:
    print("Has phone")
else:
    print("No phone")'''),
    dict(file="05_easy.md", answer="05_loop_keys.py", diff="🟢 Easy",
         name="พิมพ์ทุกคู่ในเมนู", axis="for key in dict",
         title="🍵 Dictionaries — ข้อ 4: พิมพ์เมนู",
         scenario='```python\nmenu = {"tea": 40, "coffee": 50, "cocoa": 45}\n```\n\nพิมพ์ทุกคู่เป็น `key : value`',
         conditions=None, inp="ไม่มี input", out="ทุกคู่ key/value",
         hint="`for key in menu:` แล้วใช้ `menu[key]` — ยังไม่ใช้ `.items()`",
         starter='menu = {"tea": 40, "coffee": 50, "cocoa": 45}\n\n# เขียนโค้ดตรงนี้',
         code='''menu = {"tea": 40, "coffee": 50, "cocoa": 45}
for key in menu:
    print(f"{key} : {menu[key]}")'''),
    dict(file="06_easy.md", answer="06_room_info.py", diff="🟢 Easy",
         name="ข้อมูลห้องเรียน", axis="อ่านหลาย key",
         title="🏫 Dictionaries — ข้อ 5: ข้อมูลห้องเรียน",
         scenario='```python\nroom = {"grade": "M.2", "number": 4, "teacher": "Kru May"}\n```\n\nแสดง Grade / Number / Teacher',
         conditions=None, inp="ไม่มี input", out="3 บรรทัด",
         hint="เข้าถึงทีละ key",
         starter='room = {"grade": "M.2", "number": 4, "teacher": "Kru May"}\n\n# เขียนโค้ดตรงนี้',
         code='''room = {"grade": "M.2", "number": 4, "teacher": "Kru May"}
print(f"Grade: {room['grade']}")
print(f"Number: {room['number']}")
print(f"Teacher: {room['teacher']}")'''),
    dict(file="07_medium.md", answer="07_game_profile.py", diff="🟡 Medium",
         name="โปรไฟล์เกมเพิ่มฟิลด์", axis="เพิ่ม key + ตรวจ in",
         title="🎮 Dictionaries — ข้อ 6: โปรไฟล์เกม",
         scenario='```python\nprofile = {"player": "Ash", "hp": 80}\n```\n\nเพิ่ม `"weapon"` = `"sword"` ถ้ามี weapon แสดงค่า ไม่งั้นแสดง `No weapon`',
         conditions=None, inp="ไม่มี input", out="ชื่ออาวุธหรือข้อความ",
         hint="เพิ่มก่อน แล้วค่อย `in`",
         starter='profile = {"player": "Ash", "hp": 80}\n\n# เขียนโค้ดตรงนี้',
         code='''profile = {"player": "Ash", "hp": 80}
profile["weapon"] = "sword"
if "weapon" in profile:
    print(profile["weapon"])
else:
    print("No weapon")'''),
    dict(file="08_medium.md", answer="08_price_lookup.py", diff="🟡 Medium",
         name="ค้นหาราคาจากชื่อ", axis="in + เข้าถึง + input",
         title="🛒 Dictionaries — ข้อ 7: ค้นหาราคา",
         scenario='```python\nprices = {"apple": 15, "banana": 8, "mango": 25}\n```\n\nรับชื่อผลไม้ ถ้ามีใน dict แสดงราคา ไม่งั้น `Not found`',
         conditions=None, inp="ชื่อผลไม้ 1 บรรทัด", out="ราคาหรือ Not found",
         stdin="banana\n",
         hint='เช็ค `item in prices` ก่อนอ่านค่า',
         starter='prices = {"apple": 15, "banana": 8, "mango": 25}\nitem = input()\n\n# เขียนโค้ดตรงนี้',
         code='''prices = {"apple": 15, "banana": 8, "mango": 25}
item = input()
if item in prices:
    print(prices[item])
else:
    print("Not found")'''),
    dict(file="09_medium.md", answer="09_member_card.py", diff="🟡 Medium",
         name="บัตรสมาชิกร้าน", axis="สร้าง dict + เพิ่ม + วน",
         title="💳 Dictionaries — ข้อ 8: บัตรสมาชิก",
         scenario='สร้าง dict สมาชิกชื่อ `"Nok"` ระดับ `"silver"` แล้วเพิ่ม `"points"` = 300\nพิมพ์ทุกคู่ `key : value`',
         conditions=None, inp="ไม่มี input", out="ทุกฟิลด์ของบัตร",
         hint="สร้าง dict ก่อน เพิ่ม points แล้ววน key",
         starter="# เขียนโค้ดตรงนี้",
         code='''member = {"name": "Nok", "tier": "silver"}
member["points"] = 300
for key in member:
    print(f"{key} : {member[key]}")'''),
    dict(file="10_medium.md", answer="10_order_ticket.py", diff="🟡 Medium",
         name="ตั๋วออเดอร์อาหาร", axis="อ่านค่า + คำนวณ",
         title="🍜 Dictionaries — ข้อ 9: ตั๋วออเดอร์",
         scenario='```python\norder = {"item": "Pad Thai", "price": 60, "qty": 2}\n```\n\nคำนวณยอด `price * qty` แสดง Item และ Total',
         conditions=None, inp="ไม่มี input", out="2 บรรทัด",
         hint="คูณสองค่าจาก dict",
         starter='order = {"item": "Pad Thai", "price": 60, "qty": 2}\n\n# เขียนโค้ดตรงนี้',
         code='''order = {"item": "Pad Thai", "price": 60, "qty": 2}
print(f"Item: {order['item']}")
print(f"Total: {order['price'] * order['qty']}")'''),
    dict(file="11_medium.md", answer="11_settings_panel.py", diff="🟡 Medium",
         name="แผงตั้งค่าแอป", axis="เพิ่มหลาย key + วน",
         title="⚙️ Dictionaries — ข้อ 10: แผงตั้งค่า",
         scenario='```python\nsettings = {"theme": "light"}\n```\n\nเพิ่ม `"sound"` = `"on"` และ `"lang"` = `"th"` แล้วพิมพ์ทุกคู่',
         conditions=None, inp="ไม่มี input", out="ทุกการตั้งค่า",
         hint="เพิ่มทีละ key แล้ว `for key in settings`",
         starter='settings = {"theme": "light"}\n\n# เขียนโค้ดตรงนี้',
         code='''settings = {"theme": "light"}
settings["sound"] = "on"
settings["lang"] = "th"
for key in settings:
    print(f"{key} : {settings[key]}")'''),
    dict(file="12_medium.md", answer="12_safe_score.py", diff="🟡 Medium",
         name="อ่านคะแนนอย่างปลอดภัย", axis="in ก่อนอ่าน",
         title="🛡️ Dictionaries — ข้อ 11: อ่านคะแนนอย่างปลอดภัย",
         scenario='```python\nstudent = {"name": "Ann", "age": 15}\n```\n\nถ้ามี `"score"` แสดงคะแนน ไม่งั้นแสดง `No score yet` และชื่อนักเรียน',
         conditions=None, inp="ไม่มี input", out="สถานะคะแนน + ชื่อ",
         hint="อย่าอ่าน key ที่อาจไม่มีโดยไม่เช็ค",
         starter='student = {"name": "Ann", "age": 15}\n\n# เขียนโค้ดตรงนี้',
         code='''student = {"name": "Ann", "age": 15}
if "score" in student:
    print(student["score"])
else:
    print("No score yet")
print(f"Name: {student['name']}")'''),
    dict(file="13_challenge.md", answer="13_phonebook.py", diff="🔴 Challenge",
         name="สมุดโทรศัพท์ย่อ", axis="เพิ่ม + ค้นหาด้วย input",
         title="📱 Dictionaries — ข้อ 12: สมุดโทรศัพท์",
         scenario='```python\nphonebook = {"Ann": "081-111", "Ben": "082-222"}\n```\n\nเพิ่ม `"Cara": "083-333"` รับชื่อ ถ้ามีเบอร์ให้แสดง ไม่งั้น `Not in phonebook`',
         conditions=None, inp="ชื่อ 1 บรรทัด", out="เบอร์หรือข้อความ",
         stdin="Cara\n",
         hint="เพิ่มก่อน แล้วเช็คชื่อด้วย `in`",
         starter='phonebook = {"Ann": "081-111", "Ben": "082-222"}\nname = input()\n\n# เขียนโค้ดตรงนี้',
         code='''phonebook = {"Ann": "081-111", "Ben": "082-222"}
phonebook["Cara"] = "083-333"
name = input()
if name in phonebook:
    print(phonebook[name])
else:
    print("Not in phonebook")'''),
    dict(file="14_challenge.md", answer="14_cafe_receipt.py", diff="🔴 Challenge",
         name="ใบเสร็จคาเฟ่จาก dict", axis="วน key รวมยอด",
         title="☕ Dictionaries — ข้อ 13: ใบเสร็จคาเฟ่",
         scenario='```python\nprices = {"latte": 65, "muffin": 45, "water": 20}\n```\n\nพิมพ์ทุกเมนู `key : price` รวมยอดทั้งหมด แสดงกรอบสรุปจำนวนรายการและยอด',
         conditions=None, inp="ไม่มี input", out="รายการ + กล่องสรุป",
         hint="สะสม total ตอนวน key พร้อมนับจำนวน",
         starter='prices = {"latte": 65, "muffin": 45, "water": 20}\n\n# เขียนโค้ดตรงนี้',
         code='''prices = {"latte": 65, "muffin": 45, "water": 20}
total = 0
count = 0
for key in prices:
    print(f"{key} : {prices[key]}")
    total += prices[key]
    count += 1

print("========================")
print(f"Items      : {count}")
print(f"Total      : {total}")
print("========================")'''),
    dict(file="15_challenge.md", answer="15_character_sheet.py", diff="🔴 Challenge",
         name="ชีตตัวละคร", axis="หลายฟิลด์ + เงื่อนไขจากค่า",
         title="🗡️ Dictionaries — ข้อ 14: ชีตตัวละคร",
         scenario='```python\nhero = {"name": "Luna", "hp": 40, "mp": 25}\n```\n\nเพิ่ม `"level"` = 5 ถ้า hp < 50 สถานะ `Injured` ไม่งั้น `Ready`\nแสดงกรอบชื่อ เลเวล hp mp สถานะ',
         conditions=None, inp="ไม่มี input", out="กล่องสรุปตัวละคร",
         hint="เพิ่ม level ก่อน แล้วตัดสินจาก hp",
         starter='hero = {"name": "Luna", "hp": 40, "mp": 25}\n\n# เขียนโค้ดตรงนี้',
         code='''hero = {"name": "Luna", "hp": 40, "mp": 25}
hero["level"] = 5
if hero["hp"] < 50:
    status = "Injured"
else:
    status = "Ready"

print("========================")
print("     CHARACTER SHEET")
print("========================")
print(f"Name       : {hero['name']}")
print(f"Level      : {hero['level']}")
print(f"HP         : {hero['hp']}")
print(f"MP         : {hero['mp']}")
print(f"Status     : {status}")
print("========================")'''),
    dict(file="16_challenge.md", answer="16_class_register.py", diff="🔴 Challenge",
         name="ทะเบียนห้องเรียน", axis="dict ของคะแนน + วน + นับผ่าน",
         title="📝 Dictionaries — ข้อ 15: ทะเบียนห้องเรียน",
         scenario='```python\nscores = {"Ann": 72, "Ben": 45, "Cara": 88, "Dan": 50}\n```\n\nพิมพ์ทุกคน `name : score` นับคนที่ได้ >= 50 แสดง `Passed: <จำนวน>`',
         conditions=None, inp="ไม่มี input", out="รายชื่อคะแนน + จำนวนผู้ผ่าน",
         hint="ตอนวน key อ่านคะแนนด้วย `scores[key]`",
         starter='scores = {"Ann": 72, "Ben": 45, "Cara": 88, "Dan": 50}\n\n# เขียนโค้ดตรงนี้',
         code='''scores = {"Ann": 72, "Ben": 45, "Cara": 88, "Dan": 50}
passed = 0
for name in scores:
    print(f"{name} : {scores[name]}")
    if scores[name] >= 50:
        passed += 1
print(f"Passed: {passed}")'''),
    ]
    emit("033-dictionaries", probs, "บท 033 Dictionaries",
         ["dict literal", "`dict[key]`", "เพิ่ม key ด้วย assignment", "`in` ตรวจ key", "`for key in dict:`"],
         ["ห้าม `.keys()` / `.get()` / `.items()` / `.values()` / `del` (หลายตัวยังไม่สอน / ไม่สอนในหลักสูตร)"],
         ["ข้อ `02` ไม่ซ้ำ student Alice / contact Bob จากบทเรียนตรงๆ",
          "วน dict ด้วย `for key in d:` เท่านั้น"])


def gen_034():
    # update, del, .values(), .items() — NO .keys/.get
    probs = [
    dict(file="02_test.md", answer="02_update_level.py", diff="🟢 Easy",
         name="อัปเดตเลเวลผู้เล่น", axis="แก้ค่าด้วย key",
         title="✏️ Dictionary Methods — ข้อ 1: อัปเดตเลเวล",
         scenario='```python\nplayer = {"name": "Ash", "level": 3, "hp": 80}\n```\n\nเปลี่ยน level เป็น 4 แล้วพิมพ์ level ใหม่',
         conditions=None, inp="ไม่มี input", out="1 บรรทัด",
         hint='`player["level"] = 4`',
         starter='player = {"name": "Ash", "level": 3, "hp": 80}\n\n# เขียนโค้ดตรงนี้',
         code='''player = {"name": "Ash", "level": 3, "hp": 80}
player["level"] = 4
print(f"Level: {player['level']}")'''),
    dict(file="03_test.md", answer="03_delete_temp.py", diff="🟢 Easy",
         name="ลบรหัสชั่วคราว", axis="del",
         title="🗑️ Dictionary Methods — ข้อ 2: ลบรหัสชั่วคราว",
         scenario='```python\naccount = {"user": "nok", "temp_code": "1234", "city": "CNX"}\n```\n\nลบ `"temp_code"` แล้วถ้ายังมี key นั้นแสดง `Still there` ไม่งั้น `Removed`',
         conditions=None, inp="ไม่มี input", out="Removed หรือ Still there",
         hint='`del account["temp_code"]` แล้วเช็คด้วย `in`',
         starter='account = {"user": "nok", "temp_code": "1234", "city": "CNX"}\n\n# เขียนโค้ดตรงนี้',
         code='''account = {"user": "nok", "temp_code": "1234", "city": "CNX"}
del account["temp_code"]
if "temp_code" in account:
    print("Still there")
else:
    print("Removed")'''),
    dict(file="04_test.md", answer="04_print_values.py", diff="🟢 Easy",
         name="พิมพ์เฉพาะค่า", axis=".values()",
         title="📤 Dictionary Methods — ข้อ 3: พิมพ์เฉพาะค่า",
         scenario='```python\npet = {"name": "Milo", "type": "dog", "age": 4}\n```\n\nพิมพ์เฉพาะค่าทุกตัวด้วย `.values()`',
         conditions=None, inp="ไม่มี input", out="ค่าทีละบรรทัด",
         hint="`for value in pet.values():`",
         starter='pet = {"name": "Milo", "type": "dog", "age": 4}\n\n# เขียนโค้ดตรงนี้',
         code='''pet = {"name": "Milo", "type": "dog", "age": 4}
for value in pet.values():
    print(value)'''),
    dict(file="05_easy.md", answer="05_items_loop.py", diff="🟢 Easy",
         name="วนคู่ key/value", axis=".items()",
         title="🔗 Dictionary Methods — ข้อ 4: วนคู่ items",
         scenario='```python\nmenu = {"soup": 40, "salad": 55}\n```\n\nใช้ `.items()` พิมพ์ `key: value`',
         conditions=None, inp="ไม่มี input", out="คู่เมนูทีละบรรทัด",
         hint="`for key, value in menu.items():`",
         starter='menu = {"soup": 40, "salad": 55}\n\n# เขียนโค้ดตรงนี้',
         code='''menu = {"soup": 40, "salad": 55}
for key, value in menu.items():
    print(f"{key}: {value}")'''),
    dict(file="06_easy.md", answer="06_update_many.py", diff="🟢 Easy",
         name="อัปเดตหลายฟิลด์พร้อมกัน", axis=".update()",
         title="📦 Dictionary Methods — ข้อ 5: อัปเดตหลายฟิลด์",
         scenario='```python\nstudent = {"name": "Ann", "age": 14, "score": 70}\n```\n\nใช้ `.update` ตั้ง age=15 และ score=85 แล้วพิมพ์ age กับ score',
         conditions=None, inp="ไม่มี input", out="2 บรรทัด",
         hint='`student.update({"age": 15, "score": 85})`',
         starter='student = {"name": "Ann", "age": 14, "score": 70}\n\n# เขียนโค้ดตรงนี้',
         code='''student = {"name": "Ann", "age": 14, "score": 70}
student.update({"age": 15, "score": 85})
print(f"Age: {student['age']}")
print(f"Score: {student['score']}")'''),
    dict(file="07_medium.md", answer="07_contact_editor.py", diff="🟡 Medium",
         name="แก้ผู้ติดต่อ", axis="update + del",
         title="📇 Dictionary Methods — ข้อ 6: แก้ผู้ติดต่อ",
         scenario='```python\ncontact = {"name": "Ben", "phone": "080-000", "note": "temp"}\n```\n\nอัปเดต phone เป็น `081-999` ลบ note แล้ววน `.items()` พิมพ์คู่ที่เหลือ',
         conditions=None, inp="ไม่มี input", out="คู่ที่เหลือหลังแก้",
         hint="update → del → items",
         starter='contact = {"name": "Ben", "phone": "080-000", "note": "temp"}\n\n# เขียนโค้ดตรงนี้',
         code='''contact = {"name": "Ben", "phone": "080-000", "note": "temp"}
contact.update({"phone": "081-999"})
del contact["note"]
for key, value in contact.items():
    print(f"{key}: {value}")'''),
    dict(file="08_medium.md", answer="08_sum_values.py", diff="🟡 Medium",
         name="รวมยอดจาก values", axis=".values() + รวม",
         title="💰 Dictionary Methods — ข้อ 7: รวมยอดจาก values",
         scenario='```python\nbill = {"food": 220, "drink": 80, "dessert": 60}\n```\n\nรวมทุกค่าจาก `.values()` แสดง `Total: <ยอด>`',
         conditions=None, inp="ไม่มี input", out="1 บรรทัดยอดรวม",
         hint="วน values แล้ว +=",
         starter='bill = {"food": 220, "drink": 80, "dessert": 60}\n\n# เขียนโค้ดตรงนี้',
         code='''bill = {"food": 220, "drink": 80, "dessert": 60}
total = 0
for value in bill.values():
    total += value
print(f"Total: {total}")'''),
    dict(file="09_medium.md", answer="09_stock_fix.py", diff="🟡 Medium",
         name="อัปเดตสต็อกสินค้า", axis="update หลายชิ้น + items",
         title="📦 Dictionary Methods — ข้อ 8: อัปเดตสต็อก",
         scenario='```python\nstock = {"pen": 10, "ink": 4, "paper": 25}\n```\n\nใช้ update ตั้ง pen=12, ink=6 แล้วพิมพ์ทุกคู่ด้วย items',
         conditions=None, inp="ไม่มี input", out="สต็อกหลังอัปเดต",
         hint="update ก่อน แล้ว items",
         starter='stock = {"pen": 10, "ink": 4, "paper": 25}\n\n# เขียนโค้ดตรงนี้',
         code='''stock = {"pen": 10, "ink": 4, "paper": 25}
stock.update({"pen": 12, "ink": 6})
for key, value in stock.items():
    print(f"{key}: {value}")'''),
    dict(file="10_medium.md", answer="10_remove_and_list.py", diff="🟡 Medium",
         name="ลบฟิลด์แล้วโชว์ค่าที่เหลือ", axis="del + values",
         title="🧹 Dictionary Methods — ข้อ 9: ลบแล้วโชว์ค่า",
         scenario='```python\nprofile = {"name": "Cara", "draft": True, "city": "KKU"}\n```\n\nลบ draft แล้วพิมพ์เฉพาะค่าที่เหลือ',
         conditions=None, inp="ไม่มี input", out="ค่าที่เหลือทีละบรรทัด",
         hint="del แล้ววน values",
         starter='profile = {"name": "Cara", "draft": True, "city": "KKU"}\n\n# เขียนโค้ดตรงนี้',
         code='''profile = {"name": "Cara", "draft": True, "city": "KKU"}
del profile["draft"]
for value in profile.values():
    print(value)'''),
    dict(file="11_medium.md", answer="11_price_tags_items.py", diff="🟡 Medium",
         name="ป้ายราคาด้วย items", axis="items + จัดรูปแบบ",
         title="🏷️ Dictionary Methods — ข้อ 10: ป้ายราคา",
         scenario='```python\nprices = {"book": 120, "bag": 350, "gum": 10}\n```\n\nพิมพ์ `book costs 120` แบบใช้ items',
         conditions=None, inp="ไม่มี input", out="ป้ายราคาทีละบรรทัด",
         hint="ใช้ทั้ง key และ value จาก items",
         starter='prices = {"book": 120, "bag": 350, "gum": 10}\n\n# เขียนโค้ดตรงนี้',
         code='''prices = {"book": 120, "bag": 350, "gum": 10}
for key, value in prices.items():
    print(f"{key} costs {value}")'''),
    dict(file="12_medium.md", answer="12_grade_curve.py", diff="🟡 Medium",
         name="ปรับเกรดทั้งห้อง", axis="items + แก้ค่าทีละคน",
         title="📈 Dictionary Methods — ข้อ 11: ปรับเกรด",
         scenario='```python\nscores = {"Ann": 70, "Ben": 82, "Cara": 65}\n```\n\nบวกคะแนนให้ทุกคน +5 ด้วยการวน items แล้วกำหนดค่าใหม่ แสดงคะแนนหลังปรับด้วย items',
         conditions=None, inp="ไม่มี input", out="คะแนนหลังปรับ",
         hint='ใน loop ทำ `scores[name] = score + 5`',
         starter='scores = {"Ann": 70, "Ben": 82, "Cara": 65}\n\n# เขียนโค้ดตรงนี้',
         code='''scores = {"Ann": 70, "Ben": 82, "Cara": 65}
for name, score in scores.items():
    scores[name] = score + 5
for name, score in scores.items():
    print(f"{name}: {score}")'''),
    dict(file="13_challenge.md", answer="13_order_manager.py", diff="🔴 Challenge",
         name="ตัวจัดการออเดอร์", axis="update + del + values รวม",
         title="🧾 Dictionary Methods — ข้อ 12: ตัวจัดการออเดอร์",
         scenario='```python\norder = {"soup": 40, "rice": 25, "note": "less spicy", "tea": 30}\n```\n\nอัปเดต rice=30 ลบ note รวมเฉพาะค่าตัวเลขที่เหลือ แสดงรายการด้วย items และ Total',
         conditions=None, inp="ไม่มี input", out="รายการ + Total",
         hint="ลบ note ก่อนค่อยรวม values",
         starter='order = {"soup": 40, "rice": 25, "note": "less spicy", "tea": 30}\n\n# เขียนโค้ดตรงนี้',
         code='''order = {"soup": 40, "rice": 25, "note": "less spicy", "tea": 30}
order.update({"rice": 30})
del order["note"]
for key, value in order.items():
    print(f"{key}: {value}")
total = 0
for value in order.values():
    total += value
print(f"Total: {total}")'''),
    dict(file="14_challenge.md", answer="14_user_settings.py", diff="🔴 Challenge",
         name="ตั้งค่าผู้ใช้ครบวงจร", axis="update + del + items กรอบ",
         title="⚙️ Dictionary Methods — ข้อ 13: ตั้งค่าผู้ใช้",
         scenario='```python\nsettings = {"theme": "light", "temp_flag": 1, "lang": "en"}\n```\n\nupdate theme=dark และ lang=th ลบ temp_flag แสดงกรอบทุกคู่ที่เหลือ',
         conditions=None, inp="ไม่มี input", out="กล่องการตั้งค่า",
         hint="ทำครบสามขั้นก่อนพิมพ์กรอบ",
         starter='settings = {"theme": "light", "temp_flag": 1, "lang": "en"}\n\n# เขียนโค้ดตรงนี้',
         code='''settings = {"theme": "light", "temp_flag": 1, "lang": "en"}
settings.update({"theme": "dark", "lang": "th"})
del settings["temp_flag"]

print("========================")
print("       SETTINGS")
print("========================")
for key, value in settings.items():
    print(f"{key:<10} : {value}")
print("========================")'''),
    dict(file="15_challenge.md", answer="15_inventory_desk.py", diff="🔴 Challenge",
         name="โต๊ะสต็อกขั้นสูง", axis="update + นับค่าต่ำ + items",
         title="📦 Dictionary Methods — ข้อ 14: โต๊ะสต็อก",
         scenario='```python\nstock = {"pen": 3, "ink": 12, "glue": 2, "tape": 9}\n```\n\nupdate pen=5 แล้ววน items นับสินค้าที่เหลือ < 5 แสดงรายการทั้งหมดและ `Low stock: <จำนวน>`',
         conditions=None, inp="ไม่มี input", out="รายการ + จำนวนสต็อกต่ำ",
         hint="อัปเดตก่อน แล้วนับตอนวน",
         starter='stock = {"pen": 3, "ink": 12, "glue": 2, "tape": 9}\n\n# เขียนโค้ดตรงนี้',
         code='''stock = {"pen": 3, "ink": 12, "glue": 2, "tape": 9}
stock.update({"pen": 5})
low = 0
for key, value in stock.items():
    print(f"{key}: {value}")
    if value < 5:
        low += 1
print(f"Low stock: {low}")'''),
    dict(file="16_challenge.md", answer="16_score_board.py", diff="🔴 Challenge",
         name="บอร์ดคะแนนหลังลบผู้เล่น", axis="del + values สรุป + items",
         title="🏁 Dictionary Methods — ข้อ 15: บอร์ดคะแนน",
         scenario='```python\nscores = {"Ann": 80, "Ben": 95, "Cara": 70, "Dan": 60}\n```\n\nลบ Dan รวมคะแนนที่เหลือด้วย values หาค่าเฉลี่ย แสดงรายชื่อด้วย items และกรอบสรุป',
         conditions=None, inp="ไม่มี input", out="รายชื่อ + กล่องสรุป",
         hint="del ก่อน แล้วค่อยรวมและหาร len ด้วยการนับตอนวน",
         starter='scores = {"Ann": 80, "Ben": 95, "Cara": 70, "Dan": 60}\n\n# เขียนโค้ดตรงนี้',
         code='''scores = {"Ann": 80, "Ben": 95, "Cara": 70, "Dan": 60}
del scores["Dan"]

for name, score in scores.items():
    print(f"{name}: {score}")

total = 0
count = 0
for value in scores.values():
    total += value
    count += 1
average = total / count

print("========================")
print(f"Players    : {count}")
print(f"Total      : {total}")
print(f"Average    : {average}")
print("========================")'''),
    ]
    emit("034-dictionary-methods", probs, "บท 034 Dictionary Methods",
         ["แก้ค่าด้วย key", "`.update()`", "`del`", "`.values()`", "`.items()`"],
         ["ห้าม `.keys()` / `.get()` (ไม่สอนในหลักสูตร)"],
         ["ข้อ `02` ไม่ซ้ำ student age update จากบทเรียนตรงๆ",
          "`.items()` ให้สองตัวแปร `for key, value in ...`"])


def gen_035():
    # Keep best 035 ideas reformatted: word count, quiz, shopping, inventory,
    # pet/student cards, login, frequency fruit, smoothie, weather, game bag, etc.
    # input("prompt") OK; frequency counting OK; empty {} OK
    probs = [
    dict(file="02_test.md", answer="02_student_card.py", diff="🟢 Easy",
         name="บัตรนักเรียนสั้น", axis="สร้าง dict + อ่าน",
         title="🪪 Dictionary Practice — ข้อ 1: บัตรนักเรียน",
         scenario='สร้างบัตรนักเรียน `name=Mali`, `age=14`, `room=2/3` แล้วแสดงสามบรรทัด',
         conditions=None, inp="ไม่มี input", out="Name / Age / Room",
         hint="สร้าง dict แล้วอ่านทีละ key",
         starter="# เขียนโค้ดตรงนี้",
         code='''student = {"name": "Mali", "age": 14, "room": "2/3"}
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Room: {student['room']}")'''),
    dict(file="03_test.md", answer="03_pet_card.py", diff="🟢 Easy",
         name="การ์ดสัตว์เลี้ยง", axis="dict อ่านค่า",
         title="🐶 Dictionary Practice — ข้อ 2: การ์ดสัตว์เลี้ยง",
         scenario='```python\npet = {"name": "Bao", "type": "dog", "age": 3}\n```\n\nแสดงชื่อและชนิด',
         conditions=None, inp="ไม่มี input", out="2 บรรทัด",
         hint="อ่านด้วย key",
         starter='pet = {"name": "Bao", "type": "dog", "age": 3}\n\n# เขียนโค้ดตรงนี้',
         code='''pet = {"name": "Bao", "type": "dog", "age": 3}
print(f"Name: {pet['name']}")
print(f"Type: {pet['type']}")'''),
    dict(file="04_test.md", answer="04_add_phone.py", diff="🟢 Easy",
         name="เพิ่มเบอร์โทร", axis="เพิ่ม key",
         title="📱 Dictionary Practice — ข้อ 3: เพิ่มเบอร์โทร",
         scenario='```python\ncontact = {"name": "Ann", "city": "Bangkok"}\n```\n\nเพิ่ม phone=`081-234-5678` แล้วพิมพ์เบอร์',
         conditions=None, inp="ไม่มี input", out="เบอร์โทร 1 บรรทัด",
         hint="กำหนด key ใหม่ด้วย assignment",
         starter='contact = {"name": "Ann", "city": "Bangkok"}\n\n# เขียนโค้ดตรงนี้',
         code='''contact = {"name": "Ann", "city": "Bangkok"}
contact["phone"] = "081-234-5678"
print(contact["phone"])'''),
    dict(file="05_easy.md", answer="05_update_score.py", diff="🟢 Easy",
         name="อัปเดตคะแนนเกม", axis="แก้ค่า + items",
         title="🎯 Dictionary Practice — ข้อ 4: อัปเดตคะแนนเกม",
         scenario='```python\nplayer = {"name": "Bee", "score": 500}\n```\n\nเปลี่ยน score เป็น 750 แล้วพิมพ์ด้วย items',
         conditions=None, inp="ไม่มี input", out="คู่ key/value",
         hint="แก้ค่าแล้ววน items",
         starter='player = {"name": "Bee", "score": 500}\n\n# เขียนโค้ดตรงนี้',
         code='''player = {"name": "Bee", "score": 500}
player["score"] = 750
for key, value in player.items():
    print(f"{key}: {value}")'''),
    dict(file="06_easy.md", answer="06_in_stock.py", diff="🟢 Easy",
         name="มีสินค้านี้ไหม", axis="in + input prompt",
         title="🏬 Dictionary Practice — ข้อ 5: มีสินค้านี้ไหม",
         scenario='```python\nstock = {"pen": 12, "ink": 4, "glue": 7}\n```\n\nใช้ `input("Item: ")` รับชื่อสินค้า ถ้ามีแสดงจำนวน ไม่งั้น `Out of stock`',
         conditions=None, inp="ชื่อสินค้า (มี prompt)", out="จำนวนหรือ Out of stock",
         stdin="ink\n",
         hint="บทนี้ใช้ `input(\"...\")` ที่มีข้อความได้",
         starter='stock = {"pen": 12, "ink": 4, "glue": 7}\nitem = input("Item: ")\n\n# เขียนโค้ดตรงนี้',
         code='''stock = {"pen": 12, "ink": 4, "glue": 7}
item = input("Item: ")
if item in stock:
    print(stock[item])
else:
    print("Out of stock")'''),
    dict(file="07_medium.md", answer="07_word_count.py", diff="🟡 Medium",
         name="นับคำซ้ำ", axis="frequency counting",
         title="📊 Dictionary Practice — ข้อ 6: นับคำซ้ำ",
         scenario='```python\nwords = ["cat", "dog", "cat", "bird", "dog", "cat"]\n```\n\nนับความถี่ด้วย dict ว่าง แล้วพิมพ์ `word: count` ด้วย items',
         conditions=None, inp="ไม่มี input", out="ความถี่แต่ละคำ",
         hint="ถ้ามีใน dict แล้ว `+= 1` ถ้ายังไม่มีตั้งเป็น 1",
         starter='words = ["cat", "dog", "cat", "bird", "dog", "cat"]\ncount = {}\n\n# เขียนโค้ดตรงนี้',
         code='''words = ["cat", "dog", "cat", "bird", "dog", "cat"]
count = {}
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
for word, n in count.items():
    print(f"{word}: {n}")'''),
    dict(file="08_medium.md", answer="08_fruit_count.py", diff="🟡 Medium",
         name="นับผลไม้ในตะกร้า", axis="frequency counting",
         title="🍎 Dictionary Practice — ข้อ 7: นับผลไม้ในตะกร้า",
         scenario='```python\nbasket = ["apple", "banana", "apple", "apple", "banana", "mango"]\n```\n\nนับจำนวนแต่ละชนิด แล้วพิมพ์ผล',
         conditions=None, inp="ไม่มี input", out="ความถี่ผลไม้",
         hint="แพทเทิร์นเดียวกับนับคำ",
         starter='basket = ["apple", "banana", "apple", "apple", "banana", "mango"]\ncount = {}\n\n# เขียนโค้ดตรงนี้',
         code='''basket = ["apple", "banana", "apple", "apple", "banana", "mango"]
count = {}
for fruit in basket:
    if fruit in count:
        count[fruit] += 1
    else:
        count[fruit] = 1
for fruit, n in count.items():
    print(f"{fruit}: {n}")'''),
    dict(file="09_medium.md", answer="09_quiz_check.py", diff="🟡 Medium",
         name="ตรวจข้อสอบช้อยส์", axis="input prompt + เทียบคำตอบ",
         title="❓ Dictionary Practice — ข้อ 8: ตรวจข้อสอบ",
         scenario='```python\nanswers = {"q1": "A", "q2": "C", "q3": "B"}\n```\n\nใช้ `input("q1: ")` รับคำตอบข้อแรก ถ้าถูกแสดง `Correct` ไม่งั้น `Wrong` พร้อมเฉลย',
         conditions=None, inp="คำตอบ q1 (มี prompt)", out="ผลตรวจ 1–2 บรรทัด",
         stdin="A\n",
         hint="เทียบกับ `answers[\"q1\"]`",
         starter='answers = {"q1": "A", "q2": "C", "q3": "B"}\nuser = input("q1: ")\n\n# เขียนโค้ดตรงนี้',
         code='''answers = {"q1": "A", "q2": "C", "q3": "B"}
user = input("q1: ")
if user == answers["q1"]:
    print("Correct")
else:
    print("Wrong")
    print(f"Answer: {answers['q1']}")'''),
    dict(file="10_medium.md", answer="10_smoothie_order.py", diff="🟡 Medium",
         name="สั่งน้ำปั่นหนึ่งแก้ว", axis="เมนู dict + input prompt",
         title="🥤 Dictionary Practice — ข้อ 9: สั่งน้ำปั่น",
         scenario='```python\nmenu = {"mango": 45, "berry": 50, "banana": 40}\n```\n\nรับชื่อเมนูด้วย `input("Drink: ")` ถ้ามีแสดงราคา ไม่งั้น `No such drink`',
         conditions=None, inp="ชื่อเครื่องดื่ม", out="ราคาหรือข้อความ",
         stdin="berry\n",
         hint="เช็ค `in` ก่อนอ่านราคา",
         starter='menu = {"mango": 45, "berry": 50, "banana": 40}\ndrink = input("Drink: ")\n\n# เขียนโค้ดตรงนี้',
         code='''menu = {"mango": 45, "berry": 50, "banana": 40}
drink = input("Drink: ")
if drink in menu:
    print(menu[drink])
else:
    print("No such drink")'''),
    dict(file="11_medium.md", answer="11_weather_cities.py", diff="🟡 Medium",
         name="อากาศแต่ละเมือง", axis="items แสดงตาราง",
         title="🌤️ Dictionary Practice — ข้อ 10: อากาศแต่ละเมือง",
         scenario='```python\nweather = {"Bangkok": 34, "Chiang Mai": 30, "Phuket": 32}\n```\n\nพิมพ์ `City: Temp C` ทุกเมืองด้วย items',
         conditions=None, inp="ไม่มี input", out="อุณหภูมิทุกเมือง",
         hint="วน items",
         starter='weather = {"Bangkok": 34, "Chiang Mai": 30, "Phuket": 32}\n\n# เขียนโค้ดตรงนี้',
         code='''weather = {"Bangkok": 34, "Chiang Mai": 30, "Phuket": 32}
for city, temp in weather.items():
    print(f"{city}: {temp} C")'''),
    dict(file="12_medium.md", answer="12_shopping_total.py", diff="🟡 Medium",
         name="รวมยอดตะกร้าจากราคา", axis="items + รวมยอด",
         title="🛒 Dictionary Practice — ข้อ 11: รวมยอดตะกร้า",
         scenario='```python\nprices = {"apple": 15, "banana": 8, "mango": 25}\n```\n\nพิมพ์ทุกรายการ แล้วแสดงยอดรวม',
         conditions=None, inp="ไม่มี input", out="รายการ + Total",
         hint="สะสม total ตอนวน items",
         starter='prices = {"apple": 15, "banana": 8, "mango": 25}\n\n# เขียนโค้ดตรงนี้',
         code='''prices = {"apple": 15, "banana": 8, "mango": 25}
total = 0
for item, price in prices.items():
    print(f"{item}: {price}")
    total += price
print(f"Total: {total}")'''),
    dict(file="13_challenge.md", answer="13_login.py", diff="🔴 Challenge",
         name="ล็อกอินเข้าแอพ", axis="input prompt สองค่า + ตรวจ dict",
         title="🔐 Dictionary Practice — ข้อ 12: ล็อกอิน",
         scenario='```python\nusers = {"ann": "1234", "ben": "abcd"}\n```\n\nรับ username ด้วย `input("User: ")` และ password ด้วย `input("Pass: ")`\nถ้ามี user และรหัสตรง แสดง `Welcome` ไม่งั้น `Login failed`',
         conditions=None, inp="2 บรรทัด User/Pass", out="Welcome หรือ Login failed",
         stdin="ann\n1234\n",
         hint="เช็ค user in users ก่อน แล้วค่อยเทียบรหัส",
         starter='users = {"ann": "1234", "ben": "abcd"}\nuser = input("User: ")\npassword = input("Pass: ")\n\n# เขียนโค้ดตรงนี้',
         code='''users = {"ann": "1234", "ben": "abcd"}
user = input("User: ")
password = input("Pass: ")
if user in users:
    if password == users[user]:
        print("Welcome")
    else:
        print("Login failed")
else:
    print("Login failed")'''),
    dict(file="14_challenge.md", answer="14_game_bag.py", diff="🔴 Challenge",
         name="ตะกร้าของในเกม", axis="เพิ่ม/อัปเดตจำนวนไอเท็ม",
         title="🎒 Dictionary Practice — ข้อ 13: ตะกร้าของในเกม",
         scenario='```python\nbag = {"potion": 2, "key": 1}\n```\n\nถ้ามี potion อยู่แล้วให้ +1 ไม่งั้นตั้งเป็น 1 (จำลองการเก็บของ)\nเพิ่ม `"map"` = 1 ลบ `"key"` แสดง bag ด้วย items',
         conditions=None, inp="ไม่มี input", out="ไอเท็มที่เหลือ",
         hint="แพทเทิร์นเดียวกับ frequency สำหรับ potion",
         starter='bag = {"potion": 2, "key": 1}\n\n# เขียนโค้ดตรงนี้',
         code='''bag = {"potion": 2, "key": 1}
if "potion" in bag:
    bag["potion"] += 1
else:
    bag["potion"] = 1
bag["map"] = 1
del bag["key"]
for item, n in bag.items():
    print(f"{item}: {n}")'''),
    dict(file="15_challenge.md", answer="15_two_item_order.py", diff="🔴 Challenge",
         name="สั่งของสองชิ้น", axis="สอง input + รวมราคา",
         title="🛍️ Dictionary Practice — ข้อ 14: สั่งของสองชิ้น",
         scenario='```python\nprices = {"pen": 10, "book": 80, "bag": 250}\n```\n\nรับสินค้าสองชิ้นด้วย `input("Item1: ")` และ `input("Item2: ")`\nถ้าชิ้นใดไม่มี ให้พิมพ์ `Missing item` แล้วจบ\nถ้ามีทั้งคู่พิมพ์ราคาแต่ละชิ้นและยอดรวม',
         conditions=None, inp="2 บรรทัดชื่อสินค้า", out="ราคาและยอด หรือ Missing item",
         stdin="pen\nbag\n",
         hint="เช็คทั้งสองชื่อด้วย `in` ก่อนคำนวณ",
         starter='prices = {"pen": 10, "book": 80, "bag": 250}\nitem1 = input("Item1: ")\nitem2 = input("Item2: ")\n\n# เขียนโค้ดตรงนี้',
         code='''prices = {"pen": 10, "book": 80, "bag": 250}
item1 = input("Item1: ")
item2 = input("Item2: ")
if item1 in prices:
    if item2 in prices:
        print(f"{item1}: {prices[item1]}")
        print(f"{item2}: {prices[item2]}")
        print(f"Total: {prices[item1] + prices[item2]}")
    else:
        print("Missing item")
else:
    print("Missing item")'''),
    dict(file="16_challenge.md", answer="16_inventory_system.py", diff="🔴 Challenge",
         name="ระบบคลังสินค้าย่อ", axis="update + ความถี่จากออเดอร์ + สรุป",
         title="📦 Dictionary Practice — ข้อ 15: ระบบคลังสินค้า",
         scenario='```python\nstock = {"pen": 5, "ink": 2}\norders = ["pen", "pen", "eraser", "ink", "pen"]\n```\n\nนับออเดอร์ด้วย frequency dict แล้วสำหรับทุกสินค้าใน stock ถ้าถูกสั่งให้ลดสต็อกลงตามจำนวนที่สั่ง (สมมติสต็อกพอ)\nเพิ่ม eraser ใน stock ตามจำนวนที่ถูกสั่งด้วย update หรือ assignment\nแสดง stock สุดท้ายด้วย items และจำนวนชนิดสินค้า',
         conditions=None, inp="ไม่มี input", out="สต็อกสุดท้าย + ชนิดสินค้า",
         hint="นับ orders ก่อน แล้วค่อยปรับ stock ตามยอดที่นับได้",
         starter='stock = {"pen": 5, "ink": 2}\norders = ["pen", "pen", "eraser", "ink", "pen"]\n\n# เขียนโค้ดตรงนี้',
         code='''stock = {"pen": 5, "ink": 2}
orders = ["pen", "pen", "eraser", "ink", "pen"]

count = {}
for item in orders:
    if item in count:
        count[item] += 1
    else:
        count[item] = 1

for item in count:
    if item in stock:
        stock[item] = stock[item] - count[item]
    else:
        stock[item] = count[item]

for item, n in stock.items():
    print(f"{item}: {n}")

kinds = 0
for item in stock:
    kinds += 1
print(f"Kinds: {kinds}")'''),
    ]
    emit("035-dictionary-practice", probs, "บท 035 Dictionary Practice",
         ["ฝึก dict จากบท 033–034", "`input(\"prompt\")` (ครั้งแรกในหลักสูตร)", "frequency counting จาก dict ว่าง `{}`"],
         ["ห้าม `.keys()` / `.get()`", "ห้าม `max()` — เก็บแพทเทิร์นหาค่าสูงสุดไว้บท 036"],
         ["เหลือ 15 ข้อพอดี (ลดจากชุดเดิมที่เกิน)",
          "เก็บไอเดียเด่น: นับคำ/ผลไม้, ควิซ, ล็อกอิน, น้ำปั่น, คลัง, สั่งของ 2 ชิ้น"])


def gen_036():
    # Review; max-finding by loop OK; NO builtin max()
    # Avoid duplicating lesson top-scorer Alice/Bob/Charlie 88/72/95
    probs = [
    dict(file="02_test.md", answer="02_safe_access.py", diff="🟢 Easy",
         name="อ่านค่าอย่างปลอดภัย", axis="in ก่อนอ่าน",
         title="🛡️ Review Dictionaries — ข้อ 1: อ่านค่าอย่างปลอดภัย",
         scenario='```python\nstudent = {"name": "Nok", "room": "3/1"}\n```\n\nถ้ามี score แสดงคะแนน ไม่งั้น `No score yet`',
         conditions=None, inp="ไม่มี input", out="1 บรรทัด",
         hint="ใช้ `in` เสมอตอนไม่แน่ใจว่ามี key",
         starter='student = {"name": "Nok", "room": "3/1"}\n\n# เขียนโค้ดตรงนี้',
         code='''student = {"name": "Nok", "room": "3/1"}
if "score" in student:
    print(student["score"])
else:
    print("No score yet")'''),
    dict(file="03_test.md", answer="03_build_from_lists.py", diff="🟢 Easy",
         name="สร้าง dict จากสอง list", axis="range(len) ใส่คู่",
         title="🧱 Review Dictionaries — ข้อ 2: สร้าง dict จาก list",
         scenario='```python\nnames = ["Ann", "Ben", "Cara"]\nscores = [80, 70, 90]\n```\n\nสร้าง dict ชื่อ→คะแนน แล้วพิมพ์ด้วย items',
         conditions=None, inp="ไม่มี input", out="คู่ชื่อคะแนน",
         hint="ใช้ index คู่ขนาน",
         starter='names = ["Ann", "Ben", "Cara"]\nscores = [80, 70, 90]\n\n# เขียนโค้ดตรงนี้',
         code='''names = ["Ann", "Ben", "Cara"]
scores = [80, 70, 90]
result = {}
for i in range(len(names)):
    result[names[i]] = scores[i]
for name, score in result.items():
    print(f"{name}: {score}")'''),
    dict(file="04_test.md", answer="04_merge_update.py", diff="🟢 Easy",
         name="รวมสอง dict ด้วย update", axis=".update()",
         title="🤝 Review Dictionaries — ข้อ 3: รวมสอง dict",
         scenario='```python\nbase = {"name": "Ann", "age": 15}\nextra = {"score": 88, "city": "BKK"}\n```\n\nรวม extra เข้า base ด้วย update แล้วพิมพ์ items',
         conditions=None, inp="ไม่มี input", out="ทุกคู่หลังรวม",
         hint="`base.update(extra)`",
         starter='base = {"name": "Ann", "age": 15}\nextra = {"score": 88, "city": "BKK"}\n\n# เขียนโค้ดตรงนี้',
         code='''base = {"name": "Ann", "age": 15}
extra = {"score": 88, "city": "BKK"}
base.update(extra)
for key, value in base.items():
    print(f"{key}: {value}")'''),
    dict(file="05_easy.md", answer="05_delete_field.py", diff="🟢 Easy",
         name="ลบฟิลด์แล้วตรวจ", axis="del + in",
         title="🗑️ Review Dictionaries — ข้อ 4: ลบฟิลด์",
         scenario='```python\nprofile = {"user": "bee", "temp": 1, "city": "CNX"}\n```\n\nลบ temp แล้วตอบว่ายังมี temp อยู่หรือไม่เป็น True/False',
         conditions=None, inp="ไม่มี input", out="True หรือ False",
         hint="พิมพ์ผลของ `\"temp\" in profile` หลัง del",
         starter='profile = {"user": "bee", "temp": 1, "city": "CNX"}\n\n# เขียนโค้ดตรงนี้',
         code='''profile = {"user": "bee", "temp": 1, "city": "CNX"}
del profile["temp"]
print("temp" in profile)'''),
    dict(file="06_easy.md", answer="06_sum_values.py", diff="🟢 Easy",
         name="รวมค่า values", axis=".values()",
         title="➕ Review Dictionaries — ข้อ 5: รวมค่า values",
         scenario='```python\npoints = {"stage1": 10, "stage2": 20, "stage3": 15}\n```\n\nรวมคะแนนทุกด่าน แสดง Total',
         conditions=None, inp="ไม่มี input", out="Total",
         hint="วน values",
         starter='points = {"stage1": 10, "stage2": 20, "stage3": 15}\n\n# เขียนโค้ดตรงนี้',
         code='''points = {"stage1": 10, "stage2": 20, "stage3": 15}
total = 0
for value in points.values():
    total += value
print(f"Total: {total}")'''),
    dict(file="07_medium.md", answer="07_top_product.py", diff="🟡 Medium",
         name="หาสินค้าขายดีสุด", axis="max-finding ด้วย loop",
         title="🏆 Review Dictionaries — ข้อ 6: สินค้าขายดีสุด",
         scenario='```python\nsales = {"pen": 40, "book": 25, "bag": 55, "gum": 10}\n```\n\nหาสินค้าที่ยอดสูงสุดด้วย loop (ห้าม `max()`) แสดง `Top: bag (55)`',
         conditions=None, inp="ไม่มี input", out="สินค้าขายดีสุด",
         hint="เก็บชื่อและค่ายอดสูงสุด ตอนวน items",
         starter='sales = {"pen": 40, "book": 25, "bag": 55, "gum": 10}\n\n# เขียนโค้ดตรงนี้',
         code='''sales = {"pen": 40, "book": 25, "bag": 55, "gum": 10}
top_item = ""
top_value = 0
for item, value in sales.items():
    if value > top_value:
        top_value = value
        top_item = item
print(f"Top: {top_item} ({top_value})")'''),
    dict(file="08_medium.md", answer="08_frequency_colors.py", diff="🟡 Medium",
         name="นับสีลูกปัด", axis="frequency + items",
         title="🎨 Review Dictionaries — ข้อ 7: นับสีลูกปัด",
         scenario='```python\nbeads = ["red", "blue", "red", "green", "blue", "red"]\n```\n\nนับความถี่แล้วพิมพ์ผล',
         conditions=None, inp="ไม่มี input", out="ความถี่สี",
         hint="dict ว่าง + in",
         starter='beads = ["red", "blue", "red", "green", "blue", "red"]\ncount = {}\n\n# เขียนโค้ดตรงนี้',
         code='''beads = ["red", "blue", "red", "green", "blue", "red"]
count = {}
for color in beads:
    if color in count:
        count[color] += 1
    else:
        count[color] = 1
for color, n in count.items():
    print(f"{color}: {n}")'''),
    dict(file="09_medium.md", answer="09_pass_filter.py", diff="🟡 Medium",
         name="คัดรายชื่อผู้ผ่าน", axis="items + สร้าง dict ใหม่",
         title="✅ Review Dictionaries — ข้อ 8: คัดผู้ผ่าน",
         scenario='```python\nscores = {"Ann": 45, "Ben": 72, "Cara": 88, "Dan": 50}\n```\n\nสร้าง dict ใหม่เฉพาะคนที่ได้ >= 50 แล้วพิมพ์',
         conditions=None, inp="ไม่มี input", out="ผู้ผ่านเท่านั้น",
         hint="สร้าง dict ว่าง แล้วใส่เฉพาะคนที่ผ่าน",
         starter='scores = {"Ann": 45, "Ben": 72, "Cara": 88, "Dan": 50}\n\n# เขียนโค้ดตรงนี้',
         code='''scores = {"Ann": 45, "Ben": 72, "Cara": 88, "Dan": 50}
passed = {}
for name, score in scores.items():
    if score >= 50:
        passed[name] = score
for name, score in passed.items():
    print(f"{name}: {score}")'''),
    dict(file="10_medium.md", answer="10_avg_and_status.py", diff="🟡 Medium",
         name="ค่าเฉลี่ยและสถานะห้อง", axis="values + average + if",
         title="📊 Review Dictionaries — ข้อ 9: ค่าเฉลี่ยห้อง",
         scenario='```python\nscores = {"Ann": 80, "Ben": 70, "Cara": 90}\n```\n\nหาค่าเฉลี่ย ถ้า >= 80 สถานะ Strong ไม่งั้น Normal แสดงทั้งสองอย่าง',
         conditions=None, inp="ไม่มี input", out="Average + Status",
         hint="รวม values นับจำนวน แล้วตัดสิน",
         starter='scores = {"Ann": 80, "Ben": 70, "Cara": 90}\n\n# เขียนโค้ดตรงนี้',
         code='''scores = {"Ann": 80, "Ben": 70, "Cara": 90}
total = 0
count = 0
for value in scores.values():
    total += value
    count += 1
average = total / count
if average >= 80:
    status = "Strong"
else:
    status = "Normal"
print(f"Average: {average}")
print(f"Status: {status}")'''),
    dict(file="11_medium.md", answer="11_price_lookup_prompt.py", diff="🟡 Medium",
         name="ค้นราคาแบบมี prompt", axis="input prompt + in",
         title="🔎 Review Dictionaries — ข้อ 10: ค้นราคา",
         scenario='```python\nprices = {"tea": 40, "coffee": 55, "juice": 45}\n```\n\nรับเมนูด้วย `input("Menu: ")` แสดงราคาหรือ Not found',
         conditions=None, inp="ชื่อเมนู", out="ราคาหรือ Not found",
         stdin="coffee\n",
         hint="ใช้ prompt ได้เพราะเรียนแล้วใน 035",
         starter='prices = {"tea": 40, "coffee": 55, "juice": 45}\nitem = input("Menu: ")\n\n# เขียนโค้ดตรงนี้',
         code='''prices = {"tea": 40, "coffee": 55, "juice": 45}
item = input("Menu: ")
if item in prices:
    print(prices[item])
else:
    print("Not found")'''),
    dict(file="12_medium.md", answer="12_update_then_top.py", diff="🟡 Medium",
         name="อัปเดตแล้วหาค่าสูงสุด", axis="update + max loop",
         title="🚀 Review Dictionaries — ข้อ 11: อัปเดตแล้วหา Top",
         scenario='```python\nscores = {" ann": 1}\n```',
         # will fix below
         conditions=None, inp="ไม่มี input", out="...",
         hint="...",
         starter="...",
         code="print(1)"),
    ]
    # Fix problem 12 properly
    probs[10] = dict(file="12_medium.md", answer="12_update_then_top.py", diff="🟡 Medium",
         name="อัปเดตแล้วหาค่าสูงสุด", axis="update + max loop",
         title="🚀 Review Dictionaries — ข้อ 11: อัปเดตแล้วหา Top",
         scenario='```python\nscores = {"Ann": 70, "Ben": 85, "Cara": 78}\n```\n\nใช้ update ตั้ง Ben=90 แล้วหาคนคะแนนสูงสุดด้วย loop แสดง `Top: <ชื่อ> (<คะแนน>)`',
         conditions=None, inp="ไม่มี input", out="ผู้ได้คะแนนสูงสุด",
         hint="อัปเดตก่อน แล้วค่อยวนหาค่าสูงสุดเอง",
         starter='scores = {"Ann": 70, "Ben": 85, "Cara": 78}\n\n# เขียนโค้ดตรงนี้',
         code='''scores = {"Ann": 70, "Ben": 85, "Cara": 78}
scores.update({"Ben": 90})
top_name = ""
top_score = 0
for name, score in scores.items():
    if score > top_score:
        top_score = score
        top_name = name
print(f"Top: {top_name} ({top_score})")''')

    probs += [
    dict(file="13_challenge.md", answer="13_grade_book.py", diff="🔴 Challenge",
         name="สมุดเกรดครบวงจร", axis="สร้าง+แก้+คัด+สรุป",
         title="📒 Review Dictionaries — ข้อ 12: สมุดเกรด",
         scenario='เริ่ม `grades = {"Ann": 80}` เพิ่ม Ben=65 Cara=92\nลบคนที่ได้ < 70 ออกหลังคัดเข้า dict ใหม่ หรือลบจากของเดิมหลังตรวจ\nแสดงรายชื่อที่เหลือด้วย items ค่าเฉลี่ย และคนคะแนนสูงสุด (ห้าม max)',
         conditions=None, inp="ไม่มี input", out="รายชื่อ + Average + Top",
         hint="สร้าง/เพิ่มให้ครบ แล้วสร้าง dict ใหม่เฉพาะคนที่ผ่านก่อนสรุป",
         starter='grades = {"Ann": 80}\n\n# เขียนโค้ดตรงนี้',
         code='''grades = {"Ann": 80}
grades["Ben"] = 65
grades["Cara"] = 92

passed = {}
for name, score in grades.items():
    if score >= 70:
        passed[name] = score

total = 0
count = 0
top_name = ""
top_score = 0
for name, score in passed.items():
    print(f"{name}: {score}")
    total += score
    count += 1
    if score > top_score:
        top_score = score
        top_name = name

average = total / count
print(f"Average: {average}")
print(f"Top: {top_name} ({top_score})")'''),
    dict(file="14_challenge.md", answer="14_shop_day.py", diff="🔴 Challenge",
         name="สรุปยอดร้านรายวัน", axis="frequency ออเดอร์ + ราคา + top",
         title="🏪 Review Dictionaries — ข้อ 13: สรุปยอดร้าน",
         scenario='```python\nprices = {"tea": 40, "coffee": 55, "cake": 70}\norders = ["tea", "coffee", "tea", "cake", "tea"]\n```\n\nนับออเดอร์ แสดงจำนวนแต่ละเมนู คำนวณยอดรวมทั้งวัน (จำนวน × ราคา) และเมนูที่ถูกสั่งมากสุด',
         conditions=None, inp="ไม่มี input", out="ความถี่ + Total + Top ordered",
         hint="นับ frequency ก่อน แล้วค่อยคิดเงินและหาเมนูที่สั่งมากสุด",
         starter='prices = {"tea": 40, "coffee": 55, "cake": 70}\norders = ["tea", "coffee", "tea", "cake", "tea"]\n\n# เขียนโค้ดตรงนี้',
         code='''prices = {"tea": 40, "coffee": 55, "cake": 70}
orders = ["tea", "coffee", "tea", "cake", "tea"]

count = {}
for item in orders:
    if item in count:
        count[item] += 1
    else:
        count[item] = 1

for item, n in count.items():
    print(f"{item}: {n}")

total = 0
for item, n in count.items():
    total += n * prices[item]

top_item = ""
top_n = 0
for item, n in count.items():
    if n > top_n:
        top_n = n
        top_item = item

print(f"Total: {total}")
print(f"Top ordered: {top_item} ({top_n})")'''),
    dict(file="15_challenge.md", answer="15_player_dashboard.py", diff="🔴 Challenge",
         name="แดชบอร์ดผู้เล่น", axis="update/del/items/max/กรอบ",
         title="🕹️ Review Dictionaries — ข้อ 14: แดชบอร์ดผู้เล่น",
         scenario='```python\nplayer = {"name": "Luna", "hp": 40, "mp": 20, "bonus": 5}\n```\n\nupdate hp=55 mp=25 ลบ bonus\nแสดงกรอบข้อมูล ถ้า hp >= 50 สถานะ Ready ไม่งั้น Tired',
         conditions=None, inp="ไม่มี input", out="กล่องแดชบอร์ด",
         hint="อัปเดตและลบก่อนตัดสินสถานะ",
         starter='player = {"name": "Luna", "hp": 40, "mp": 20, "bonus": 5}\n\n# เขียนโค้ดตรงนี้',
         code='''player = {"name": "Luna", "hp": 40, "mp": 20, "bonus": 5}
player.update({"hp": 55, "mp": 25})
del player["bonus"]
if player["hp"] >= 50:
    status = "Ready"
else:
    status = "Tired"

print("========================")
print("    PLAYER DASHBOARD")
print("========================")
for key, value in player.items():
    print(f"{key:<10} : {value}")
print(f"{'status':<10} : {status}")
print("========================")'''),
    dict(file="16_challenge.md", answer="16_exam_center.py", diff="🔴 Challenge",
         name="ศูนย์สอบรวมท้าย", axis="ผสมทุกทักษะ dict",
         title="🏫 Review Dictionaries — ข้อ 15: ศูนย์สอบรวมท้าย",
         scenario='```python\nscores = {"Ann": 78, "Ben": 92, "Cara": 85, "Dan": 60}\n```\n\nรับชื่อด้วย `input("Name: ")` ถ้าไม่มีชื่อ แสดง `Not found` แล้วจบ\nถ้ามี แสดงคะแนนของคนนั้น ค่าเฉลี่ยทั้งห้อง คนคะแนนสูงสุด และว่าคนที่ค้นผ่านเกณฑ์ 80 หรือไม่ (`Pass`/`Fail`)',
         conditions=None, inp="ชื่อ 1 บรรทัด", out="สรุปหลายบรรทัดหรือ Not found",
         stdin="Ben\n",
         hint="เช็คชื่อก่อน แล้วค่อยคำนวณสรุปรอบห้อง",
         starter='scores = {"Ann": 78, "Ben": 92, "Cara": 85, "Dan": 60}\nname = input("Name: ")\n\n# เขียนโค้ดตรงนี้',
         code='''scores = {"Ann": 78, "Ben": 92, "Cara": 85, "Dan": 60}
name = input("Name: ")
if name in scores:
    print(f"Score: {scores[name]}")

    total = 0
    count = 0
    top_name = ""
    top_score = 0
    for student, score in scores.items():
        total += score
        count += 1
        if score > top_score:
            top_score = score
            top_name = student
    average = total / count
    print(f"Average: {average}")
    print(f"Top: {top_name} ({top_score})")
    if scores[name] >= 80:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not found")'''),
    ]
    emit("036-review-dictionaries", probs, "บท 036 Review Dictionaries",
         ["ทบทวน dict ทั้งบท 033–035", "หาค่าสูงสุดด้วย loop เปรียบเทียบ", "`input(\"prompt\")`", "frequency counting"],
         ["ห้าม builtin `max()` / `min()`", "ห้าม `.keys()` / `.get()`"],
         ["อย่าลอกโปรแกรม Top scorer Alice/Bob/Charlie จากบทเรียน",
          "ข้อ Challenge ผสมหลายทักษะในสถานการณ์เดียว"])


if __name__ == "__main__":
    gen_033()
    gen_034()
    gen_035()
    gen_036()
    print("033-036 complete")
