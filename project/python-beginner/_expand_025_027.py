# -*- coding: utf-8 -*-
"""Expand weeks 025-036 collections to 15 problems each."""
from _expand_helpers import write_week

def p(n, title, slug, body, out_desc, sample_out, starter, answer, hint=None, sample_in=None):
    return dict(
        n=n, title=title, slug=slug, body=body,
        input_desc="ดูตัวอย่าง" if sample_in is not None else "ไม่มี",
        output_desc=out_desc, sample_input=sample_in, sample_output=sample_out,
        hint=hint, starter=starter, answer=answer,
    )


def simple_index(title, scope, bans, names):
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

**ขอบเขตของบทนี้:** {scope}

> ❌ {bans}

---

## ลำดับที่แนะนำ

| # | ไฟล์ | ระดับ | โจทย์ | แกนการคิด |
|---|------|-------|-------|-----------|
{rows}

**สรุป:** 🟢 Easy 5 ข้อ · 🟡 Medium 6 ข้อ · 🔴 Challenge 4 ข้อ = **15 ข้อ**
"""


def week_025():
    names = [
        ("สมาชิกแรก", "index 0"), ("สมาชิกท้าย", "index -1"), ("ความยาว", "len"),
        ("วนพิมพ์", "for-in"), ("ตำแหน่งกลาง", "index 1"),
        ("รวมคะแนน", "accumulator"), ("พิมพ์คู่แรก-ท้าย", "0 และ -1"),
        ("นับสมาชิก", "len ป้าย"), ("ลิสต์ว่าง?", "len==0 via print"), 
        ("ผลรวมและจำนวน", "total+len"), ("แสดงพร้อมลำดับคร่าวๆ", "ค่าอย่างเดียว"),
        ("รายงานผลไม้", "index หลายตัว"), ("เฉลี่ยคะแนน", "total/len"),
        ("สลับความหมายขอบ", "0 vs -1"), ("โปรไฟล์ลิสต์", "ผสม"),
    ]
    # Fix weak names - keep axes simple
    names[8] = ("พิมพ์ทุกตัว", "for loop")
    names[10] = ("สามค่าแรก", "index 0,1,2")
    idx = simple_index("บท 025 Lists", "list literal / index / negative index / len / for-in / สะสม",
                       "ห้าม .append .remove .sort (บท 026)", names)
    fruits = 'fruits = ["apple", "banana", "mango"]'
    scores = "scores = [85, 90, 78, 92, 88]"
    probs = [
        p(2, "สมาชิกแรก", "first_item", f"มี {fruits} แสดงสมาชิกแรก", "1 บรรทัด", "apple",
          f"{fruits}\n# แสดง", f'{fruits}\nprint(fruits[0])'),
        p(3, "สมาชิกท้าย", "last_item", f"มี {fruits} แสดงสมาชิกท้ายด้วย index ติดลบ", "1 บรรทัด", "mango",
          f"{fruits}\n# แสดง", f'{fruits}\nprint(fruits[-1])'),
        p(4, "ความยาว", "list_len", f"มี {fruits} แสดงจำนวนสมาชิก", "1 บรรทัด", "3",
          f"{fruits}\n# ความยาว", f'{fruits}\nprint(len(fruits))'),
        p(8, "วนพิมพ์", "print_all", f"มี {fruits} พิมพ์ทีละผล", "3 บรรทัด", "apple\nbanana\nmango",
          f"{fruits}\n# วน", f'{fruits}\nfor f in fruits:\n    print(f)'),
        p(9, "ตำแหน่งกลาง", "middle_item", f"มี {fruits} แสดงสมาชิก index 1", "1 บรรทัด", "banana",
          f"{fruits}\n# กลาง", f'{fruits}\nprint(fruits[1])'),
        p(6, "รวมคะแนน", "sum_scores", f"มี {scores} รวมคะแนนทั้งหมด", "1 บรรทัด", "433",
          f"{scores}\ntotal = 0\n# รวม",
          f"{scores}\ntotal = 0\nfor s in scores:\n    total = total + s\nprint(total)", "สะสมทีละตัว"),
        p(7, "พิมพ์คู่แรก-ท้าย", "first_last", f"มี {fruits} แสดงแรกและท้ายคนละบรรทัด", "2 บรรทัด", "apple\nmango",
          f"{fruits}\n# แสดง", f'{fruits}\nprint(fruits[0])\nprint(fruits[-1])', "ใช้ 0 และ -1"),
        p(10, "นับสมาชิก", "len_label", f'มี names = ["Ann", "Ben", "Cat", "Dan"] แสดง Count: ...',
          "1 บรรทัด", "Count: 4",
          'names = ["Ann", "Ben", "Cat", "Dan"]\n# นับ',
          'names = ["Ann", "Ben", "Cat", "Dan"]\nprint(f"Count: {len(names)}")'),
        p(11, "พิมพ์ทุกตัว", "print_nums", "มี nums = [10, 20, 30] พิมพ์ทีละค่า", "3 บรรทัด", "10\n20\n30",
          "nums = [10, 20, 30]\n# วน", "nums = [10, 20, 30]\nfor n in nums:\n    print(n)"),
        p(12, "ผลรวมและจำนวน", "total_and_len", f"มี {scores} แสดง Total และ Count", "2 บรรทัด", "Total: 433\nCount: 5",
          f"{scores}\ntotal = 0\n# สรุป",
          f'{scores}\ntotal = 0\nfor s in scores:\n    total = total + s\nprint(f"Total: {{total}}")\nprint(f"Count: {{len(scores)}}")',
          "รวมก่อน แล้วค่อย len"),
        p(13, "สามค่าแรก", "first_three", "มี data = [4, 5, 6, 7, 8] แสดง index 0 1 2 คนละบรรทัด",
          "3 บรรทัด", "4\n5\n6",
          "data = [4, 5, 6, 7, 8]\n# สามค่าแรก",
          "data = [4, 5, 6, 7, 8]\nprint(data[0])\nprint(data[1])\nprint(data[2])"),
        p(5, "รายงานผลไม้", "fruit_report", f"มี {fruits} แสดง First/Second/Last ตามป้าย",
          "3 บรรทัด", "First: apple\nSecond: banana\nLast: mango",
          f"{fruits}\n# รายงาน",
          f'{fruits}\nprint(f"First: {{fruits[0]}}")\nprint(f"Second: {{fruits[1]}}")\nprint(f"Last: {{fruits[-1]}}")',
          "ใช้ทั้ง index บวกและลบ"),
        p(14, "เฉลี่ยคะแนน", "avg_scores", f"มี {scores} แสดง Average ทศนิยม 1 ตำแหน่ง",
          "1 บรรทัด", "86.6",
          f"{scores}\ntotal = 0\n# เฉลี่ย",
          f'{scores}\ntotal = 0\nfor s in scores:\n    total = total + s\nprint(f"{{total / len(scores):.1f}}")',
          "total / len"),
        p(15, "สลับความหมายขอบ", "edge_values", "มี nums = [9, 8, 7] แสดง head=nums[0] และ tail=nums[-1]",
          "2 บรรทัด", "head=9\ntail=7",
          "nums = [9, 8, 7]\n# ขอบ",
          'nums = [9, 8, 7]\nprint(f"head={nums[0]}")\nprint(f"tail={nums[-1]}")'),
        p(16, "โปรไฟล์ลิสต์", "list_profile",
          'มี items = ["pen", "book", "bag"] แสดงความยาว สมาชิกแรก และพิมพ์ทุกชิ้นหลังป้าย Items:',
          "5 บรรทัด", "Len: 3\nFirst: pen\nItems:\npen\nbook\nbag",
          'items = ["pen", "book", "bag"]\n# โปรไฟล์',
          'items = ["pen", "book", "bag"]\nprint(f"Len: {len(items)}")\nprint(f"First: {items[0]}")\nprint("Items:")\nfor x in items:\n    print(x)',
          "ผสม len index และ for"),
    ]
    # Fix sample for 16 - that's 6 lines not 5
    probs[-1]["sample_output"] = "Len: 3\nFirst: pen\nItems:\npen\nbook\nbag"
    probs[-1]["output_desc"] = "หลายบรรทัด"
    write_week("025-lists", chapter="Lists", emoji="📋", index_md=idx, problems=probs)


def week_026():
    names = [
        ("เพิ่มท้าย", "append"), ("ลบค่า", "remove"), ("เรียงน้อยไปมาก", "sort"),
        ("เรียงมากไปน้อย", "sort reverse"), ("แก้ค่าตาม index", "index assign"),
        ("เพิ่มแล้วเรียง", "append+sort"), ("ลบแล้วพิมพ์", "remove+print"),
        ("แก้กลางลิสต์", "เปลี่ยน [1]"), ("ต่อคิวงาน", "append หลายครั้ง"),
        ("จัดอันดับคะแนน", "sort reverse รายงาน"), ("ลบผลไม้", "remove แล้ววน"),
        ("อัปเดตรายการ", "assign+append"), ("จัดคลัง", "หลายเมธอด"),
        ("คิวเสร็จสิ้น", "append+remove"), ("กระดานคะแนน", "ผสม"),
    ]
    idx = simple_index("บท 026 List Methods", "append / remove / sort / sort(reverse=True) / แก้ค่าด้วย index",
                       "ห้าม insert/pop/extend/index/count/sorted", names)
    probs = [
        p(2, "เพิ่มท้าย", "do_append", 'เริ่ม nums = [1, 2] แล้ว append(3) แสดงลิสต์', "1 บรรทัด", "[1, 2, 3]",
          "nums = [1, 2]\n# เพิ่ม", "nums = [1, 2]\nnums.append(3)\nprint(nums)"),
        p(3, "ลบค่า", "do_remove", 'fruits = ["a", "b", "c"] ลบ "b" แล้วแสดง', "1 บรรทัด", "['a', 'c']",
          'fruits = ["a", "b", "c"]\n# ลบ', 'fruits = ["a", "b", "c"]\nfruits.remove("b")\nprint(fruits)'),
        p(4, "เรียงน้อยไปมาก", "do_sort", "nums = [5, 1, 4] เรียงแล้วแสดง", "1 บรรทัด", "[1, 4, 5]",
          "nums = [5, 1, 4]\n# เรียง", "nums = [5, 1, 4]\nnums.sort()\nprint(nums)"),
        p(8, "เรียงมากไปน้อย", "sort_desc", "nums = [5, 1, 4] เรียงจากมากไปน้อย", "1 บรรทัด", "[5, 4, 1]",
          "nums = [5, 1, 4]\n# เรียงกลับ", "nums = [5, 1, 4]\nnums.sort(reverse=True)\nprint(nums)"),
        p(9, "แก้ค่าตาม index", "index_assign", 'fruits = ["apple", "banana", "mango"] เปลี่ยนตัวกลางเป็น "orange"',
          "1 บรรทัด", "['apple', 'orange', 'mango']",
          'fruits = ["apple", "banana", "mango"]\n# แก้',
          'fruits = ["apple", "banana", "mango"]\nfruits[1] = "orange"\nprint(fruits)'),
        p(6, "เพิ่มแล้วเรียง", "append_sort", "nums = [3, 1] append 2 แล้ว sort", "1 บรรทัด", "[1, 2, 3]",
          "nums = [3, 1]\n# เพิ่มและเรียง", "nums = [3, 1]\nnums.append(2)\nnums.sort()\nprint(nums)", "ทำทีละขั้น"),
        p(7, "ลบแล้วพิมพ์", "remove_print", 'colors = ["red", "blue", "green"] ลบ red แล้วพิมพ์ทีละสี',
          "2 บรรทัด", "blue\ngreen",
          'colors = ["red", "blue", "green"]\n# ลบแล้ววน',
          'colors = ["red", "blue", "green"]\ncolors.remove("red")\nfor c in colors:\n    print(c)'),
        p(10, "แก้กลางลิสต์", "fix_middle", "data = [10, 0, 30] เปลี่ยนค่ากลางเป็น 20", "1 บรรทัด", "[10, 20, 30]",
          "data = [10, 0, 30]\n# แก้", "data = [10, 0, 30]\ndata[1] = 20\nprint(data)"),
        p(11, "ต่อคิวงาน", "queue_append", 'todos = ["A"] append "B" และ "C" แล้วแสดง', "1 บรรทัด", "['A', 'B', 'C']",
          'todos = ["A"]\n# ต่อคิว', 'todos = ["A"]\ntodos.append("B")\ntodos.append("C")\nprint(todos)'),
        p(12, "จัดอันดับคะแนน", "rank_scores", "scores = [70, 95, 80] เรียงมากไปน้อยแล้วพิมพ์ทีละค่า",
          "3 บรรทัด", "95\n80\n70",
          "scores = [70, 95, 80]\n# จัดอันดับ",
          "scores = [70, 95, 80]\nscores.sort(reverse=True)\nfor s in scores:\n    print(s)", "sort ก่อนวน"),
        p(13, "ลบผลไม้", "remove_fruit", 'fruits = ["apple", "banana", "mango"] ลบ banana แล้วพิมพ์เหลือ',
          "2 บรรทัด", "apple\nmango",
          'fruits = ["apple", "banana", "mango"]\n# ลบ',
          'fruits = ["apple", "banana", "mango"]\nfruits.remove("banana")\nfor f in fruits:\n    print(f)'),
        p(5, "อัปเดตรายการ", "update_list", 'items = ["pen", "x", "bag"] แก้ "x" เป็น "book" แล้ว append "gum"',
          "1 บรรทัด", "['pen', 'book', 'bag', 'gum']",
          'items = ["pen", "x", "bag"]\n# อัปเดต',
          'items = ["pen", "x", "bag"]\nitems[1] = "book"\nitems.append("gum")\nprint(items)', "แก้ก่อนค่อยเพิ่ม"),
        p(14, "จัดคลัง", "warehouse", "stock = [5, 2, 9] append 1 แล้ว sort จากน้อยไปมาก",
          "1 บรรทัด", "[1, 2, 5, 9]",
          "stock = [5, 2, 9]\n# จัด", "stock = [5, 2, 9]\nstock.append(1)\nstock.sort()\nprint(stock)"),
        p(15, "คิวเสร็จสิ้น", "finish_queue", 'q = ["task1", "task2", "task3"] ลบ task1 แล้ว append task4',
          "1 บรรทัด", "['task2', 'task3', 'task4']",
          'q = ["task1", "task2", "task3"]\n# คิว',
          'q = ["task1", "task2", "task3"]\nq.remove("task1")\nq.append("task4")\nprint(q)'),
        p(16, "กระดานคะแนน", "scoreboard",
          "scores = [60, 90, 70] เปลี่ยนตัวแรกเป็น 80 แล้วเรียงมากไปน้อย แสดงลิสต์",
          "1 บรรทัด", "[90, 80, 70]",
          "scores = [60, 90, 70]\n# กระดาน",
          "scores = [60, 90, 70]\nscores[0] = 80\nscores.sort(reverse=True)\nprint(scores)",
          "assign แล้ว sort"),
    ]
    write_week("026-list-methods", chapter="List Methods", emoji="🛠️", index_md=idx, problems=probs)


def week_027():
    names = [
        ("กรองมากกว่า 10", "filter"), ("นับผ่านเกณฑ์", "count"), ("พิมพ์พร้อมเลขที่", "range(len)"),
        ("กรองคู่", "even filter"), ("นับสระคร่าวๆ", "count A"),
        ("กรองแล้วเก็บใหม่", "new list append"), ("นับไม่ผ่าน", "count fail"),
        ("to-do มีเลข", "index loop"), ("กรองชื่อสั้น", "len item"),
        ("นับและรวม", "สองตัวสะสม"), ("รายการมีลำดับ", "i+1"),
        ("กรองโบนัส", "filter>"), ("สรุปผ่าน/ตก", "count สองทาง"),
        ("เมนูมีเลข", "range len"), ("คลังกรอง", "ผสม"),
    ]
    idx = simple_index("บท 027 List Practice", "กรองเข้าลิสต์ใหม่ / นับ / for i in range(len())",
                       "ใช้ได้แค่เมธอดจาก 026", names)
    probs = [
        p(2, "กรองมากกว่า 10", "filter_gt10",
          "numbers = [3, 15, 7, 22, 8, 30] สร้างลิสต์ big ของค่า >10 แล้วแสดง big",
          "1 บรรทัด", "[15, 22, 30]",
          "numbers = [3, 15, 7, 22, 8, 30]\nbig = []\n# กรอง",
          "numbers = [3, 15, 7, 22, 8, 30]\nbig = []\nfor n in numbers:\n    if n > 10:\n        big.append(n)\nprint(big)"),
        p(3, "นับผ่านเกณฑ์", "count_pass",
          "scores = [85, 45, 92, 38, 77, 61] นับที่ >=50",
          "1 บรรทัด", "4",
          "scores = [85, 45, 92, 38, 77, 61]\npassed = 0\n# นับ",
          "scores = [85, 45, 92, 38, 77, 61]\npassed = 0\nfor score in scores:\n    if score >= 50:\n        passed = passed + 1\nprint(passed)"),
        p(4, "พิมพ์พร้อมเลขที่", "numbered_todo",
          'todos = ["Buy food", "Do homework", "Clean room"] พิมพ์เลขที่ ช่องว่าง จุด ช่องว่าง ชื่องาน',
          "3 บรรทัด", "1 . Buy food\n2 . Do homework\n3 . Clean room",
          'todos = ["Buy food", "Do homework", "Clean room"]\n# เลขที่',
          'todos = ["Buy food", "Do homework", "Clean room"]\nfor i in range(len(todos)):\n    print(i + 1, ".", todos[i])'),
        p(8, "กรองคู่", "filter_evens", "nums = [1, 2, 3, 4, 5, 6] สร้าง evens แล้วแสดง",
          "1 บรรทัด", "[2, 4, 6]",
          "nums = [1, 2, 3, 4, 5, 6]\nevens = []\n# กรอง",
          "nums = [1, 2, 3, 4, 5, 6]\nevens = []\nfor n in nums:\n    if n % 2 == 0:\n        evens.append(n)\nprint(evens)"),
        p(9, "นับสระคร่าวๆ", "count_a", 'words = ["A", "B", "A", "C"] นับ "A"',
          "1 บรรทัด", "2",
          'words = ["A", "B", "A", "C"]\ncount = 0\n# นับ',
          'words = ["A", "B", "A", "C"]\ncount = 0\nfor w in words:\n    if w == "A":\n        count = count + 1\nprint(count)'),
        p(6, "กรองแล้วเก็บใหม่", "filter_append", "temps = [28, 35, 19, 40] เก็บค่า >=30 ใน hot",
          "1 บรรทัด", "[35, 40]",
          "temps = [28, 35, 19, 40]\nhot = []\n# กรอง",
          "temps = [28, 35, 19, 40]\nhot = []\nfor t in temps:\n    if t >= 30:\n        hot.append(t)\nprint(hot)", "append เมื่อเข้าเกณฑ์"),
        p(7, "นับไม่ผ่าน", "count_fail", "scores = [40, 55, 30, 70] นับที่ <50",
          "1 บรรทัด", "2",
          "scores = [40, 55, 30, 70]\nfail = 0\n# นับ",
          "scores = [40, 55, 30, 70]\nfail = 0\nfor s in scores:\n    if s < 50:\n        fail = fail + 1\nprint(fail)"),
        p(10, "to-do มีเลข", "todo_nums", 'jobs = ["Wash", "Cook"] พิมพ์แบบ 1 . ...',
          "2 บรรทัด", "1 . Wash\n2 . Cook",
          'jobs = ["Wash", "Cook"]\n# เลข',
          'jobs = ["Wash", "Cook"]\nfor i in range(len(jobs)):\n    print(i + 1, ".", jobs[i])'),
        p(11, "กรองชื่อสั้น", "short_names", 'names = ["Ann", "Jonathan", "Bo"] เก็บชื่อที่ len <= 3',
          "1 บรรทัด", "['Ann', 'Bo']",
          'names = ["Ann", "Jonathan", "Bo"]\nshort = []\n# กรอง',
          'names = ["Ann", "Jonathan", "Bo"]\nshort = []\nfor name in names:\n    if len(name) <= 3:\n        short.append(name)\nprint(short)', "len ของสตริง"),
        p(12, "นับและรวม", "count_and_sum", "nums = [5, 10, 15] นับสมาชิกและรวมค่า แสดงสองบรรทัด",
          "2 บรรทัด", "Count: 3\nTotal: 30",
          "nums = [5, 10, 15]\ncount = 0\ntotal = 0\n# สรุป",
          'nums = [5, 10, 15]\ncount = 0\ntotal = 0\nfor n in nums:\n    count = count + 1\n    total = total + n\nprint(f"Count: {count}")\nprint(f"Total: {total}")'),
        p(13, "รายการมีลำดับ", "indexed_items", 'items = ["A", "B", "C"] พิมพ์ i:value โดย i เริ่ม 0',
          "3 บรรทัด", "0:A\n1:B\n2:C",
          'items = ["A", "B", "C"]\n# ลำดับ',
          'items = ["A", "B", "C"]\nfor i in range(len(items)):\n    print(f"{i}:{items[i]}")'),
        p(5, "กรองโบนัส", "bonus_filter", "points = [8, 12, 5, 20] เก็บค่า >=10 ใน bonus แล้วแสดง",
          "1 บรรทัด", "[12, 20]",
          "points = [8, 12, 5, 20]\nbonus = []\n# กรอง",
          "points = [8, 12, 5, 20]\nbonus = []\nfor p in points:\n    if p >= 10:\n        bonus.append(p)\nprint(bonus)", "ระวังชื่อตัวแปรวน"),
        p(14, "สรุปผ่าน/ตก", "pass_fail_count", "scores = [90, 40, 60] นับผ่าน (>=50) และตก แสดงสองบรรทัด",
          "2 บรรทัด", "Pass: 2\nFail: 1",
          "scores = [90, 40, 60]\npasse = 0\nfail = 0\n# นับ",
          'scores = [90, 40, 60]\npasse = 0\nfail = 0\nfor s in scores:\n    if s >= 50:\n        passe = passe + 1\n    else:\n        fail = fail + 1\nprint(f"Pass: {passe}")\nprint(f"Fail: {fail}")'),
        p(15, "เมนูมีเลข", "menu_numbers", 'menu = ["Tea", "Coffee", "Juice"] พิมพ์เลขที่แบบ 1 . ...',
          "3 บรรทัด", "1 . Tea\n2 . Coffee\n3 . Juice",
          'menu = ["Tea", "Coffee", "Juice"]\n# เมนู',
          'menu = ["Tea", "Coffee", "Juice"]\nfor i in range(len(menu)):\n    print(i + 1, ".", menu[i])'),
        p(16, "คลังกรอง", "stock_filter",
          "stock = [2, 0, 5, 0, 3] สร้าง available จากค่า >0 แล้วแสดงจำนวนและลิสต์",
          "2 บรรทัด", "Count: 3\n[2, 5, 3]",
          "stock = [2, 0, 5, 0, 3]\navailable = []\n# กรอง",
          'stock = [2, 0, 5, 0, 3]\navailable = []\nfor n in stock:\n    if n > 0:\n        available.append(n)\nprint(f"Count: {len(available)}")\nprint(available)'),
    ]
    write_week("027-list-practice", chapter="List Practice", emoji="🏋️", index_md=idx, problems=probs)


if __name__ == "__main__":
    week_025()
    week_026()
    week_027()
    print("025-027 done")
