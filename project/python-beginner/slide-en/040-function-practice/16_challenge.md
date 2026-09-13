# 🔥 Practice Function — Challenge: RPG Player

**Difficulty:** 🔴 Hard

---

## Task

Build a simple RPG player system with **4 functions**:

| Function | Job |
|----------|-----|
| `create_player(name)` | return `{"name": name, "hp": 100}` |
| `take_damage(player, dmg)` | reduce hp (not below 0) |
| `is_alive(player)` | return True if hp > 0 |
| `show_status(player)` | print name, hp, Alive/Dead |

---

## Example

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
