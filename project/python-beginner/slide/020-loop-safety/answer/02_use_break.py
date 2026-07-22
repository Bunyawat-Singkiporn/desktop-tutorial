# โจทย์: วน 1–10 แต่ break เมื่อเจอ 6

for i in range(1, 11):
    if i == 6:
        print("Stopped at 6")
        break           # หยุด loop ทันที
    print(i)
