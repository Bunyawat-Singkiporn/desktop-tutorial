# 🔥 Practice Function — Challenge: School Library

**Difficulty:** 🔴 Hard

---

## Task

Build a tiny library system with **3 functions**:

| Function | Job |
|----------|-----|
| `add_book(books, title)` | add a book title |
| `count_books(books)` | return number of books |
| `show_books(books)` | print all titles |

---

## Example Session

```
How many books? 3
Title: Python Basics
Title: Fun Games
Title: Space Kids
=== Library ===
Python Basics
Fun Games
Space Kids
Total books: 3
```

---

## Starter Code

```python
def add_book(books, title):
    # Write your code here

def count_books(books):
    # Write your code here

def show_books(books):
    # Write your code here

books = []
n = int(input("How many books? "))
for i in range(n):
    add_book(books, input("Title: "))

print("=== Library ===")
show_books(books)
print(f"Total books: {count_books(books)}")
```
