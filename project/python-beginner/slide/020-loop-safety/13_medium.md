# 📋 loop-safety — ข้อ 13: เมนูคำสั่งจน exit

**Difficulty:** 🟡 Medium

---

## โจทย์

ใช้ `while True` รับคำสั่ง
ถ้าได้ `"exit"` พิมพ์ `Bye` แล้ว break
คำสั่งอื่นพิมพ์ `CMD: <คำสั่ง>`

---

## Input

คำสั่งทีละบรรทัด จบด้วย exit

## Output

CMD ของคำสั่งก่อน exit แล้ว Bye

---

## ตัวอย่าง

**Input:**

```text
help
list
exit
```

**Output:**

```text
CMD: help
CMD: list
Bye
```

---

## 💡 Hint

คล้ายข้อ Echo แต่ข้อความปิดท้ายต่างกัน

---

## Starter Code

```python
# เขียนโค้ดตรงนี้
```
