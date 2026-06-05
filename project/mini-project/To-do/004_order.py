# ถ้าเราอยากให้มีเลข 1 2 3 ข้างหน้า ทำยังไง?

tasks = [
    "Homework",
    "Read Book"
]

for i in range(len(tasks)):
    print(i + 1, tasks[i])


# len() ไว้นับจำนวน

# for i in range() คือการใช้ลูป for เพื่อวนลูปผ่านตัวเลขตั้งแต่ 0 ถึงจำนวนงานใน tasks - 1 (วนรอบตามจำนวนงานใน tasks)

# print(i + 1, tasks[i]) ผลลัพธ์คือ 1 Homework เพราะ print 0+1=1 และ tasks[0] คือ Homework
# คิดว่ารอบสองจะแสดงอะไรออกมา?