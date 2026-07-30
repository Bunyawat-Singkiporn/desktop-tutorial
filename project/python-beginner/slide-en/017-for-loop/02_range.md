# 📐 range() — Setting a Number Range

---

## Forms

```
range(start, stop)
range(start, stop, step)
```

| Parameter | Meaning |
|-----------|---------|
| `start` | Start at this number |
| `stop` | Stop **before** this number |
| `step` | Jump size each time (default = 1) |

---

## Example — start and stop

```python
for i in range(1, 6):
    print(i)
```

**Output:**
```
1
2
3
4
5
```

> Starts at 1, stops before 6

---

## Example — with step

```python
for i in range(2, 11, 2):
    print(i)
```

**Output:**
```
2
4
6
8
10
```

> Starts at 2, stops before 11, jumps by 2

---

## Comparison

| range | Result |
|-------|--------|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(2, 11, 2)` | 2, 4, 6, 8, 10 |
