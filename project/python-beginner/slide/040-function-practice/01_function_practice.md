# 🧩 Function Practice — ฝึกใช้ Function

---

## ทบทวน Functions ที่เรียนมา

| ทักษะ | ตัวอย่าง |
|-------|---------|
| สร้าง function | `def greet():` |
| ใช้ parameter | `def greet(name):` |
| ส่งค่ากลับ | `return result` |
| เรียกใช้ | `greet("Alice")` |

---

## รวม Function กับ List

```python
def get_total(scores):
    total = 0
    for score in scores:
        total += score
    return total

my_scores = [80, 75, 90, 65, 88]
print("Total:", get_total(my_scores))
```

---

## รวม Function กับ Dictionary

```python
def show_student(student):
    for key, value in student.items():
        print(f"{key}: {value}")

alice = {"name": "Alice", "score": 92}
show_student(alice)
```

---

## รวม Function หลายตัว

```python
def get_average(scores):
    return sum(scores) / len(scores)

def get_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    else:
        return "C"

scores = [85, 90, 78]
avg = get_average(scores)
grade = get_grade(avg)
print(f"Average: {avg:.1f}, Grade: {grade}")
```

---

## แนวคิด: Function ที่ดี

- ทำงานอย่างเดียว (Single Responsibility)
- ตั้งชื่อสื่อความหมาย
- ไม่ยาวเกิน 10–15 บรรทัด
