# ⚙️ Final Review — Question 3: Functions

**Difficulty:** 🟡 Medium

---

## โจทย์

สร้าง function `analyze(scores)` ที่ return dict ของผลวิเคราะห์

```python
{
    "total": ...,
    "average": ...,
    "passed": ...,    # จำนวนคน >= 50
    "grade": ...      # "A" >= 80, "B" >= 70, "C" >= 60, "F" < 60
}
```

**Output:**
```
total: 413
average: 82.6
passed: 5
grade: A
```

---

## Starter Code

```python
def analyze(scores):
    # Write your code here
    # return a dict with total, average, passed, grade

result = analyze([78, 85, 92, 70, 88])
for key, value in result.items():
    print(f"{key}: {value}")
```
