# Practice Dictionary — Question 20: App Login

**Difficulty:** 🟡 Medium

---

## Task

User accounts:

```python
accounts = {"alice": "1234", "bob": "abcd"}
```

Read username and password.  
If match → `Welcome!`  
If user missing or wrong password → `Login failed`

---

## Example

**Input:**
```
alice
1234
```

**Output:**
```
Welcome!
```

**Input:**
```
alice
0000
```

**Output:**
```
Login failed
```

---

## Starter Code

```python
accounts = {"alice": "1234", "bob": "abcd"}

user = input()
password = input()
# Write your code here
```
