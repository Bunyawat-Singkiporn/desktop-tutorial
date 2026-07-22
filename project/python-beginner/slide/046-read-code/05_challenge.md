# 🔥 Read Code — Question 4: Find and Fix Bug

**Difficulty:** 🔴 Hard

---

## โจทย์

อ่านโค้ดด้านล่าง **โดยไม่รัน** หาบัค แล้วอธิบายและแก้ไข

```python
def find_average(scores):
    total = 0
    for score in scores:
        total = total + score
    return total / 10    # ← ตรวจดี ๆ

def classify(avg):
    if avg > 80:         # ← ตรวจดี ๆ
        return "Excellent"
    if avg > 60:
        return "Good"
    else:
        return "Needs Work"

data = [70, 80, 90, 85, 75]
avg = find_average(data)
print(f"Average: {avg}")
print(f"Level: {classify(avg)}")
```

**Output ที่ถูกต้อง:**
```
Average: 80.0
Level: Excellent
```

---

## คำถาม

1. บัคอยู่ที่ไหน? (โดยไม่รัน)
2. บัคประเภทใด?
3. แก้อย่างไร?

---

## Starter Code

```python
# อธิบายบัคที่พบ:
# บัค 1: บรรทัด __ เพราะ __
# บัค 2: บรรทัด __ เพราะ __

# แก้โค้ดให้ถูกต้อง:
```
