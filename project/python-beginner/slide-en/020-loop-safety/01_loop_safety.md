♪ Loop City ♫ Keep Loop safe

---

# break # stop Loop immediately```python
for i in range(10):
    if i == 5:
        break
    print(i)
```Results:```
0
1
2
3
4
```& Immediately out of log does not do around the rest

---

♪ continue across this round```python
for i in range(6):
    if i == 3:
        continue
    print(i)
```Results:```
0
1
2
4
5
```> ^3

---

¶ break vs continue ¶

▪ Command
----------------------
▪ Stop log immediately
♫ ♫ across this cycle ♫

---

♪ while True + break

Get Input Repeated Until Users"quit"```python
while True:
    word = input()
    if word == "quit":
        break
    print("You typed:", word)

print("Goodbye!")
```

```
hello → You typed: hello
world → You typed: world
quit  → Goodbye!
```---

#### continue filtering

Show only odd numbers:```python
for i in range(1, 11):
    if i % 2 == 0:
        continue     # ข้ามเลขคู่
    print(i)
```Results:```
1
3
5
7
9
```---

# Loop Safe Checklist #

- [ Tires screech ]
- [ ] Take a break. To stop in the middle.
- [ ] Use ^] To skip some round.
- [] Test with multiple inputs.