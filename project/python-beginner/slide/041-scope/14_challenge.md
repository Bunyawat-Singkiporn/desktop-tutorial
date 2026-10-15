# 🔭 Scope — ข้อ 14: โหมดเงียบ

**Difficulty:** 🔴 Challenge

---

## โจทย์

สลับโหมดเงียบ

**เงื่อนไข:**

- `quiet = False`
- `toggle()` สลับค่า quiet ด้วย global (True↔False)
- เรียก toggle แล้วพิมพ์ quiet แล้ว toggle อีกครั้งแล้วพิมพ์อีก

---

## ตัวอย่าง

**Output:**

```text
True
False
```


---

## 💡 Hint

สลับด้วย if หรือ not

---

## Starter Code

```python
quiet = False

def toggle():
    # สลับค่า

toggle()
print(quiet)
toggle()
print(quiet)
```
