# 🔥 Practice Dictionaries — Question 4: Phonebook Lookup

**Difficulty:** 🔴 Hard

---

## Problem

Create a phonebook for three people. Ask the user for a name and look up the corresponding phone number. Repeat this three times.

```python
phonebook = {
    "Alice": "081-111-1111",
    "Bob": "082-222-2222",
    "Charlie": "083-333-3333"
}
```

**Example Session:**
```
Search: Alice
Phone: 081-111-1111
Search: David
Not found: David
Search: Bob
Phone: 082-222-2222
```

---

## 💡 Hint

Use `if name in phonebook:` before accessing the value.

---

## Starter Code

```python
phonebook = {
    "Alice": "081-111-1111",
    "Bob": "082-222-2222",
    "Charlie": "083-333-3333"
}

for i in range(3):
    name = input("Search: ")
    # Write your code here
```
