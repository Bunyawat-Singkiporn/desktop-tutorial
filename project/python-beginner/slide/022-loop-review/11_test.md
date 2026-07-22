# 🏆 Practice: Loop Review — Question 10: All Pass Check

**Difficulty:** 🟡 Medium

---

## โจทย์

ตรวจว่าทุกคนในชั้นเรียนผ่านหรือไม่ (>= 60)

```python
scores = [80, 90, 75, 65, 88]   # ทุกคนผ่าน
```

**Output:**
```
All passed!
```

```python
scores = [80, 55, 75, 65, 88]   # มีคนไม่ผ่าน
```

**Output:**
```
Someone failed.
```

---

## 💡 Hint

- ตั้ง `all_pass = True` ก่อน
- ถ้าเจอคะแนนที่ < 60 → `all_pass = False` แล้ว `break`

---

## Starter Code

```python
scores = [80, 90, 75, 65, 88]
all_pass = True

for s in scores:
    # If s < 60, set all_pass to False and break

if all_pass:
    print("All passed!")
else:
    print("Someone failed.")
```
