# 🧠 Logic Integration — ข้อ 2: เก็บชื่อ 3 คน

**Difficulty:** 🟢 Easy

---

## โจทย์

รับชื่อ 3 คนเก็บใน list แล้วพิมพ์ทีละชื่อ

**เงื่อนไข:**

- ใช้ลูปอ่าน input 3 ครั้ง

---

## Input

ดูตัวอย่าง

## Output

3 บรรทัด

---

## ตัวอย่าง

**Input:**

```text
Ann
Ben
Cat
```

**Output:**

```text
Ann
Ben
Cat
```


---

## Starter Code

```python
names = []
for i in range(3):
    names.append(input())

for name in names:
    print(name)
```
