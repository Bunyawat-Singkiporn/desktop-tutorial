# คำนวณความยาวเฉลี่ยของชื่อผลไม้
fruits = ["apple", "banana", "mango"]
total = 0

for fruit in fruits:
    total += len(fruit)

avg = total / len(fruits)
print(avg)
