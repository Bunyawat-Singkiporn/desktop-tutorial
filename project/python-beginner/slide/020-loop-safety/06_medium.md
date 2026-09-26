# 📇 loop-safety — ข้อ 6: ค้นหาชื่อในรายการ

**Difficulty:** 🟡 Medium

---

## โจทย์

มีลิสต์ชื่อ รับชื่อที่ต้องการค้นหา
วนลิสต์ด้วยตัวนับตำแหน่งเริ่มที่ 1
เมื่อเจอชื่อตรงกันพิมพ์ `Found at <ตำแหน่ง>` แล้ว `break`
ถ้าวนจบแล้วยังไม่เจอพิมพ์ `Not Found`

---

## Input

ชื่อที่ค้นหา 1 บรรทัด

## Output

Found at ... หรือ Not Found

---

## ตัวอย่าง

**Input:**

```text
Cara
```

**Output:**

```text
Found at 3
```

---

## 💡 Hint

ใช้ตัวแปร found เป็นข้อความเริ่มต้น Not Found ถ้าเจอให้เปลี่ยนแล้ว break

---

## Starter Code

```python
names = ["Ann", "Ben", "Cara", "Dan"]
target = input()

# เขียนโค้ดตรงนี้
```
