# 🔥 Practice: Data Types — Question 4: Game Status

**Difficulty:** 🔴 Hard

---

## Problem

Create a program that shows game status using **all 4 data types**, and also show the type of each variable.

**Data to store:**
| Variable | Value | Type |
|----------|-------|------|
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

Use `type(x).__name__` to get just the type name, e.g. `int` (without `<class '...'>`)

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
