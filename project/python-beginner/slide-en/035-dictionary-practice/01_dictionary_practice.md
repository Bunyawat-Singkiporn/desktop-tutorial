# 💾 Dictionary Practice — Practice Using Dictionaries

---

## Review: Dictionaries Covered So Far

| Skill | Example |
|-------|---------|
| Create | `d = {"a": 1, "b": 2}` |
| Access | `d["a"]` → `1` |
| Add/change | `d["c"] = 3` |
| Update | `d.update({"a": 10})` |
| Delete | `del d["b"]` |
| Loop | `for k, v in d.items():` |

---

## Common Pattern — Frequency Count

```python
words = ["cat", "dog", "cat", "bird", "dog", "cat"]
count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)
# {'cat': 3, 'dog': 2, 'bird': 1}
```

---

## Pattern — Check Answers

```python
answers = {"q1": "A", "q2": "C", "q3": "B"}
user_answer = input("q1: ")

if user_answer == answers["q1"]:
    print("Correct!")
else:
    print("Wrong!")
```

---

## Program Example — Product Prices

```python
prices = {"apple": 15, "banana": 8, "mango": 25}
total = 0

for item, price in prices.items():
    print(f"{item}: {price} baht")
    total += price

print(f"Total: {total} baht")
```
