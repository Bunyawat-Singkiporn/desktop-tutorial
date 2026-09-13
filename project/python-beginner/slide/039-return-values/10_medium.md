# Practice Return — Question 9: แก้คะแนนเกมให้ถูกต้อง

**Difficulty:** 🟡 Medium

---

## โจทย์

ในเกม คะแนนต้องอยู่ระหว่าง 0–100 เท่านั้น

สร้าง `fix_score(score)`:
- น้อยกว่า 0 → return `0`
- มากกว่า 100 → return `100`
- นอกนั้นคืนค่าเดิม

รับคะแนนผิดๆ มา 3 ค่า แล้วแสดงคะแนนที่แก้แล้ว

---

## ตัวอย่าง Session

```
Raw score: -5
Fixed: 0
Raw score: 150
Fixed: 100
Raw score: 85
Fixed: 85
```

---

## Starter Code

```python
def fix_score(score):
    # Write your code here

for i in range(3):
    score = int(input("Raw score: "))
    print(f"Fixed: {fix_score(score)}")
```
