# ✨ Code Readability — ข้อ 13: ป้ายสถานะอ่านง่าย

**Difficulty:** 🟡 Medium

---

## โจทย์

แบตเตอรี่ต่ำเมื่อ < 20

**เงื่อนไข:**

- รับเปอร์เซ็นต์แบต
- `is_low = battery < 20`
- พิมพ์ `Low` หรือ `OK`

---

## Input

ดูตัวอย่าง

## Output

1 บรรทัด

---

## ตัวอย่าง

**Input:**

```text
15
```

**Output:**

```text
Low
```


---

## 💡 Hint

ใช้ is_low ใน if

---

## Starter Code

```python
battery = int(input())
is_low = battery < 20

# พิมพ์สถานะ
```
