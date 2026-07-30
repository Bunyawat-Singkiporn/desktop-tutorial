# 🔁 Review — Review Everything

---

## What You Learned Across 11 Weeks

| Week | Topic | Most important |
|------|-------|----------------|
| 1 | What is Python | `print("Hello")` |
| 2 | Environment | Read Errors → fix them |
| 3 | Syntax | lowercase, paired marks, no extra indent |
| 4 | Comments | `# explain the code` |
| 5 | Variables | `name = "Alice"` |
| 6 | Naming Rules | snake_case, meaningful names |
| 7 | Data Types | int, float, str, bool |
| 8 | Type Conversion | `int()`, `float()`, `str()` |
| 9 | Input | `name = input()` |
| 10 | Output Formatting | `f"Hello {name}"` |
| 11 | Operators | `+`, `-`, `*`, `/`, `%`, `**` |

---

## Example Program That Combines Everything

```python
# Get data from the user
name = input()
age = int(input())
price = float(input())

# Calculate
price_with_vat = price * 1.07

# Display results
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Price + VAT: {price_with_vat:.2f} baht")
```

Input:
```
Alice
13
100
```

Output:
```
Name: Alice
Age: 13
Price + VAT: 107.00 baht
```

---

## Basic Program Pattern

```
1. Get input     → input()
2. Process       → operators, variables
3. Show output   → print() / f-string
```

---

## Checklist Before Submitting

- [ ] Variable names use snake_case
- [ ] Convert `input()` with `int()` or `float()` before calculating
- [ ] Use f-strings for output that includes variables
- [ ] Add comments explaining important parts
- [ ] Test with several different inputs

---

## Common Mistakes

| Mistake | Cause | How to fix |
|---------|-------|------------|
| `NameError` | Used `Print` instead of `print` | Always use lowercase |
| `TypeError` | `"5" + 5` | Convert with `int()` or `str()` |
| `SyntaxError` | Missing `)` or `"` | Check that marks come in pairs |

---

## Congratulations! 🎉

You have finished the Python basics! Next lessons will cover:

- **Even / Odd** — `%` and `if/else`
- **elif** — multiple conditions
- **Logical Operators** — `and`, `or`, `not`
- **For Loop** — repeating
