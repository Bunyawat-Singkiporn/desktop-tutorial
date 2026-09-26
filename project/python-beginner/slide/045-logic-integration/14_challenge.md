# 🧠 Logic Integration — ข้อ 14: โปรไฟล์หลายคน

**Difficulty:** 🔴 Challenge

---

## โจทย์

สร้าง dict จากคู่ชื่อ-คะแนน

**เงื่อนไข:**

- รับ n
- อ่าน n รอบ แต่ละรอบชื่อแล้วคะแนน
- พิมพ์ dict ทั้งก้อน

---

## Input

ดูตัวอย่าง

## Output

1 บรรทัด

---

## ตัวอย่าง

**Input:**

```text
2
Ada
90
Ben
70
```

**Output:**

```text
{'Ada': 90, 'Ben': 70}
```


---

## 💡 Hint

ใส่ key ทีละคน

---

## Starter Code

```python
n = int(input())
profiles = {}
for i in range(n):
    name = input()
    score = int(input())
    profiles[name] = score
print(profiles)
```
