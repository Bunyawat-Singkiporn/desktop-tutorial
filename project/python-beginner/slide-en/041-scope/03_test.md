# 🔭 Scope — Q3: local ทับชื่อ

**Difficulty:** 🟢 Easy

---

## Task

ตัวแปรชื่อเดียวกันคนละที่

**Requirements:**

- นอกฟังก์ชัน `x = 100`
- ใน `demo()` ตั้ง `x = 50` แล้วพิมพ์ `Inside: 50`
- หลังเรียกฟังก์ชันพิมพ์ `Outside: 100`

---

## Input

None (values are set in the program)

## Output

2 line(s)

---

## Example

**Output:**

```text
Inside: 50
Outside: 100
```


---

## Starter Code

```python
x = 100

def demo():
    # local x

demo()
print(f"Outside: {x}")
```
