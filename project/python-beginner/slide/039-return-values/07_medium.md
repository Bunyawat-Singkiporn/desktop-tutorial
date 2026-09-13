# Practice Return — Question 6: เกมเลขนำโชค

**Difficulty:** 🟡 Medium

---

## โจทย์

ทำเกมเล็กๆ: ผู้เล่นสุ่มเลข (พิมพ์เอง) แล้วบอกว่าคู่หรือคี่

สร้าง `lucky(n)` ที่ return `"Even"` หรือ `"Odd"`

เล่น 3 รอบ

---

## ตัวอย่าง Session

```
Your number: 4
4 is Even
Your number: 7
7 is Odd
Your number: 10
10 is Even
```

---

## Starter Code

```python
def lucky(n):
    # Write your code here

for i in range(3):
    n = int(input("Your number: "))
    print(f"{n} is {lucky(n)}")
```
