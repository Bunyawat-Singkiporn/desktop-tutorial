# 🖥️ Python Environment — Getting started with code

---

## What is an editor?

An **editor** is a program for writing code.

Like a **notebook** 📒 for programmers, with features that make coding easier.

| Editor | Notes |
|--------|--------|
| **VS Code** | Works with any language ✅ (recommended) |
| PyCharm | Python-focused |
| IDLE | Bundled with Python |

---

## How to run Python code

### Method 1: ▶ button in VS Code
1. Open a `.py` file
2. Click **▶ Run** at the top right
3. See output in the **Terminal** at the bottom

### Method 2: Terminal
```bash
python hello.py
```

---

## What is an error message?

When code has a mistake, Python reports it — called an **Error**.

> Do not fear errors! They are **help messages** that say where to fix 🆘

```
SyntaxError: '(' was never closed
  File "hello.py", line 1
    print("Hello"
         ^
```

| Part of the error | Meaning |
|-------------------|---------|
| `SyntaxError` | Type of problem |
| `'(' was never closed` | Detail: parenthesis not closed |
| `line 1` | Line with the problem |

---

## Common errors

| Error | Cause | Fix |
|-------|--------|--------|
| `SyntaxError` | Invalid code shape | Check parentheses / quotes |
| `NameError` | Unknown name | Check spelling (`print` not `Print`) |
| `IndentationError` | Bad indentation | Remove leading spaces at line start |

---

## Example: broken vs correct code

❌ **Wrong:**
```python
print("Hello"
```
```
SyntaxError: '(' was never closed
```

✅ **Correct:**
```python
print("Hello")
```
```
Hello
```

---

## Tips for fixing errors

1. **Read the error** carefully — it names the problem line
2. **Check parentheses** — every `(` needs a matching `)`
3. **Check quotes** — every `"` needs a closing `"` 
4. **Try Googling** the error message — someone else hit the same issue!
