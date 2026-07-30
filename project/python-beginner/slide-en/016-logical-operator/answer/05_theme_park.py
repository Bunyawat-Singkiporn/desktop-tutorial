# โจทย์: ตรวจสอบการเข้าสวนสนุกตามกฎ
# - เด็ก (อายุ < 12): เข้าได้เฉพาะเมื่อมีผู้ปกครองมาด้วย
# - ผู้ใหญ่ (อายุ >= 12): เข้าได้เสมอ ยกเว้นถูกแบน
# ผสมความรู้: and + or + not + elif

age = int(input())       # รับอายุ
has_guardian = input()   # รับค่า "True" หรือ "False" (เป็น string)
banned = input()         # รับค่า "True" หรือ "False" (เป็น string)

# กรณีที่ 1: เด็ก → ต้องมีผู้ปกครองมาด้วย
if age < 12:
    if has_guardian == "True":   # มีผู้ปกครอง → เข้าได้
        print("Welcome")
    else:                        # ไม่มีผู้ปกครอง → เข้าไม่ได้
        print("Not Allowed")

# กรณีที่ 2: ผู้ใหญ่ → เข้าได้เสมอ ยกเว้นถูกแบน
else:
    if banned == "True":         # ถูกแบน → เข้าไม่ได้
        print("Not Allowed")
    else:                        # ไม่ถูกแบน → เข้าได้
        print("Welcome")
