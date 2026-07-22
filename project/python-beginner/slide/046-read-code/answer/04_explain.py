# อธิบายโปรแกรม:
# รับ: list ของคำ (words)
# ประมวลผล: จัดกลุ่มคำตามตัวอักษรตัวแรก (A, B, C, ...)
# แสดงผล: แต่ละตัวอักษร: [รายชื่อคำที่ขึ้นต้นด้วยตัวอักษรนั้น]

def process(data):
    result = {}
    for item in data:
        first_letter = item[0].upper()
        if first_letter in result:
            result[first_letter].append(item)
        else:
            result[first_letter] = [item]
    return result

words = ["apple", "banana", "avocado", "blueberry", "cherry", "apricot"]
grouped = process(words)
for letter, group in grouped.items():
    print(f"{letter}: {group}")
