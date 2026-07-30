# 🐛 Debugging Loops — Fix bugs in Loops.

---

## Bug 1: Off-by-One Error

```python
# ❌ Wanted 1–5 but got only 1–4
for i in range(1, 5):
    print(i)

# ✅ Correct
for i in range(1, 6):
    print(i)
```

> `range(1, 5)` = 1, 2, 3, 4 — **not including 5**
> Requires 1–5 `range(1, 6)` required.

---

## Bug 2: Infinite Loop

```python
# ❌ Forgot to update count → Non-stop loop!
count = 1
while count <= 5:
    print(count)

# ✅ Correct
count = 1
while count <= 5:
    print(count)
    count = count + 1   # ← This line must be present.
```

---

## Bug 3: Indent is wrong.

```python
# ❌ print outside loop — print only once
for i in range(3):
    pass
print(i)

# ✅ Fix: put indent in loop
for i in range(3):
    print(i)
```

---

## Bug 4: Use the name List instead of loop variables.

```python
names = ["Alice", "Bob", "Charlie"]

# ❌ Incorrect: Use names instead of name
for name in names:
    print(names)   # Show all lists every round!

# ✅ Correct
for name in names:
    print(name)    # Show each name
```

---

## Debug Loop Method

Temporarily add `print`, look at the values ​​each cycle:

```python
for i in range(5):
    print(f"[debug] i = {i}")   # ← Delete when finished.
    total = total + i
```

---

## Summary of bugs to be careful of

| Bug |signal|Solution|
|-----|--------|--------|
| Off-by-one |Less effective/more than 1 cycle|Check the value in `range()`|
| Infinite loop |The program freezes.|Verify that variables have been changed.|
|Indent is wrong|The code behaves strangely.|Check leading space|
|Wrong name|Strange Output|Check variable names|
