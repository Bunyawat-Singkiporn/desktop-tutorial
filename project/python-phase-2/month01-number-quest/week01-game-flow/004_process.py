# Week 1 - เช็คพอยต์ 3 : PROCESS
print("=" * 30)
print("   NUMBER QUEST - CREATE HERO")
print("=" * 30)

name = input("ชื่อฮีโร่ของเธอ: ")
print(f"ยินดีต้อนรับ {name}!")

print("เลือกอาชีพ")
print("  1) นักดาบ")
print("  2) นักธนู")
print("  3) นักเวทย์")
job = int(input("พิมพ์เลข 1-3: "))

if job == 1:
    job_name = "นักดาบ"
    attack = 10
    hp = 100
elif job == 2:
    job_name = "นักธนู"
    attack = 8
    hp = 90
else:
    job_name = "นักเวทย์"
    attack = 12
    hp = 80
