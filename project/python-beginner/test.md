# Python Fundamentals Quiz

---

### Question 1: School Sign

**Problem description:** แสดงข้อความต่อไปนี้ให้ตรงตามตัวอย่าง

**Output format:**

```text
Welcome to Python Class
Let's Learn Together
```

**Hint:** ใช้ `print()` มากกว่า 1 ครั้ง

**Difficulty:** Easy

---

### Question 2: Pet Information

**Problem description:** สร้างตัวแปรชื่อ `pet_name` และ `pet_type` แล้วแสดงผลในรูปแบบ

```text
Milo is a Dog
```

**Hint:** เก็บข้อมูลในตัวแปรก่อน แล้วนำมาแสดงผล

**Difficulty:** Easy

---

### Question 3: Student Data

**Problem description:** สร้างตัวแปรดังต่อไปนี้

- ชื่อนักเรียน
- อายุ
- ส่วนสูง
- เป็นนักเรียนหรือไม่

จากนั้นแสดงผลค่าของตัวแปรทั้งหมด

**Hint:** ใช้ string, int, float และ bool

**Difficulty:** Easy

---

### Question 4: Dream Job

**Problem description:** รับชื่อและอาชีพในฝัน แล้วแสดงผลในรูปแบบ

```text
Anna wants to be a Doctor
```

**Input format:**

ข้อความ 2 บรรทัด

**Example input:**

```text
Anna
Doctor
```

**Example output:**

```text
Anna wants to be a Doctor
```

**Hint:** ใช้ `input()` 2 ครั้ง

**Difficulty:** Easy

---

### Question 5: Birthday Calculation

**Problem description:** รับอายุปัจจุบัน และแสดงอายุในอีก 3 ปีข้างหน้า

**Input format:**

จำนวนเต็ม 1 จำนวน

**Example input:**

```text
12
```

**Example output:**

```text
15
```

**Hint:** ใช้ `int()` ก่อนคำนวณ

**Difficulty:** Easy

---

### Question 6: Team Score

**Problem description:** รับคะแนนของทีม 2 รอบการแข่งขัน แล้วแสดงผลรวมคะแนน

**Input format:**

จำนวนเต็ม 2 จำนวน

**Example input:**

```text
35
40
```

**Example output:**

```text
75
```

**Hint:** ใช้เครื่องหมาย `+`

**Difficulty:** Medium

---

### Question 7: Sharing Pizza

**Problem description:** รับจำนวนชิ้นพิซซ่า และจำนวนเพื่อนที่ต้องแบ่งกันกิน แสดงจำนวนชิ้นที่แต่ละคนจะได้รับ

**Input format:**

จำนวนเต็ม 2 จำนวน

**Example input:**

```text
12
4
```

**Example output:**

```text
3.0
```

**Hint:** ใช้เครื่องหมาย `/`

**Difficulty:** Medium

**Starter Code:**

```python
pizza = int(input())
friends = int(input())

# Write your code here
```

---

### Question 8: Tall Student

**Problem description:** รับส่วนสูง

ถ้าส่วนสูงมากกว่า 150 ให้แสดง

```text
Tall
```

ถ้าไม่ถึง 150 ไม่ต้องแสดงอะไร

**Input format:**

จำนวนเต็ม 1 จำนวน

**Example input:**

```text
160
```

**Example output:**

```text
Tall
```

**Hint:** ใช้ `if`

**Difficulty:** Medium

**Starter Code:**

```python
height = int(input())

# Write your code here
```

---

### Question 9: Library Entry

**Problem description:** รับอายุ

ถ้าอายุตั้งแต่ 12 ปีขึ้นไป ให้แสดง

```text
Can Enter
```

ถ้าอายุน้อยกว่า 12 ปี ให้แสดง

```text
Cannot Enter
```

**Input format:**

จำนวนเต็ม 1 จำนวน

**Example input:**

```text
10
```

**Example output:**

```text
Cannot Enter
```

**Hint:** ใช้ `if` และ `else`

**Difficulty:** Medium

**Starter Code:**

```python
age = int(input())

# Write your code here
```

---

### Question 10: Buy a Notebook

**Problem description:** สมุดราคา 30 บาท

รับจำนวนเงินจากผู้ใช้

ถ้ามีเงินเพียงพอ

- แสดงคำว่า `Can Buy`
- แสดงเงินทอน

ถ้ามีเงินไม่เพียงพอ

- แสดงคำว่า `Need More Money`

**Input format:**

จำนวนเต็ม 1 จำนวน

**Example input:**

```text
50
```

**Example output:**

```text
Can Buy
20
```

**Hint:** ใช้การลบ และ `if/else`

**Difficulty:** Medium-Hard

**Starter Code:**

```python
money = int(input())
price = 30

# Write your code here
```