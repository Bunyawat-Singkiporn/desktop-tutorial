# -*- coding: utf-8 -*-
"""Expand weeks 032-036 dictionaries arc."""
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


def week_032():
    names = [("ลิสต์มีซ้ำ", "list"), ("ทูเพิลคงที่", "tuple"), ("เซตตัดซ้ำ", "set"),
             ("เข้าถึงลิสต์", "index"), ("เข้าถึงทูเพิล", "index"),
             ("วนลิสต์", "for"), ("แปลงไม่ซ้ำ", "set(list)"), ("ความยาวเทียบ", "len"),
             ("เพิ่มในลิสต์", "append"), ("สมาชิกเซต", "in"), ("ยูเนียนสั้น", "|"),
             ("รวมสามชนิด", "ผสม"), ("ห้องเรียน", "list+set"), ("พิกัด+ชื่อ", "tuple+list"), ("ปิดทบทวน", "สรุป")]
    index = idx("บท 032 Collection Review", "list/tuple/set เคียงข้างกัน", "ไม่มี dict ยัง", names)
    probs = [
        p(2, "ลิสต์มีซ้ำ", "list_dup", 'students = ["Alice", "Bob", "Alice"] แสดงความยาว', "1 บรรทัด", "3",
          'students = ["Alice", "Bob", "Alice"]\n# ', 'students = ["Alice", "Bob", "Alice"]\nprint(len(students))'),
        p(3, "ทูเพิลคงที่", "tuple_days", 'days = ("Mon", "Tue", "Wed") แสดงท้าย', "1 บรรทัด", "Wed",
          'days = ("Mon", "Tue", "Wed")\n# ', 'days = ("Mon", "Tue", "Wed")\nprint(days[-1])'),
        p(4, "เซตตัดซ้ำ", "set_unique", 'unique_students = {"Alice", "Bob", "Alice"} แสดงจำนวน', "1 บรรทัด", "2",
          'unique_students = {"Alice", "Bob", "Alice"}\n# ', 'unique_students = {"Alice", "Bob", "Alice"}\nprint(len(unique_students))'),
        p(8, "เข้าถึงลิสต์", "list_access", 'students = ["Alice", "Bob"] แสดงแรก', "1 บรรทัด", "Alice",
          'students = ["Alice", "Bob"]\n# ', 'students = ["Alice", "Bob"]\nprint(students[0])'),
        p(9, "เข้าถึงทูเพิล", "tuple_access", 'grade_info = ("Grade 9", "Room 3") แสดงห้อง', "1 บรรทัด", "Room 3",
          'grade_info = ("Grade 9", "Room 3")\n# ', 'grade_info = ("Grade 9", "Room 3")\nprint(grade_info[1])'),
        p(6, "วนลิสต์", "loop_list", 'students = ["Alice", "Bob"] พิมพ์ทีละคน', "2 บรรทัด", "Alice\nBob",
          'students = ["Alice", "Bob"]\n# ', 'students = ["Alice", "Bob"]\nfor s in students:\n    print(s)'),
        p(7, "แปลงไม่ซ้ำ", "to_set", 'all_students = ["A", "B", "A"] แสดงจำนวนไม่ซ้ำ', "1 บรรทัด", "2",
          'all_students = ["A", "B", "A"]\n# ', 'all_students = ["A", "B", "A"]\nprint(len(set(all_students)))', "set(...)"),
        p(10, "ความยาวเทียบ", "len_compare",
          'lst = ["A", "A"] st = set(lst) แสดงสองความยาว', "2 บรรทัด", "2\n1",
          'lst = ["A", "A"]\n# ', 'lst = ["A", "A"]\nst = set(lst)\nprint(len(lst))\nprint(len(st))'),
        p(11, "เพิ่มในลิสต์", "list_append", 's = ["A"] append "B"', "1 บรรทัด", "['A', 'B']",
          's = ["A"]\n# ', 's = ["A"]\ns.append("B")\nprint(s)'),
        p(12, "สมาชิกเซต", "set_in", 's = {"A", "B"} แสดง "A" in s', "1 บรรทัด", "True",
          's = {"A", "B"}\n# ', 's = {"A", "B"}\nprint("A" in s)'),
        p(13, "ยูเนียนสั้น", "union_short", 'a = {1} b = {2} แสดงจำนวน a|b', "1 บรรทัด", "2",
          "a = {1}\nb = {2}\n# ", "a = {1}\nb = {2}\nprint(len(a | b))"),
        p(5, "รวมสามชนิด", "three_together",
          'students list มีซ้ำ, days tuple, unique set จาก list — แสดงสามความยาว',
          "3 บรรทัด", "3\n2\n2",
          'students = ["Alice", "Bob", "Alice"]\ndays = ("Mon", "Tue")\n# ',
          'students = ["Alice", "Bob", "Alice"]\ndays = ("Mon", "Tue")\nunique_students = set(students)\nprint(len(students))\nprint(len(days))\nprint(len(unique_students))',
          "แปลง list เป็น set"),
        p(14, "ห้องเรียน", "classroom",
          'names = ["Ann", "Ben", "Ann"] แสดง All และ Unique',
          "2 บรรทัด", "All: 3\nUnique: 2",
          'names = ["Ann", "Ben", "Ann"]\n# ',
          'names = ["Ann", "Ben", "Ann"]\nprint(f"All: {len(names)}")\nprint(f"Unique: {len(set(names))}")'),
        p(15, "พิกัด+ชื่อ", "point_name", 'point = (1, 2) names = ["Map"] แสดง X และชื่อ',
          "2 บรรทัด", "X: 1\nMap",
          'point = (1, 2)\nnames = ["Map"]\n# ',
          'point = (1, 2)\nnames = ["Map"]\nprint(f"X: {point[0]}")\nprint(names[0])'),
        p(16, "ปิดทบทวน", "coll_finale",
          'a = [1, 1] แปลงเป็นเซตแล้ว add 2 แสดงจำนวน',
          "1 บรรทัด", "2",
          "a = [1, 1]\n# ", "a = [1, 1]\ns = set(a)\ns.add(2)\nprint(len(s))"),
    ]
    write_week("032-collection-review", chapter="Collection Review", emoji="📚", index_md=index, problems=probs)


def week_033():
    names = [("อ่านชื่อ", "dict[key]"), ("อ่านอายุ", "access"), ("เพิ่มคะแนน", "assign new"),
             ("มีคีย์ไหม", "in"), ("วนคีย์", "for key"),
             ("นามบัตร", "หลายฟิลด์"), ("อัปเดตเบอร์", "overwrite"), ("พิมพ์คู่คีย์ค่า", "loop"),
             ("คอนแท็กต์", "phone"), ("เช็กคีย์", "if in"), ("โปรไฟล์เกม", "dict"),
             ("รายงานนักเรียน", "หลาย print"), ("เพิ่มเมือง", "new key"), ("บัตรสมาชิก", "ผสม"), ("สรุป dict", "วน")]
    index = idx("บท 033 Dictionaries", "dict literal / d[key] / เพิ่มคีย์ / in / for key in d",
                "ห้าม .keys .get .items .values del (บท 034)", names)
    student = 'student = {"name": "Alice", "age": 15, "score": 92}'
    probs = [
        p(2, "อ่านชื่อ", "read_name", f"มี {student} แสดงชื่อ", "1 บรรทัด", "Alice",
          f"{student}\n# ", f'{student}\nprint(student["name"])'),
        p(3, "อ่านอายุ", "read_age", f"มี {student} แสดงอายุ", "1 บรรทัด", "15",
          f"{student}\n# ", f'{student}\nprint(student["age"])'),
        p(4, "เพิ่มคะแนน", "add_score", 'd = {"name": "Bob"} แล้วตั้ง d["score"] = 88 แสดงคะแนน',
          "1 บรรทัด", "88",
          'd = {"name": "Bob"}\n# ', 'd = {"name": "Bob"}\nd["score"] = 88\nprint(d["score"])'),
        p(8, "มีคีย์ไหม", "key_in", f'มี {student} แสดงผล "name" in student', "1 บรรทัด", "True",
          f"{student}\n# ", f'{student}\nprint("name" in student)'),
        p(9, "วนคีย์", "for_keys", 'd = {"a": 1, "b": 2} พิมพ์ทีละคีย์', "2 บรรทัด", "a\nb",
          'd = {"a": 1, "b": 2}\n# ', 'd = {"a": 1, "b": 2}\nfor key in d:\n    print(key)'),
        p(6, "นามบัตร", "name_card", f"มี {student} แสดง Name และ Age", "2 บรรทัด", "Name: Alice\nAge: 15",
          f"{student}\n# ",
          f'{student}\nprint(f"Name: {{student[\'name\']}}")\nprint(f"Age: {{student[\'age\']}}")', "อ่านสองคีย์"),
        p(7, "อัปเดตเบอร์", "update_phone", 'contact = {"name": "Bob", "phone": "000"} เปลี่ยน phone เป็น 081-111 และแสดง',
          "1 บรรทัด", "081-111",
          'contact = {"name": "Bob", "phone": "000"}\n# ',
          'contact = {"name": "Bob", "phone": "000"}\ncontact["phone"] = "081-111"\nprint(contact["phone"])'),
        p(10, "พิมพ์คู่คีย์ค่า", "print_pairs", 'd = {"x": 10, "y": 20} พิมพ์ key : value',
          "2 บรรทัด", "x : 10\ny : 20",
          'd = {"x": 10, "y": 20}\n# ',
          'd = {"x": 10, "y": 20}\nfor key in d:\n    print(key, ":", d[key])'),
        p(11, "คอนแท็กต์", "contact_read", 'c = {"name": "Bob", "phone": "081-234-5678"} แสดงเบอร์',
          "1 บรรทัด", "081-234-5678",
          'c = {"name": "Bob", "phone": "081-234-5678"}\n# ',
          'c = {"name": "Bob", "phone": "081-234-5678"}\nprint(c["phone"])'),
        p(12, "เช็กคีย์", "safe_key", 'd = {"score": 90} ถ้ามี score แสดง Found: ค่า ไม่งั้น No',
          "1 บรรทัด", "Found: 90",
          'd = {"score": 90}\n# ',
          'd = {"score": 90}\nif "score" in d:\n    print("Found:", d["score"])\nelse:\n    print("No")', "ใช้ in"),
        p(13, "โปรไฟล์เกม", "game_dict", 'g = {"player": "Nova"} เพิ่ม level=3 แล้วแสดงสองค่า',
          "2 บรรทัด", "Nova\n3",
          'g = {"player": "Nova"}\n# ',
          'g = {"player": "Nova"}\ng["level"] = 3\nprint(g["player"])\nprint(g["level"])'),
        p(5, "รายงานนักเรียน", "student_report", f"มี {student} แสดงสามบรรทัด name/age/score",
          "3 บรรทัด", "name : Alice\nage : 15\nscore : 92",
          f"{student}\n# ",
          f'{student}\nfor key in student:\n    print(key, ":", student[key])', "วนคีย์"),
        p(14, "เพิ่มเมือง", "add_city", 'c = {"name": "Bob"} เพิ่ม city=Bangkok แสดง city',
          "1 บรรทัด", "Bangkok",
          'c = {"name": "Bob"}\n# ',
          'c = {"name": "Bob"}\nc["city"] = "Bangkok"\nprint(c["city"])'),
        p(15, "บัตรสมาชิก", "member_card",
          'm = {"id": 1, "name": "Ann"} แสดง ID และ Name',
          "2 บรรทัด", "ID: 1\nName: Ann",
          'm = {"id": 1, "name": "Ann"}\n# ',
          'm = {"id": 1, "name": "Ann"}\nprint(f"ID: {m[\'id\']}")\nprint(f"Name: {m[\'name\']}")'),
        p(16, "สรุป dict", "dict_finale",
          'd = {"a": 1, "b": 2, "c": 3} พิมพ์ทุกคีย์ แล้วแสดงจำนวนคีย์ด้วยตัวนับ',
          "4 บรรทัด", "a\nb\nc\nCount: 3",
          'd = {"a": 1, "b": 2, "c": 3}\ncount = 0\n# ',
          'd = {"a": 1, "b": 2, "c": 3}\ncount = 0\nfor key in d:\n    print(key)\n    count = count + 1\nprint(f"Count: {count}")'),
    ]
    write_week("033-dictionaries", chapter="Dictionaries", emoji="📖", index_md=index, problems=probs)


def week_034():
    names = [("อัปเดตอายุ", "assign"), ("update หลายคีย์", "update"), ("ลบคีย์", "del"),
             ("วนค่า", "values"), ("วนคู่", "items"),
             ("แก้คะแนน", "update score"), ("ลบแล้ววน", "del+loop"), ("พิมพ์สวย", "items f"),
             ("เพิ่มด้วย update", "update"), ("รายงานค่า", "values only"), ("เปลี่ยนเบอร์", "assign"),
             ("โปรไฟล์เต็ม", "หลายเมธอด"), ("ล้างคะแนน", "del"), ("คู่คีย์ค่า", "items"), ("สรุป methods", "ผสม")]
    index = idx("บท 034 Dictionary Methods", "update / del / values / items", "ห้าม .keys .get", names)
    probs = [
        p(2, "อัปเดตอายุ", "set_age", 's = {"name": "Alice", "age": 15} เปลี่ยน age เป็น 16 แสดง age',
          "1 บรรทัด", "16",
          's = {"name": "Alice", "age": 15}\n# ',
          's = {"name": "Alice", "age": 15}\ns["age"] = 16\nprint(s["age"])'),
        p(3, "update หลายคีย์", "do_update", 's = {"name": "Alice"} แล้ว update age=16 score=90 แสดง age',
          "1 บรรทัด", "16",
          's = {"name": "Alice"}\n# ',
          's = {"name": "Alice"}\ns.update({"age": 16, "score": 90})\nprint(s["age"])'),
        p(4, "ลบคีย์", "do_del", 's = {"name": "Alice", "score": 90} ลบ score แล้วแสดงผล "score" in s',
          "1 บรรทัด", "False",
          's = {"name": "Alice", "score": 90}\n# ',
          's = {"name": "Alice", "score": 90}\ndel s["score"]\nprint("score" in s)'),
        p(8, "วนค่า", "for_values", 's = {"name": "Alice", "age": 15} พิมพ์ทุกค่าด้วย .values()',
          "2 บรรทัด", "Alice\n15",
          's = {"name": "Alice", "age": 15}\n# ',
          's = {"name": "Alice", "age": 15}\nfor value in s.values():\n    print(value)'),
        p(9, "วนคู่", "for_items", 's = {"name": "Alice", "age": 15} พิมพ์ key: value ด้วย .items()',
          "2 บรรทัด", "name: Alice\nage: 15",
          's = {"name": "Alice", "age": 15}\n# ',
          's = {"name": "Alice", "age": 15}\nfor key, value in s.items():\n    print(f"{key}: {value}")'),
        p(6, "แก้คะแนน", "fix_score", 's = {"score": 80} update เป็น 95 แสดง',
          "1 บรรทัด", "95",
          's = {"score": 80}\n# ',
          's = {"score": 80}\ns.update({"score": 95})\nprint(s["score"])', "update"),
        p(7, "ลบแล้ววน", "del_loop", 's = {"a": 1, "b": 2, "c": 3} ลบ b แล้วพิมพ์คีย์ที่เหลือ',
          "2 บรรทัด", "a\nc",
          's = {"a": 1, "b": 2, "c": 3}\n# ',
          's = {"a": 1, "b": 2, "c": 3}\ndel s["b"]\nfor key in s:\n    print(key)'),
        p(10, "พิมพ์สวย", "pretty_items", 'd = {"x": 1, "y": 2} พิมพ์ด้วย items',
          "2 บรรทัด", "x: 1\ny: 2",
          'd = {"x": 1, "y": 2}\n# ',
          'd = {"x": 1, "y": 2}\nfor key, value in d.items():\n    print(f"{key}: {value}")'),
        p(11, "เพิ่มด้วย update", "update_add", 'd = {"a": 1} update {"b": 2} แสดง b',
          "1 บรรทัด", "2",
          'd = {"a": 1}\n# ',
          'd = {"a": 1}\nd.update({"b": 2})\nprint(d["b"])'),
        p(12, "รายงานค่า", "values_only", 'd = {"math": 80, "sci": 90} พิมพ์ทุกคะแนน',
          "2 บรรทัด", "80\n90",
          'd = {"math": 80, "sci": 90}\n# ',
          'd = {"math": 80, "sci": 90}\nfor v in d.values():\n    print(v)'),
        p(13, "เปลี่ยนเบอร์", "change_phone", 'c = {"phone": "000"} ตั้งเป็น 999 แสดง',
          "1 บรรทัด", "999",
          'c = {"phone": "000"}\n# ',
          'c = {"phone": "000"}\nc["phone"] = "999"\nprint(c["phone"])'),
        p(5, "โปรไฟล์เต็ม", "full_profile",
          's = {"name": "Alice", "age": 15} update score=90 แล้วพิมพ์ทุกคู่',
          "3 บรรทัด", "name: Alice\nage: 15\nscore: 90",
          's = {"name": "Alice", "age": 15}\n# ',
          's = {"name": "Alice", "age": 15}\ns.update({"score": 90})\nfor key, value in s.items():\n    print(f"{key}: {value}")',
          "update แล้ว items"),
        p(14, "ล้างคะแนน", "clear_score", 's = {"name": "A", "score": 10} ลบ score แสดงคีย์ที่เหลือ',
          "1 บรรทัด", "name",
          's = {"name": "A", "score": 10}\n# ',
          's = {"name": "A", "score": 10}\ndel s["score"]\nfor key in s:\n    print(key)'),
        p(15, "คู่คีย์ค่า", "pairs", 'd = {"p": 1, "q": 2} พิมพ์ p=1 แบบ f-string จาก items',
          "2 บรรทัด", "p=1\nq=2",
          'd = {"p": 1, "q": 2}\n# ',
          'd = {"p": 1, "q": 2}\nfor key, value in d.items():\n    print(f"{key}={value}")'),
        p(16, "สรุป methods", "methods_finale",
          'd = {"a": 1} update b=2 ลบ a พิมพ์ค่าที่เหลือด้วย values',
          "1 บรรทัด", "2",
          'd = {"a": 1}\n# ',
          'd = {"a": 1}\nd.update({"b": 2})\ndel d["a"]\nfor v in d.values():\n    print(v)'),
    ]
    write_week("034-dictionary-methods", chapter="Dictionary Methods", emoji="🧰", index_md=index, problems=probs)


def week_035():
    names = [("นับความถี่", "freq"), ("ตรวจคำตอบ", "quiz input"), ("ราคาผลไม้", "items loop"),
             ("นับคำ", "count dict"), ("เพิ่มจากว่าง", "empty {}"),
             ("รวมราคา", "total"), ("เช็กคีย์ก่อนนับ", "if in"), ("ควิซสองข้อ", "input prompt"),
             ("เมนูราคา", "items"), ("นับเกรด", "freq"), ("ตะกร้า", "sum prices"),
             ("คลังความถี่", "ผสม"), ("ตรวจข้อสอบ", "compare"), ("บิลร้าน", "items+total"), ("สรุป practice", "freq+print")]
    index = idx("บท 035 Dictionary Practice", "ฝึก dict + input(prompt) + นับความถี่", "ใช้เมธอดที่สอนแล้ว", names)
    probs = [
        p(2, "นับความถี่", "word_freq",
          'words = ["cat", "dog", "cat"] นับความถี่ใน count แล้วแสดง count["cat"]',
          "1 บรรทัด", "2",
          'words = ["cat", "dog", "cat"]\ncount = {}\n# ',
          'words = ["cat", "dog", "cat"]\ncount = {}\nfor word in words:\n    if word in count:\n        count[word] = count[word] + 1\n    else:\n        count[word] = 1\nprint(count["cat"])'),
        p(3, "ตรวจคำตอบ", "check_answer",
          'answers = {"q1": "A"} รับคำตอบหนึ่งบรรทัด ถ้าถูกพิมพ์ Correct ไม่งั้น Wrong',
          "1 บรรทัด", "Correct",
          'answers = {"q1": "A"}\n# ',
          'answers = {"q1": "A"}\nuser_answer = input()\nif user_answer == answers["q1"]:\n    print("Correct")\nelse:\n    print("Wrong")',
          sample_in="A", hint="เทียบกับ answers[\"q1\"]"),
        p(4, "ราคาผลไม้", "fruit_prices",
          'prices = {"apple": 15, "banana": 8} พิมพ์ทุกคู่แบบ apple: 15',
          "2 บรรทัด", "apple: 15\nbanana: 8",
          'prices = {"apple": 15, "banana": 8}\n# ',
          'prices = {"apple": 15, "banana": 8}\nfor item, price in prices.items():\n    print(f"{item}: {price}")'),
        p(8, "นับคำ", "count_words",
          'words = ["a", "b", "a", "a"] แสดงจำนวน "a"',
          "1 บรรทัด", "3",
          'words = ["a", "b", "a", "a"]\ncount = {}\n# ',
          'words = ["a", "b", "a", "a"]\ncount = {}\nfor w in words:\n    if w in count:\n        count[w] = count[w] + 1\n    else:\n        count[w] = 1\nprint(count["a"])'),
        p(9, "เพิ่มจากว่าง", "from_empty",
          'เริ่ม {} ตั้ง d["x"]=1 และ d["y"]=2 แสดง y',
          "1 บรรทัด", "2",
          "d = {}\n# ", 'd = {}\nd["x"] = 1\nd["y"] = 2\nprint(d["y"])'),
        p(6, "รวมราคา", "sum_prices",
          'prices = {"apple": 15, "banana": 8, "mango": 25} รวมราคาทั้งหมด',
          "1 บรรทัด", "48",
          'prices = {"apple": 15, "banana": 8, "mango": 25}\ntotal = 0\n# ',
          'prices = {"apple": 15, "banana": 8, "mango": 25}\ntotal = 0\nfor item, price in prices.items():\n    total = total + price\nprint(total)', "สะสมจาก values ผ่าน items"),
        p(7, "เช็กคีย์ก่อนนับ", "safe_count",
          'count = {"cat": 2} เพิ่ม "dog" เป็น 1 แบบเช็ก in',
          "1 บรรทัด", "1",
          'count = {"cat": 2}\nword = "dog"\n# ',
          'count = {"cat": 2}\nword = "dog"\nif word in count:\n    count[word] = count[word] + 1\nelse:\n    count[word] = 1\nprint(count["dog"])'),
        p(10, "ควิซสองข้อ", "two_quiz",
          'answers = {"q1": "A", "q2": "C"} รับคำตอบสองบรรทัด (q1 แล้ว q2) แสดงจำนวนข้อถูก',
          "1 บรรทัด", "Correct: 1",
          'answers = {"q1": "A", "q2": "C"}\n# ',
          'answers = {"q1": "A", "q2": "C"}\ncorrect = 0\na1 = input()\nif a1 == answers["q1"]:\n    correct = correct + 1\na2 = input()\nif a2 == answers["q2"]:\n    correct = correct + 1\nprint(f"Correct: {correct}")',
          sample_in="A\nB", hint="นับข้อถูก"),
        p(11, "เมนูราคา", "menu_prices",
          'menu = {"tea": 30, "coffee": 45} พิมพ์รายการ',
          "2 บรรทัด", "tea: 30\ncoffee: 45",
          'menu = {"tea": 30, "coffee": 45}\n# ',
          'menu = {"tea": 30, "coffee": 45}\nfor k, v in menu.items():\n    print(f"{k}: {v}")'),
        p(12, "นับเกรด", "grade_freq",
          'grades = ["A", "B", "A"] นับจำนวน A',
          "1 บรรทัด", "2",
          'grades = ["A", "B", "A"]\ncount = {}\n# ',
          'grades = ["A", "B", "A"]\ncount = {}\nfor g in grades:\n    if g in count:\n        count[g] = count[g] + 1\n    else:\n        count[g] = 1\nprint(count["A"])'),
        p(13, "ตะกร้า", "cart_total",
          'cart = {"pen": 10, "gum": 5} รวมยอด',
          "1 บรรทัด", "Total: 15",
          'cart = {"pen": 10, "gum": 5}\ntotal = 0\n# ',
          'cart = {"pen": 10, "gum": 5}\ntotal = 0\nfor item, price in cart.items():\n    total = total + price\nprint(f"Total: {total}")'),
        p(5, "คลังความถี่", "freq_report",
          'words = ["cat", "dog", "cat", "bird", "dog", "cat"] สร้าง count แล้วพิมพ์ทุกคู่',
          "3 บรรทัด", "cat: 3\ndog: 2\nbird: 1",
          'words = ["cat", "dog", "cat", "bird", "dog", "cat"]\ncount = {}\n# ',
          'words = ["cat", "dog", "cat", "bird", "dog", "cat"]\ncount = {}\nfor word in words:\n    if word in count:\n        count[word] = count[word] + 1\n    else:\n        count[word] = 1\nfor key, value in count.items():\n    print(f"{key}: {value}")',
          "นับแล้วค่อย items"),
        p(14, "ตรวจข้อสอบ", "exam_check",
          'answers = {"q1": "B"} รับคำตอบ แสดง OK/NO',
          "1 บรรทัด", "OK",
          'answers = {"q1": "B"}\n# ',
          'answers = {"q1": "B"}\nans = input()\nif ans == answers["q1"]:\n    print("OK")\nelse:\n    print("NO")',
          sample_in="B"),
        p(15, "บิลร้าน", "shop_bill",
          'prices = {"rice": 40, "egg": 5} พิมพ์รายการแล้ว Total',
          "3 บรรทัด", "rice: 40\negg: 5\nTotal: 45",
          'prices = {"rice": 40, "egg": 5}\ntotal = 0\n# ',
          'prices = {"rice": 40, "egg": 5}\ntotal = 0\nfor item, price in prices.items():\n    print(f"{item}: {price}")\n    total = total + price\nprint(f"Total: {total}")'),
        p(16, "สรุป practice", "practice_finale",
          'data = ["x", "y", "x"] นับความถี่ แสดงจำนวนชนิดคำ (len ของ dict)',
          "1 บรรทัด", "Kinds: 2",
          'data = ["x", "y", "x"]\ncount = {}\n# ',
          'data = ["x", "y", "x"]\ncount = {}\nfor w in data:\n    if w in count:\n        count[w] = count[w] + 1\n    else:\n        count[w] = 1\nprint(f"Kinds: {len(count)}")'),
    ]
    write_week("035-dictionary-practice", chapter="Dictionary Practice", emoji="🎯", index_md=index, problems=probs)


def week_036():
    names = [("อ่านปลอดภัย", "if in"), ("หาคะแนนสูงสุด", "manual max"), ("อัปเดต", "update"),
             ("ลบคีย์", "del"), ("พิมพ์ items", "items"),
             ("รวมค่า", "sum values"), ("นับคีย์", "count keys"), ("Top ชื่อ", "track max"),
             ("มีคะแนนไหม", "safe"), ("รายงาน", "items"), ("เปลี่ยนค่า", "assign"),
             ("กระดานคะแนน", "top"), ("ลบแล้วเช็ก", "del+in"), ("สรุปห้อง", "ผสม"), ("ปิด dict", "finale")]
    index = idx("บท 036 Review Dictionaries", "ทบทวน dict ทั้งชุด — หา max ด้วยลูปเอง", "ห้าม builtin max()", names)
    probs = [
        p(2, "อ่านปลอดภัย", "safe_read", 's = {"name": "A"} ถ้ามี score แสดงค่า ไม่งั้น No score yet',
          "1 บรรทัด", "No score yet",
          's = {"name": "A"}\n# ',
          's = {"name": "A"}\nif "score" in s:\n    print(s["score"])\nelse:\n    print("No score yet")'),
        p(3, "หาคะแนนสูงสุด", "top_score",
          'scores = {"Alice": 88, "Bob": 72, "Charlie": 95} หาชื่อและคะแนนสูงสุดด้วยลูป',
          "1 บรรทัด", "Top: Charlie (95)",
          'scores = {"Alice": 88, "Bob": 72, "Charlie": 95}\nhighest = ""\nmax_score = 0\n# ',
          'scores = {"Alice": 88, "Bob": 72, "Charlie": 95}\nhighest = ""\nmax_score = 0\nfor name, score in scores.items():\n    if score > max_score:\n        max_score = score\n        highest = name\nprint(f"Top: {highest} ({max_score})")',
          "อย่าใช้ max()"),
        p(4, "อัปเดต", "rev_update", 's = {"age": 10} update เป็น 11 แสดง',
          "1 บรรทัด", "11",
          's = {"age": 10}\n# ',
          's = {"age": 10}\ns.update({"age": 11})\nprint(s["age"])'),
        p(8, "ลบคีย์", "rev_del", 's = {"a": 1, "b": 2} ลบ a แสดง "a" in s',
          "1 บรรทัด", "False",
          's = {"a": 1, "b": 2}\n# ',
          's = {"a": 1, "b": 2}\ndel s["a"]\nprint("a" in s)'),
        p(9, "พิมพ์ items", "rev_items", 'd = {"k": 5} พิมพ์ k: 5',
          "1 บรรทัด", "k: 5",
          'd = {"k": 5}\n# ',
          'd = {"k": 5}\nfor key, value in d.items():\n    print(f"{key}: {value}")'),
        p(6, "รวมค่า", "sum_vals", 'd = {"a": 10, "b": 15} รวมค่า',
          "1 บรรทัด", "25",
          'd = {"a": 10, "b": 15}\nt = 0\n# ',
          'd = {"a": 10, "b": 15}\nt = 0\nfor v in d.values():\n    t = t + v\nprint(t)', "วน values"),
        p(7, "นับคีย์", "count_keys", 'd = {"a": 1, "b": 2, "c": 3} นับคีย์ด้วยลูป',
          "1 บรรทัด", "3",
          'd = {"a": 1, "b": 2, "c": 3}\nc = 0\n# ',
          'd = {"a": 1, "b": 2, "c": 3}\nc = 0\nfor key in d:\n    c = c + 1\nprint(c)'),
        p(10, "Top ชื่อ", "top_name",
          'scores = {"Ann": 50, "Ben": 80} แสดงชื่อที่ได้สูงสุด',
          "1 บรรทัด", "Ben",
          'scores = {"Ann": 50, "Ben": 80}\nhighest = ""\nbest = 0\n# ',
          'scores = {"Ann": 50, "Ben": 80}\nhighest = ""\nbest = 0\nfor name, score in scores.items():\n    if score > best:\n        best = score\n        highest = name\nprint(highest)'),
        p(11, "มีคะแนนไหม", "has_score", 's = {"score": 70} แสดง Found หรือ Missing',
          "1 บรรทัด", "Found",
          's = {"score": 70}\n# ',
          's = {"score": 70}\nif "score" in s:\n    print("Found")\nelse:\n    print("Missing")'),
        p(12, "รายงาน", "report_items", 'd = {"math": 80, "eng": 75} พิมพ์วิชา:คะแนน',
          "2 บรรทัด", "math: 80\neng: 75",
          'd = {"math": 80, "eng": 75}\n# ',
          'd = {"math": 80, "eng": 75}\nfor k, v in d.items():\n    print(f"{k}: {v}")'),
        p(13, "เปลี่ยนค่า", "change_val", 'd = {"hp": 10} ตั้งเป็น 20',
          "1 บรรทัด", "20",
          'd = {"hp": 10}\n# ',
          'd = {"hp": 10}\nd["hp"] = 20\nprint(d["hp"])'),
        p(5, "กระดานคะแนน", "scoreboard",
          'scores = {"A": 10, "B": 30, "C": 20} แสดง Top: ชื่อ (คะแนน)',
          "1 บรรทัด", "Top: B (30)",
          'scores = {"A": 10, "B": 30, "C": 20}\nh = ""\nm = 0\n# ',
          'scores = {"A": 10, "B": 30, "C": 20}\nh = ""\nm = 0\nfor name, score in scores.items():\n    if score > m:\n        m = score\n        h = name\nprint(f"Top: {h} ({m})")'),
        p(14, "ลบแล้วเช็ก", "del_check", 'd = {"x": 1, "y": 2} ลบ x แล้วแสดงจำนวนคีย์',
          "1 บรรทัด", "1",
          'd = {"x": 1, "y": 2}\n# ',
          'd = {"x": 1, "y": 2}\ndel d["x"]\nprint(len(d))'),
        p(15, "สรุปห้อง", "class_summary",
          'room = {"students": 30, "teacher": 1} รวมค่าตัวเลข',
          "1 บรรทัด", "People: 31",
          'room = {"students": 30, "teacher": 1}\nt = 0\n# ',
          'room = {"students": 30, "teacher": 1}\nt = 0\nfor v in room.values():\n    t = t + v\nprint(f"People: {t}")'),
        p(16, "ปิด dict", "dict_close",
          'scores = {"Ann": 40, "Ben": 90} แสดงชื่อคนที่ได้ >=50 ทีละบรรทัด',
          "1 บรรทัด", "Ben",
          'scores = {"Ann": 40, "Ben": 90}\n# ',
          'scores = {"Ann": 40, "Ben": 90}\nfor name, score in scores.items():\n    if score >= 50:\n        print(name)'),
    ]
    write_week("036-review-dictionaries", chapter="Review Dictionaries", emoji="📘", index_md=index, problems=probs)


if __name__ == "__main__":
    week_032()
    week_033()
    week_034()
    week_035()
    week_036()
    print("032-036 done")
