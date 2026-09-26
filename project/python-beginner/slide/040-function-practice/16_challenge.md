# 🧩 Function Practice — ข้อ 16: ตัวละคร HP

**Difficulty:** 🔴 Challenge

---

## โจทย์

ตัวละครมีเลือด

**เงื่อนไข:**

- `create_player(name)` คืน `{"name": name, "hp": 100}`
- `take_damage(player, dmg)` ลด hp
- `is_alive(player)` คืน True ถ้า hp > 0
- `show_status(player)` พิมพ์ `Name: ... / HP: ...`
- สร้าง Hero โดน 40 แล้ว show และพิมพ์ is_alive

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม / เรียกฟังก์ชันในโค้ด)

## Output

3 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
Name: Hero
HP: 60
True
```


---

## 💡 Hint

dict เก็บสถานะ แก้ผ่าน key

---

## Starter Code

```python
def create_player(name):
    # เขียนโค้ดตรงนี้

def take_damage(player, dmg):
    # เขียนโค้ดตรงนี้

def is_alive(player):
    # เขียนโค้ดตรงนี้

def show_status(player):
    # เขียนโค้ดตรงนี้

p = create_player("Hero")
take_damage(p, 40)
show_status(p)
print(is_alive(p))
```
