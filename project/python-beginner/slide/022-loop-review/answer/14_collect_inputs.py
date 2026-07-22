# โจทย์: รับตัวเลข 5 ครั้งด้วย while แล้วหาค่าเฉลี่ย

numbers = []

while len(numbers) < 5:
    n = int(input())
    numbers.append(n)

print(f"Average: {sum(numbers)/len(numbers):.1f}")
