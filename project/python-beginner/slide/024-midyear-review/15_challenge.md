# 🏆 midyear-review — ข้อ 15: ระบบเข้าคิวร้าน

**Difficulty:** 🔴 Challenge

---

## โจทย์

รับคำสั่งทีละบรรทัด
- ถ้าเป็น `join` พิมพ์ `Added`
- ถ้าเป็น `quit` พิมพ์ `Closed` แล้วหยุด
- คำอื่นพิมพ์ `Unknown`

---

## Input

คำสั่งทีละบรรทัด จบด้วย quit

## Output

ข้อความตอบกลับตามคำสั่ง

---

## ตัวอย่าง

**Input:**

```text
join
hello
quit
```

**Output:**

```text
Added
Unknown
Closed
```


---

## 💡 Hint

ใช้ while True แล้วค่อยแยกคำสั่ง

---

## Starter Code

```python
# while True อ่านคำสั่ง
```
