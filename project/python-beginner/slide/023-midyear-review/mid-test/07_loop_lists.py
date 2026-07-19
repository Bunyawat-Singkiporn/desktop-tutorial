# ข้อ 7 : loop with lists
# โจทย์: วนซ้ำ list คะแนน แสดงหมายเลขและคะแนน แล้วแสดงค่าเฉลี่ย

scores = [88, 95, 72, 100, 65]

for i in range(len(scores)):
    print("Student", i + 1, ":", scores[i])  # print(f"Student {i + 1}: {scores[i]}")

average = sum(scores) / len(scores)
print("Average:", average)  # print(f"Average: {average}")




#=======================================================

# วิธีที่ 2 : for score in scores (ใช้ counter แยก)

# scores = [88, 95, 72, 100, 65]
# count = 1

# for score in scores:
#     print("Student", count, ":", score)
#     count = count + 1

# average = sum(scores) / len(scores)
# print("Average:", average)
