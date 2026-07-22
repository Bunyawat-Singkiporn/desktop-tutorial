# รับตัวเลข 2 ตัว คำนวณผลคูณ และตรวจว่าเป็นเลขคู่หรือคี่
num1 = int(input())
num2 = int(input())

result = num1 * num2
print(f"Result: {result}")

if result % 2 == 0:
    print("Even")
else:
    print("Odd")
