# โจทย์: แก้ TypeError — ไม่สามารถต่อ str กับ int ด้วย +
# ปัญหา: passed_score เป็น int ไม่สามารถต่อกับ str ด้วย + ได้

student_name = input()
score = input()
passed_score = 50

# ✅ แก้โดยแปลง int → str ด้วย str()
print("Name: " + student_name)
print("Score: " + score)
print("Pass score: " + str(passed_score))  # แปลง int เป็น str ก่อนต่อ
