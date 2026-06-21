# โจทย์: แสดงตัวเลขทั้งหมดในบรรทัดเดียว พร้อม stats ครบ

numbers = [3, 7, 1, 9, 4, 6, 2, 8, 5]

# พิมพ์ตัวเลขทั้งหมดในบรรทัดเดียว
print("Numbers:", end=" ")
for n in numbers:
    print(n, end=" ")
print()   # ขึ้นบรรทัดใหม่

# แสดง stats ใช้ built-in functions
print("Count:", len(numbers))
print("Total:", sum(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
print(f"Average: {sum(numbers) / len(numbers):.1f}")
