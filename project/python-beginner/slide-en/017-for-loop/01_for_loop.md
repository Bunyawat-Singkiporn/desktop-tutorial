# 🔁 for Loop — Repeating Actions

---

## What is a Loop?

A loop makes the computer **repeat work** without writing the same code many times.

**Instead of writing this...**

```python
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
```

**We can write this instead!**

```python
for i in range(5):
    print("Hello")
```

---

## What is `range(5)`?

`range(5)` creates the numbers **0 through 4** — 5 rounds total.

> ⚠️ Always starts at **0** and stops before the given number

```python
for i in range(5):
    print(i)
```

**Output:**
```
0
1
2
3
4
```

---

## Summary

| Code | Meaning |
|------|---------|
| `for i in range(5):` | Loop 5 times (i = 0, 1, 2, 3, 4) |
| `    print(i)` | Print i each round |
