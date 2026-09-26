# 🏁 Final Review — ข้อ 15: เครื่องคิดเลขเมนู

**Difficulty:** 🔴 Challenge

---

## โจทย์

รับตัวเลือก 1=บวก 2=คูณ แล้วรับ a, b พิมพ์ผล

**เงื่อนไข:**

- มีฟังก์ชัน `add` และ `mul`

---

## Input

ดูตัวอย่าง

## Output

1 บรรทัด

---

## ตัวอย่าง

**Input:**

```text
2
3
4
```

**Output:**

```text
12
```


---

## 💡 Hint

เลือกฟังก์ชันตามเมนู

---

## Starter Code

```python
def add(a, b):
    return a + b

def mul(a, b):
    return a * b

op = int(input())
a = int(input())
b = int(input())
if op == 1:
    print(add(a, b))
else:
    print(mul(a, b))
```
