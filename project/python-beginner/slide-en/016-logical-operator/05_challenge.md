# 🔥 Practice and/or/not — Question 4: Theme Park Entry

**Difficulty:** 🔴 Hard

---

## Problem

The theme park has these rules:

- **Child** (age < 12): may enter **only with a guardian**
- **Adult** (age >= 12): may always enter **except** when `banned = True`

Read:
1. age (int)
2. has a guardian (`True` / `False`)
3. is banned (`True` / `False`)

Show `Welcome` or `Not Allowed`

> Mix skills: and + or + not + elif

---

## Example

**Input:**
```
10
True
False
```
**Output:**
```
Welcome
```

**Input:**
```
10
False
False
```
**Output:**
```
Not Allowed
```

**Input:**
```
20
True
True
```
**Output:**
```
Not Allowed
```

---

## 💡 Hint

- Split into 2 main cases: child vs adult
- Each case has different conditions

---

## Starter Code

```python
age = int(input())
has_guardian = input()
banned = input()

# Write your code here
```
