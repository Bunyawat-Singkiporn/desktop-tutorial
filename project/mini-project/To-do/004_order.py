# ถ้าเราอยากให้มีเลข 1 2 3 ข้างหน้า ทำยังไง?

tasks = [
    "Homework",
    "Read Book"
]

for i in range(len(tasks)):
    print(i + 1, tasks[i])

# ผลลัพธ์
# 1 Homework
# 2 Read Book

# len(tasks)
# ใช้นับจำนวนข้อมูลใน list

# len(tasks) = 2

# range(2)
# จะได้ 0, 1

# รอบแรก
# i = 0
# print(1, tasks[0])

# รอบสอง
# i = 1
# print(2, tasks[1])