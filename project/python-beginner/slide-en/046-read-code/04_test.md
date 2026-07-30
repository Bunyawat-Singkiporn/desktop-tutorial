# 💬 Read Code — Question 3: Explain the Code

**Difficulty:** 🟡 Medium

---

## Problem

Read the code below and explain in the comment block:
1. What data the program receives.
2. How it processes the data.
3. What it displays.

```python
def process(data):
    result = {}
    for item in data:
        first_letter = item[0].upper()
        if first_letter in result:
            result[first_letter].append(item)
        else:
            result[first_letter] = [item]
    return result

words = ["apple", "banana", "avocado", "blueberry", "cherry", "apricot"]
grouped = process(words)
for letter, group in grouped.items():
    print(f"{letter}: {group}")
```

---

## Starter Code

```python
# Explain the program below:
# Input:
# Processing:
# Output:

def process(data):
    result = {}
    for item in data:
        first_letter = item[0].upper()
        if first_letter in result:
            result[first_letter].append(item)
        else:
            result[first_letter] = [item]
    return result

words = ["apple", "banana", "avocado", "blueberry", "cherry", "apricot"]
grouped = process(words)
for letter, group in grouped.items():
    print(f"{letter}: {group}")
```
