# -*- coding: utf-8 -*-
"""Expand weeks 033-036 to 15-problem standard."""
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


# ─── 033 dictionaries ────────────────────────────────────────────────────────
# NO .items / .values / del / .keys / .get

write_week(
    "033-dictionaries",
    chapter="Dictionaries",
    emoji="📖",
    index_md=idx(
        "บท 033 Dictionaries",
        "dict literal · `d[key]` · เพิ่มคีย์ด้วย assignment · `key in d` · `for key in d:`",
        "ไม่มี `.items()` / `.values()` / `del` / `.keys()` / `.get()` (บางส่วนสอนบท 034) · ห้าม empty `{}` นับความถี่ (บท 035)",
        [
            ("02_test.md", "🟢", "อ่านชื่อจากสมุดโทรศัพท์", "เข้าถึงด้วยคีย์"),
            ("03_test.md", "🟢", "เพิ่มคะแนนเข้าโปรไฟล์", "เพิ่มคีย์ใหม่"),
            ("04_test.md", "🟢", "เช็คว่ามีเบอร์หรือยัง", "in กับ dict"),
            ("08_easy.md", "🟢", "วนพิมพ์คีย์สินค้า", "for key in d"),
            ("09_easy.md", "🟢", "อ่านราคาเมนู", "d[key] หลายครั้ง"),
            ("06_medium.md", "🟡", "บัตรนักเรียนสั้น", "อ่านหลายคีย์"),
            ("07_medium.md", "🟡", "เพิ่มเมืองแล้วอ่าน", "เพิ่ม + อ่าน"),
            ("10_medium.md", "🟡", "พิมพ์คู่คีย์-ค่า", "for key + d[key]"),
            ("11_medium.md", "🟡", "เช็คแล้วแสดงคะแนน", "in + เข้าถึง"),
            ("12_medium.md", "🟡", "เมนูเครื่องดื่มสองแก้ว", "อ่านสองราคา + รวม"),
            ("13_medium.md", "🟡", "โปรไฟล์สัตว์เลี้ยง", "หลายคีย์ + กล่อง"),
            ("05_challenge.md", "🔴", "สมุดติดต่อพร้อมเช็ค", "in + วนคีย์"),
            ("14_challenge.md", "🔴", "ใบเสร็จสินค้าคงที่", "อ่านราคา + รวม"),
            ("15_challenge.md", "🔴", "รายงานห้องเรียน", "เพิ่มคีย์ + วนพิมพ์"),
            ("16_challenge.md", "🔴", "กล่องข้อมูลพนักงาน", "ครบชุด dict พื้นฐาน"),
        ],
        "- ข้อ 02 ไม่ซ้ำตัวอย่าง student/contact ในบทเรียนแบบเดิม\n"
        "- วนคีย์ด้วย `for key in d` แล้วอ่าน `d[key]` — ห้าม .items/.values/.keys/.get/del\n"
        "- ยังไม่ใช้ empty dict นับความถี่",
    ),
    problems=[
        p(2, "อ่านชื่อจากสมุดโทรศัพท์", "phone_name",
          "เปิดสมุดโทรศัพท์แล้วอ่านชื่อเจ้าของเบอร์\n\n"
          "กำหนด `contact = {\"name\": \"Mew\", \"phone\": \"081-111-2222\"}`\n\n"
          "แสดง `Name: Mew`",
          "บรรทัดเดียว", "Name: Mew",
          'contact = {"name": "Mew", "phone": "081-111-2222"}\n\n# เขียนโค้ดตรงนี้',
          'contact = {"name": "Mew", "phone": "081-111-2222"}\nprint(f"Name: {contact[\'name\']}")'),
        p(3, "เพิ่มคะแนนเข้าโปรไฟล์", "add_score",
          "โปรไฟล์นักเรียนยังไม่มีคะแนน\n\n"
          "กำหนด `student = {\"name\": \"Pim\", \"age\": 14}`\n\n"
          "เพิ่มคีย์ `score` ค่า `88` แล้วแสดงค่าคะแนน",
          "บรรทัดเดียว", "Score: 88",
          'student = {"name": "Pim", "age": 14}\n\n# เขียนโค้ดตรงนี้',
          'student = {"name": "Pim", "age": 14}\nstudent["score"] = 88\nprint(f"Score: {student[\'score\']}")'),
        p(4, "เช็คว่ามีเบอร์หรือยัง", "has_phone",
          "เช็คว่าใน dict มีคีย์ phone หรือไม่\n\n"
          "กำหนด `user = {\"name\": \"Ohm\", \"city\": \"Bangkok\"}`\n\n"
          "ถ้ามี `phone` แสดง `Has phone` ไม่เช่นนั้น `No phone`",
          "บรรทัดเดียว", "No phone",
          'user = {"name": "Ohm", "city": "Bangkok"}\n\n# เขียนโค้ดตรงนี้',
          'user = {"name": "Ohm", "city": "Bangkok"}\nif "phone" in user:\n    print("Has phone")\nelse:\n    print("No phone")'),
        p(8, "วนพิมพ์คีย์สินค้า", "product_keys",
          "พิมพ์ชื่อคีย์ของสินค้าทีละบรรทัด\n\n"
          "กำหนด `product = {\"id\": \"P01\", \"name\": \"Soap\", \"price\": 25}`\n\n"
          "ใช้ `for key in product:` พิมพ์คีย์",
          "3 บรรทัด", "id\nname\nprice",
          'product = {"id": "P01", "name": "Soap", "price": 25}\n\n# เขียนโค้ดตรงนี้',
          'product = {"id": "P01", "name": "Soap", "price": 25}\nfor key in product:\n    print(key)'),
        p(9, "อ่านราคาเมนู", "menu_prices",
          "อ่านราคากาแฟและชาจากเมนู\n\n"
          "กำหนด `menu = {\"coffee\": 50, \"tea\": 35, \"juice\": 40}`\n\n"
          "แสดงราคา coffee และ tea",
          "2 บรรทัด", "Coffee: 50\nTea: 35",
          'menu = {"coffee": 50, "tea": 35, "juice": 40}\n\n# เขียนโค้ดตรงนี้',
          'menu = {"coffee": 50, "tea": 35, "juice": 40}\nprint(f"Coffee: {menu[\'coffee\']}")\nprint(f"Tea: {menu[\'tea\']}")'),
        p(6, "บัตรนักเรียนสั้น", "student_card",
          "พิมพ์บัตรนักเรียนจาก dict\n\n"
          "กำหนด `student = {\"name\": \"Fern\", \"age\": 13, \"room\": \"M1/2\"}`\n\n"
          "แสดงตามตัวอย่าง",
          "3 บรรทัด", "Name: Fern\nAge : 13\nRoom: M1/2",
          'student = {"name": "Fern", "age": 13, "room": "M1/2"}\n\n# เขียนโค้ดตรงนี้',
          'student = {"name": "Fern", "age": 13, "room": "M1/2"}\nprint(f"Name: {student[\'name\']}")\nprint(f"Age : {student[\'age\']}")\nprint(f"Room: {student[\'room\']}")',
          "อ่านทีละคีย์ด้วย []"),
        p(7, "เพิ่มเมืองแล้วอ่าน", "add_city",
          "โปรไฟล์ยังไม่มีเมือง\n\n"
          "กำหนด `profile = {\"name\": \"Beam\", \"age\": 15}`\n\n"
          "เพิ่ม `city` เป็น `Chiang Mai` แล้วแสดงชื่อกับเมือง",
          "2 บรรทัด", "Beam\nChiang Mai",
          'profile = {"name": "Beam", "age": 15}\n\n# เขียนโค้ดตรงนี้',
          'profile = {"name": "Beam", "age": 15}\nprofile["city"] = "Chiang Mai"\nprint(profile["name"])\nprint(profile["city"])',
          "assignment เพิ่มคีย์ใหม่ได้"),
        p(10, "พิมพ์คู่คีย์-ค่า", "print_pairs",
          "พิมพ์ทุกคีย์พร้อมค่า\n\n"
          "กำหนด `pet = {\"name\": \"Milo\", \"type\": \"Cat\", \"age\": 2}`\n\n"
          "ใช้ for key แล้วพิมพ์แบบ `name: Milo`",
          "3 บรรทัด", "name: Milo\ntype: Cat\nage: 2",
          'pet = {"name": "Milo", "type": "Cat", "age": 2}\n\n# เขียนโค้ดตรงนี้',
          'pet = {"name": "Milo", "type": "Cat", "age": 2}\nfor key in pet:\n    print(f"{key}: {pet[key]}")',
          "ห้ามใช้ .items() ในบทนี้ — ใช้ pet[key]"),
        p(11, "เช็คแล้วแสดงคะแนน", "check_score",
          "เช็คว่ามีคะแนนแล้วค่อยแสดง\n\n"
          "กำหนด `student = {\"name\": \"Ann\", \"score\": 92}`\n\n"
          "ถ้ามีคีย์ `score` แสดงค่าคะแนน ไม่เช่นนั้นแสดง `No score`",
          "บรรทัดเดียว", "92",
          'student = {"name": "Ann", "score": 92}\n\n# เขียนโค้ดตรงนี้',
          'student = {"name": "Ann", "score": 92}\nif "score" in student:\n    print(student["score"])\nelse:\n    print("No score")',
          "เช็ค in ก่อนอ่านค่า"),
        p(12, "เมนูเครื่องดื่มสองแก้ว", "two_drinks",
          "สั่งเครื่องดื่มสองอย่างแล้วรวมราคา\n\n"
          "กำหนด `menu = {\"latte\": 55, \"mocha\": 60, \"tea\": 40}`\n\n"
          "อ่านราคา latte กับ mocha แล้วแสดงราคารวม",
          "บรรทัดเดียว", "Total: 115",
          'menu = {"latte": 55, "mocha": 60, "tea": 40}\n\n# เขียนโค้ดตรงนี้',
          'menu = {"latte": 55, "mocha": 60, "tea": 40}\ntotal = menu["latte"] + menu["mocha"]\nprint(f"Total: {total}")',
          "อ่านสองคีย์แล้วบวก"),
        p(13, "โปรไฟล์สัตว์เลี้ยง", "pet_box",
          "แสดงโปรไฟล์สัตว์เลี้ยงแบบมีป้ายกำกับ\n\n"
          "กำหนด `pet = {\"name\": \"Lucky\", \"type\": \"Dog\", \"age\": 4}`\n\n"
          "แสดงตามตัวอย่าง",
          "3 บรรทัด", "Name : Lucky\nType : Dog\nAge  : 4",
          'pet = {"name": "Lucky", "type": "Dog", "age": 4}\n\n# เขียนโค้ดตรงนี้',
          'pet = {"name": "Lucky", "type": "Dog", "age": 4}\nprint(f"Name : {pet[\'name\']}")\nprint(f"Type : {pet[\'type\']}")\nprint(f"Age  : {pet[\'age\']}")',
          "จัดช่องว่างให้ตรงคอลัมน์"),
        p(5, "สมุดติดต่อพร้อมเช็ค", "contact_check",
          "สมุดติดต่อต้องเช็คคีย์ก่อนแล้ววนพิมพ์ทุกคีย์\n\n"
          "กำหนด `contact = {\"name\": \"Nida\", \"phone\": \"089-000-1111\", \"city\": \"Khon Kaen\"}`\n\n"
          "ถ้ามี `email` แสดง Found email ไม่เช่นนั้น No email\n"
          "จากนั้นพิมพ์ทุกคีย์ทีละบรรทัด",
          "4 บรรทัด", "No email\nname\nphone\ncity",
          'contact = {"name": "Nida", "phone": "089-000-1111", "city": "Khon Kaen"}\n\n# เขียนโค้ดตรงนี้',
          'contact = {"name": "Nida", "phone": "089-000-1111", "city": "Khon Kaen"}\nif "email" in contact:\n    print("Found email")\nelse:\n    print("No email")\nfor key in contact:\n    print(key)',
          "เช็คคีย์ที่อาจไม่มี แล้วค่อยวนคีย์ที่มี"),
        p(14, "ใบเสร็จสินค้าคงที่", "item_receipt",
          "ใบเสร็จอ่านราคาจาก dict สินค้า\n\n"
          "กำหนด `prices = {\"pen\": 10, \"book\": 45, \"glue\": 20}`\n\n"
          "แสดงราคาทั้งสามอย่างแล้วปิดท้ายด้วยยอดรวม",
          "4 บรรทัด",
          "pen: 10\nbook: 45\nglue: 20\nTotal: 75",
          'prices = {"pen": 10, "book": 45, "glue": 20}\n\n# เขียนโค้ดตรงนี้',
          'prices = {"pen": 10, "book": 45, "glue": 20}\ntotal = 0\nfor key in prices:\n    print(f"{key}: {prices[key]}")\n    total += prices[key]\nprint(f"Total: {total}")',
          "วนคีย์แล้วบวกค่าไปเรื่อยๆ"),
        p(15, "รายงานห้องเรียน", "class_dict",
          "รายงานห้องเรียนจาก dict\n\n"
          "กำหนด `room = {\"name\": \"M2/1\", \"size\": 30}`\n\n"
          "เพิ่มคีย์ `teacher` เป็น `Ms. Lek` แล้วพิมพ์ทุกคู่คีย์-ค่า",
          "3 บรรทัด", "name: M2/1\nsize: 30\nteacher: Ms. Lek",
          'room = {"name": "M2/1", "size": 30}\n\n# เขียนโค้ดตรงนี้',
          'room = {"name": "M2/1", "size": 30}\nroom["teacher"] = "Ms. Lek"\nfor key in room:\n    print(f"{key}: {room[key]}")',
          "เพิ่มคีย์ก่อนวนพิมพ์"),
        p(16, "กล่องข้อมูลพนักงาน", "staff_box",
          "แสดงข้อมูลพนักงานแบบมีกรอบ\n\n"
          "กำหนด `staff = {\"name\": \"Ada\", \"role\": \"Cashier\", \"id\": \"S12\"}`\n\n"
          "เพิ่ม `shift` เป็น `Morning` แล้วแสดงตามตัวอย่าง",
          "กล่องสรุป",
          "====================\nname: Ada\nrole: Cashier\nid: S12\nshift: Morning\n====================",
          'staff = {"name": "Ada", "role": "Cashier", "id": "S12"}\n\n# เขียนโค้ดตรงนี้',
          'staff = {"name": "Ada", "role": "Cashier", "id": "S12"}\nstaff["shift"] = "Morning"\nprint("====================")\nfor key in staff:\n    print(f"{key}: {staff[key]}")\nprint("====================")',
          "เพิ่มคีย์ แล้ววนพิมพ์ในกรอบ"),
    ],
)


# ─── 034 dictionary-methods ──────────────────────────────────────────────────

write_week(
    "034-dictionary-methods",
    chapter="Dict Methods",
    emoji="🔧",
    index_md=idx(
        "บท 034 Dictionary Methods",
        "อัปเดตค่า · `.update()` · `del` · `.values()` · `.items()`",
        "ไม่มี `.keys()` / `.get()` · ห้าม empty dict นับความถี่ (บท 035)",
        [
            ("02_test.md", "🟢", "อัปเดตอายุนักเรียน", "แก้ค่าด้วยคีย์"),
            ("03_test.md", "🟢", "อัปเดตหลายฟิลด์", "update"),
            ("04_test.md", "🟢", "ลบคะแนนเก่า", "del"),
            ("08_easy.md", "🟢", "พิมพ์เฉพาะค่า", "values"),
            ("09_easy.md", "🟢", "พิมพ์คู่ด้วย items", "items"),
            ("06_medium.md", "🟡", "แก้ราคาแล้ววนค่า", "อัปเดต + values"),
            ("07_medium.md", "🟡", "อัปเดตแล้วลบคีย์", "update + del"),
            ("10_medium.md", "🟡", "รวมค่าราคา", "values + รวม"),
            ("11_medium.md", "🟡", "รายงานด้วย items", "items + รูปแบบ"),
            ("12_medium.md", "🟡", "ย้ายกะพนักงาน", "แก้ค่า + items"),
            ("13_medium.md", "🟡", "อัปเดตเมนูแล้วสรุป", "update + values"),
            ("05_challenge.md", "🔴", "จัดการโปรไฟล์เต็มชุด", "update+del+items"),
            ("14_challenge.md", "🔴", "ใบเสร็จหลังปรับราคา", "แก้ + รวม values"),
            ("15_challenge.md", "🔴", "ลบฟิลด์แล้วรายงาน", "del + items"),
            ("16_challenge.md", "🔴", "กล่องอัปเดตสินค้า", "ครบ method ที่สอน"),
        ],
        "- ข้อ 02 ไม่ซ้ำตัวอย่าง student age=16 ในบทเรียนแบบเดิมทุกขั้น\n"
        "- ใช้ได้ update / del / values / items\n"
        "- ห้าม keys / get",
    ),
    problems=[
        p(2, "อัปเดตอายุนักเรียน", "update_age",
          "นักเรียนวันเกิดแล้วต้องแก้อายุ\n\n"
          "กำหนด `student = {\"name\": \"Ann\", \"age\": 12}`\n\n"
          "แก้ age เป็น 13 แล้วแสดงอายุใหม่",
          "บรรทัดเดียว", "Age: 13",
          'student = {"name": "Ann", "age": 12}\n\n# เขียนโค้ดตรงนี้',
          'student = {"name": "Ann", "age": 12}\nstudent["age"] = 13\nprint(f"Age: {student[\'age\']}")'),
        p(3, "อัปเดตหลายฟิลด์", "multi_update",
          "อัปเดตข้อมูลติดต่อหลายฟิลด์พร้อมกัน\n\n"
          "กำหนด `user = {\"name\": \"Ben\", \"city\": \"Bangkok\", \"score\": 70}`\n\n"
          "ใช้ `.update({\"city\": \"Phuket\", \"score\": 85})` แล้วแสดง city และ score",
          "2 บรรทัด", "Phuket\n85",
          'user = {"name": "Ben", "city": "Bangkok", "score": 70}\n\n# เขียนโค้ดตรงนี้',
          'user = {"name": "Ben", "city": "Bangkok", "score": 70}\nuser.update({"city": "Phuket", "score": 85})\nprint(user["city"])\nprint(user["score"])'),
        p(4, "ลบคะแนนเก่า", "del_score",
          "ลบคะแนนเก่าออกจากโปรไฟล์\n\n"
          "กำหนด `student = {\"name\": \"Cara\", \"score\": 60, \"room\": \"M2\"}`\n\n"
          "ใช้ `del` ลบคีย์ score แล้วพิมพ์ทุกคีย์ที่เหลือ",
          "2 บรรทัด", "name\nroom",
          'student = {"name": "Cara", "score": 60, "room": "M2"}\n\n# เขียนโค้ดตรงนี้',
          'student = {"name": "Cara", "score": 60, "room": "M2"}\ndel student["score"]\nfor key in student:\n    print(key)'),
        p(8, "พิมพ์เฉพาะค่า", "print_values",
          "พิมพ์เฉพาะค่าใน dict สินค้า\n\n"
          "กำหนด `item = {\"name\": \"Mug\", \"price\": 80, \"stock\": 12}`\n\n"
          "ใช้ `.values()` พิมพ์ทีละค่า",
          "3 บรรทัด", "Mug\n80\n12",
          'item = {"name": "Mug", "price": 80, "stock": 12}\n\n# เขียนโค้ดตรงนี้',
          'item = {"name": "Mug", "price": 80, "stock": 12}\nfor value in item.values():\n    print(value)'),
        p(9, "พิมพ์คู่ด้วย items", "print_items",
          "พิมพ์คู่คีย์-ค่าด้วย `.items()`\n\n"
          "กำหนด `book = {\"title\": \"Python\", \"pages\": 120}`\n\n"
          "แสดงแบบ `title: Python`",
          "2 บรรทัด", "title: Python\npages: 120",
          'book = {"title": "Python", "pages": 120}\n\n# เขียนโค้ดตรงนี้',
          'book = {"title": "Python", "pages": 120}\nfor key, value in book.items():\n    print(f"{key}: {value}")'),
        p(6, "แก้ราคาแล้ววนค่า", "fix_price_values",
          "แก้ราคาสินค้าแล้วพิมพ์ทุกค่า\n\n"
          "กำหนด `product = {\"name\": \"Tea\", \"price\": 30, \"stock\": 20}`\n\n"
          "แก้ price เป็น 35 แล้วพิมพ์ values",
          "3 บรรทัด", "Tea\n35\n20",
          'product = {"name": "Tea", "price": 30, "stock": 20}\n\n# เขียนโค้ดตรงนี้',
          'product = {"name": "Tea", "price": 30, "stock": 20}\nproduct["price"] = 35\nfor value in product.values():\n    print(value)',
          "แก้ค่าก่อน แล้วค่อยวน values"),
        p(7, "อัปเดตแล้วลบคีย์", "update_then_del",
          "อัปเดตโปรไฟล์แล้วลบฟิลด์ที่ไม่ใช้\n\n"
          "กำหนด `profile = {\"name\": \"Dan\", \"temp\": 0, \"city\": \"Rayong\"}`\n\n"
          "update city เป็น `Chonburi` แล้ว del คีย์ `temp` จากนั้นพิมพ์ items",
          "2 บรรทัด", "name: Dan\ncity: Chonburi",
          'profile = {"name": "Dan", "temp": 0, "city": "Rayong"}\n\n# เขียนโค้ดตรงนี้',
          'profile = {"name": "Dan", "temp": 0, "city": "Rayong"}\nprofile.update({"city": "Chonburi"})\ndel profile["temp"]\nfor key, value in profile.items():\n    print(f"{key}: {value}")',
          "update → del → items"),
        p(10, "รวมค่าราคา", "sum_values",
          "รวมราคาสินค้าจาก values\n\n"
          "กำหนด `prices = {\"pen\": 10, \"ruler\": 15, \"eraser\": 5}`\n\n"
          "วน `.values()` รวมแล้วแสดง `Total: ...`",
          "บรรทัดเดียว", "Total: 30",
          'prices = {"pen": 10, "ruler": 15, "eraser": 5}\n\n# เขียนโค้ดตรงนี้',
          'prices = {"pen": 10, "ruler": 15, "eraser": 5}\ntotal = 0\nfor value in prices.values():\n    total += value\nprint(f"Total: {total}")',
          "values ให้เฉพาะตัวเลขราคา"),
        p(11, "รายงานด้วย items", "items_report",
          "รายงานสภาพอากาศด้วย items\n\n"
          "กำหนด `weather = {\"city\": \"Hua Hin\", \"temp\": 31, \"rain\": \"No\"}`\n\n"
          "พิมพ์แบบ `city -> Hua Hin`",
          "3 บรรทัด", "city -> Hua Hin\ntemp -> 31\nrain -> No",
          'weather = {"city": "Hua Hin", "temp": 31, "rain": "No"}\n\n# เขียนโค้ดตรงนี้',
          'weather = {"city": "Hua Hin", "temp": 31, "rain": "No"}\nfor key, value in weather.items():\n    print(f"{key} -> {value}")',
          "items ให้ทั้งคีย์และค่า"),
        p(12, "ย้ายกะพนักงาน", "shift_change",
          "ย้ายกะพนักงานแล้วพิมพ์รายการใหม่\n\n"
          "กำหนด `staff = {\"name\": \"Eve\", \"shift\": \"Morning\", \"role\": \"Barista\"}`\n\n"
          "แก้ shift เป็น `Evening` แล้วพิมพ์ items",
          "3 บรรทัด", "name: Eve\nshift: Evening\nrole: Barista",
          'staff = {"name": "Eve", "shift": "Morning", "role": "Barista"}\n\n# เขียนโค้ดตรงนี้',
          'staff = {"name": "Eve", "shift": "Morning", "role": "Barista"}\nstaff["shift"] = "Evening"\nfor key, value in staff.items():\n    print(f"{key}: {value}")',
          "แก้ค่าแล้วรายงานใหม่"),
        p(13, "อัปเดตเมนูแล้วสรุป", "menu_update_sum",
          "อัปเดตราคาเมนูแล้วรวม\n\n"
          "กำหนด `menu = {\"soup\": 40, \"salad\": 50, \"steak\": 120}`\n\n"
          "update soup เป็น 45 salad เป็น 55 แล้วรวม values",
          "บรรทัดเดียว", "Total: 220",
          'menu = {"soup": 40, "salad": 50, "steak": 120}\n\n# เขียนโค้ดตรงนี้',
          'menu = {"soup": 40, "salad": 50, "steak": 120}\nmenu.update({"soup": 45, "salad": 55})\ntotal = 0\nfor value in menu.values():\n    total += value\nprint(f"Total: {total}")',
          "update หลายคีย์ก่อนรวม"),
        p(5, "จัดการโปรไฟล์เต็มชุด", "full_profile",
          "จัดการโปรไฟล์ด้วยหลายคำสั่ง\n\n"
          "กำหนด `user = {\"name\": \"Finn\", \"age\": 16, \"temp\": 1, \"city\": \"Nan\"}`\n\n"
          "update age เป็น 17 และ city เป็น `Lampang` แล้ว del `temp`\n"
          "จากนั้นพิมพ์ items",
          "3 บรรทัด", "name: Finn\nage: 17\ncity: Lampang",
          'user = {"name": "Finn", "age": 16, "temp": 1, "city": "Nan"}\n\n# เขียนโค้ดตรงนี้',
          'user = {"name": "Finn", "age": 16, "temp": 1, "city": "Nan"}\nuser.update({"age": 17, "city": "Lampang"})\ndel user["temp"]\nfor key, value in user.items():\n    print(f"{key}: {value}")',
          "update หลายคีย์ ลบของชั่วคราว แล้วรายงาน"),
        p(14, "ใบเสร็จหลังปรับราคา", "receipt_adjust",
          "ปรับราคาสินค้าแล้วพิมพ์ใบเสร็จ\n\n"
          "กำหนด `cart = {\"milk\": 20, \"bread\": 25, \"egg\": 40}`\n\n"
          "แก้ egg เป็น 35 แล้วพิมพ์แต่ละรายการด้วย items และยอดรวม",
          "4 บรรทัด",
          "milk: 20\nbread: 25\negg: 35\nTotal: 80",
          'cart = {"milk": 20, "bread": 25, "egg": 40}\n\n# เขียนโค้ดตรงนี้',
          'cart = {"milk": 20, "bread": 25, "egg": 40}\ncart["egg"] = 35\ntotal = 0\nfor key, value in cart.items():\n    print(f"{key}: {value}")\n    total += value\nprint(f"Total: {total}")',
          "แก้ราคาแล้ววน items พร้อมสะสมยอด"),
        p(15, "ลบฟิลด์แล้วรายงาน", "delete_report",
          "ลบฟิลด์รหัสชั่วคราวแล้วรายงานข้อมูลห้อง\n\n"
          "กำหนด `room = {\"name\": \"Lab\", \"code\": \"TMP\", \"seats\": 24}`\n\n"
          "del คีย์ code แล้วพิมพ์ items และจำนวนคีย์ที่เหลือ",
          "3 บรรทัด", "name: Lab\nseats: 24\nFields: 2",
          'room = {"name": "Lab", "code": "TMP", "seats": 24}\n\n# เขียนโค้ดตรงนี้',
          'room = {"name": "Lab", "code": "TMP", "seats": 24}\ndel room["code"]\nfor key, value in room.items():\n    print(f"{key}: {value}")\nprint(f"Fields: {len(room)}")',
          "หลัง del ใช้ len นับคีย์ที่เหลือ"),
        p(16, "กล่องอัปเดตสินค้า", "product_box",
          "อัปเดตสินค้าแล้วแสดงแบบมีกรอบ\n\n"
          "กำหนด `product = {\"name\": \"Soap\", \"price\": 25, \"note\": \"old\"}`\n\n"
          "update price เป็น 28 แล้ว del note จากนั้นแสดงตามตัวอย่าง",
          "กล่องสรุป",
          "====================\nname: Soap\nprice: 28\n====================",
          'product = {"name": "Soap", "price": 25, "note": "old"}\n\n# เขียนโค้ดตรงนี้',
          'product = {"name": "Soap", "price": 25, "note": "old"}\nproduct.update({"price": 28})\ndel product["note"]\nprint("====================")\nfor key, value in product.items():\n    print(f"{key}: {value}")\nprint("====================")',
          "update + del + items ในกรอบ"),
    ],
)


# ─── 035 dictionary-practice ─────────────────────────────────────────────────
# input(prompt) OK; empty dict; frequency; CUT to 15 (was 23)

write_week(
    "035-dictionary-practice",
    chapter="Dict Practice",
    emoji="🏋️",
    index_md=idx(
        "บท 035 Dictionary Practice",
        "ฝึก dict ทั้งก้อน + **`input(\"prompt\")`** + empty dict + นับความถี่",
        "ห้าม `.keys()` / `.get()` · ห้าม `min()`/`max()` · ตัดเหลือ 15 ข้อ (เดิมมีเกิน)",
        [
            ("02_test.md", "🟢", "บัตรนักเรียนสั้น", "อ่านหลายคีย์"),
            ("03_test.md", "🟢", "เพิ่มเบอร์โทร", "เพิ่มคีย์"),
            ("04_test.md", "🟢", "นับผลไม้ในตะกร้า", "frequency พื้นฐาน"),
            ("08_easy.md", "🟢", "อัปเดตคะแนนสอบ", "แก้ค่า"),
            ("09_easy.md", "🟢", "เช็คของในคลัง", "in + ข้อความ"),
            ("06_medium.md", "🟡", "เมนูสมูทตี้", "items + รวม"),
            ("07_medium.md", "🟡", "แปลสีสั้นๆ", "อ่านคีย์จาก input พร้อม prompt"),
            ("10_medium.md", "🟡", "นับคำในประโยคสั้น", "frequency จาก list"),
            ("11_medium.md", "🟡", "สั่งเครื่องดื่ม", "input prompt + ราคา"),
            ("12_medium.md", "🟡", "คะแนนเพื่อน", "items + ผ่านเกณฑ์"),
            ("13_medium.md", "🟡", "รวมแต้มสองรอบ", "บวกค่าใน dict"),
            ("05_challenge.md", "🔴", "ตรวจคำตอบควิซ", "input prompt หลายข้อ"),
            ("14_challenge.md", "🔴", "นับสินค้าแล้วเรียงคีย์", "frequency + แสดง"),
            ("15_challenge.md", "🔴", "กระเป๋าเกม", "เพิ่ม/อัปเดตจำนวน"),
            ("16_challenge.md", "🔴", "สรุปออเดอร์สองชิ้น", "input + รวมราคา"),
        ],
        "- ข้อ 02 ไม่ซ้ำตัวอย่าง word count cat/dog/bird ในบทเรียน\n"
        "- input มี prompt ได้แล้วในบทนี้\n"
        "- ตัดจากชุดเดิมที่เกิน 15 ข้อ ให้เหลือตามมาตรฐาน",
    ),
    problems=[
        p(2, "บัตรนักเรียนสั้น", "student_card",
          "พิมพ์บัตรนักเรียนจาก dict\n\n"
          "กำหนด `student = {\"name\": \"Ann\", \"age\": 12, \"grade\": \"M1\"}`\n\n"
          "แสดง Name / Age / Grade",
          "3 บรรทัด", "Name: Ann\nAge: 12\nGrade: M1",
          'student = {"name": "Ann", "age": 12, "grade": "M1"}\n\n# เขียนโค้ดตรงนี้',
          'student = {"name": "Ann", "age": 12, "grade": "M1"}\nprint(f"Name: {student[\'name\']}")\nprint(f"Age: {student[\'age\']}")\nprint(f"Grade: {student[\'grade\']}")'),
        p(3, "เพิ่มเบอร์โทร", "add_phone",
          "โปรไฟล์ยังไม่มีเบอร์\n\n"
          "กำหนด `user = {\"name\": \"Ben\", \"city\": \"Bangkok\"}`\n\n"
          "เพิ่ม `phone` เป็น `081-222-3333` แล้วแสดงเบอร์",
          "บรรทัดเดียว", "Phone: 081-222-3333",
          'user = {"name": "Ben", "city": "Bangkok"}\n\n# เขียนโค้ดตรงนี้',
          'user = {"name": "Ben", "city": "Bangkok"}\nuser["phone"] = "081-222-3333"\nprint(f"Phone: {user[\'phone\']}")'),
        p(4, "นับผลไม้ในตะกร้า", "count_fruit",
          "นับจำนวนผลไม้แต่ละชนิดในตะกร้า\n\n"
          "กำหนด `fruits = [\"apple\", \"banana\", \"apple\", \"mango\", \"banana\", \"apple\"]`\n\n"
          "เริ่มจาก `count = {}` นับความถี่ แล้วพิมพ์ด้วย items",
          "3 บรรทัด", "apple: 3\nbanana: 2\nmango: 1",
          'fruits = ["apple", "banana", "apple", "mango", "banana", "apple"]\ncount = {}\n\n# เขียนโค้ดตรงนี้',
          'fruits = ["apple", "banana", "apple", "mango", "banana", "apple"]\ncount = {}\nfor fruit in fruits:\n    if fruit in count:\n        count[fruit] += 1\n    else:\n        count[fruit] = 1\nfor key, value in count.items():\n    print(f"{key}: {value}")'),
        p(8, "อัปเดตคะแนนสอบ", "update_score",
          "แก้คะแนนสอบล่าสุด\n\n"
          "กำหนด `scores = {\"Ann\": 70, \"Ben\": 80}`\n\n"
          "แก้คะแนน Ann เป็น 85 แล้วพิมพ์ items",
          "2 บรรทัด", "Ann: 85\nBen: 80",
          'scores = {"Ann": 70, "Ben": 80}\n\n# เขียนโค้ดตรงนี้',
          'scores = {"Ann": 70, "Ben": 80}\nscores["Ann"] = 85\nfor key, value in scores.items():\n    print(f"{key}: {value}")'),
        p(9, "เช็คของในคลัง", "in_stock",
          "เช็คว่ามีสินค้าในคลังหรือไม่\n\n"
          "กำหนด `stock = {\"rice\": 10, \"oil\": 4, \"salt\": 7}`\n\n"
          "ถ้ามีคีย์ `sugar` แสดง `In stock` ไม่เช่นนั้น `Sold out`",
          "บรรทัดเดียว", "Sold out",
          'stock = {"rice": 10, "oil": 4, "salt": 7}\n\n# เขียนโค้ดตรงนี้',
          'stock = {"rice": 10, "oil": 4, "salt": 7}\nif "sugar" in stock:\n    print("In stock")\nelse:\n    print("Sold out")'),
        p(6, "เมนูสมูทตี้", "smoothie_menu",
          "พิมพ์เมนูสมูทตี้พร้อมราคารวม\n\n"
          "กำหนด `menu = {\"mango\": 45, \"berry\": 50, \"banana\": 40}`\n\n"
          "พิมพ์แต่ละรายการด้วย items แล้วแสดงยอดรวม",
          "4 บรรทัด",
          "mango: 45\nberry: 50\nbanana: 40\nTotal: 135",
          'menu = {"mango": 45, "berry": 50, "banana": 40}\n\n# เขียนโค้ดตรงนี้',
          'menu = {"mango": 45, "berry": 50, "banana": 40}\ntotal = 0\nfor item, price in menu.items():\n    print(f"{item}: {price}")\n    total += price\nprint(f"Total: {total}")',
          "วน items พร้อมสะสมยอด"),
        p(7, "แปลสีสั้นๆ", "translate_color",
          "พจนานุกรมแปลสี\n\n"
          "กำหนด `colors = {\"red\": \"แดง\", \"blue\": \"น้ำเงิน\", \"green\": \"เขียว\"}`\n\n"
          "รับคำภาษาอังกฤษจากผู้ใช้ด้วย `input(\"color: \")` แล้วแสดงคำแปล\n"
          "(ตัวอย่างใส่ `blue`)\n\n"
          "> หมายเหตุ: prompt ของ input จะโผล่ใน Output ด้วย",
          "บรรทัดเดียว (รวม prompt)", "color: น้ำเงิน",
          'colors = {"red": "แดง", "blue": "น้ำเงิน", "green": "เขียว"}\n\n# เขียนโค้ดตรงนี้',
          'colors = {"red": "แดง", "blue": "น้ำเงิน", "green": "เขียว"}\nword = input("color: ")\nprint(colors[word])',
          None,
          "blue",
          "1 บรรทัด — ชื่อสีภาษาอังกฤษ"),
        p(10, "นับคำในประโยคสั้น", "count_words",
          "นับคำจาก list คำ\n\n"
          "กำหนด `words = [\"hi\", \"yo\", \"hi\", \"hey\", \"yo\", \"hi\"]`\n\n"
          "นับความถี่ด้วย empty dict แล้วพิมพ์ items",
          "3 บรรทัด", "hi: 3\nyo: 2\nhey: 1",
          'words = ["hi", "yo", "hi", "hey", "yo", "hi"]\ncount = {}\n\n# เขียนโค้ดตรงนี้',
          'words = ["hi", "yo", "hi", "hey", "yo", "hi"]\ncount = {}\nfor word in words:\n    if word in count:\n        count[word] += 1\n    else:\n        count[word] = 1\nfor key, value in count.items():\n    print(f"{key}: {value}")',
          "ถ้ามีคีย์แล้วบวก 1 ถ้ายังไม่มีตั้งเป็น 1"),
        p(11, "สั่งเครื่องดื่ม", "order_drink",
          "รับชื่อเครื่องดื่มแล้วบอกราคา\n\n"
          "กำหนด `menu = {\"latte\": 55, \"mocha\": 60, \"tea\": 40}`\n\n"
          "ใช้ `input(\"drink: \")` แล้วแสดงราคาในรูปแบบ `Price: ...`\n"
          "(ตัวอย่างใส่ `mocha`)\n\n"
          "> หมายเหตุ: prompt ของ input จะโผล่ใน Output ด้วย",
          "รวม prompt + ราคา", "drink: Price: 60",
          'menu = {"latte": 55, "mocha": 60, "tea": 40}\n\n# เขียนโค้ดตรงนี้',
          'menu = {"latte": 55, "mocha": 60, "tea": 40}\ndrink = input("drink: ")\nprint(f"Price: {menu[drink]}")',
          "อ่านคีย์จาก input แล้วไปดูราคา",
          "mocha",
          "1 บรรทัด — ชื่อเครื่องดื่ม"),
        p(12, "คะแนนเพื่อน", "friends_pass",
          "พิมพ์คะแนนเพื่อนและสถานะผ่านเกณฑ์ 50\n\n"
          "กำหนด `scores = {\"Ann\": 80, \"Ben\": 40, \"Cara\": 65}`\n\n"
          "พิมพ์แบบ `Ann 80 Pass` หรือ Fail",
          "3 บรรทัด", "Ann 80 Pass\nBen 40 Fail\nCara 65 Pass",
          'scores = {"Ann": 80, "Ben": 40, "Cara": 65}\n\n# เขียนโค้ดตรงนี้',
          'scores = {"Ann": 80, "Ben": 40, "Cara": 65}\nfor name, score in scores.items():\n    if score >= 50:\n        status = "Pass"\n    else:\n        status = "Fail"\n    print(f"{name} {score} {status}")',
          "วน items แล้วตัดสิน Pass/Fail"),
        p(13, "รวมแต้มสองรอบ", "add_scores",
          "รวมแต้มรอบใหม่เข้ากระดานเดิม\n\n"
          "กำหนด `scores = {\"Ann\": 10, \"Ben\": 8}` และ `bonus = {\"Ann\": 5, \"Ben\": 2}`\n\n"
          "บวก bonus ให้คนชื่อเดียวกัน แล้วพิมพ์ items",
          "2 บรรทัด", "Ann: 15\nBen: 10",
          'scores = {"Ann": 10, "Ben": 8}\nbonus = {"Ann": 5, "Ben": 2}\n\n# เขียนโค้ดตรงนี้',
          'scores = {"Ann": 10, "Ben": 8}\nbonus = {"Ann": 5, "Ben": 2}\nfor name in bonus:\n    scores[name] += bonus[name]\nfor name, score in scores.items():\n    print(f"{name}: {score}")',
          "วนคีย์ใน bonus แล้วบวกเข้า scores"),
        p(5, "ตรวจคำตอบควิซ", "quiz_check",
          "ตรวจคำตอบควิซ 3 ข้อ\n\n"
          "กำหนด `answers = {\"q1\": \"A\", \"q2\": \"C\", \"q3\": \"B\"}`\n\n"
          "รับคำตอบผู้ใช้ด้วย `input(\"q1: \")` แบบเดียวกันกับ q2 q3\n"
          "ถ้าถูกพิมพ์ `Correct` ผิดพิมพ์ `Wrong` แล้วปิดท้ายด้วยคะแนนรวม (ข้อละ 1)\n\n"
          "ตัวอย่างคำตอบผู้ใช้: A / B / B\n\n"
          "> หมายเหตุ: prompt ของ input จะโผล่หน้าคำว่า Correct/Wrong",
          "4 บรรทัด (รวม prompt)",
          "q1: Correct\nq2: Wrong\nq3: Correct\nScore: 2",
          'answers = {"q1": "A", "q2": "C", "q3": "B"}\n\n# เขียนโค้ดตรงนี้',
          'answers = {"q1": "A", "q2": "C", "q3": "B"}\nscore = 0\nfor q in answers:\n    user = input(f"{q}: ")\n    if user == answers[q]:\n        print("Correct")\n        score += 1\n    else:\n        print("Wrong")\nprint(f"Score: {score}")',
          "เทียบคำตอบทีละข้อแล้วสะสมคะแนน",
          "A\nB\nB",
          "3 บรรทัด — คำตอบ q1 q2 q3"),
        p(14, "นับสินค้าแล้วเรียงคีย์", "count_items",
          "นับสินค้าจากรายการสั่งซื้อ\n\n"
          "กำหนด `items = [\"pen\", \"book\", \"pen\", \"glue\", \"book\", \"pen\"]`\n\n"
          "นับความถี่ แล้วพิมพ์คีย์เรียงตามตัวอักษรพร้อมจำนวน\n"
          "(สร้าง list จากคีย์ แล้ว sort ก่อนพิมพ์)",
          "3 บรรทัด", "book: 2\nglue: 1\npen: 3",
          'items = ["pen", "book", "pen", "glue", "book", "pen"]\ncount = {}\n\n# เขียนโค้ดตรงนี้',
          'items = ["pen", "book", "pen", "glue", "book", "pen"]\ncount = {}\nfor item in items:\n    if item in count:\n        count[item] += 1\n    else:\n        count[item] = 1\nkeys = list(count)\nkeys.sort()\nfor key in keys:\n    print(f"{key}: {count[key]}")',
          "นับก่อน แล้วเรียงคีย์ก่อนแสดง"),
        p(15, "กระเป๋าเกม", "game_bag",
          "อัปเดตจำนวนไอเท็มในกระเป๋าเกม\n\n"
          "กำหนด `bag = {\"potion\": 2, \"coin\": 5}`\n\n"
          "เพิ่ม potion อีก 1 (บวกค่า) และเพิ่มคีย์ `gem` ค่า 3\n"
          "แล้วพิมพ์ items",
          "3 บรรทัด", "potion: 3\ncoin: 5\ngem: 3",
          'bag = {"potion": 2, "coin": 5}\n\n# เขียนโค้ดตรงนี้',
          'bag = {"potion": 2, "coin": 5}\nbag["potion"] += 1\nbag["gem"] = 3\nfor key, value in bag.items():\n    print(f"{key}: {value}")',
          "บวกของเดิม และเพิ่มคีย์ใหม่"),
        p(16, "สรุปออเดอร์สองชิ้น", "two_items_order",
          "รับชื่อสินค้าสองชิ้นแล้วรวมราคา\n\n"
          "กำหนด `prices = {\"pen\": 10, \"book\": 45, \"glue\": 20}`\n\n"
          "ใช้ `input(\"item1: \")` และ `input(\"item2: \")` แล้วแสดงราคารวม\n"
          "ตัวอย่าง: book / glue\n\n"
          "> หมายเหตุ: prompt จะโผล่ใน Output — เพื่อให้อ่านง่ายให้พิมพ์ผลลัพธ์คนละบรรทัดหลังรับครบ",
          "รวม prompt + ยอด", "item1: item2: Total: 65",
          'prices = {"pen": 10, "book": 45, "glue": 20}\n\n# เขียนโค้ดตรงนี้',
          'prices = {"pen": 10, "book": 45, "glue": 20}\nitem1 = input("item1: ")\nitem2 = input("item2: ")\ntotal = prices[item1] + prices[item2]\nprint(f"Total: {total}")',
          "อ่านสองคีย์จาก input แล้วบวกราคา",
          "book\nglue",
          "2 บรรทัด — ชื่อสินค้า"),
    ],
)


# ─── 036 review-dictionaries ─────────────────────────────────────────────────
# no builtin max(); manual max idiom; don't duplicate Alice/Bob/Charlie top scorer

write_week(
    "036-review-dictionaries",
    chapter="Review Dicts",
    emoji="🔁",
    index_md=idx(
        "บท 036 Review Dictionaries",
        "ทบทวน dict ทั้งหมด + หาค่าสูงสุดด้วย loop เทียบเอง",
        "ห้าม builtin `max()` / `min()` / `.get()` / `.keys()` · ห้ามซ้ำโจทย์ Top scorer ในบทเรียน",
        [
            ("02_test.md", "🟢", "อ่านค่าปลอดภัย", "in ก่อนอ่าน"),
            ("03_test.md", "🟢", "อัปเดตโปรไฟล์สั้น", "แก้ค่า"),
            ("04_test.md", "🟢", "ลบคีย์ชั่วคราว", "del"),
            ("08_easy.md", "🟢", "พิมพ์ด้วย items", "items"),
            ("09_easy.md", "🟢", "รวม values", "values + รวม"),
            ("06_medium.md", "🟡", "นับแท็กซ้ำ", "frequency"),
            ("07_medium.md", "🟡", "หาคะแนนสูงสุดด้วยมือ", "manual max"),
            ("10_medium.md", "🟡", "อัปเดตหลายฟิลด์", "update"),
            ("11_medium.md", "🟡", "เช็คแล้วเพิ่มคีย์", "in + เพิ่ม"),
            ("12_medium.md", "🟡", "เมนูพร้อมยอดรวม", "items + รวม"),
            ("13_medium.md", "🟡", "หาชื่อที่ได้แต้มน้อยสุด", "manual min แบบเทียบ"),
            ("05_challenge.md", "🔴", "กระดานคะแนนพร้อม Top", "manual max + รายงาน"),
            ("14_challenge.md", "🔴", "คลังสินค้าปรับสต็อก", "แก้ค่า + del + สรุป"),
            ("15_challenge.md", "🔴", "นับคำแล้วหาคำยอดนิยม", "frequency + manual max"),
            ("16_challenge.md", "🔴", "กล่องสรุปสมาชิก", "ครบชุดทบทวน dict"),
        ],
        "- ข้อ 02 ไม่ซ้ำตัวอย่าง top scorer Alice/Bob/Charlie ในบทเรียน\n"
        "- หาสูงสุด/ต่ำสุดต้องเทียบใน loop ห้าม max()/min()\n"
        "- ทบทวน in / update / del / values / items / frequency",
    ),
    problems=[
        p(2, "อ่านค่าปลอดภัย", "safe_access",
          "อ่านคะแนนแบบเช็คคีย์ก่อน\n\n"
          "กำหนด `student = {\"name\": \"Gina\", \"room\": \"M3\"}`\n\n"
          "ถ้ามี `score` แสดงค่า ไม่งั้นแสดง `No score yet`",
          "บรรทัดเดียว", "No score yet",
          'student = {"name": "Gina", "room": "M3"}\n\n# เขียนโค้ดตรงนี้',
          'student = {"name": "Gina", "room": "M3"}\nif "score" in student:\n    print(student["score"])\nelse:\n    print("No score yet")'),
        p(3, "อัปเดตโปรไฟล์สั้น", "profile_fix",
          "แก้เมืองในโปรไฟล์\n\n"
          "กำหนด `user = {\"name\": \"Hugo\", \"city\": \"Trang\"}`\n\n"
          "แก้ city เป็น `Krabi` แล้วแสดงเมือง",
          "บรรทัดเดียว", "City: Krabi",
          'user = {"name": "Hugo", "city": "Trang"}\n\n# เขียนโค้ดตรงนี้',
          'user = {"name": "Hugo", "city": "Trang"}\nuser["city"] = "Krabi"\nprint(f"City: {user[\'city\']}")'),
        p(4, "ลบคีย์ชั่วคราว", "del_temp",
          "ลบโน้ตชั่วคราวออกจากสินค้า\n\n"
          "กำหนด `item = {\"name\": \"Lamp\", \"note\": \"demo\", \"price\": 199}`\n\n"
          "del note แล้วพิมพ์คีย์ที่เหลือ",
          "2 บรรทัด", "name\nprice",
          'item = {"name": "Lamp", "note": "demo", "price": 199}\n\n# เขียนโค้ดตรงนี้',
          'item = {"name": "Lamp", "note": "demo", "price": 199}\ndel item["note"]\nfor key in item:\n    print(key)'),
        p(8, "พิมพ์ด้วย items", "review_items",
          "พิมพ์คู่คีย์-ค่า\n\n"
          "กำหนด `car = {\"brand\": \"Toyota\", \"year\": 2020}`",
          "2 บรรทัด", "brand: Toyota\nyear: 2020",
          'car = {"brand": "Toyota", "year": 2020}\n\n# เขียนโค้ดตรงนี้',
          'car = {"brand": "Toyota", "year": 2020}\nfor key, value in car.items():\n    print(f"{key}: {value}")'),
        p(9, "รวม values", "sum_review",
          "รวมค่าใช้จ่ายจาก dict\n\n"
          "กำหนด `bills = {\"food\": 120, \"bus\": 30, \"drink\": 40}`\n\n"
          "แสดง `Total: 190`",
          "บรรทัดเดียว", "Total: 190",
          'bills = {"food": 120, "bus": 30, "drink": 40}\n\n# เขียนโค้ดตรงนี้',
          'bills = {"food": 120, "bus": 30, "drink": 40}\ntotal = 0\nfor value in bills.values():\n    total += value\nprint(f"Total: {total}")'),
        p(6, "นับแท็กซ้ำ", "count_tags",
          "นับแท็กจาก list\n\n"
          "กำหนด `tags = [\"fun\", \"code\", \"fun\", \"game\", \"code\", \"fun\"]`\n\n"
          "นับความถี่แล้วพิมพ์ items",
          "3 บรรทัด", "fun: 3\ncode: 2\ngame: 1",
          'tags = ["fun", "code", "fun", "game", "code", "fun"]\ncount = {}\n\n# เขียนโค้ดตรงนี้',
          'tags = ["fun", "code", "fun", "game", "code", "fun"]\ncount = {}\nfor tag in tags:\n    if tag in count:\n        count[tag] += 1\n    else:\n        count[tag] = 1\nfor key, value in count.items():\n    print(f"{key}: {value}")',
          "pattern นับความถี่ด้วย empty dict"),
        p(7, "หาคะแนนสูงสุดด้วยมือ", "manual_top",
          "หากลุ่มที่ได้คะแนนสูงสุดโดยเทียบเอง\n\n"
          "กำหนด `scores = {\"Red\": 12, \"Blue\": 18, \"Green\": 15}`\n\n"
          "หาชื่อกลุ่มที่คะแนนสูงสุด (ห้าม max) แล้วแสดง `Top: Blue (18)`",
          "บรรทัดเดียว", "Top: Blue (18)",
          'scores = {"Red": 12, "Blue": 18, "Green": 15}\n\n# เขียนโค้ดตรงนี้',
          'scores = {"Red": 12, "Blue": 18, "Green": 15}\ntop_name = ""\ntop_score = 0\nfor name, score in scores.items():\n    if score > top_score:\n        top_score = score\n        top_name = name\nprint(f"Top: {top_name} ({top_score})")',
          "เก็บชื่อและคะแนนที่ดีที่สุดขณะวน loop"),
        p(10, "อัปเดตหลายฟิลด์", "review_update",
          "อัปเดตข้อมูลสมาชิกหลายฟิลด์\n\n"
          "กำหนด `member = {\"name\": \"Ivy\", \"point\": 10, \"level\": 1}`\n\n"
          "update point เป็น 25 level เป็น 2 แล้วพิมพ์ items",
          "3 บรรทัด", "name: Ivy\npoint: 25\nlevel: 2",
          'member = {"name": "Ivy", "point": 10, "level": 1}\n\n# เขียนโค้ดตรงนี้',
          'member = {"name": "Ivy", "point": 10, "level": 1}\nmember.update({"point": 25, "level": 2})\nfor key, value in member.items():\n    print(f"{key}: {value}")',
          "ใช้ update ทีเดียวหลายคีย์"),
        p(11, "เช็คแล้วเพิ่มคีย์", "check_add",
          "ถ้ายังไม่มีอีเมลให้เพิ่ม\n\n"
          "กำหนด `user = {\"name\": \"Jay\", \"city\": \"Ubon\"}`\n\n"
          "ถ้ายังไม่มีคีย์ `email` ให้เพิ่มเป็น `jay@mail.com` แล้วพิมพ์ email",
          "บรรทัดเดียว", "jay@mail.com",
          'user = {"name": "Jay", "city": "Ubon"}\n\n# เขียนโค้ดตรงนี้',
          'user = {"name": "Jay", "city": "Ubon"}\nif "email" not in user:\n    user["email"] = "jay@mail.com"\nprint(user["email"])',
          "ใช้ not in ก่อนเพิ่มคีย์"),
        p(12, "เมนูพร้อมยอดรวม", "menu_total",
          "พิมพ์เมนูและยอดรวม\n\n"
          "กำหนด `menu = {\"rice\": 40, \"soup\": 35, \"salad\": 45}`",
          "4 บรรทัด",
          "rice: 40\nsoup: 35\nsalad: 45\nTotal: 120",
          'menu = {"rice": 40, "soup": 35, "salad": 45}\n\n# เขียนโค้ดตรงนี้',
          'menu = {"rice": 40, "soup": 35, "salad": 45}\ntotal = 0\nfor key, value in menu.items():\n    print(f"{key}: {value}")\n    total += value\nprint(f"Total: {total}")',
          "items + accumulator"),
        p(13, "หาชื่อที่ได้แต้มน้อยสุด", "manual_low",
          "หาคนที่ได้แต้มน้อยสุดด้วยการเทียบเอง (ห้าม min)\n\n"
          "กำหนด `points = {\"Ann\": 9, \"Ben\": 4, \"Cara\": 7}`\n\n"
          "แสดง `Low: Ben (4)`",
          "บรรทัดเดียว", "Low: Ben (4)",
          'points = {"Ann": 9, "Ben": 4, "Cara": 7}\n\n# เขียนโค้ดตรงนี้',
          'points = {"Ann": 9, "Ben": 4, "Cara": 7}\nlow_name = ""\nlow_score = 999\nfor name, score in points.items():\n    if score < low_score:\n        low_score = score\n        low_name = name\nprint(f"Low: {low_name} ({low_score})")',
          "เริ่มจากค่าสูงๆ แล้วอัปเดตเมื่อเจอค่าน้อยกว่า"),
        p(5, "กระดานคะแนนพร้อม Top", "scoreboard_top",
          "พิมพ์กระดานคะแนนแล้วหาอันดับหนึ่งด้วยมือ\n\n"
          "กำหนด `board = {\"Nida\": 70, \"Ohm\": 95, \"Pim\": 88}`\n\n"
          "พิมพ์ทุกคนแบบ `Nida: 70` แล้วปิดท้าย `Top: Ohm (95)`",
          "4 บรรทัด",
          "Nida: 70\nOhm: 95\nPim: 88\nTop: Ohm (95)",
          'board = {"Nida": 70, "Ohm": 95, "Pim": 88}\n\n# เขียนโค้ดตรงนี้',
          'board = {"Nida": 70, "Ohm": 95, "Pim": 88}\ntop_name = ""\ntop_score = 0\nfor name, score in board.items():\n    print(f"{name}: {score}")\n    if score > top_score:\n        top_score = score\n        top_name = name\nprint(f"Top: {top_name} ({top_score})")',
          "พิมพ์ไปด้วย หากสูงสุดไปด้วยใน loop เดียว"),
        p(14, "คลังสินค้าปรับสต็อก", "stock_review",
          "ปรับสต็อกสินค้า\n\n"
          "กำหนด `stock = {\"rice\": 10, \"oil\": 3, \"temp\": 0, \"salt\": 8}`\n\n"
          "แก้ oil เป็น 5 แล้ว del temp จากนั้นพิมพ์ items และจำนวนชนิดสินค้า",
          "4 บรรทัด",
          "rice: 10\noil: 5\nsalt: 8\nKinds: 3",
          'stock = {"rice": 10, "oil": 3, "temp": 0, "salt": 8}\n\n# เขียนโค้ดตรงนี้',
          'stock = {"rice": 10, "oil": 3, "temp": 0, "salt": 8}\nstock["oil"] = 5\ndel stock["temp"]\nfor key, value in stock.items():\n    print(f"{key}: {value}")\nprint(f"Kinds: {len(stock)}")',
          "แก้ → ลบ → รายงาน"),
        p(15, "นับคำแล้วหาคำยอดนิยม", "popular_word",
          "นับคำแล้วหาคำที่โผล่บ่อยสุดด้วยมือ\n\n"
          "กำหนด `words = [\"go\", \"run\", \"go\", \"jump\", \"go\", \"run\"]`\n\n"
          "นับความถี่ แล้วหาคำที่ยอดนิยมที่สุด แสดง `Popular: go (3)`",
          "บรรทัดเดียว", "Popular: go (3)",
          'words = ["go", "run", "go", "jump", "go", "run"]\ncount = {}\n\n# เขียนโค้ดตรงนี้',
          'words = ["go", "run", "go", "jump", "go", "run"]\ncount = {}\nfor word in words:\n    if word in count:\n        count[word] += 1\n    else:\n        count[word] = 1\ntop_word = ""\ntop_n = 0\nfor word, n in count.items():\n    if n > top_n:\n        top_n = n\n        top_word = word\nprint(f"Popular: {top_word} ({top_n})")',
          "นับก่อน แล้วค่อยวนหาค่าสูงสุดเอง"),
        p(16, "กล่องสรุปสมาชิก", "member_box",
          "สรุปข้อมูลสมาชิกแบบมีกรอบ\n\n"
          "กำหนด `member = {\"name\": \"Kate\", \"point\": 40, \"city\": \"Loei\"}`\n\n"
          "update point เป็น 55 เพิ่มคีย์ `tier` เป็น `Silver`\n"
          "แล้วแสดงตามตัวอย่าง",
          "กล่องสรุป",
          "====================\nname: Kate\npoint: 55\ncity: Loei\ntier: Silver\n====================",
          'member = {"name": "Kate", "point": 40, "city": "Loei"}\n\n# เขียนโค้ดตรงนี้',
          'member = {"name": "Kate", "point": 40, "city": "Loei"}\nmember.update({"point": 55})\nmember["tier"] = "Silver"\nprint("====================")\nfor key, value in member.items():\n    print(f"{key}: {value}")\nprint("====================")',
          "update + เพิ่มคีย์ + items ในกรอบ"),
    ],
)

print("done 033-036")
