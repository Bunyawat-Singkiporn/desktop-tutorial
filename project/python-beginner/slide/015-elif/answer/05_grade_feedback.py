# โจทย์: รับคะแนน 0-100 แล้วแสดงเกรดพร้อมข้อความให้กำลังใจ
# - >= 80 → A + "Excellent!"
# - >= 70 → B + "Good Job!"
# - >= 60 → C + "Keep Going!"
# - >= 50 → D + "Need More Practice"
# - < 50  → F + "Please Retake"
# ผสมความรู้: elif + print หลายบรรทัด

score = int(input())  # รับคะแนนเป็น int

# เรียงเงื่อนไขจากคะแนนสูงสุดลงมา
# Python หยุดที่เงื่อนไขแรกที่เป็นจริง
if score >= 80:
    print("A")
    print("Excellent!")
elif score >= 70:    # ถึงบรรทัดนี้ score < 80 แล้ว
    print("B")
    print("Good Job!")
elif score >= 60:    # ถึงบรรทัดนี้ score < 70 แล้ว
    print("C")
    print("Keep Going!")
elif score >= 50:    # ถึงบรรทัดนี้ score < 60 แล้ว
    print("D")
    print("Need More Practice")
else:                # ถึงบรรทัดนี้ score < 50 แล้ว
    print("F")
    print("Please Retake")
