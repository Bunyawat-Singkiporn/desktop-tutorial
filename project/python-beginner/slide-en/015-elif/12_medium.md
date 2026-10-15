# 🍽️ elif — Q10: ดาวรีวิวร้านอาหาร

**Difficulty:** 🟡 Medium

---

## Task

แอปรีวิวร้านอาหารแปลงจำนวนดาวเป็นข้อความสั้นๆ

เขียนโปรแกรมรับจำนวนดาว (1–5) แล้วบอกระดับรีวิว

**Rules:**

- ดาว `== 5` → `Excellent`
- ดาว `== 4` → `Good`
- ดาว `== 3` → `Average`
- นอกนั้น → `Poor`

---

## Input

จำนวนดาวเป็นจำนวนเต็ม 1 บรรทัด

## Output

2 บรรทัด — จำนวนดาว และข้อความรีวิว

---

## Example

**Input:**

```text
4
```

**Output:**

```text
Stars  : 4
Review : Good
```

---

## Hint

ข้อนี้เทียบด้วย `==` ไม่ใช่ `>=` เพราะแต่ละค่าตรงกับข้อความคนละอัน

---

## Starter Code

```python
stars = int(input())

# Write your code here
```
