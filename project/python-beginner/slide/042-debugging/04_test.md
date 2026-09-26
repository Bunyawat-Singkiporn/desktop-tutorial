# 🐛 Debugging — ข้อ 4: แก้ index เกิน

**Difficulty:** 🟢 Easy

---

## โจทย์

อ่านสมาชิกใน list แต่ต้องไม่เกินขอบ

**เงื่อนไข:**

- มี `nums = [10, 20, 30]`
- รับ index เป็นจำนวนเต็ม
- ถ้า index อยู่ระหว่าง 0 ถึง len-1 พิมพ์ค่า ไม่งั้นพิมพ์ `Out of range`

---

## Input

ดูตัวอย่าง

## Output

1 บรรทัด

---

## ตัวอย่าง

**Input:**

```text
5
```

**Output:**

```text
Out of range
```


---

## 💡 Hint

เทียบกับ len(nums)

---

## Starter Code

```python
nums = [10, 20, 30]
index = int(input())

# เช็กขอบเขตก่อน
```
