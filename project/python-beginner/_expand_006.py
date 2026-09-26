# -*- coding: utf-8 -*-
"""Expand 006-naming-rules to 15-problem standard."""
from _expand_helpers import write_week

INDEX = """
# 📋 สารบัญโจทย์ — บท 006 Naming Rules

**ขอบเขตของบทนี้:** ตั้งชื่อตัวแปรแบบ `snake_case` / ชื่อสื่อความหมาย / `print` แสดงผล (ความรู้บท 005)

> ❌ ไม่มี `input()` · ไม่มี `if` · ไม่มี f-string · ห้ามใช้ชื่อสั้นๆ ไร้ความหมายเป็นคำตอบหลัก

---

## ลำดับที่แนะนำ

| # | ไฟล์ | ระดับ | โจทย์ | แกนการคิด |
|---|------|-------|-------|-----------|
| 1 | `02_test.md` | 🟢 | ราคาเสื้อยืด | ชื่อสื่อความหมายแทน x/y |
| 2 | `03_test.md` | 🟢 | ชื่อเต็มนักเรียน | snake_case สองส่วน |
| 3 | `04_test.md` | 🟢 | คะแนนผู้เล่น | player_score แทน s |
| 4 | `08_easy.md` | 🟢 | สถานะเกม | is_ นำหน้า bool |
| 5 | `09_easy.md` | 🟢 | ที่อยู่จัดส่ง | หลายชื่อยาวอ่านรู้เรื่อง |
| 6 | `06_medium.md` | 🟡 | สรุปร้านค้า | หลายตัวแปรชื่อดี |
| 7 | `07_medium.md` | 🟡 | ส่วนหลังลดแบบคงที่ | original/final ไม่ใช้ x |
| 8 | `10_medium.md` | 🟡 | เวลาเรียน | hours/minutes ชัดเจน |
| 9 | `11_medium.md` | 🟡 | สต็อกหนังสือ | book_title + copies |
| 10 | `12_medium.md` | 🟡 | โปรไฟล์แมว | pet_name / age_years |
| 11 | `13_medium.md` | 🟡 | บิลค่าน้ำ | meter ก่อน-หลัง |
| 12 | `05_challenge.md` | 🔴 | ใบเสร็จของเล่น | ชื่อยาวหลายตัว + รวม |
| 13 | `14_challenge.md` | 🔴 | ทีมฟุตบอล | team_name / goals |
| 14 | `15_challenge.md` | 🔴 | ทริปครอบครัว | travelers / budget |
| 15 | `16_challenge.md` | 🔴 | สมุดพกห้องแล็บ | experiment หลายฟิลด์ |

**สรุป:** 🟢 Easy 5 ข้อ · 🟡 Medium 6 ข้อ · 🔴 Challenge 4 ข้อ = **15 ข้อ**
"""

NO_INPUT = "ไม่มี (กำหนดค่าในตัวแปร)"


def P(n, title, slug, body, out_desc, sample, starter, answer, hint=None):
    return dict(n=n, title=title, slug=slug, body=body, input_desc=NO_INPUT,
                output_desc=out_desc, sample_input=None, sample_output=sample,
                hint=hint, starter=starter, answer=answer)


PROBLEMS = [
    P(2, "ราคาเสื้อยืด", "tshirt_price",
      "แทนที่จะใช้ `x` และ `y` ให้ใช้ชื่อที่ดี: `product_name = \"T-Shirt\"`, `original_price = 500`, `discount_amount = 100`, `final_price = original_price` แล้วกำหนด `final_price` เป็น 400 ตามตัวอย่าง (หรือ `final_price = 400`)\n\nแสดงชื่อสินค้าและราคาสุดท้าย",
      "2 บรรทัด",
      "Product: T-Shirt\nFinal Price: 400",
      'product_name = "T-Shirt"\noriginal_price = 500\ndiscount_amount = 100\nfinal_price = 400\n\n# แสดงผล',
      'product_name = "T-Shirt"\noriginal_price = 500\ndiscount_amount = 100\nfinal_price = 400\nprint("Product:", product_name)\nprint("Final Price:", final_price)'),
    P(3, "ชื่อเต็มนักเรียน", "full_student_name",
      '`first_name = "Ada"`, `last_name = "Lovelace"` แสดงชื่อเต็มด้วย print สองค่า',
      "1 บรรทัด",
      "Full Name: Ada Lovelace",
      'first_name = "Ada"\nlast_name = "Lovelace"\n\n# แสดงชื่อเต็ม',
      'first_name = "Ada"\nlast_name = "Lovelace"\nprint("Full Name:", first_name, last_name)'),
    P(4, "คะแนนผู้เล่น", "player_score_name",
      '`player_score = 95` แสดงคะแนน (ห้ามใช้ชื่อตัวแปร `s`)',
      "1 บรรทัด",
      "Player Score: 95",
      "player_score = 95\n\n# แสดงผล",
      'player_score = 95\nprint("Player Score:", player_score)'),
    P(8, "สถานะเกม", "game_over_flag",
      '`is_game_over = False` แสดงสถานะเกม',
      "1 บรรทัด",
      "Game Over: False",
      "is_game_over = False\n\n# แสดงผล",
      'is_game_over = False\nprint("Game Over:", is_game_over)'),
    P(9, "ที่อยู่จัดส่ง", "shipping_address",
      '`city_name = "Chiang Mai"`, `postal_code = 50000` แสดงที่อยู่',
      "2 บรรทัด",
      "City: Chiang Mai\nPostal Code: 50000",
      'city_name = "Chiang Mai"\npostal_code = 50000\n\n# แสดงผล',
      'city_name = "Chiang Mai"\npostal_code = 50000\nprint("City:", city_name)\nprint("Postal Code:", postal_code)'),
    P(6, "สรุปร้านค้า", "shop_summary",
      '`shop_name = "Bean Shop"`, `open_hour = 8`, `close_hour = 18` แสดงสรุป',
      "3 บรรทัด",
      "Shop: Bean Shop\nOpens: 8\nCloses: 18",
      'shop_name = "Bean Shop"\nopen_hour = 8\nclose_hour = 18\n\n# แสดงสรุป',
      'shop_name = "Bean Shop"\nopen_hour = 8\nclose_hour = 18\nprint("Shop:", shop_name)\nprint("Opens:", open_hour)\nprint("Closes:", close_hour)',
      "ใช้ snake_case ทั้งสามชื่อ"),
    P(7, "ราคาหลังลดแบบคงที่", "named_prices",
      '`original_price = 250`, `sale_price = 199` แสดงทั้งสองด้วยชื่อที่อ่านรู้เรื่อง',
      "2 บรรทัด",
      "Original Price: 250\nSale Price: 199",
      "original_price = 250\nsale_price = 199\n\n# แสดงผล",
      'original_price = 250\nsale_price = 199\nprint("Original Price:", original_price)\nprint("Sale Price:", sale_price)',
      "อย่าใช้ตัวแปรชื่อ p1/p2"),
    P(10, "เวลาเรียน", "class_time",
      '`class_hours = 2`, `break_minutes = 15` แสดงเวลา',
      "2 บรรทัด",
      "Class Hours: 2\nBreak Minutes: 15",
      "class_hours = 2\nbreak_minutes = 15\n\n# แสดงผล",
      'class_hours = 2\nbreak_minutes = 15\nprint("Class Hours:", class_hours)\nprint("Break Minutes:", break_minutes)',
      "ชื่อต้องบอกหน่วยคร่าวๆ"),
    P(11, "สต็อกหนังสือ", "book_stock",
      '`book_title = "Python Kids"`, `copy_count = 12` แสดงสต็อก',
      "2 บรรทัด",
      "Title: Python Kids\nCopies: 12",
      'book_title = "Python Kids"\ncopy_count = 12\n\n# แสดงผล',
      'book_title = "Python Kids"\ncopy_count = 12\nprint("Title:", book_title)\nprint("Copies:", copy_count)',
      "snake_case สำหรับชื่อหนังสือ"),
    P(12, "โปรไฟล์แมว", "cat_profile",
      '`pet_name = "Mochi"`, `age_years = 2` แสดงโปรไฟล์',
      "2 บรรทัด",
      "Pet: Mochi\nAge: 2",
      'pet_name = "Mochi"\nage_years = 2\n\n# แสดงผล',
      'pet_name = "Mochi"\nage_years = 2\nprint("Pet:", pet_name)\nprint("Age:", age_years)',
      "age_years ชัดกว่า age อย่างเดียว"),
    P(13, "บิลค่าน้ำ", "water_bill_names",
      '`meter_before = 120`, `meter_after = 135`, `units_used = 15` แสดงค่ามิเตอร์',
      "3 บรรทัด",
      "Before: 120\nAfter: 135\nUnits: 15",
      "meter_before = 120\nmeter_after = 135\nunits_used = 15\n\n# แสดงผล",
      'meter_before = 120\nmeter_after = 135\nunits_used = 15\nprint("Before:", meter_before)\nprint("After:", meter_after)\nprint("Units:", units_used)',
      "ตั้งชื่อให้รู้ว่าก่อน/หลัง/ยูนิต"),
    P(5, "ใบเสร็จของเล่น", "toy_receipt",
      '`toy_name = "Robot Kit"`, `toy_price = 890`, `box_fee = 20`, `total_price = 910` แสดงใบเสร็จ',
      "ใบเสร็จ",
      "Toy: Robot Kit\nPrice: 890\nBox Fee: 20\nTotal: 910",
      'toy_name = "Robot Kit"\ntoy_price = 890\nbox_fee = 20\ntotal_price = 910\n\n# แสดงใบเสร็จ',
      'toy_name = "Robot Kit"\ntoy_price = 890\nbox_fee = 20\ntotal_price = 910\nprint("Toy:", toy_name)\nprint("Price:", toy_price)\nprint("Box Fee:", box_fee)\nprint("Total:", total_price)',
      "ทุกตัวแปรต้อง snake_case และสื่อความหมาย"),
    P(14, "ทีมฟุตบอล", "football_team",
      '`team_name = "Blue Hawks"`, `goals_scored = 3`, `goals_conceded = 1` แสดงสถิติ',
      "3 บรรทัด",
      "Team: Blue Hawks\nScored: 3\nConceded: 1",
      'team_name = "Blue Hawks"\ngoals_scored = 3\ngoals_conceded = 1\n\n# แสดงผล',
      'team_name = "Blue Hawks"\ngoals_scored = 3\ngoals_conceded = 1\nprint("Team:", team_name)\nprint("Scored:", goals_scored)\nprint("Conceded:", goals_conceded)',
      "อย่าใช้ g1/g2"),
    P(15, "ทริปครอบครัว", "family_trip",
      '`trip_place = "Zoo"`, `traveler_count = 4`, `ticket_budget = 800` แสดงแผนทริป',
      "3 บรรทัด",
      "Place: Zoo\nTravelers: 4\nBudget: 800",
      'trip_place = "Zoo"\ntraveler_count = 4\nticket_budget = 800\n\n# แสดงผล',
      'trip_place = "Zoo"\ntraveler_count = 4\nticket_budget = 800\nprint("Place:", trip_place)\nprint("Travelers:", traveler_count)\nprint("Budget:", ticket_budget)',
      "ชื่อต้องอ่านแล้วรู้ว่าเก็บอะไร"),
    P(16, "สมุดพกห้องแล็บ", "lab_notebook",
      '`experiment_name = "Plant Growth"`, `day_number = 7`, `height_cm = 12.5` แสดงบันทึก',
      "3 บรรทัด",
      "Experiment: Plant Growth\nDay: 7\nHeight: 12.5",
      'experiment_name = "Plant Growth"\nday_number = 7\nheight_cm = 12.5\n\n# แสดงผล',
      'experiment_name = "Plant Growth"\nday_number = 7\nheight_cm = 12.5\nprint("Experiment:", experiment_name)\nprint("Day:", day_number)\nprint("Height:", height_cm)',
      "ใส่หน่วยในชื่อตัวแปรเมื่อช่วย confer ความหมาย"),
]


if __name__ == "__main__":
    write_week("006-naming-rules", chapter="Naming Rules", emoji="🏷️", index_md=INDEX, problems=PROBLEMS)
