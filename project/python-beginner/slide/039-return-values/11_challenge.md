# 🔥 Practice Return — Challenge: คำยาวไหม?

**Difficulty:** 🔴 Hard

---

## โจทย์

สร้าง 2 functions:
1. `word_len(text)` — return ความยาวข้อความ
2. `is_long(text)` — return `True` ถ้าความยาว >= 8 ไม่งั้น `False`
   (ให้เรียก `word_len` ข้างใน)

รับคำจาก `input` แล้วพิมพ์ความยาว + `Long` หรือ `Short`

> ผสมความรู้: return + function ซ้อน + input + if + len

---

## ตัวอย่าง

**Input:**
```
pythonista
```

**Output:**
```
Length: 10
Long
```

---

## Starter Code

```python
def word_len(text):
    # Write your code here

def is_long(text):
    # Write your code here

text = input()
print(f"Length: {word_len(text)}")
if is_long(text):
    print("Long")
else:
    print("Short")
```
