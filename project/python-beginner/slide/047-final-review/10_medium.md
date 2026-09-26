# 🏁 Final Review — ข้อ 10: นับใน dict

**Difficulty:** 🟡 Medium

---

## โจทย์

นับตัวอักษรใน list `letters = ["a", "b", "a", "c", "a"]` แล้วพิมพ์จำนวน `a`

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม)

## Output

1 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
3
```


---

## 💡 Hint

แบบนับความถี่

---

## Starter Code

```python
letters = ["a", "b", "a", "c", "a"]
freq = {}
for ch in letters:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1
print(freq["a"])
```
