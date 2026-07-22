# 🛑 Practice: Loop Safety — Question 1: Use break

**Difficulty:** 🟢 Easy

---

## โจทย์

วนซ้ำ 1–10 แต่หยุดทันทีเมื่อพบเลข 6

**Output:**
```
1
2
3
4
5
Stopped at 6
```

---

## 💡 Hint

- ใช้ `for i in range(1, 11):`
- ถ้า `i == 6` ให้ `print` ข้อความแล้ว `break`

---

## Starter Code

```python
for i in range(1, 11):
    if i == 6:
        print("Stopped at 6")
        # Stop the loop
    # Print i (only reached if i != 6)
```
