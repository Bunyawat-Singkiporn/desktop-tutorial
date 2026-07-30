# 🔄 Review Lists — Review List

---

## All the things I learned

### Create and access
```python
fruits = ["apple", "banana", "mango"]
print(fruits[0])    # apple
print(fruits[-1])   # mango
print(len(fruits))  # 3
```

### Loop
```python
for fruit in fruits:
    print(fruit)

for i in range(len(fruits)):
    print(i, ":", fruits[i])
```

### Methods
```python
fruits.append("kiwi")        # add at the end
fruits.remove("banana")      # Delete by value
fruits[0] = "grape"          # Edit according to position
fruits.sort()                # Sort less→more
fruits.sort(reverse=True)    # Arrange more→less
```

---

## Pattern sums scores and averages

```python
scores = [80, 75, 90, 65, 88]
total = 0

for score in scores:
    total += score

average = total / len(scores)
print("Average:", average)
```

---

## Common errors

|problem|example|correct|
|-------|---------|-------|
|Index over size|`fruits[5]` (only 3)|Check with `len()`|
|Delete missing values.| `fruits.remove("grape")` |Check with `in` first.|
|Forgot index starts at 0|`fruits[1]` is the second one.|Remember: first one = `[0]`|

---

## Checklist before exam

- [ ] can create a list
- [ ] Access data with index (plus / minus).
- [ ] Can use `len()`
- [ ] loop through lists can be used in both ways.
- [ ] Can use `.append()`, `.remove()`, `.sort()`.
- [ ] filter and count with loop
