# 🏢 Logical — ข้อ 9: เข้าออฟฟิศได้ไหม

**Difficulty:** 🟡 Medium

---

## โจทย์

ระบบประตูออฟฟิศเปิดให้เข้าเมื่อเป็นวันทำงาน และมีบัตรพนักงาน

เขียนโปรแกรมรับประเภทวันกับสถานะบัตร แล้วบอกว่าเข้าได้หรือไม่

**เงื่อนไข:**

- วันเป็น `workday` **และ** บัตรเป็น `1` → `Access Granted`
- ถ้าไม่ใช่ → `Access Denied`

---

## Input

2 บรรทัด — ประเภทวัน (`workday` หรือ `holiday`) และสถานะบัตร (`1` / `0`)

## Output

2 บรรทัด — ประเภทวัน และผลการเข้า

---

## ตัวอย่าง

**Input:**

```text
workday
1
```

**Output:**

```text
Day    : workday
Access : Access Granted
```

---

## 💡 Hint

เทียบทั้งข้อความและตัวเลขในเงื่อนไขเดียวด้วย `and`

---

## Starter Code

```python
day_type = input()
has_badge = int(input())

# เขียนโค้ดตรงนี้
```
