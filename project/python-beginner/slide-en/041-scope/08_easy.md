# 🔭 Scope — Q8: นับด้วย global

**Difficulty:** 🟢 Easy

---

## Task

นับครั้งที่กดปุ่ม

**Requirements:**

- มี `count = 0` นอกฟังก์ชัน
- `add_one()` ใช้ `global count` แล้ว `count += 1`
- เรียก 2 ครั้ง แล้วพิมพ์ count

---

## Input

None (values are set in the program)

## Output

1 line(s)

---

## Example

**Output:**

```text
2
```


---

## Starter Code

```python
count = 0

def add_one():
    # ใช้ global

add_one()
add_one()
print(count)
```
