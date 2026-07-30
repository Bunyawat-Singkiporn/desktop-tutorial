# 🔭 Practice Scope — Question 1: Predict the Output

**Difficulty:** 🟢 Easy

---

## Problem

Read the code below and predict its output without running it.
Then run the code to confirm your answer.

```python
x = 10

def change():
    x = 99
    print("Inside:", x)

change()
print("Outside:", x)
```

**Correct Output:**
```
Inside: 99
Outside: 10
```

---

## 💡 Question

Why is the `x` outside the function still `10` even though `change()` assigns `x = 99`?

---

## Starter Code

```python
x = 10

def change():
    x = 99
    print("Inside:", x)

change()
print("Outside:", x)
# Add a comment explaining why the x outside the function does not change
```
