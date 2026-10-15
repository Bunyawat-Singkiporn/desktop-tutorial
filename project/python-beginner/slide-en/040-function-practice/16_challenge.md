# 🧩 Function Practice — Q16: ตัวละคร HP

**Difficulty:** 🔴 Challenge

---

## Task

ตัวละครมีเลือด

**Requirements:**

- `create_player(name)` คืน `{"name": name, "hp": 100}`
- `take_damage(player, dmg)` ลด hp
- `is_alive(player)` คืน True ถ้า hp > 0
- `show_status(player)` พิมพ์ `Name: ... / HP: ...`
- สร้าง Hero โดน 40 แล้ว show และพิมพ์ is_alive

---

## Example

**Output:**

```text
Name: Hero
HP: 60
True
```


---

## Hint

dict เก็บสถานะ แก้ผ่าน key

---

## Starter Code

```python
def create_player(name):
    # Write your code here

def take_damage(player, dmg):
    # Write your code here

def is_alive(player):
    # Write your code here

def show_status(player):
    # Write your code here

p = create_player("Hero")
take_damage(p, 40)
show_status(p)
print(is_alive(p))
```
