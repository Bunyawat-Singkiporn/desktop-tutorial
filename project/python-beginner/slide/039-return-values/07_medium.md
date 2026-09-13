# Practice Return Values — Medium: คู่/คี่จาก Input

**Difficulty:** 🟡 Medium

---

## โจทย์

สร้าง function `parity(n)` ที่ return `"Even"` หรือ `"Odd"`

รับตัวเลขจาก `input` 3 ครั้ง (ใช้ `for`) แล้วพิมพ์ผลแต่ละรอบ

> ผสมความรู้: return + input + for loop + if

---

## ตัวอย่าง Session

```
Enter number: 4
4 → Even
Enter number: 7
7 → Odd
Enter number: 10
10 → Even
```

---

## Starter Code

```python
def parity(n):
    # Write your code here

for i in range(3):
    n = int(input("Enter number: "))
    print(f"{n} → {parity(n)}")
```
