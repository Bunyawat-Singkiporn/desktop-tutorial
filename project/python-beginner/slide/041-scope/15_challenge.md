# 🔭 Scope — ข้อ 15: คลังไอเทม

**Difficulty:** 🔴 Challenge

---

## โจทย์

คลังไอเทมเป็น list global

**เงื่อนไข:**

- `items = []`
- `add_item(name)` append ด้วย global
- เพิ่ม Potion กับ Sword แล้วพิมพ์ items

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม)

## Output

1 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
['Potion', 'Sword']
```


---

## 💡 Hint

append บน list global

---

## Starter Code

```python
items = []

def add_item(name):
    # global

add_item("Potion")
add_item("Sword")
print(items)
```
