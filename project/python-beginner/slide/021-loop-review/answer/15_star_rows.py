# โจทย์: สามเหลี่ยมดาวพร้อมบอกจำนวนดาวต่อแถว

n = int(input())

for row in range(1, n + 1):
    stars = ""
    for j in range(row):
        stars += "*"
    print(f"Row {row}: {stars} ({row} stars)")
