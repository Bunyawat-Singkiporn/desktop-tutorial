# 🏋️ Dict Practice — ข้อ 5: ตรวจคำตอบควิซ

**Difficulty:** 🔴 Challenge

---

## โจทย์

ตรวจคำตอบควิซ 3 ข้อ

กำหนด `answers = {"q1": "A", "q2": "C", "q3": "B"}`

รับคำตอบผู้ใช้ด้วย `input("q1: ")` แบบเดียวกันกับ q2 q3
ถ้าถูกพิมพ์ `Correct` ผิดพิมพ์ `Wrong` แล้วปิดท้ายด้วยคะแนนรวม (ข้อละ 1)

ตัวอย่างคำตอบผู้ใช้: A / B / B

> หมายเหตุ: prompt ของ input จะโผล่หน้าคำว่า Correct/Wrong

---

## Input

3 บรรทัด — คำตอบ q1 q2 q3

## Output

4 บรรทัด (รวม prompt)

---

## ตัวอย่าง

**Input:**

```text
A
B
B
```

**Output:**

```text
q1: Correct
q2: Wrong
q3: Correct
Score: 2
```


---

## 💡 Hint

เทียบคำตอบทีละข้อแล้วสะสมคะแนน

---

## Starter Code

```python
answers = {"q1": "A", "q2": "C", "q3": "B"}

# เขียนโค้ดตรงนี้
```
