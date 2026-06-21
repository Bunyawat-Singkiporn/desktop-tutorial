# ⬜ Practice: Nested Loops — Question 1: Rectangle

**Difficulty:** 🟢 Easy

---

## โจทย์

แสดงสี่เหลี่ยมผืนผ้าขนาด 4 × 3 ด้วยเครื่องหมาย `*`

**Output:**
```
****
****
****
```

---

## 💡 Hint

- Loop นอก: วน 3 รอบ (3 แถว)
- Loop ใน: วน 4 รอบ (4 ดาว)
- ใช้ `print("*", end="")` และ `print()` ขึ้นบรรทัด

---

## Starter Code

```python
for row in range(3):
    for col in range(4):
        print("*", end="")
    print()   # new line after each row
```
