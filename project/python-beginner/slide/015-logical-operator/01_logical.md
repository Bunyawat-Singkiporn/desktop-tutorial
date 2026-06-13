# Logical Operators

บางครั้งเงื่อนไขเดียวไม่พอ

เราต้องรวมหลายเงื่อนไขเข้าด้วยกัน

มี 3 ตัวหลัก

and

or

not

----------------

and

ทุกเงื่อนไขต้องเป็นจริง

ตัวอย่าง

```python
age = 15
score = 80

if age >= 12 and score >= 50:
    print("Pass")
```

ถ้าอายุถึง

แต่คะแนนไม่ถึง

จะไม่เข้าเงื่อนไข

----------------

or

จริงแค่ตัวเดียวก็พอ

```python
if score > 90 or score < 20:
    print("Special")
```

----------------

not

กลับค่า

True -> False

False -> True

ตัวอย่าง

```python
is_raining = False

if not is_raining:
    print("Go Outside")
```