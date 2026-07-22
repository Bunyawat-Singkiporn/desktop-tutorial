# ข้อ 3 : input + type conversion
# โจทย์: รับชื่อและปีเกิด แล้วคำนวณอายุในปี 2026

name = input("What is your name? ")
birth_year = int(input("What year were you born? "))
age = 2026 - birth_year

print(f"Hello {name}!")
print(f"You are {age} years old.")
