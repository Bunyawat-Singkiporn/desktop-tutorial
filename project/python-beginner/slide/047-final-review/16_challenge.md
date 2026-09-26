# 🏁 Final Review — ข้อ 16: สรุปพร้อมเช็กขอบ

**Difficulty:** 🔴 Challenge

---

## โจทย์

รับ n คะแนน ถ้า n เป็น 0 พิมพ์ `No scores` ไม่งั้นพิมพ์ค่าเฉลี่ยทศนิยม 1 ตำแหน่ง

---

## Input

ดูตัวอย่าง

## Output

1 บรรทัด

---

## ตัวอย่าง

**Input:**

```text
0
```

**Output:**

```text
No scores
```


---

## 💡 Hint

กันหารศูนย์ด้วยการเช็ก n

---

## Starter Code

```python
n = int(input())
if n == 0:
    print("No scores")
else:
    total = 0
    for i in range(n):
        total += int(input())
    print(f"{total / n:.1f}")
```
