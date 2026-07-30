# ✨ Code Readability — Easy-to-Read Code

---

## What Makes Code Good?

Good code should not only **run**—it should also be **easy to understand**.

---

## Use Meaningful Names

```python
# ❌ Unclear
x = 75
y = x >= 50

# ✅ Clear at a glance
score = 75
is_passed = score >= 50
```

---

## Use Correct Indentation

```python
# ❌ Incorrect indentation
def greet():
print("Hello")     # ← This line should be indented by 4 spaces

# ✅ Correct
def greet():
    print("Hello")
```

---

## Add Comments Only When Needed

```python
# ❌ Commenting every line creates clutter
x = 10       # Set x to 10
y = 20       # Set y to 20
z = x + y    # Add x and y

# ✅ Comment only where the reason needs explanation
DISCOUNT_RATE = 0.1   # 10% discount for all items
price = 200
final_price = price * (1 - DISCOUNT_RATE)
```

---

## Use f-Strings Instead of Joining Strings

```python
# ❌ Hard to read
print("Name: " + name + ", Age: " + str(age))

# ✅ Easy to read
print(f"Name: {name}, Age: {age}")
```

---

## Split Long Code into Functions

```python
# ❌ Dense, lengthy code
n = int(input())
t = 0
for i in range(n):
    t += i
print(t)

# ✅ Clearly separated
def get_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total

n = int(input())
print(get_sum(n))
```

---

## Five Clean Code Principles

1. Use meaningful names.
2. Always indent code correctly.
3. Add comments only for complex parts.
4. Use f-strings.
5. Create a separate function for each task.
