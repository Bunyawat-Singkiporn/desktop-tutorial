# 🏁 Final Review — ข้อ 11: set สมาชิก

**Difficulty:** 🟡 Medium

---

## โจทย์

มี `vip = {"Ann", "Ben"}` รับชื่อ แล้วพิมพ์ `VIP` หรือ `Guest`

---

## Input

ดูตัวอย่าง

## Output

1 บรรทัด

---

## ตัวอย่าง

**Input:**

```text
Ann
```

**Output:**

```text
VIP
```


---

## 💡 Hint

ใช้ in

---

## Starter Code

```python
vip = {"Ann", "Ben"}
name = input()
if name in vip:
    print("VIP")
else:
    print("Guest")
```
