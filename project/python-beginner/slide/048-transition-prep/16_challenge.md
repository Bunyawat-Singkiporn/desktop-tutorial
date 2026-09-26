# 🚀 Transition Prep — ข้อ 16: โจทย์รวมท้าย Phase 1

**Difficulty:** 🔴 Challenge

---

## โจทย์

รับจำนวนนักเรียน n แล้วอ่านชื่อกับคะแนน สร้าง dict แล้วพิมพ์คนที่ได้คะแนนสูงสุดแบบเทียบเอง (ห้าม max)

**เงื่อนไข:**

- พิมพ์ `Top: <name> <score>`

---

## Input

ดูตัวอย่าง

## Output

1 บรรทัด

---

## ตัวอย่าง

**Input:**

```text
3
Ann
80
Bee
95
Cat
70
```

**Output:**

```text
Top: Bee 95
```


---

## 💡 Hint

เก็บใน dict แล้วไล่เทียบ

---

## Starter Code

```python
n = int(input())
data = {}
for i in range(n):
    name = input()
    score = int(input())
    data[name] = score

best_name = ""
best_score = -1
for name, score in data.items():
    if score > best_score:
        best_score = score
        best_name = name
print(f"Top: {best_name} {best_score}")
```
