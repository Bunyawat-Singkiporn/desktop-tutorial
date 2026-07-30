# โจทย์: รับชื่อและคะแนน แล้วแสดงเกรด

name = input()
score = int(input())

print(f"Name: {name}")
print(f"Score: {score}")

# ตรวจเกรดด้วย if/elif/else
if score >= 80:
    print("Grade: A")
elif score >= 60:
    print("Grade: B")
else:
    print("Grade: C")
