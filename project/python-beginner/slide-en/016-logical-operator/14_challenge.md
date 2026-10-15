# I don't know what to do

difficulty:

---

♪ Task

The hotel charges the room for $1,500 on the base and then two fines.

Long-term membership discount.

▪ Prescription
•--------
I'm a member.
▪ In addition

A special day.

▪ Add to
•----------
It's a holiday.
▪ In addition

Total number = (1500 × . . . . . . . . . . . . . .

Program a return amount of membership, day type, and holiday status, and then issue a room certificate.

---

♪ Input

4 lines night, membership (1) type day

♪ Output

The room's bill in the frame shows a break price, a discount, extra and total.

---

## Example

**Input:*```text
4
1
weekday
0
```

**Output:**

```text
============================
         HOTEL
============================
Stay     : 6000
Discount : 300
Surcharge: 0
Total    : 5700
============================
```---

♪ Hint

It's the last night's rent.
And then use the first set of ^if/else with ^and) to find a second discount with ^or

---

♪ Starter Code```python
nights = int(input())
is_member = int(input())
day = input()
is_holiday = int(input())

# Write your code here
```
