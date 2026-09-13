# Practice Function — Medium: Password Check

**Difficulty:** 🟡 Medium

---

## Task

Create `is_strong(password)` that returns `True` if:
- length >= 8 **and**
- has at least one digit

Otherwise return `False`.

Main program asks for a password and prints `Strong` or `Weak`.

> Combines: return + input + if + for + str

---

## Example

**Input:**
```
hello123
```

**Output:**
```
Strong
```

---

## 💡 Hint

Check digits with `for ch in password:` and `ch.isdigit()`

---

## Starter Code

```python
def is_strong(password):
    # Write your code here

password = input()
if is_strong(password):
    print("Strong")
else:
    print("Weak")
```
