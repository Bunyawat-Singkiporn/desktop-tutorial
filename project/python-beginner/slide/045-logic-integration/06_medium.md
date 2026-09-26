# 🧠 Logic Integration — ข้อ 6: รับคะแนน n คน

**Difficulty:** 🟡 Medium

---

## โจทย์

รับจำนวน n แล้วอ่านคะแนน n ค่า แล้วพิมพ์ผลรวม

**เงื่อนไข:**

- บรรทัดแรกคือ n
- ตามด้วยคะแนน n บรรทัด

---

## Input

ดูตัวอย่าง

## Output

1 บรรทัด

---

## ตัวอย่าง

**Input:**

```text
3
40
50
60
```

**Output:**

```text
150
```


---

## 💡 Hint

สร้าง list จาก input ก่อนรวม

---

## Starter Code

```python
n = int(input())
scores = []
for i in range(n):
    scores.append(int(input()))
print(sum(scores))
```
