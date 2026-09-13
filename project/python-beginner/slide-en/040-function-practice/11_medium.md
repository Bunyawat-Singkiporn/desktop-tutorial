# Practice Function — Medium: Student Names

**Difficulty:** 🟡 Medium

---

## Task

Create:
- `add_student(students, name)` — append name to list
- `show_students(students)` — print each name

Read how many students, then each name, then show the list.

> Combines: function + list + input + for

---

## Example Session

```
How many students? 3
Name: Alice
Name: Bob
Name: Cara
Alice
Bob
Cara
```

---

## Starter Code

```python
def add_student(students, name):
    # Write your code here

def show_students(students):
    # Write your code here

students = []
n = int(input("How many students? "))
for i in range(n):
    name = input("Name: ")
    add_student(students, name)

show_students(students)
```
