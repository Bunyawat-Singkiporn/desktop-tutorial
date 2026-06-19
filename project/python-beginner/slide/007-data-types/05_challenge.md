# 🔥 Practice: Data Types — Question 4: Game Status

**Difficulty:** 🔴 Hard

---

## โจทย์

สร้างโปรแกรมแสดงสถานะเกมโดยใช้ **ครบทั้ง 4 data types** และแสดง type ของแต่ละตัวแปรด้วย

**ข้อมูลที่ต้องเก็บ:**
| Variable | ค่า | Type |
|----------|-----|------|
| `player_name` | `"Hero"` | str |
| `player_level` | `5` | int |
| `player_hp` | `87.5` | float |
| `is_boss_defeated` | `False` | bool |

**Output:**
```
=== Game Status ===
Player  : Hero       (str)
Level   : 5          (int)
HP      : 87.5       (float)
Boss    : False      (bool)
```

---

## 💡 Hint

ใช้ `type(x).__name__` เพื่อได้แค่ชื่อ type เช่น `int` (ไม่มี `<class '...'>`)

```python
print(type(42).__name__)    # int
```

---

## Starter Code

```python
player_name = "Hero"
player_level = 5
player_hp = 87.5
is_boss_defeated = False

# Print each with its type name
```
