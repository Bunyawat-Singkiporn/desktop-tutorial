# 🧩 Function Practice — ข้อ 21: หารค่าอาหารหลังกินบุฟเฟต์

**Difficulty:** 🟡 Medium

---

## โจทย์

เพื่อนๆ กินบุฟเฟต์ด้วยกัน อยากหารบิลแบบรวมทิป 10%
รับยอดบิลกับจำนวนคน แล้วคำนวณทิปและเงินที่แต่ละคนควรจ่าย

**เงื่อนไข:**

- `calc_tip(bill)` คืนทิป `bill * 10 // 100` (ใช้หารลงตัว ไม่มีทศนิยม)
- `per_person(bill, tip, people)` คืน `(bill + tip) // people`
- พิมพ์ทิปบรรทัดแรก และเงินต่อคนบรรทัดสอง

---

## Input

2 บรรทัด — ยอดบิล และจำนวนคน

## Output

2 บรรทัด — ทิป และเงินต่อคน

---

## ตัวอย่าง

**Input:**

```text
400
4
```

**Output:**

```text
40
110
```

---

## 💡 Hint

แยกคิดทิปก่อน แล้วค่อยส่งเข้าฟังก์ชันหารคน

---

## Starter Code

```python
def calc_tip(bill):
    # เขียนโค้ดตรงนี้

def per_person(bill, tip, people):
    # เขียนโค้ดตรงนี้

bill = int(input())
people = int(input())
tip = calc_tip(bill)
print(tip)
print(per_person(bill, tip, people))
```
