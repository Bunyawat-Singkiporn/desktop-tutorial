# 🔀 elif — multiple conditions

---

## Why must there be an elif?

`if / else` has only **2 options**.

```
✅ Passed
❌ Not passed
```

But sometimes we have **more than 2 cases** such as a student's grade:

```
A → high score
B → Medium
C → enough to pass
F → Fail
```

So we can use `elif` to keep adding conditions.

---

## writing style

```python
if condition 1:
    # done when condition 1 is true

elif condition 2:
    # Do it when condition 2 is true.

elif condition 3:
    # done when condition 3 is true

else:
    # Do it when none of the conditions are true.
```

---

## Example program — graded

```python
score = int(input())

if score >= 80:
    print("A")
elif score >= 70:
    print("B")
elif score >= 60:
    print("C")
else:
    print("F")
```

---

## How it works

> Python checks conditions **from top to bottom**
> When you encounter a true condition → **Immediately stop** Do not continue checking.

| Input (score) | Output |
|---------------|--------|
| `85` | `A` |
| `72` | `B` |
| `61` | `C` |
| `45` | `F` |