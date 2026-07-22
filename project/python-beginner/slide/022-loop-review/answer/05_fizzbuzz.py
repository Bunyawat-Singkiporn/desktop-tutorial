# โจทย์: FizzBuzz — แสดง Fizz/Buzz/FizzBuzz ตามกฎ

n = int(input())

for i in range(1, n + 1):
    if i % 15 == 0:     # ตรวจ 15 ก่อน (หารได้ทั้ง 3 และ 5)
        print("FizzBuzz")
    elif i % 3 == 0:    # หารด้วย 3 ลงตัว
        print("Fizz")
    elif i % 5 == 0:    # หารด้วย 5 ลงตัว
        print("Buzz")
    else:
        print(i)
