# โจทย์: รับตัวเลขซ้ำๆ จนพิมพ์ 0 แล้วแสดงสถิติ

numbers = []

# รับค่าวนซ้ำจนกว่าจะพิมพ์ 0
while True:
    n = int(input())
    if n == 0:
        break         # หยุดเมื่อพิมพ์ 0
    numbers.append(n)  # เก็บตัวเลขใน list

# คำนวณและแสดง stats
print("Count:", len(numbers))
print("Total:", sum(numbers))
print(f"Average: {sum(numbers) / len(numbers):.2f}")
print("Largest:", max(numbers))
print("Smallest:", min(numbers))
