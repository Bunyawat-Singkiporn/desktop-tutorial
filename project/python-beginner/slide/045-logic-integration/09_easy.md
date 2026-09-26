# 🧠 Logic Integration — ข้อ 9: หาค่าสูงสุดเอง

**Difficulty:** 🟢 Easy

---

## โจทย์

หาค่ามากสุดโดยไม่ใช้ max()

**เงื่อนไข:**

- `nums = [3, 9, 2, 7]`
- เริ่มจากตัวแรก แล้วเทียบทีละตัว
- พิมพ์ค่ามากสุด

---

## Input

ไม่มี (กำหนดค่าในโปรแกรม)

## Output

1 บรรทัด

---

## ตัวอย่าง

**Output:**

```text
9
```


---

## Starter Code

```python
nums = [3, 9, 2, 7]
best = nums[0]
for n in nums:
    # อัปเดต best
print(best)
```
