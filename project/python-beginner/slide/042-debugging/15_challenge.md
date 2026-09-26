# 🐛 Debugging — ข้อ 15: กัน list ว่าง

**Difficulty:** 🔴 Challenge

---

## โจทย์

หาค่าเฉลี่ยคะแนน ต้องกัน list ว่าง

**เงื่อนไข:**

- สร้าง `safe_avg(scores)` ถ้า len เป็น 0 คืน 0 ไม่งั้นคืน sum/len
- พิมพ์ผลของ `[]` และ `[10, 20]`

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม)

## Output

2 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
0
15.0
```


---

## 💡 Hint

เช็ก len ก่อนหาร

---

## Starter Code

```python
def safe_avg(scores):
    # กันว่าง

print(safe_avg([]))
print(safe_avg([10, 20]))
```
