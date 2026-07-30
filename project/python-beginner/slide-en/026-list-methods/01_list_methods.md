# 🛠️ List Methods — Managing data in Lists

---

## List is Mutable

List can **change** after creation.

---

## Edit data directly (Modify by Index)

```python
fruits = ["apple", "banana", "mango"]
fruits[1] = "orange"
print(fruits)  # ['apple', 'orange', 'mango']
```

---

## .append() — add data to the end

```python
fruits = ["apple", "banana"]
fruits.append("mango")
print(fruits)  # ['apple', 'banana', 'mango']
```

---

## .remove() — remove data based on value

```python
fruits = ["apple", "banana", "mango"]
fruits.remove("banana")
print(fruits)  # ['apple', 'mango']
```

> If the specified value does not exist in the list, a **ValueError** will occur.

---

## .sort() — sort data

Sort from **lowest to highest** (default):
```python
numbers = [5, 2, 9, 1, 7]
numbers.sort()
print(numbers)  # [1, 2, 5, 7, 9]
```

Arranged from **highest to lowest**:
```python
numbers.sort(reverse=True)
print(numbers)  # [9, 7, 5, 2, 1]
```

---

## Summary Methods

| Method |duty|example|
|--------|---------|---------|
| `list[i] = x` |Edit i position| `fruits[0] = "grape"` |
| `.append(x)` |add at the end| `fruits.append("kiwi")` |
| `.remove(x)` |Delete by value| `fruits.remove("apple")` |
| `.sort()` |Sort less→more| `numbers.sort()` |
| `.sort(reverse=True)` |Arrange more→less| `numbers.sort(reverse=True)` |

---

## ExampleProgram

```python
scores = [85, 72, 90, 68, 95]
scores.append(80)        # Add a new score
scores.remove(68)        # Delete lowest score
scores.sort(reverse=True)  # Sort by descending
print(scores)
```
