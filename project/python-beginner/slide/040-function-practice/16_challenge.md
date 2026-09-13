# 🔥 Practice Function — Challenge: ตัวละครในเกม RPG

**Difficulty:** 🔴 Hard

---

## โจทย์

ทำระบบตัวละครเกมง่ายๆ ด้วย **4 functions**:

| Function | หน้าที่ |
|----------|---------|
| `create_player(name)` | return dict `{"name": name, "hp": 100}` |
| `take_damage(player, dmg)` | ลด hp (ไม่ต่ำกว่า 0) |
| `is_alive(player)` | return `True` ถ้า hp > 0 |
| `show_status(player)` | แสดงชื่อ + hp + Alive/Dead |

รับชื่อผู้เล่นและดาเมจจาก `input` แล้วแสดงสถานะหลังโดนตี

---

## ตัวอย่าง

**Input:**
```
Hero
30
```

**Output:**
```
=== Player Status ===
Name: Hero
HP: 70
Status: Alive
```

**Input:**
```
Hero
120
```

**Output:**
```
=== Player Status ===
Name: Hero
HP: 0
Status: Dead
```

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

name = input()
dmg = int(input())
player = create_player(name)
take_damage(player, dmg)
show_status(player)
```
