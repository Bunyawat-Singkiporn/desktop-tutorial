# Nasted Loops #

---

# Nasted Loop #

"Nested Loop* is the loop inside the other loop.```python
for i in range(3):        # Loop นอก — วน 3 รอบ
    for j in range(3):    # Loop ใน — วน 3 รอบ ทุกครั้ง
        print(i, j)
```Results:```
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
```> Loop

---

♪ The total count ♪```
Loop นอก 3 รอบ × Loop ใน 4 รอบ = 12 ครั้งรวม
```

```python
for row in range(3):
    for col in range(4):
        print("*", end="")
    print()    # ขึ้นบรรทัดใหม่
```Results:```
****
****
****
```---

#### Example:```python
for row in range(1, 6):
    for col in range(row):
        print("*", end="")
    print()
```Results:```
*
**
***
****
*****
```^rangekrow)

---

#### Example:```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end="\t")
    print()
```Results:```
1	2	3	
2	4	6	
3	6	9	
```---

♪ To sum

▪ About ▪
•--------
♫ Loop outside ♫ N lap ▪
^ Loop in ^ circuit M around every time loop outside ^
^ including N× M times ▪
Print In One line
□ Free