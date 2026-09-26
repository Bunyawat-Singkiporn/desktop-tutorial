#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from _gen_lib import emit

def gen_025():
    probs = [
    dict(file="02_test.md", answer="02_first_last.py", diff="🟢 Easy",
         name="เมนูเครื่องดื่มตัวแรกและตัวสุดท้าย", axis="index 0 กับ -1",
         title="🧋 Lists — ข้อ 1: เมนูเครื่องดื่ม",
         scenario='ร้านกาแฟมีเมนูเครื่องดื่มเก็บใน list\n\n```python\ndrinks = ["latte", "mocha", "matcha", "espresso"]\n```\n\nแสดงชื่อเครื่องดื่มตัวแรกและตัวสุดท้าย คนละบรรทัด',
         conditions=None, inp="ไม่มี input (ใช้ list ที่ให้มา)", out="2 บรรทัด — ชื่อเครื่องดื่มตัวแรก และตัวสุดท้าย",
         hint="ใช้ `[0]` สำหรับตัวแรก และ `[-1]` สำหรับตัวสุดท้าย",
         starter='drinks = ["latte", "mocha", "matcha", "espresso"]\n\n# เขียนโค้ดตรงนี้',
         code='drinks = ["latte", "mocha", "matcha", "espresso"]\n\nprint(drinks[0])\nprint(drinks[-1])'),
    dict(file="03_test.md", answer="03_print_snacks.py", diff="🟢 Easy",
         name="พิมพ์รายการของว่างทั้งหมด", axis="for-in-list",
         title="🍿 Lists — ข้อ 2: รายการของว่าง",
         scenario='ตู้ขายของว่างในโรงหนังมีสินค้าดังนี้\n\n```python\nsnacks = ["popcorn", "nachos", "candy", "soda"]\n```\n\nพิมพ์ชื่อสินค้าทุกชิ้น คนละบรรทัด',
         conditions=None, inp="ไม่มี input", out="ชื่อสินค้าทุกชิ้น คนละบรรทัด",
         hint="ใช้ `for` วนทีละชิ้นใน list แล้ว `print`",
         starter='snacks = ["popcorn", "nachos", "candy", "soda"]\n\n# เขียนโค้ดตรงนี้',
         code='snacks = ["popcorn", "nachos", "candy", "soda"]\n\nfor snack in snacks:\n    print(snack)'),
    dict(file="04_test.md", answer="04_playlist_count.py", diff="🟢 Easy",
         name="นับจำนวนเพลงในเพลย์ลิสต์", axis="len()",
         title="🎵 Lists — ข้อ 3: นับเพลงในเพลย์ลิสต์",
         scenario='แอปเพลงมีเพลย์ลิสต์\n\n```python\nplaylist = ["Song A", "Song B", "Song C", "Song D", "Song E"]\n```\n\nแสดงจำนวนเพลงในรูปแบบ `Songs: <จำนวน>`',
         conditions=None, inp="ไม่มี input", out="1 บรรทัด แสดงจำนวนเพลง",
         hint="ใช้ `len()` กับ list แล้วพิมพ์ผล",
         starter='playlist = ["Song A", "Song B", "Song C", "Song D", "Song E"]\n\n# เขียนโค้ดตรงนี้',
         code='playlist = ["Song A", "Song B", "Song C", "Song D", "Song E"]\n\nprint(f"Songs: {len(playlist)}")'),
    dict(file="05_easy.md", answer="05_middle_seat.py", diff="🟢 Easy",
         name="ที่นั่งแถวกลาง", axis="index ตรงกลาง",
         title="🎫 Lists — ข้อ 4: ที่นั่งแถวกลาง",
         scenario='โรงหนังจองที่นั่งแถวหนึ่งไว้ 5 ที่\n\n```python\nseats = ["A1", "A2", "A3", "A4", "A5"]\n```\n\nแสดงรหัสที่นั่งตรงกลาง (index 2)',
         conditions=None, inp="ไม่มี input", out="รหัสที่นั่งตรงกลาง 1 บรรทัด",
         hint="list มี 5 ตัว ตรงกลางคือ index `2`",
         starter='seats = ["A1", "A2", "A3", "A4", "A5"]\n\n# เขียนโค้ดตรงนี้',
         code='seats = ["A1", "A2", "A3", "A4", "A5"]\n\nprint(seats[2])'),
    dict(file="06_easy.md", answer="06_last_two_days.py", diff="🟢 Easy",
         name="อุณหภูมิสองวันล่าสุด", axis="negative index สองค่า",
         title="🌡️ Lists — ข้อ 5: อุณหภูมิสองวันล่าสุด",
         scenario="แอปอากาศเก็บอุณหภูมิทั้งสัปดาห์\n\n```python\ntemps = [31, 32, 30, 33, 34, 29, 28]\n```\n\nแสดงอุณหภูมิของ **สองวันล่าสุด** คนละบรรทัด (ใช้ negative index)",
         conditions=None, inp="ไม่มี input", out="2 บรรทัด — วันรองสุดท้าย แล้ววันสุดท้าย",
         hint="วันสุดท้ายใช้ `[-1]` วันก่อนหน้านั้นใช้ `[-2]`",
         starter="temps = [31, 32, 30, 33, 34, 29, 28]\n\n# เขียนโค้ดตรงนี้",
         code="temps = [31, 32, 30, 33, 34, 29, 28]\n\nprint(temps[-2])\nprint(temps[-1])"),
    dict(file="07_medium.md", answer="07_cart_total.py", diff="🟡 Medium",
         name="รวมราคารถเข็น", axis="สะสมยอดด้วย +=",
         title="🛒 Lists — ข้อ 6: รวมราคารถเข็น",
         scenario="แอปช้อปออนไลน์เก็บราคาสินค้าในรถเข็น\n\n```python\nprices = [120, 45, 80, 200, 55]\n```\n\nรวมราคาสินค้าทั้งหมด แล้วแสดง `Total: <ยอด>`",
         conditions=None, inp="ไม่มี input", out="1 บรรทัด แสดงยอดรวม",
         hint="สร้างตัวแปรยอดเริ่มที่ 0 แล้ววน `for` บวกทีละราคาด้วย `+=`",
         starter="prices = [120, 45, 80, 200, 55]\n\n# เขียนโค้ดตรงนี้",
         code='prices = [120, 45, 80, 200, 55]\n\ntotal = 0\nfor price in prices:\n    total += price\n\nprint(f"Total: {total}")'),
    dict(file="08_medium.md", answer="08_quiz_average.py", diff="🟡 Medium",
         name="คะแนนเฉลี่ยควิซ", axis="total / len",
         title="📝 Lists — ข้อ 7: คะแนนเฉลี่ยควิซ",
         scenario="ครูเก็บคะแนนควิซของนักเรียนคนหนึ่ง\n\n```python\nquizzes = [8, 7, 9, 6, 10]\n```\n\nคำนวณค่าเฉลี่ย แล้วแสดง `Average: <ค่า>`",
         conditions=None, inp="ไม่มี input", out="1 บรรทัด แสดงค่าเฉลี่ย",
         hint="รวมคะแนนก่อน แล้วหารด้วย `len(quizzes)`",
         starter="quizzes = [8, 7, 9, 6, 10]\n\n# เขียนโค้ดตรงนี้",
         code='quizzes = [8, 7, 9, 6, 10]\n\ntotal = 0\nfor score in quizzes:\n    total += score\n\naverage = total / len(quizzes)\nprint(f"Average: {average}")'),
    dict(file="09_medium.md", answer="09_price_tags.py", diff="🟡 Medium",
         name="ติดป้ายราคาสินค้า", axis="for + ข้อความกำกับ",
         title="🏷️ Lists — ข้อ 8: ติดป้ายราคา",
         scenario="ร้านเครื่องเขียนติดป้ายราคาให้สินค้า\n\n```python\nprices = [25, 40, 15, 60]\n```\n\nพิมพ์ราคาแต่ละชิ้นในรูปแบบ `Price: <ราคา>` คนละบรรทัด",
         conditions=None, inp="ไม่มี input", out="ราคาทุกชิ้น คนละบรรทัด พร้อมป้าย",
         hint="วน `for` แล้วพิมพ์ข้อความเดียวกันนำหน้าทุกบรรทัด",
         starter="prices = [25, 40, 15, 60]\n\n# เขียนโค้ดตรงนี้",
         code='prices = [25, 40, 15, 60]\n\nfor price in prices:\n    print(f"Price: {price}")'),
    dict(file="10_medium.md", answer="10_sales_compare.py", diff="🟡 Medium",
         name="ยอดขายวันแรก vs วันสุดท้าย", axis="เทียบ index สองตัว + if",
         title="📈 Lists — ข้อ 9: ยอดขายวันแรกกับวันสุดท้าย",
         scenario="ร้านสะดวกซื้อเก็บยอดขายรายวันทั้งสัปดาห์\n\n```python\nsales = [4200, 3800, 5100, 4700, 3900, 6200, 5500]\n```\n\nเทียบยอดวันแรกกับวันสุดท้าย",
         conditions=["ถ้ายอดวันสุดท้ายมากกว่าหรือเท่ากับวันแรก → `Sales Up`", "ถ้าไม่ใช่ → `Sales Down`"],
         inp="ไม่มี input", out="ข้อความสถานะ 1 บรรทัด",
         hint="ดึง `sales[0]` กับ `sales[-1]` มาเก็บในตัวแปรก่อน แล้วค่อยเทียบ",
         starter="sales = [4200, 3800, 5100, 4700, 3900, 6200, 5500]\n\n# เขียนโค้ดตรงนี้",
         code='sales = [4200, 3800, 5100, 4700, 3900, 6200, 5500]\n\nfirst = sales[0]\nlast = sales[-1]\n\nif last >= first:\n    print("Sales Up")\nelse:\n    print("Sales Down")'),
    dict(file="11_medium.md", answer="11_first_three.py", diff="🟡 Medium",
         name="รวมราคาสามชิ้นแรก", axis="เข้าถึงหลาย index แล้วบวก",
         title="🛍️ Lists — ข้อ 10: รวมสามชิ้นแรก",
         scenario="ลูกค้าหยิบของใส่ตะกร้าแล้ว แต่โปรโมชันคิดแค่ **สามชิ้นแรก**\n\n```python\nprices = [99, 150, 45, 200, 80]\n```\n\nรวมราคา index 0, 1 และ 2 แล้วแสดง `Subtotal: <ยอด>`",
         conditions=None, inp="ไม่มี input", out="1 บรรทัด แสดงยอดสามชิ้นแรก",
         hint="บวก `prices[0] + prices[1] + prices[2]` โดยตรงได้เลย",
         starter="prices = [99, 150, 45, 200, 80]\n\n# เขียนโค้ดตรงนี้",
         code='prices = [99, 150, 45, 200, 80]\n\nsubtotal = prices[0] + prices[1] + prices[2]\nprint(f"Subtotal: {subtotal}")'),
    dict(file="12_medium.md", answer="12_hot_days.py", diff="🟡 Medium",
         name="นับวันร้อนเกินเกณฑ์", axis="ตัวนับ + if ใน for",
         title="☀️ Lists — ข้อ 11: นับวันร้อน",
         scenario="สถานีอากาศบันทึกอุณหภูมิรายวัน\n\n```python\ntemps = [34, 29, 36, 31, 38, 27, 35]\n```\n\nนับว่ามีกี่วันที่อุณหภูมิ **มากกว่าหรือเท่ากับ 35** แล้วแสดง `Hot days: <จำนวน>`",
         conditions=None, inp="ไม่มี input", out="1 บรรทัด แสดงจำนวนวันร้อน",
         hint="สร้างตัวนับเริ่มที่ 0 วนทุกค่า ถ้าเข้าเกณฑ์ให้บวก 1",
         starter="temps = [34, 29, 36, 31, 38, 27, 35]\n\n# เขียนโค้ดตรงนี้",
         code='temps = [34, 29, 36, 31, 38, 27, 35]\n\ncount = 0\nfor temp in temps:\n    if temp >= 35:\n        count += 1\n\nprint(f"Hot days: {count}")'),
    dict(file="13_challenge.md", answer="13_order_summary.py", diff="🔴 Challenge",
         name="สรุปออเดอร์ในกรอบ", axis="len + first/last + total",
         title="📦 Lists — ข้อ 12: สรุปออเดอร์",
         scenario="ร้านอาหารออนไลน์สรุปออเดอร์จากราคาสินค้า\n\n```python\nprices = [89, 120, 55, 200]\n```\n\nแสดงสรุปในกรอบ: จำนวนรายการ ราคาชิ้นแรก ราคาชิ้นสุดท้าย และยอดรวม",
         conditions=None, inp="ไม่มี input", out="กล่องสรุปออเดอร์",
         hint="หา `len` / index แรก-สุดท้าย / รวมยอด ให้ครบก่อน แล้วค่อยพิมพ์กรอบ",
         starter="prices = [89, 120, 55, 200]\n\n# เขียนโค้ดตรงนี้",
         code='''prices = [89, 120, 55, 200]

total = 0
for price in prices:
    total += price

print("========================")
print("      ORDER SUMMARY")
print("========================")
print(f"Items      : {len(prices)}")
print(f"First      : {prices[0]}")
print(f"Last       : {prices[-1]}")
print(f"Total      : {total}")
print("========================")'''),
    dict(file="14_challenge.md", answer="14_premium_items.py", diff="🔴 Challenge",
         name="แสดงเฉพาะสินค้าราคาแพง", axis="กรองด้วย print ใน loop",
         title="💎 Lists — ข้อ 13: สินค้าราคาพรีเมียม",
         scenario="แคตตาล็อกร้านแฟชัน\n\n```python\nprices = [450, 1200, 890, 1500, 300, 2000]\n```\n\nพิมพ์เฉพาะราคาที่ **มากกว่าหรือเท่ากับ 1000** คนละบรรทัด แล้วบรรทัดสุดท้ายแสดง `Count: <จำนวนที่พิมพ์>`",
         conditions=None, inp="ไม่มี input", out="ราคาที่เข้าเกณฑ์ทีละบรรทัด ตามด้วยจำนวน",
         hint="วนทุกราคา ถ้าเข้าเกณฑ์ให้พิมพ์ทันที และบวกตัวนับไปด้วย",
         starter="prices = [450, 1200, 890, 1500, 300, 2000]\n\n# เขียนโค้ดตรงนี้",
         code='''prices = [450, 1200, 890, 1500, 300, 2000]

count = 0
for price in prices:
    if price >= 1000:
        print(price)
        count += 1

print(f"Count: {count}")'''),
    dict(file="15_challenge.md", answer="15_top_score.py", diff="🔴 Challenge",
         name="หาคะแนนสูงสุดด้วย loop", axis="เทียบทีละตัวเก็บค่าสูงสุด",
         title="🏆 Lists — ข้อ 14: คะแนนสูงสุดในห้อง",
         scenario="ครูมีคะแนนสอบของนักเรียน\n\n```python\nscores = [72, 88, 65, 91, 77, 84]\n```\n\nหาคะแนนสูงสุดด้วยการวน loop เปรียบเทียบเอง (ห้ามใช้ `max()`) แล้วแสดง `Highest: <คะแนน>`",
         conditions=None, inp="ไม่มี input", out="1 บรรทัด แสดงคะแนนสูงสุด",
         hint="เริ่มจากสมมติว่าตัวแรกสูงสุด แล้ววนเทียบตัวถัดไปทีละตัว",
         starter="scores = [72, 88, 65, 91, 77, 84]\n\n# เขียนโค้ดตรงนี้",
         code='''scores = [72, 88, 65, 91, 77, 84]

highest = scores[0]
for score in scores:
    if score > highest:
        highest = score

print(f"Highest: {highest}")'''),
    dict(file="16_challenge.md", answer="16_team_result.py", diff="🔴 Challenge",
         name="ผลรวมทีมผ่านเกณฑ์ไหม", axis="total + average + if",
         title="⚽ Lists — ข้อ 15: ผลคะแนนทีม",
         scenario="โค้ชเก็บคะแนนฟอร์มผู้เล่น 5 คน\n\n```python\nratings = [78, 82, 69, 91, 85]\n```\n\nคำนวณค่าเฉลี่ย แล้วตัดสินผลทีม แสดงกรอบสรุปจำนวนคน ค่าเฉลี่ย และสถานะ",
         conditions=["ถ้าค่าเฉลี่ย >= 80 → สถานะ `Qualified`", "ถ้าไม่ใช่ → `Need Practice`"],
         inp="ไม่มี input", out="กล่องสรุปผลทีม",
         hint="รวมคะแนน → หารด้วยจำนวน → ค่อยตัดสินสถานะ แล้วพิมพ์กรอบทีเดียว",
         starter="ratings = [78, 82, 69, 91, 85]\n\n# เขียนโค้ดตรงนี้",
         code='''ratings = [78, 82, 69, 91, 85]

total = 0
for rating in ratings:
    total += rating

average = total / len(ratings)

if average >= 80:
    status = "Qualified"
else:
    status = "Need Practice"

print("========================")
print("       TEAM REPORT")
print("========================")
print(f"Players    : {len(ratings)}")
print(f"Average    : {average}")
print(f"Status     : {status}")
print("========================")'''),
    ]
    emit("025-lists", probs, "บท 025 Lists",
         ["list literal `[...]`", "indexing `list[0]` / `list[-1]`", "`len(list)`", "`for x in list:`", "accumulator ด้วย `+=`"],
         ["ยังไม่มี `.append` / `.remove` / `.sort` (บท 026)", "ยังไม่มี `range(len(...))` (บท 027)"],
         ["ข้อ `02` ไม่ซ้ำตัวอย่างในบทเรียน (บทเรียนใช้ fruits / names / รวมคะแนน scores)",
          "ห้ามใช้ `.append` เพื่อสร้าง list ใหม่ — กรองด้วยการ `print` หรือนับด้วยตัวนับแทน"])


def gen_026():
    probs = [
    dict(file="02_test.md", answer="02_add_task.py", diff="🟢 Easy",
         name="เพิ่มงานใน to-do", axis=".append()",
         title="✅ List Methods — ข้อ 1: เพิ่มงานใน to-do",
         scenario='แอปจดงานมีรายการเริ่มต้น\n\n```python\ntasks = ["wash dishes", "water plants"]\n```\n\nเพิ่มงาน `"do homework"` ต่อท้าย แล้วพิมพ์ list ทั้งก้อน',
         conditions=None, inp="ไม่มี input", out="list หลังเพิ่มงาน 1 บรรทัด",
         hint="ใช้ `.append()` แล้ว `print(tasks)`",
         starter='tasks = ["wash dishes", "water plants"]\n\n# เขียนโค้ดตรงนี้',
         code='tasks = ["wash dishes", "water plants"]\ntasks.append("do homework")\nprint(tasks)'),
    dict(file="03_test.md", answer="03_cancel_order.py", diff="🟢 Easy",
         name="ยกเลิกรายการสั่งอาหาร", axis=".remove()",
         title="🍜 List Methods — ข้อ 2: ยกเลิกเมนู",
         scenario='ลูกค้าสั่งอาหารแล้วอยากยกเลิกหนึ่งอย่าง\n\n```python\norder = ["pad thai", "som tum", "mango sticky rice", "thai tea"]\n```\n\nลบ `"som tum"` ออก แล้วพิมพ์ list ที่เหลือ',
         conditions=None, inp="ไม่มี input", out="list หลังลบ 1 บรรทัด",
         hint="ใช้ `.remove()` ด้วยชื่อเมนูที่ต้องการลบ",
         starter='order = ["pad thai", "som tum", "mango sticky rice", "thai tea"]\n\n# เขียนโค้ดตรงนี้',
         code='order = ["pad thai", "som tum", "mango sticky rice", "thai tea"]\norder.remove("som tum")\nprint(order)'),
    dict(file="04_test.md", answer="04_sort_ages.py", diff="🟢 Easy",
         name="เรียงอายุจากน้อยไปมาก", axis=".sort()",
         title="👶 List Methods — ข้อ 3: เรียงอายุ",
         scenario="ค่ายอาสาเก็บอายุผู้เข้าร่วม\n\n```python\nages = [17, 14, 19, 15, 18]\n```\n\nเรียงจากน้อยไปมาก แล้วพิมพ์ list",
         conditions=None, inp="ไม่มี input", out="list ที่เรียงแล้ว 1 บรรทัด",
         hint="เรียก `.sort()` แล้วพิมพ์ทั้ง list",
         starter="ages = [17, 14, 19, 15, 18]\n\n# เขียนโค้ดตรงนี้",
         code="ages = [17, 14, 19, 15, 18]\nages.sort()\nprint(ages)"),
    dict(file="05_easy.md", answer="05_fix_typo.py", diff="🟢 Easy",
         name="แก้ชื่อสินค้าที่พิมพ์ผิด", axis="index assignment",
         title="✏️ List Methods — ข้อ 4: แก้ชื่อสินค้า",
         scenario='รายการสินค้าพิมพ์ชื่อผิดตำแหน่งที่สอง\n\n```python\nitems = ["notebook", "pensil", "eraser", "ruler"]\n```\n\nแก้ `"pensil"` เป็น `"pencil"` แล้วพิมพ์ list',
         conditions=None, inp="ไม่มี input", out="list หลังแก้ 1 บรรทัด",
         hint="กำหนดค่าใหม่ที่ `items[1]`",
         starter='items = ["notebook", "pensil", "eraser", "ruler"]\n\n# เขียนโค้ดตรงนี้',
         code='items = ["notebook", "pensil", "eraser", "ruler"]\nitems[1] = "pencil"\nprint(items)'),
    dict(file="06_easy.md", answer="06_rank_desc.py", diff="🟢 Easy",
         name="เรียงคะแนนจากมากไปน้อย", axis="sort(reverse=True)",
         title="🥇 List Methods — ข้อ 5: อันดับคะแนน",
         scenario="เกมเก็บคะแนนผู้เล่น\n\n```python\nscores = [120, 85, 200, 150, 95]\n```\n\nเรียงจากมากไปน้อย แล้วพิมพ์ list",
         conditions=None, inp="ไม่มี input", out="list ที่เรียงจากมากไปน้อย",
         hint="ใช้ `.sort(reverse=True)`",
         starter="scores = [120, 85, 200, 150, 95]\n\n# เขียนโค้ดตรงนี้",
         code="scores = [120, 85, 200, 150, 95]\nscores.sort(reverse=True)\nprint(scores)"),
    dict(file="07_medium.md", answer="07_cart_edit.py", diff="🟡 Medium",
         name="แก้รถเข็นแล้วเพิ่มของ", axis="assignment + append",
         title="🛒 List Methods — ข้อ 6: แก้รถเข็น",
         scenario='ลูกค้ามีของในรถเข็น\n\n```python\ncart = ["milk", "bread", "eggs"]\n```\n\nเปลี่ยน `"bread"` เป็น `"toast"` แล้วเพิ่ม `"butter"` ต่อท้าย พิมพ์ list สุดท้าย',
         conditions=None, inp="ไม่มี input", out="list หลังแก้ไข 1 บรรทัด",
         hint="แก้ด้วย index ก่อน แล้วค่อย `.append()`",
         starter='cart = ["milk", "bread", "eggs"]\n\n# เขียนโค้ดตรงนี้',
         code='cart = ["milk", "bread", "eggs"]\ncart[1] = "toast"\ncart.append("butter")\nprint(cart)'),
    dict(file="08_medium.md", answer="08_waitlist.py", diff="🟡 Medium",
         name="คิวร้านตัดผม", axis="append + remove",
         title="💇 List Methods — ข้อ 7: คิวร้านตัดผม",
         scenario='คิวลูกค้าวันนี้\n\n```python\nqueue = [" ann", "Ben", "Cara"]\n```\n\nรอ — ใช้ข้อมูลจริง:\n\n```python\nqueue = ["Ann", "Ben", "Cara"]\n```\n\nเพิ่ม `"Dan"` ต่อท้าย แล้วลบ `"Ben"` ที่ยกเลิกคิว พิมพ์คิวที่เหลือ',
         conditions=None, inp="ไม่มี input", out="คิวหลังอัปเดต 1 บรรทัด",
         hint="`.append` ก่อน แล้ว `.remove` ตามชื่อ",
         starter='queue = ["Ann", "Ben", "Cara"]\n\n# เขียนโค้ดตรงนี้',
         code='queue = ["Ann", "Ben", "Cara"]\nqueue.append("Dan")\nqueue.remove("Ben")\nprint(queue)'),
    dict(file="09_medium.md", answer="09_price_board.py", diff="🟡 Medium",
         name="ป้ายราคาเรียงจากถูกไปแพง", axis="sort แล้ววนพิมพ์",
         title="🏷️ List Methods — ข้อ 8: ป้ายราคาเรียงลำดับ",
         scenario="ร้านพิมพ์ป้ายราคาจากถูกไปแพง\n\n```python\nprices = [89, 25, 120, 45, 60]\n```\n\nเรียงจากน้อยไปมาก แล้วพิมพ์แต่ละราคาในรูป `Price: <ค่า>` คนละบรรทัด",
         conditions=None, inp="ไม่มี input", out="ราคาทุกชิ้นหลังเรียง คนละบรรทัด",
         hint="`.sort()` ก่อน แล้วค่อย `for` พิมพ์",
         starter="prices = [89, 25, 120, 45, 60]\n\n# เขียนโค้ดตรงนี้",
         code='prices = [89, 25, 120, 45, 60]\nprices.sort()\nfor price in prices:\n    print(f"Price: {price}")'),
    dict(file="10_medium.md", answer="10_leaderboard.py", diff="🟡 Medium",
         name="บอร์ดคะแนน Top หลังอัปเดต", axis="append + sort reverse + index",
         title="🎮 List Methods — ข้อ 9: บอร์ดคะแนน",
         scenario="เกมมีคะแนนเดิม แล้วมีผู้เล่นใหม่\n\n```python\nscores = [880, 720, 950]\n```\n\nเพิ่มคะแนน `810` เรียงจากมากไปน้อย แล้วแสดงคะแนนอันดับ 1 ในรูป `Top: <คะแนน>`",
         conditions=None, inp="ไม่มี input", out="1 บรรทัด แสดงคะแนนสูงสุดหลังเรียง",
         hint="append → sort(reverse=True) → อ่าน `scores[0]`",
         starter="scores = [880, 720, 950]\n\n# เขียนโค้ดตรงนี้",
         code='scores = [880, 720, 950]\nscores.append(810)\nscores.sort(reverse=True)\nprint(f"Top: {scores[0]}")'),
    dict(file="11_medium.md", answer="11_playlist_fix.py", diff="🟡 Medium",
         name="แก้เพลย์ลิสต์และลบเพลง", axis="assignment + remove",
         title="🎶 List Methods — ข้อ 10: แก้เพลย์ลิสต์",
         scenario='เพลย์ลิสต์มีเพลง\n\n```python\nsongs = ["Intro", "Track 2", "Outro", "Bonus"]\n```\n\nเปลี่ยน `"Track 2"` เป็น `"Chorus"` แล้วลบ `"Bonus"` พิมพ์ list สุดท้าย',
         conditions=None, inp="ไม่มี input", out="เพลย์ลิสต์หลังแก้ 1 บรรทัด",
         hint="แก้ index ก่อน แล้ว `.remove`",
         starter='songs = ["Intro", "Track 2", "Outro", "Bonus"]\n\n# เขียนโค้ดตรงนี้',
         code='songs = ["Intro", "Track 2", "Outro", "Bonus"]\nsongs[1] = "Chorus"\nsongs.remove("Bonus")\nprint(songs)'),
    dict(file="12_medium.md", answer="12_class_scores.py", diff="🟡 Medium",
         name="อัปเดตคะแนนห้องแล้วเรียง", axis="append + remove + sort",
         title="📚 List Methods — ข้อ 11: อัปเดตคะแนนห้อง",
         scenario="คะแนนสอบกลางภาค\n\n```python\nscores = [65, 80, 55, 90, 70]\n```\n\nเพิ่มคะแนน `75` ลบคะแนน `55` แล้วเรียงจากน้อยไปมาก พิมพ์ list",
         conditions=None, inp="ไม่มี input", out="list คะแนนหลังอัปเดตและเรียง",
         hint="ทำสามขั้นตามลำดับ: append → remove → sort",
         starter="scores = [65, 80, 55, 90, 70]\n\n# เขียนโค้ดตรงนี้",
         code="scores = [65, 80, 55, 90, 70]\nscores.append(75)\nscores.remove(55)\nscores.sort()\nprint(scores)"),
    dict(file="13_challenge.md", answer="13_shopping_flow.py", diff="🔴 Challenge",
         name="ไหลงานตะกร้าช้อปปิ้ง", axis="หลาย method + สรุป",
         title="🛍️ List Methods — ข้อ 12: ไหลงานตะกร้า",
         scenario='ตะกร้าเริ่มต้น\n\n```python\ncart = ["apple", "bread", "milk", "cookie"]\n```\n\nทำตามลำดับ: เปลี่ยน `"bread"` เป็น `"bagel"` · เพิ่ม `"yogurt"` · ลบ `"cookie"` · เรียงชื่อ A→Z\nแล้วแสดงจำนวนชิ้นและ list สุดท้าย',
         conditions=None, inp="ไม่มี input", out="2 บรรทัด — จำนวนชิ้น และ list",
         hint="ทำทีละขั้นตามโจทย์ อย่าสลับลำดับ แล้วใช้ `len` ตอนท้าย",
         starter='cart = ["apple", "bread", "milk", "cookie"]\n\n# เขียนโค้ดตรงนี้',
         code='''cart = ["apple", "bread", "milk", "cookie"]
cart[1] = "bagel"
cart.append("yogurt")
cart.remove("cookie")
cart.sort()
print(f"Items: {len(cart)}")
print(cart)'''),
    dict(file="14_challenge.md", answer="14_race_results.py", diff="🔴 Challenge",
         name="ผลการแข่งขันวิ่ง", axis="append + sort reverse + แสดงอันดับ",
         title="🏃 List Methods — ข้อ 13: ผลการวิ่ง",
         scenario="เวลานักวิ่ง (วินาที ยิ่งน้อยยิ่งดี — แต่โจทย์นี้เรียงคะแนนความเร็วที่ให้มาจากมากไปน้อย)\n\n```python\npoints = [88, 92, 75, 90]\n```\n\nเพิ่ม `85` เรียงจากมากไปน้อย แล้วพิมพ์อันดับ 1–3 ในรูป `1. <คะแนน>` เป็นต้น",
         conditions=None, inp="ไม่มี input", out="3 บรรทัด อันดับ 1 ถึง 3",
         hint="หลังเรียงแล้ว ตัวที่ index 0, 1, 2 คือสามอันดับแรก",
         starter="points = [88, 92, 75, 90]\n\n# เขียนโค้ดตรงนี้",
         code='''points = [88, 92, 75, 90]
points.append(85)
points.sort(reverse=True)
print(f"1. {points[0]}")
print(f"2. {points[1]}")
print(f"3. {points[2]}")'''),
    dict(file="15_challenge.md", answer="15_inventory_desk.py", diff="🔴 Challenge",
         name="โต๊ะคลังสินค้า", axis="หลายการแก้ + กรอบสรุป",
         title="📦 List Methods — ข้อ 14: โต๊ะคลังสินค้า",
         scenario='คลังมีรหัสสินค้า\n\n```python\nskus = ["A12", "B07", "C03", "D19"]\n```\n\nเปลี่ยน `"B07"` เป็น `"B08"` เพิ่ม `"E21"` ลบ `"C03"` เรียง A→Z\nแสดงกรอบสรุปจำนวนและชิ้นแรก/ชิ้นสุดท้ายหลังเรียง',
         conditions=None, inp="ไม่มี input", out="กล่องสรุปคลัง",
         hint="ทำครบทุกขั้นก่อน แล้วค่อยอ่าน `len` / `[0]` / `[-1]`",
         starter='skus = ["A12", "B07", "C03", "D19"]\n\n# เขียนโค้ดตรงนี้',
         code='''skus = ["A12", "B07", "C03", "D19"]
skus[1] = "B08"
skus.append("E21")
skus.remove("C03")
skus.sort()

print("========================")
print("      WAREHOUSE")
print("========================")
print(f"Count      : {len(skus)}")
print(f"First      : {skus[0]}")
print(f"Last       : {skus[-1]}")
print("========================")'''),
    dict(file="16_challenge.md", answer="16_grade_cleanup.py", diff="🔴 Challenge",
         name="ทำความสะอาดคะแนนแล้วหาค่าเฉลี่ย", axis="remove + append + sort + average",
         title="📊 List Methods — ข้อ 15: ทำความสะอาดคะแนน",
         scenario="คะแนนดิบมีค่าผิดพลาด\n\n```python\nscores = [40, 78, 0, 85, 92, 66]\n```\n\nลบ `0` ออก (คะแนนว่าง) เพิ่มคะแนนชดเชย `70` เรียงจากน้อยไปมาก\nคำนวณค่าเฉลี่ยหลังทำความสะอาด แสดง list ที่เรียงแล้วและ `Average: <ค่า>`",
         conditions=None, inp="ไม่มี input", out="2 บรรทัด — list และค่าเฉลี่ย",
         hint="ลบและเพิ่มก่อนเรียง รวมคะแนนด้วย loop แล้วหาร `len`",
         starter="scores = [40, 78, 0, 85, 92, 66]\n\n# เขียนโค้ดตรงนี้",
         code='''scores = [40, 78, 0, 85, 92, 66]
scores.remove(0)
scores.append(70)
scores.sort()

total = 0
for score in scores:
    total += score

average = total / len(scores)
print(scores)
print(f"Average: {average}")'''),
    ]
    # fix waitlist scenario typo - clean it
    probs[7]["scenario"] = 'คิวลูกค้าวันนี้\n\n```python\nqueue = ["Ann", "Ben", "Cara"]\n```\n\nเพิ่ม `"Dan"` ต่อท้าย แล้วลบ `"Ben"` ที่ยกเลิกคิว พิมพ์คิวที่เหลือ'
    emit("026-list-methods", probs, "บท 026 List Methods",
         ["index assignment `list[i] = ...`", "`.append()`", "`.remove()`", "`.sort()` / `.sort(reverse=True)`", "พิมพ์ list ทั้งก้อน"],
         ["ห้าม `.insert` / `.pop` / `.extend` / `.index` / `.count` / `sorted()`"],
         ["ข้อ `02` ไม่ซ้ำตัวอย่างในบทเรียน (บทเรียนใช้ fruits / numbers.sort / scores append-remove-sort)",
          "ใช้ได้เฉพาะ 4 อย่าง: append, remove, sort, การกำหนดค่าด้วย index"])


def gen_027():
    probs = [
    dict(file="02_test.md", answer="02_filter_heavy.py", diff="🟢 Easy",
         name="กรองพัสดุหนัก", axis="filter เข้า list ใหม่",
         title="📦 List Practice — ข้อ 1: กรองพัสดุหนัก",
         scenario="คลังคัดพัสดุที่หนักเกินเกณฑ์\n\n```python\nweights = [2, 15, 8, 22, 5, 30]\n```\n\nสร้าง list ใหม่เก็บเฉพาะน้ำหนักที่ **มากกว่า 10** แล้วพิมพ์ list นั้น",
         conditions=None, inp="ไม่มี input", out="list ของน้ำหนักที่ผ่านเกณฑ์",
         hint="สร้าง list ว่าง แล้ว `.append` เฉพาะค่าที่เข้าเงื่อนไข",
         starter="weights = [2, 15, 8, 22, 5, 30]\n\n# เขียนโค้ดตรงนี้",
         code='''weights = [2, 15, 8, 22, 5, 30]
heavy = []
for w in weights:
    if w > 10:
        heavy.append(w)
print(heavy)'''),
    dict(file="03_test.md", answer="03_count_pass.py", diff="🟢 Easy",
         name="นับคนสอบผ่าน", axis="ตัวนับ + เงื่อนไข",
         title="✅ List Practice — ข้อ 2: นับคนสอบผ่าน",
         scenario="คะแนนสอบ\n\n```python\nscores = [45, 72, 88, 39, 60, 55]\n```\n\nนับคนที่ได้ **มากกว่าหรือเท่ากับ 50** แสดง `Passed: <จำนวน>`",
         conditions=None, inp="ไม่มี input", out="1 บรรทัด จำนวนผู้ผ่าน",
         hint="ตัวนับเริ่ม 0 ถ้าคะแนนเข้าเกณฑ์ให้ `+= 1`",
         starter="scores = [45, 72, 88, 39, 60, 55]\n\n# เขียนโค้ดตรงนี้",
         code='''scores = [45, 72, 88, 39, 60, 55]
passed = 0
for score in scores:
    if score >= 50:
        passed += 1
print(f"Passed: {passed}")'''),
    dict(file="04_test.md", answer="04_numbered_menu.py", diff="🟢 Easy",
         name="เมนูมีหมายเลข", axis="range(len())",
         title="🍽️ List Practice — ข้อ 3: เมนูมีหมายเลข",
         scenario='เมนูร้านข้าวแกง\n\n```python\nmenu = ["krapow", "omlette", "tom yum", "fried rice"]\n```\n\nพิมพ์เป็น `1. krapow` แบบมีหมายเลขเริ่มที่ 1',
         conditions=None, inp="ไม่มี input", out="เมนูทีละบรรทัดพร้อมหมายเลข",
         hint="ใช้ `for i in range(len(menu)):` แล้วพิมพ์ `i + 1` กับ `menu[i]`",
         starter='menu = ["krapow", "omlette", "tom yum", "fried rice"]\n\n# เขียนโค้ดตรงนี้',
         code='''menu = ["krapow", "omlette", "tom yum", "fried rice"]
for i in range(len(menu)):
    print(f"{i + 1}. {menu[i]}")'''),
    dict(file="05_easy.md", answer="05_filter_short.py", diff="🟢 Easy",
         name="กรองชื่องานสั้น", axis="filter ตาม len ของข้อความ",
         title="✂️ List Practice — ข้อ 4: ชื่องานสั้น",
         scenario='รายชื่องาน\n\n```python\ntasks = ["pay", "homework", "run", "presentation", "buy"]\n```\n\nเก็บเฉพาะชื่องานที่ความยาว **น้อยกว่าหรือเท่ากับ 4 ตัวอักษร** แล้วพิมพ์ list',
         conditions=None, inp="ไม่มี input", out="list ของชื่องานสั้น",
         hint="ใช้ `len(task)` ในเงื่อนไขตอนกรอง",
         starter='tasks = ["pay", "homework", "run", "presentation", "buy"]\n\n# เขียนโค้ดตรงนี้',
         code='''tasks = ["pay", "homework", "run", "presentation", "buy"]
short = []
for task in tasks:
    if len(task) <= 4:
        short.append(task)
print(short)'''),
    dict(file="06_easy.md", answer="06_count_even.py", diff="🟢 Easy",
         name="นับเลขคู่ในบิล", axis="นับด้วย % 2",
         title="🔢 List Practice — ข้อ 5: นับเลขคู่",
         scenario="เลขที่โต๊ะในร้าน\n\n```python\ntables = [1, 2, 3, 4, 5, 6, 8]\n```\n\nนับโต๊ะเลขคู่ แสดง `Even tables: <จำนวน>`",
         conditions=None, inp="ไม่มี input", out="1 บรรทัด จำนวนโต๊ะเลขคู่",
         hint="ใช้ `table % 2 == 0` เพื่อเช็คเลขคู่",
         starter="tables = [1, 2, 3, 4, 5, 6, 8]\n\n# เขียนโค้ดตรงนี้",
         code='''tables = [1, 2, 3, 4, 5, 6, 8]
count = 0
for table in tables:
    if table % 2 == 0:
        count += 1
print(f"Even tables: {count}")'''),
    dict(file="07_medium.md", answer="07_filter_and_count.py", diff="🟡 Medium",
         name="กรองราคาแล้ววนนับ", axis="filter + len ของผลลัพธ์",
         title="💸 List Practice — ข้อ 6: กรองราคาส่งฟรี",
         scenario="ยอดสั่งซื้อ\n\n```python\norders = [180, 320, 90, 450, 250, 500]\n```\n\nเก็บออเดอร์ที่ **มากกว่าหรือเท่ากับ 300** (ส่งฟรี) แล้วแสดง list และ `Free shipping: <จำนวน>`",
         conditions=None, inp="ไม่มี input", out="2 บรรทัด — list และจำนวน",
         hint="กรองเข้า list ใหม่ แล้วใช้ `len` ของ list นั้น",
         starter="orders = [180, 320, 90, 450, 250, 500]\n\n# เขียนโค้ดตรงนี้",
         code='''orders = [180, 320, 90, 450, 250, 500]
free = []
for order in orders:
    if order >= 300:
        free.append(order)
print(free)
print(f"Free shipping: {len(free)}")'''),
    dict(file="08_medium.md", answer="08_index_labels.py", diff="🟡 Medium",
         name="ป้ายชั้นวางสินค้า", axis="range(len) + ข้อความ",
         title="🏪 List Practice — ข้อ 7: ป้ายชั้นวาง",
         scenario='สินค้าบนชั้น\n\n```python\nitems = ["rice", "oil", "sugar", "salt"]\n```\n\nพิมพ์ `Shelf 0: rice` โดยใช้ index จริงจาก `range(len(...))`',
         conditions=None, inp="ไม่มี input", out="ป้ายชั้นทีละบรรทัด",
         hint="`for i in range(len(items)):` แล้วใช้ทั้ง `i` และ `items[i]`",
         starter='items = ["rice", "oil", "sugar", "salt"]\n\n# เขียนโค้ดตรงนี้',
         code='''items = ["rice", "oil", "sugar", "salt"]
for i in range(len(items)):
    print(f"Shelf {i}: {items[i]}")'''),
    dict(file="09_medium.md", answer="09_double_pass.py", diff="🟡 Medium",
         name="นับผ่านและตก", axis="ตัวนับสองตัว",
         title="📊 List Practice — ข้อ 8: นับผ่านและตก",
         scenario="คะแนนวิชา\n\n```python\nscores = [40, 55, 70, 48, 90, 61]\n```\n\nนับคนที่ได้ >= 50 เป็นผ่าน และที่เหลือเป็นตก แสดงสองบรรทัด `Pass:` / `Fail:`",
         conditions=None, inp="ไม่มี input", out="2 บรรทัด จำนวนผ่านและตก",
         hint="ใช้ตัวนับสองตัวใน loop เดียวกัน",
         starter="scores = [40, 55, 70, 48, 90, 61]\n\n# เขียนโค้ดตรงนี้",
         code='''scores = [40, 55, 70, 48, 90, 61]
passed = 0
failed = 0
for score in scores:
    if score >= 50:
        passed += 1
    else:
        failed += 1
print(f"Pass: {passed}")
print(f"Fail: {failed}")'''),
    dict(file="10_medium.md", answer="10_copy_positive.py", diff="🟡 Medium",
         name="คัดยอดเงินบวก", axis="filter ค่าบวก",
         title="💰 List Practice — ข้อ 9: คัดยอดเงินบวก",
         scenario="รายการเงินเข้า-ออก\n\n```python\nmoves = [200, -50, 120, -30, 80, -10]\n```\n\nเก็บเฉพาะยอดที่เป็นบวก แล้วพิมพ์ list และผลรวมของยอดบวก",
         conditions=None, inp="ไม่มี input", out="2 บรรทัด — list ยอดบวก และ Total",
         hint="กรอง `n > 0` แล้ววนรวมอีกรอบ หรือรวมไปพร้อมกรอง",
         starter="moves = [200, -50, 120, -30, 80, -10]\n\n# เขียนโค้ดตรงนี้",
         code='''moves = [200, -50, 120, -30, 80, -10]
income = []
for n in moves:
    if n > 0:
        income.append(n)

total = 0
for n in income:
    total += n

print(income)
print(f"Total: {total}")'''),
    dict(file="11_medium.md", answer="11_todo_done.py", diff="🟡 Medium",
         name="ติ๊กงานด้วยหมายเลข", axis="range(len) + แก้ค่า",
         title="☑️ List Practice — ข้อ 10: ติ๊กงานเสร็จ",
         scenario='รายการงาน\n\n```python\ntodos = ["email", "laundry", "study", "cook"]\n```\n\nเปลี่ยนงาน index 1 เป็น `"DONE"` แล้วพิมพ์ทั้ง list แบบมีหมายเลข `1. ...`',
         conditions=None, inp="ไม่มี input", out="รายการงานหลังติ๊ก พร้อมหมายเลข",
         hint="แก้ `todos[1]` ก่อน แล้วค่อยวน `range(len(...))` พิมพ์",
         starter='todos = ["email", "laundry", "study", "cook"]\n\n# เขียนโค้ดตรงนี้',
         code='''todos = ["email", "laundry", "study", "cook"]
todos[1] = "DONE"
for i in range(len(todos)):
    print(f"{i + 1}. {todos[i]}")'''),
    dict(file="12_medium.md", answer="12_above_avg_count.py", diff="🟡 Medium",
         name="นับคนที่สูงกว่าค่าเฉลี่ย", axis="average แล้ววนนับ",
         title="📈 List Practice — ข้อ 11: สูงกว่าค่าเฉลี่ย",
         scenario="คะแนนห้อง\n\n```python\nscores = [70, 80, 60, 90, 75]\n```\n\nหาค่าเฉลี่ยก่อน แล้วนับว่ามีกี่คนที่ได้ **มากกว่า** ค่าเฉลี่ย แสดง `Above average: <จำนวน>`",
         conditions=None, inp="ไม่มี input", out="1 บรรทัด จำนวนคนที่สูงกว่าค่าเฉลี่ย",
         hint="วนรวมหา average ให้จบก่อน แล้วค่อยวนนับรอบสอง",
         starter="scores = [70, 80, 60, 90, 75]\n\n# เขียนโค้ดตรงนี้",
         code='''scores = [70, 80, 60, 90, 75]
total = 0
for score in scores:
    total += score
average = total / len(scores)

count = 0
for score in scores:
    if score > average:
        count += 1

print(f"Above average: {count}")'''),
    dict(file="13_challenge.md", answer="13_receipt_filter.py", diff="🔴 Challenge",
         name="ใบเสร็จเฉพาะรายการแพง", axis="filter + หมายเลข + รวม",
         title="🧾 List Practice — ข้อ 12: ใบเสร็จรายการแพง",
         scenario="ราคาสินค้าในบิล\n\n```python\nprices = [40, 120, 75, 200, 30, 150]\n```\n\nคัดเฉพาะราคา >= 100 แสดงเป็นรายการมีหมายเลข แล้วสรุปจำนวนและยอดรวมในกรอบ",
         conditions=None, inp="ไม่มี input", out="รายการมีหมายเลข ตามด้วยกล่องสรุป",
         hint="กรองก่อน แล้วค่อยวนพิมพ์หมายเลขและรวมยอด",
         starter="prices = [40, 120, 75, 200, 30, 150]\n\n# เขียนโค้ดตรงนี้",
         code='''prices = [40, 120, 75, 200, 30, 150]
pricey = []
for price in prices:
    if price >= 100:
        pricey.append(price)

for i in range(len(pricey)):
    print(f"{i + 1}. {pricey[i]}")

total = 0
for price in pricey:
    total += price

print("========================")
print(f"Count      : {len(pricey)}")
print(f"Total      : {total}")
print("========================")'''),
    dict(file="14_challenge.md", answer="14_seat_map.py", diff="🔴 Challenge",
         name="แผนผังที่นั่งว่าง/จอง", axis="range(len) + สองสถานะ",
         title="🎟️ List Practice — ข้อ 13: แผนผังที่นั่ง",
         scenario='สถานะที่นั่ง (`"free"` / `"taken"`)\n\n```python\nseats = ["free", "taken", "free", "free", "taken"]\n```\n\nพิมพ์ `Seat 1: free` แบบหมายเลขเริ่ม 1 แล้วนับที่ว่างแสดง `Free: <จำนวน>`',
         conditions=None, inp="ไม่มี input", out="แผนผังทีละบรรทัด ตามด้วยจำนวนที่ว่าง",
         hint="ใช้ `range(len(seats))` ทั้งพิมพ์และนับใน loop เดียวกันได้",
         starter='seats = ["free", "taken", "free", "free", "taken"]\n\n# เขียนโค้ดตรงนี้',
         code='''seats = ["free", "taken", "free", "free", "taken"]
free = 0
for i in range(len(seats)):
    print(f"Seat {i + 1}: {seats[i]}")
    if seats[i] == "free":
        free += 1
print(f"Free: {free}")'''),
    dict(file="15_challenge.md", answer="15_temp_report.py", diff="🔴 Challenge",
         name="รายงานอุณหภูมิกรอง+นับ", axis="filter + count + average ของชุดกรอง",
         title="🌡️ List Practice — ข้อ 14: รายงานอุณหภูมิ",
         scenario="อุณหภูมิรายชั่วโมง\n\n```python\ntemps = [28, 33, 36, 30, 37, 29, 34]\n```\n\nเก็บเฉพาะวัน/ชั่วโมงที่ >= 33 แสดง list นั้น จำนวน และค่าเฉลี่ยของชุดที่กรองแล้ว",
         conditions=None, inp="ไม่มี input", out="3 บรรทัด — list / Count / Average",
         hint="กรองก่อน แล้วค่อยหา len กับค่าเฉลี่ยจาก list ใหม่",
         starter="temps = [28, 33, 36, 30, 37, 29, 34]\n\n# เขียนโค้ดตรงนี้",
         code='''temps = [28, 33, 36, 30, 37, 29, 34]
hot = []
for temp in temps:
    if temp >= 33:
        hot.append(temp)

total = 0
for temp in hot:
    total += temp

average = total / len(hot)
print(hot)
print(f"Count: {len(hot)}")
print(f"Average: {average}")'''),
    dict(file="16_challenge.md", answer="16_task_manager.py", diff="🔴 Challenge",
         name="ตัวจัดการงานแบบย่อ", axis="append + remove + range(len) + count",
         title="📋 List Practice — ข้อ 15: ตัวจัดการงาน",
         scenario='เริ่มจาก\n\n```python\ntasks = ["math", "dishes", "essay"]\n```\n\nเพิ่ม `"laundry"` ลบ `"dishes"` แล้วพิมพ์รายการมีหมายเลข\nจากนั้นนับงานที่ความยาวชื่อ > 4 แสดง `Long tasks: <จำนวน>`',
         conditions=None, inp="ไม่มี input", out="รายการมีหมายเลข ตามด้วยจำนวนงานชื่อยาว",
         hint="อัปเดต list ให้เสร็จก่อน แล้วค่อยพิมพ์และนับ",
         starter='tasks = ["math", "dishes", "essay"]\n\n# เขียนโค้ดตรงนี้',
         code='''tasks = ["math", "dishes", "essay"]
tasks.append("laundry")
tasks.remove("dishes")

for i in range(len(tasks)):
    print(f"{i + 1}. {tasks[i]}")

long_tasks = 0
for task in tasks:
    if len(task) > 4:
        long_tasks += 1

print(f"Long tasks: {long_tasks}")'''),
    ]
    emit("027-list-practice", probs, "บท 027 List Practice",
         ["filter เข้า list ใหม่ด้วย `.append`", "นับด้วยตัวนับ", "`for i in range(len(...)):`", "ทักษะ list จากบท 025–026"],
         ["ห้าม `enumerate()`", "ห้าม list comprehension"],
         ["ข้อ `02` ไม่ซ้ำตัวอย่างในบทเรียนตรงๆ (บทเรียนใช้ numbers>10 / scores>=50 / todos หมายเลข)",
          "เน้นสองแพทเทิร์น: กรองเก็บ list ใหม่ และนับด้วยตัวนับ"])


def gen_028():
    probs = [
    dict(file="02_test.md", answer="02_first_last_len.py", diff="🟢 Easy",
         name="สรุปชั้นหนังสือ", axis="index + len ทบทวน",
         title="📚 Review Lists — ข้อ 1: สรุปชั้นหนังสือ",
         scenario='ชั้นหนังสือ\n\n```python\nbooks = ["Python 101", "Thai History", "Cooking", "Space"]\n```\n\nแสดงชื่อเล่มแรก เล่มสุดท้าย และจำนวนเล่ม',
         conditions=None, inp="ไม่มี input", out="3 บรรทัด First / Last / Count",
         hint="ใช้ `[0]` `[-1]` และ `len`",
         starter='books = ["Python 101", "Thai History", "Cooking", "Space"]\n\n# เขียนโค้ดตรงนี้',
         code='''books = ["Python 101", "Thai History", "Cooking", "Space"]
print(f"First: {books[0]}")
print(f"Last: {books[-1]}")
print(f"Count: {len(books)}")'''),
    dict(file="03_test.md", answer="03_skip_middle.py", diff="🟢 Easy",
         name="ข้ามรายการกลางตอนพิมพ์", axis="for + if ข้ามค่า",
         title="⏭️ Review Lists — ข้อ 2: ข้ามรายการกลาง",
         scenario='รายการสถานีรถไฟฟ้า\n\n```python\nstops = ["Mo Chit", "Siam", "Asok", "On Nut"]\n```\n\nพิมพ์ทุกสถานี **ยกเว้น** `"Siam"`',
         conditions=None, inp="ไม่มี input", out="ชื่อสถานีที่เหลือ คนละบรรทัด",
         hint="วนปกติ แล้วใช้ `if` เพื่อข้ามค่าที่ไม่ต้องการพิมพ์",
         starter='stops = ["Mo Chit", "Siam", "Asok", "On Nut"]\n\n# เขียนโค้ดตรงนี้',
         code='''stops = ["Mo Chit", "Siam", "Asok", "On Nut"]
for stop in stops:
    if stop == "Siam":
        continue
    print(stop)'''),
    dict(file="04_test.md", answer="04_word_lengths.py", diff="🟢 Easy",
         name="ความยาวชื่อเมนู", axis="for + len ของสมาชิก",
         title="🔤 Review Lists — ข้อ 3: ความยาวชื่อเมนู",
         scenario='เมนูเครื่องดื่ม\n\n```python\ndrinks = ["tea", "coffee", "juice"]\n```\n\nพิมพ์ความยาวของแต่ละชื่อ คนละบรรทัด',
         conditions=None, inp="ไม่มี input", out="ความยาวทีละบรรทัด",
         hint="`print(len(drink))` ใน loop",
         starter='drinks = ["tea", "coffee", "juice"]\n\n# เขียนโค้ดตรงนี้',
         code='''drinks = ["tea", "coffee", "juice"]
for drink in drinks:
    print(len(drink))'''),
    dict(file="05_easy.md", answer="05_merge_sort_names.py", diff="🟢 Easy",
         name="รวมสองคิวแล้วเรียง", axis="append ทีละชื่อ + sort",
         title="🔀 Review Lists — ข้อ 4: รวมคิวแล้วเรียง",
         scenario='คิว A และรายชื่อที่จะเข้ามาต่อ\n\n```python\nqueue = ["Bee", "Ann"]\nextra = ["Dan", "Cara"]\n```\n\nนำชื่อใน `extra` ไปต่อท้าย `queue` ทีละชื่อ แล้วเรียง A→Z พิมพ์ผล',
         conditions=None, inp="ไม่มี input", out="คิวรวมที่เรียงแล้ว",
         hint="วน `extra` แล้ว `.append` เข้า `queue` จากนั้น `.sort()`",
         starter='queue = ["Bee", "Ann"]\nextra = ["Dan", "Cara"]\n\n# เขียนโค้ดตรงนี้',
         code='''queue = ["Bee", "Ann"]
extra = ["Dan", "Cara"]
for name in extra:
    queue.append(name)
queue.sort()
print(queue)'''),
    dict(file="06_easy.md", answer="06_index_print.py", diff="🟢 Easy",
         name="พิมพ์คู่ index:ค่า", axis="range(len) ทบทวน",
         title="📍 Review Lists — ข้อ 5: พิมพ์ index กับค่า",
         scenario='รหัสที่นั่ง\n\n```python\ncodes = ["A", "B", "C", "D"]\n```\n\nพิมพ์ `0 : A` รูปแบบ `index : ค่า`',
         conditions=None, inp="ไม่มี input", out="คู่ index กับค่า คนละบรรทัด",
         hint="ใช้ `range(len(codes))`",
         starter='codes = ["A", "B", "C", "D"]\n\n# เขียนโค้ดตรงนี้',
         code='''codes = ["A", "B", "C", "D"]
for i in range(len(codes)):
    print(f"{i} : {codes[i]}")'''),
    dict(file="07_medium.md", answer="07_avg_report.py", diff="🟡 Medium",
         name="รายงานค่าเฉลี่ยคะแนน", axis="total / len + กรอบ",
         title="📝 Review Lists — ข้อ 6: รายงานค่าเฉลี่ย",
         scenario="คะแนน\n\n```python\nscores = [80, 75, 90, 65, 88]\n```\n\nแสดงจำนวนคน ยอดรวม และค่าเฉลี่ยในกรอบ",
         conditions=None, inp="ไม่มี input", out="กล่องสรุปคะแนน",
         hint="สะสม total แล้วหารด้วย len",
         starter="scores = [80, 75, 90, 65, 88]\n\n# เขียนโค้ดตรงนี้",
         code='''scores = [80, 75, 90, 65, 88]
total = 0
for score in scores:
    total += score
average = total / len(scores)

print("========================")
print("      SCORE REPORT")
print("========================")
print(f"Count      : {len(scores)}")
print(f"Total       : {total}")
print(f"Average     : {average}")
print("========================")'''),
    dict(file="08_medium.md", answer="08_replace_and_filter.py", diff="🟡 Medium",
         name="แก้ค่าแล้วกรอง", axis="assignment + filter",
         title="🔧 Review Lists — ข้อ 7: แก้ค่าแล้วกรอง",
         scenario="ยอดขายรายวัน\n\n```python\nsales = [100, -1, 250, 180, 90]\n```\n\nแก้ค่า `-1` ที่ index 1 เป็น `120` แล้วเก็บเฉพาะยอด >= 150 พิมพ์ list ผลลัพธ์",
         conditions=None, inp="ไม่มี input", out="list ยอดที่ผ่านเกณฑ์หลังแก้",
         hint="แก้ก่อน แล้วค่อยวนกรองเข้า list ใหม่",
         starter="sales = [100, -1, 250, 180, 90]\n\n# เขียนโค้ดตรงนี้",
         code='''sales = [100, -1, 250, 180, 90]
sales[1] = 120
big = []
for n in sales:
    if n >= 150:
        big.append(n)
print(big)'''),
    dict(file="09_medium.md", answer="09_remove_sort_print.py", diff="🟡 Medium",
         name="ลบแล้วเรียงแล้วพิมพ์หมายเลข", axis="remove + sort + range(len)",
         title="🧹 Review Lists — ข้อ 8: ลบแล้วเรียง",
         scenario='รายการงาน\n\n```python\ntasks = ["clean", "code", "call", "cook"]\n```\n\nลบ `"call"` เรียง A→Z แล้วพิมพ์แบบมีหมายเลข',
         conditions=None, inp="ไม่มี input", out="รายการมีหมายเลขหลังลบและเรียง",
         hint="remove → sort → range(len)",
         starter='tasks = ["clean", "code", "call", "cook"]\n\n# เขียนโค้ดตรงนี้',
         code='''tasks = ["clean", "code", "call", "cook"]
tasks.remove("call")
tasks.sort()
for i in range(len(tasks)):
    print(f"{i + 1}. {tasks[i]}")'''),
    dict(file="10_medium.md", answer="10_two_lists_sum.py", diff="🟡 Medium",
         name="รวมยอดสองแผนก", axis="สอง list + สอง total",
         title="🏢 Review Lists — ข้อ 9: รวมยอดสองแผนก",
         scenario="ยอดขายสองแผนก\n\n```python\nfood = [120, 80, 60]\ndrink = [40, 55, 35]\n```\n\nรวมยอดแต่ละแผนก แล้วแสดงยอดรวมทั้งร้าน",
         conditions=None, inp="ไม่มี input", out="3 บรรทัด Food / Drink / Grand",
         hint="วนรวมแยกกันสองรอบ แล้วบวกสองยอดตอนท้าย",
         starter="food = [120, 80, 60]\ndrink = [40, 55, 35]\n\n# เขียนโค้ดตรงนี้",
         code='''food = [120, 80, 60]
drink = [40, 55, 35]

food_total = 0
for n in food:
    food_total += n

drink_total = 0
for n in drink:
    drink_total += n

print(f"Food: {food_total}")
print(f"Drink: {drink_total}")
print(f"Grand: {food_total + drink_total}")'''),
    dict(file="11_medium.md", answer="11_pass_list.py", diff="🟡 Medium",
         name="สร้างรายชื่อผู้ผ่าน", axis="filter ชื่อคู่กับคะแนน",
         title="🎓 Review Lists — ข้อ 10: รายชื่อผู้ผ่าน",
         scenario='ชื่อและคะแนนตำแหน่งเดียวกัน\n\n```python\nnames = ["Ann", "Ben", "Cara", "Dan"]\nscores = [45, 72, 88, 50]\n```\n\nใช้ `range(len(names))` เก็บชื่อที่ได้คะแนน >= 50 แล้วพิมพ์ list ชื่อผู้ผ่าน',
         conditions=None, inp="ไม่มี input", out="list ชื่อผู้ผ่าน",
         hint="ดู `scores[i]` เพื่อตัดสินว่าจะ append `names[i]` หรือไม่",
         starter='names = ["Ann", "Ben", "Cara", "Dan"]\nscores = [45, 72, 88, 50]\n\n# เขียนโค้ดตรงนี้',
         code='''names = ["Ann", "Ben", "Cara", "Dan"]
scores = [45, 72, 88, 50]
passed = []
for i in range(len(names)):
    if scores[i] >= 50:
        passed.append(names[i])
print(passed)'''),
    dict(file="12_medium.md", answer="12_min_by_loop.py", diff="🟡 Medium",
         name="หาราคาถูกสุดด้วย loop", axis="เทียบเก็บค่าน้อยสุด",
         title="🏷️ Review Lists — ข้อ 11: ราคาถูกสุด",
         scenario="ราคาในตลาด\n\n```python\nprices = [45, 30, 55, 28, 60]\n```\n\nหาราคาถูกสุดด้วย loop (ห้าม `min()`) แสดง `Cheapest: <ราคา>`",
         conditions=None, inp="ไม่มี input", out="1 บรรทัด ราคาถูกสุด",
         hint="เริ่มจากตัวแรก แล้วอัปเดตเมื่อเจอค่าที่น้อยกว่า",
         starter="prices = [45, 30, 55, 28, 60]\n\n# เขียนโค้ดตรงนี้",
         code='''prices = [45, 30, 55, 28, 60]
cheapest = prices[0]
for price in prices:
    if price < cheapest:
        cheapest = price
print(f"Cheapest: {cheapest}")'''),
    dict(file="13_challenge.md", answer="13_grade_tracker.py", diff="🔴 Challenge",
         name="ตัวติดตามเกรด", axis="append + filter + average + สถานะ",
         title="📒 Review Lists — ข้อ 12: ตัวติดตามเกรด",
         scenario="คะแนนเดิม\n\n```python\nscores = [70, 82]\n```\n\nเพิ่มคะแนนใหม่สามค่า `75, 90, 60` เรียงจากมากไปน้อย\nนับคนที่ได้ >= 80 หาค่าเฉลี่ยทั้งชุด แสดงกรอบสรุป",
         conditions=None, inp="ไม่มี input", out="กล่องสรุปเกรด",
         hint="append ทั้งสามค่า → sort reverse → นับและหา average",
         starter="scores = [70, 82]\n\n# เขียนโค้ดตรงนี้",
         code='''scores = [70, 82]
scores.append(75)
scores.append(90)
scores.append(60)
scores.sort(reverse=True)

high = 0
total = 0
for score in scores:
    total += score
    if score >= 80:
        high += 1

average = total / len(scores)

print("========================")
print("      GRADE TRACKER")
print("========================")
print(f"Scores     : {scores}")
print(f"High (>=80): {high}")
print(f"Average    : {average}")
print("========================")'''),
    dict(file="14_challenge.md", answer="14_stock_alert.py", diff="🔴 Challenge",
         name="แจ้งเตือนสต็อกต่ำ", axis="filter + หมายเลข + เทียบจำนวน",
         title="📦 Review Lists — ข้อ 13: แจ้งเตือนสต็อก",
         scenario="จำนวนคงเหลือต่อชั้น\n\n```python\nstock = [12, 3, 8, 2, 15, 1]\n```\n\nเก็บเฉพาะชั้นที่เหลือ **น้อยกว่า 5** พิมพ์หมายเลขรายการที่กรอง แล้วถ้าจำนวนชั้นที่เตือน >= 3 แสดง `Status: Restock` ไม่งั้น `Status: OK`",
         conditions=None, inp="ไม่มี input", out="รายการเตือนมีหมายเลข ตามด้วยสถานะ",
         hint="กรองก่อน แล้วใช้ len ของผลลัพธ์ตัดสินสถานะ",
         starter="stock = [12, 3, 8, 2, 15, 1]\n\n# เขียนโค้ดตรงนี้",
         code='''stock = [12, 3, 8, 2, 15, 1]
low = []
for n in stock:
    if n < 5:
        low.append(n)

for i in range(len(low)):
    print(f"{i + 1}. {low[i]}")

if len(low) >= 3:
    status = "Restock"
else:
    status = "OK"
print(f"Status: {status}")'''),
    dict(file="15_challenge.md", answer="15_playlist_builder.py", diff="🔴 Challenge",
         name="สร้างเพลย์ลิสต์จากสองแหล่ง", axis="รวม + ลบ + เรียง + สรุป",
         title="🎧 Review Lists — ข้อ 14: สร้างเพลย์ลิสต์",
         scenario='```python\nbase = ["Intro", "Verse", "Outro"]\nmore = ["Chorus", "Bridge"]\n```\n\nต่อเพลงจาก `more` เข้า `base` ลบ `"Outro"` เรียง A→Z\nแสดงจำนวนเพลง เพลงแรก เพลงสุดท้าย',
         conditions=None, inp="ไม่มี input", out="3 บรรทัดสรุปเพลย์ลิสต์",
         hint="วน append จาก more → remove → sort → อ่านสรุป",
         starter='base = ["Intro", "Verse", "Outro"]\nmore = ["Chorus", "Bridge"]\n\n# เขียนโค้ดตรงนี้',
         code='''base = ["Intro", "Verse", "Outro"]
more = ["Chorus", "Bridge"]
for song in more:
    base.append(song)
base.remove("Outro")
base.sort()
print(f"Songs: {len(base)}")
print(f"First: {base[0]}")
print(f"Last: {base[-1]}")'''),
    dict(file="16_challenge.md", answer="16_exam_board.py", diff="🔴 Challenge",
         name="บอร์ดคะแนนสอบรวม", axis="คู่ขนาน + filter ชื่อ + top",
         title="🏆 Review Lists — ข้อ 15: บอร์ดคะแนนสอบ",
         scenario='```python\nnames = ["Ann", "Ben", "Cara", "Dan", "Eve"]\nscores = [66, 91, 58, 84, 73]\n```\n\nสร้าง list ชื่อผู้ได้ >= 70 พิมพ์รายชื่อมีหมายเลข\nหาคะแนนสูงสุดด้วย loop แสดง `Top score: <ค่า>`',
         conditions=None, inp="ไม่มี input", out="รายชื่อมีหมายเลข ตามด้วยคะแนนสูงสุด",
         hint="ใช้ index คู่ขนานสำหรับกรองชื่อ และวน scores เพื่อหาค่าสูงสุด",
         starter='names = ["Ann", "Ben", "Cara", "Dan", "Eve"]\nscores = [66, 91, 58, 84, 73]\n\n# เขียนโค้ดตรงนี้',
         code='''names = ["Ann", "Ben", "Cara", "Dan", "Eve"]
scores = [66, 91, 58, 84, 73]

passed = []
for i in range(len(names)):
    if scores[i] >= 70:
        passed.append(names[i])

for i in range(len(passed)):
    print(f"{i + 1}. {passed[i]}")

top = scores[0]
for score in scores:
    if score > top:
        top = score
print(f"Top score: {top}")'''),
    ]
    emit("028-review-lists", probs, "บท 028 Review Lists",
         ["ทบทวน list ทั้งบท 025–027", "index / len / for / append / remove / sort", "filter และ range(len)"],
         ["ยังไม่ใช้ `in` เป็น membership หลัก (สอนจริงบท 030)", "ห้าม `sorted()` / `min()` / `max()`"],
         ["เป็นบททบทวน — ผสมหลายทักษะในข้อเดียวได้",
          "ข้อ Challenge ยากเพราะหลายขั้นตอน ไม่ใช่เพราะของใหม่"])


if __name__ == "__main__":
    gen_025()
    gen_026()
    gen_027()
    gen_028()
    print("025-028 complete")
