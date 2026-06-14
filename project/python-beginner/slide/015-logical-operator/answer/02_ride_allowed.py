# โจทย์: รับอายุและส่วนสูง แล้วตรวจสอบว่าขึ้นเครื่องเล่นได้หรือไม่
# - ต้องผ่านทั้งสองเงื่อนไข: อายุ >= 12 AND ส่วนสูง >= 140
# - ผ่านทั้งคู่ → Ride Allowed
# - ไม่ผ่านข้อใดข้อหนึ่ง → Cannot Ride

age = int(input())     # รับอายุ
height = int(input())  # รับส่วนสูง

# and: ต้องเป็นจริงทั้งสองเงื่อนไขพร้อมกัน
if age >= 12 and height >= 140:
    print("Ride Allowed")
else:
    print("Cannot Ride")
