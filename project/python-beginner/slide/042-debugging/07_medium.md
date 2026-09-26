# 🐛 Debugging — ข้อ 7: ตรวจความยาว list

**Difficulty:** 🟡 Medium

---

## โจทย์

จะอ่านสมาชิกตัวสุดท้าย ต้องมีข้อมูลก่อน

**เงื่อนไข:**

- รับ n แล้วอ่าน n จำนวนเต็มเก็บใน list
- ถ้า list ว่างพิมพ์ `Empty` ไม่งั้นพิมพ์ตัวสุดท้าย

---

## Input

ดูตัวอย่าง

## Output

1 บรรทัด

---

## ตัวอย่าง

**Input:**

```text
0
```

**Output:**

```text
Empty
```


---

## 💡 Hint

ดู len ก่อนใช้ index

---

## Starter Code

```python
n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

# เช็กว่าง
```
