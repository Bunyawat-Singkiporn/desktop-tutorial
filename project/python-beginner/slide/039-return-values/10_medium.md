# Practice Return — Medium: Clamp คะแนน

**Difficulty:** 🟡 Medium

---

## โจทย์

สร้าง `clamp(score)` ที่ return คะแนนให้อยู่ในช่วง 0–100:
- ถ้า < 0 → return `0`
- ถ้า > 100 → return `100`
- นอกนั้น return ค่าเดิม

รับคะแนนจาก `input` 3 ครั้ง แล้วพิมพ์ค่าที่ clamp แล้ว

> ผสมความรู้: return + input + for + if/elif/else

---

## ตัวอย่าง Session

```
Enter score: -5
0
Enter score: 150
100
Enter score: 85
85
```

---

## Starter Code

```python
def clamp(score):
    # Write your code here

for i in range(3):
    score = int(input("Enter score: "))
    print(clamp(score))
```
