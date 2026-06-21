# โจทย์: หาชื่อใน list แล้วแสดงตำแหน่ง หรือ "not found"

names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
target = input()
found = False

for i in range(len(names)):
    if names[i] == target:
        print(f"Found {target} at position {i + 1}")
        found = True
        break   # หยุดเมื่อเจอแล้ว

# ถ้าวนครบแล้วยังไม่เจอ
if not found:
    print(target, "not found")
