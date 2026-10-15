# 🧊 elif — Q8: สถานะตู้เย็น

**Difficulty:** 🟡 Medium

---

## Task

เซนเซอร์ตู้เย็นแจ้งสถานะตามอุณหภูมิภายใน

เขียนโปรแกรมรับอุณหภูมิ แล้วแสดงอุณหภูมิกับสถานะ

**Rules:**

- อุณหภูมิ `<= -10` → `Deep Freeze`
- อุณหภูมิ `<= 0` → `Freezing`
- อุณหภูมิ `<= 5` → `Chilled`
- มากกว่านั้น → `Too Warm`

---

## Input

อุณหภูมิเป็นจำนวนเต็ม 1 บรรทัด (อาจติดลบได้)

## Output

2 บรรทัด — อุณหภูมิ และสถานะ

---

## Example

**Input:**

```text
-3
```

**Output:**

```text
Temp   : -3
Status : Freezing
```

---

## Hint

ครั้งนี้เรียงจากค่าน้อยไปมาก เพราะใช้ `<=`
เริ่มจากช่วงที่เย็นสุดก่อน

---

## Starter Code

```python
temp = int(input())

# Write your code here
```
