# โจทย์: รับอุณหภูมิ แล้วแสดงระดับความร้อน
# - 40+  → Very Hot
# - 30+  → Hot
# - 20+  → Warm
# - <20  → Cold

temp = int(input())  # รับอุณหภูมิเป็น int

# เรียงเงื่อนไขจากค่ามากที่สุดก่อนเสมอ
# ไม่เช่นนั้น 45 จะได้ "Hot" แทนที่จะได้ "Very Hot"
if temp >= 40:
    print("Very Hot")
elif temp >= 30:  # ถึงบรรทัดนี้ temp < 40 แล้ว
    print("Hot")
elif temp >= 20:  # ถึงบรรทัดนี้ temp < 30 แล้ว
    print("Warm")
else:             # ถึงบรรทัดนี้ temp < 20 แล้ว
    print("Cold")
