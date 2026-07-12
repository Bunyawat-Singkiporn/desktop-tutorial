# ⬇️ Practice: Loop Review — Question 5: Countdown

**Difficulty:** 🟢 Easy

---

## โจทย์

รับตัวเลข n แล้วนับถอยหลังจาก n ลงมาถึง 1 แล้วพิมพ์ "Go!"

**Input:**
```
5
```

**Output:**
```
5
4
3
2
1
Go!
```

---

## 💡 Hint

- ใช้ `range(n, 0, -1)` — range 3 ตัวเลข: เริ่ม, หยุด, step
- step `-1` = ลดลงทีละ 1

---

## Starter Code

```python
n = int(input())

for i in range(n, 0, -1):
    # Print i

print("Go!")
```
