# โจทย์: รับชื่อและปีเกิด แล้วคำนวณอายุและแสดงข้อมูลครบถ้วน

# รับข้อมูล
name = input()
birth_year = int(input())

# ปีปัจจุบัน (hardcode)
current_year = 2025

# คำนวณ
age = current_year - birth_year
next_age = age + 1

# แสดงผล
print("Name:", name)
print("Birth Year:", birth_year)
print("Current Year:", current_year)
print("Age:", age)
print("Next Birthday Age:", next_age)
