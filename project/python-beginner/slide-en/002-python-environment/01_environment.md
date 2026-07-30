# 🖥️ Python Environment — Getting Started Writing Code

---

## What is an Editor?

An **Editor** is a program for writing code.

It is like a **notebook** 📒 but for programmers, with features that make writing code easier.

| Editor | Description |
|--------|-------------|
| **VS Code** | Works with every language ✅ (recommended) |
| PyCharm | Python-focused |
| IDLE | Comes with Python |

---

## How to Run Python Code

### Method 1: The ▶ button in VS Code
1. Open a `.py` file
2. Click the **▶ Run** button in the top-right corner
3. See the result in the **Terminal** at the bottom

### Method 2: Terminal
```bash
python hello.py
```

---

## What is an Error Message?

When code has a mistake, Python warns you — that is called an **Error**.

> Don't fear Errors! They are **helpful messages** that tell you what to fix 🆘

```
SyntaxError: '(' was never closed
  File "hello.py", line 1
    print("Hello"
         ^
```

| Part of the Error | Meaning |
|-------------------|---------|
| `SyntaxError` | Type of mistake |
| `'(' was never closed` | Detail: parenthesis not closed |
| `line 1` | Line that has the problem |

---

## Common Errors

| Error | Cause | How to fix |
|-------|-------|------------|
| `SyntaxError` | Code written in the wrong form | Check parentheses / punctuation |
| `NameError` | Used a name that does not exist | Check spelling (`print` not `Print`) |
| `IndentationError` | Incorrect indentation | Remove leading spaces on the line |

---

## Example: Broken Code vs Correct Code

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

## Tips for Fixing Errors

1. **Read the Error** carefully — it tells you which line has the problem
2. **Check parentheses** — every `(` needs a closing `)`
3. **Check quotation marks** — every `"` needs a closing `"`
4. **Try Googling** the error message — someone else has hit the same problem!
