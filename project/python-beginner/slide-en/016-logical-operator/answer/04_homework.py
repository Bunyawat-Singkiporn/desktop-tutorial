# โจทย์: ตรวจสอบว่านักเรียนทำการบ้านแล้วหรือยัง
# - homework_done = False หมายถึงยังไม่ได้ทำ
# - ถ้ายังไม่ทำ → แสดง "Do Homework"

homework_done = False  # กำหนดค่าเริ่มต้น: ยังไม่ทำการบ้าน

# not กลับค่า: not False = True
# ดังนั้น if จะเป็นจริง และแสดงผล
if not homework_done:
    print("Do Homework")
