scores = [85, 92, 78]

# Bug 1 fixed: ใช้ index ที่มีอยู่จริง (2 = ตัวสุดท้าย)
print(scores[2])

# Bug 2 fixed: แปลง input เป็น int ก่อนบวก
age = int(input("Age: "))
next_year = age + 1
print(next_year)
