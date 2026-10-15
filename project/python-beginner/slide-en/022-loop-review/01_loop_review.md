♪ Loop Review • Review all types

---

♪ To sum up all the loops I've learned ♪

^ Loop ^
•--------------~--------
^forrange)
^For listen ^ ^ Through members of list ^
♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫
^nested ^oop
▪ Stop in the middle
^3

---

# Na-na na-na na-na #```python
scores = [85, 92, 78, 95, 88]
total = 0

for score in scores:
    total = total + score

average = total / len(scores)
print(f"Total: {total}")
print(f"Average: {average:.1f}")
```

```
Total: 438
Average: 87.6
```---

## Example combined: Get Input Repeat till you type 0.```python
total = 0
count = 0

while True:
    number = int(input())
    if number == 0:
        break
    total += number
    count += 1

print(f"Count: {count}, Total: {total}")
```---

#### Example 3:Pttern by the size```python
n = int(input())

for row in range(1, n + 1):
    for col in range(row):
        print("*", end="")
    print()
```

Input: `4`
```
*
**
***
****
```---

## Choose Loop How? !```
รู้จำนวนรอบ?
 YES → for range() หรือ for list
 NO  → while
       ต้องหยุดกลางคัน?  → ใช้ break
       ต้องข้ามบางรอบ?   → ใช้ continue
```
