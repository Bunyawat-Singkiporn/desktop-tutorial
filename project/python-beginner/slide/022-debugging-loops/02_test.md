# 🐛 Practice: Debugging Loops — Question 1: Fix Off-by-One

**Difficulty:** 🟢 Easy

---

## โจทย์

โค้ดด้านล่างต้องการแสดง 1–10 แต่แสดงได้แค่ 1–9 — แก้ให้ถูกต้อง

```python
for i in range(1, 10):
    print(i)
```

**Output ที่ต้องการ:**
```
1
2
3
4
5
6
7
8
9
10
```

---

## 💡 Hint

`range(1, 10)` หยุดก่อน 10 — ต้องเปลี่ยนอะไร?

---

## Starter Code

```python
for i in range(1, 10):   # ← แก้บรรทัดนี้
    print(i)
```
