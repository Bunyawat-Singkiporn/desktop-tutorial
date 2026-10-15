# 🧩 Function Practice — Q5: ระบบคะแนน dict

**Difficulty:** 🔴 Challenge

---

## Task

เก็บคะแนนนักเรียนใน dict

**Requirements:**

- `add_score(scores, name, score)` ใส่คะแนนแล้วคืน scores
- `get_average(scores)` คืนค่าเฉลี่ยจาก `.values()`
- เพิ่ม Alice=80 Bob=100 แล้วพิมพ์ค่าเฉลี่ย

---

## Example

**Output:**

```text
90.0
```


---

## Hint

ใช้ .values() รวมคะแนน

---

## Starter Code

```python
def add_score(scores, name, score):
    # Write your code here

def get_average(scores):
    # Write your code here

scores = {}
scores = add_score(scores, "Alice", 80)
scores = add_score(scores, "Bob", 100)
print(get_average(scores))
```
