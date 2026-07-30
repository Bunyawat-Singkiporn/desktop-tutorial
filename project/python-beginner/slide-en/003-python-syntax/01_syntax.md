# 📐 Python Syntax — Rules for Writing Code

---

## What is Syntax?

**Syntax** means the **writing rules** of the Python language.

Just like English has rules:
- A sentence needs a subject + verb
- Spelling and punctuation must be correct

Python has rules too — break a rule → **Error!**

---

## Rule 1: Uppercase / Lowercase Matters a Lot

Python is **case sensitive**.

| ❌ Wrong | ✅ Correct | Error you get |
|----------|------------|---------------|
| `Print("Hello")` | `print("Hello")` | `NameError` |
| `PRINT("Hello")` | `print("Hello")` | `NameError` |

> **All Python commands always use lowercase**

---

## Rule 2: Marks Must Come in Pairs

| Every... | Must have... | Wrong example | Correct example |
|----------|--------------|---------------|-----------------|
| `(` | closing `)` | `print("Hi"` | `print("Hi")` |
| opening `"` | closing `"` | `print("Hi)` | `print("Hi")` |

---

## Rule 3: Indentation

Normal code **must not have leading spaces**:

```python
print("Line 1")    ← correct
print("Line 2")    ← correct
```

```python
print("Line 1")    ← correct
  print("Line 2")  ← wrong! IndentationError
```

> Indentation will have special meaning when you learn `if` and `for`

---

## Real Error Examples

```python
Print("Hello")
```
```
NameError: name 'Print' is not defined
```
> Cause: capital `P` — Python does not know `Print`

---

```python
print("Hello"
```
```
SyntaxError: '(' was never closed
```
> Cause: missing closing `)`

---

```python
  print("Hello")
```
```
IndentationError: unexpected indent
```
> Cause: unnecessary leading space

---

## Summary of 3 Rules

| # | Rule | Remember |
|---|------|----------|
| 1 | Always lowercase | `print` not `Print` |
| 2 | Marks in pairs | `(` has `)`, `"` has `"` |
| 3 | No leading spaces | Start at the beginning of the line |
