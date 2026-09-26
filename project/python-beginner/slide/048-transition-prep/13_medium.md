# 🚀 Transition Prep — ข้อ 13: ผสม dict+ลูป

**Difficulty:** 🟡 Medium

---

## โจทย์

วน `progress = {"vars": 1, "loops": 1, "funcs": 1}` พิมพ์ `key: value`

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม)

## Output

3 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
vars: 1
loops: 1
funcs: 1
```


---

## 💡 Hint

ใช้ .items()

---

## Starter Code

```python
progress = {"vars": 1, "loops": 1, "funcs": 1}
for k, v in progress.items():
    print(f"{k}: {v}")
```
