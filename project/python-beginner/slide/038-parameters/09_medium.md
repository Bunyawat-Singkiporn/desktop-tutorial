# Practice Parameters — Question 8: บัตรสุขภาพในคลาสพละ

**Difficulty:** 🟡 Medium

---

## โจทย์

ครูพละให้นักเรียนกรอกน้ำหนักและส่วนสูง แล้วคำนวณ BMI

สร้าง `health_card(weight, height)` ที่พิมพ์ BMI  
สูตร: `weight / (height ** 2)` แสดงทศนิยม 2 ตำแหน่ง

---

## ตัวอย่าง

**Input:**
```
60
1.7
```

**Output:**
```
Health Card
Weight: 60.0 kg
Height: 1.7 m
BMI: 20.76
```

---

## Starter Code

```python
def health_card(weight, height):
    # Write your code here

weight = float(input())
height = float(input())
health_card(weight, height)
```
