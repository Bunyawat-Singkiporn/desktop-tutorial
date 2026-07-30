# โจทย์: รับชื่อและคะแนน 3 วิชา แล้วแสดงรายงานผลการเรียน

# รับข้อมูล
name = input()
math = int(input())
english = int(input())
science = int(input())

# คำนวณค่าเฉลี่ย
average = (math + english + science) / 3

# แสดงรายงานด้วย f-string
print("=== Score Report ===")
print(f"Name: {name}")
print(f"Math: {math}")
print(f"English: {english}")
print(f"Science: {science}")
print(f"Average: {average:.2f}")
