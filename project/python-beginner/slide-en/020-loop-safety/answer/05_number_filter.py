# โจทย์: รับตัวเลขซ้ำๆ แสดงเฉพาะที่หารด้วย 3 ลงตัว

count = 0

while True:
    n = int(input())
    if n == 0:
        break            # หยุดเมื่อพิมพ์ 0

    if n % 3 != 0:
        continue         # ข้ามตัวเลขที่ไม่ใช่ผลคูณของ 3

    # ถึงตรงนี้ได้ = หารด้วย 3 ลงตัว
    print(n)
    count += 1

print(f"Count of multiples of 3: {count}")
