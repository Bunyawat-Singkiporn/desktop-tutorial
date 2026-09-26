# 🧠 Logic Integration — ข้อ 5: คิวร้านตัดซ้ำ

**Difficulty:** 🔴 Challenge

---

## โจทย์

คิวชื่ออาจซ้ำ ให้พิมพ์จำนวนชื่อไม่ซ้ำ

**เงื่อนไข:**

- รับ n แล้วอ่าน n ชื่อ
- ใช้ set หาจำนวนไม่ซ้ำแล้วพิมพ์

---

## Input

ดูตัวอย่าง

## Output

1 บรรทัด

---

## ตัวอย่าง

**Input:**

```text
4
Ann
Ben
Ann
Cat
```

**Output:**

```text
3
```


---

## 💡 Hint

set ตัดชื่อซ้ำ

---

## Starter Code

```python
n = int(input())
names = []
for i in range(n):
    names.append(input())
print(len(set(names)))
```
