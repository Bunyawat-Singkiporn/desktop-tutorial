# 🐛 Debugging — Q7: ตรวจความยาว list

**Difficulty:** 🟡 Medium

---

## Task

จะอ่านสมาชิกตัวสุดท้าย ต้องมีข้อมูลก่อน

**Requirements:**

- รับ n แล้วอ่าน n จำนวนเต็มเก็บใน list
- ถ้า list ว่างพิมพ์ `Empty` ไม่งั้นพิมพ์ตัวสุดท้าย

---

## Input

See example

## Output

1 บรรทัด

---

## Example

**Input:**

```text
0
```

**Output:**

```text
Empty
```


---

## 💡 Hint

ดู len ก่อนใช้ index

---

## Starter Code

```python
n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

# เช็กว่าง
```
