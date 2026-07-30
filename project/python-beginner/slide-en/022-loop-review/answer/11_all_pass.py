# โจทย์: ตรวจว่าทุกคนผ่านหรือไม่ (flag pattern)

scores = [80, 90, 75, 65, 88]
all_pass = True

for s in scores:
    if s < 60:
        all_pass = False
        break

if all_pass:
    print("All passed!")
else:
    print("Someone failed.")
