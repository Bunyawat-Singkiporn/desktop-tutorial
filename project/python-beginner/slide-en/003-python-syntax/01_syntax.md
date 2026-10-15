# 📐 Python Syntax — Coding rules

---

## What is syntax?

**Syntax** is Python’s **writing rules**.

Like Thai has rules:
- Sentences need subject + verb
- Tone marks must be correct

Python has rules too — break them → **Error!**

---

## Rule 1: Uppercase and lowercase matter

Python is **case sensitive**.

| ❌ Wrong | ✅ Correct | Error |
|--------|--------|------------|
| `Print("Hello")` | `print("Hello")` | `NameError` |
| `PRINT("Hello")` | `print("Hello")` | `NameError` |

> **Python commands are always lowercase**

---

## Rule 2: Symbols must come in pairs

| Every... | needs... | Wrong | Correct |
|--------|----------|------------|------------|
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

> Indentation becomes important when you learn `if` and `for`

---

## Real error examples

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
> Cause: unnecessary leading spaces

---

## Three rules summary

| # | Rule | Remember |
|---|----|----|
| 1 | Lowercase commands | `print` not `Print` |
| 2 | Matched symbols | `(` with `)`, `"` with `"` |
| 3 | No leading spaces | Start at column zero |
