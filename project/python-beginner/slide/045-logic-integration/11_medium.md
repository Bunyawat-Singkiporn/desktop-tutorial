# 🧠 Logic Integration — ข้อ 11: รวมราคาจาก dict

**Difficulty:** 🟡 Medium

---

## โจทย์

สั่งอาหารจากเมนู dict

**เงื่อนไข:**

- `menu = {"a": 40, "b": 25}` `order = ["a", "b", "a"]`
- พิมพ์ยอดรวม

---

## ตัวอย่าง

**Output:**

```text
105
```


---

## 💡 Hint

วน order ดึงราคา

---

## Starter Code

```python
menu = {"a": 40, "b": 25}
order = ["a", "b", "a"]
total = 0
for item in order:
    total += menu[item]
print(total)
```
