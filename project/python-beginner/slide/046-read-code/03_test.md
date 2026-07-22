# 🔍 Read Code — Question 2: Trace Variables

**Difficulty:** 🟡 Medium

---

## โจทย์

ไล่ค่าตัวแปรทีละขั้นแล้วเขียน trace table ลงใน comment
จากนั้นรันโค้ดเพื่อตรวจสอบ

```python
def mystery(items):
    count = 0
    total = 0
    for item in items:
        if item > 5:
            count += 1
            total += item
    return total, count

result = mystery([3, 8, 2, 9, 5, 7])
print(result)
```

---

## คำถาม

เติม trace table:

| รอบ | item | item > 5? | count | total |
|-----|------|-----------|-------|-------|
| 1 | 3 | False | 0 | 0 |
| 2 | 8 | True | ? | ? |
| 3 | 2 | ? | ? | ? |
| 4 | 9 | ? | ? | ? |
| 5 | 5 | ? | ? | ? |
| 6 | 7 | ? | ? | ? |

Output คือ: ?

---

## Starter Code

```python
# ตอบ trace table ใน comment ก่อน

def mystery(items):
    count = 0
    total = 0
    for item in items:
        if item > 5:
            count += 1
            total += item
    return total, count

result = mystery([3, 8, 2, 9, 5, 7])
print(result)
```
