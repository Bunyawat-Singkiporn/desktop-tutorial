# 🔥 Practice Function — Question 4: Score System

**Difficulty:** 🔴 Hard

---

## โจทย์

สร้างระบบคะแนนโดยใช้ functions แยกส่วน:

| Function | หน้าที่ |
|----------|---------|
| `add_score(scores, name, score)` | เพิ่มคะแนนลงใน dict |
| `get_average(scores)` | return ค่าเฉลี่ยของค่าทั้งหมดใน dict |
| `get_top(scores)` | return ชื่อและคะแนนสูงสุด |
| `show_all(scores)` | แสดงทุกคนพร้อมคะแนน |

**ตัวอย่าง Output:**
```
Alice: 85
Bob: 92
Charlie: 78
Average: 85.0
Top: Bob (92)
```

---

## Starter Code

```python
def add_score(scores, name, score):
    # Write your code here

def get_average(scores):
    # Write your code here

def get_top(scores):
    # Write your code here

def show_all(scores):
    # Write your code here

scores = {}
add_score(scores, "Alice", 85)
add_score(scores, "Bob", 92)
add_score(scores, "Charlie", 78)

show_all(scores)
print(f"Average: {get_average(scores):.1f}")
top_name, top_score = get_top(scores)
print(f"Top: {top_name} ({top_score})")
```
