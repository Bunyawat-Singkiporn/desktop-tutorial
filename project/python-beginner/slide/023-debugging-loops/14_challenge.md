# 🐛 debugging-loops — ข้อ 14: แก้คิวสั่งอาหาร

**Difficulty:** 🔴 Challenge

---

## โจทย์

รับชื่อเมนูทีละบรรทัดจนเจอ `end`
พิมพ์เมนูที่รับจริง (ไม่รวม end) แล้วปิดท้ายด้วย `Count: <จำนวน>`
โค้ดเริ่มต้นพิมพ์ end และนับรวม end — แก้ลำดับเงื่อนไขให้ถูก

---

## Input

ชื่อเมนูทีละบรรทัด จบด้วย end

## Output

รายการเมนูแล้วตามด้วย Count

---

## ตัวอย่าง

**Input:**

```text
Pad Thai
Green Curry
end
```

**Output:**

```text
Pad Thai
Green Curry
Count: 2
```


---

## 💡 Hint

เช็คคำจบก่อนพิมพ์และก่อนนับ

---

## Starter Code

```python
count = 0
while True:
    menu = input()
    print(menu)
    count = count + 1
    if menu == "end":
        break
print(f"Count: {count}")
```
