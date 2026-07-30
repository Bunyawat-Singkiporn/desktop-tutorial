# 👁️ Read Code — Reading Code

---

## Why Learn to Read Code?

- Fix bugs in code you did not write.
- Work with a team.
- Review old code.

---

## How to Read Code Step by Step

```
1. Start with the big picture.
2. Find the input: what values does the program receive?
3. Follow the code from top to bottom.
4. Trace variable values one step at a time.
5. For a loop, ask: "How many times does it run, and how do the values change?"
6. For an `if` statement, ask: "Is the condition true?"
7. Find the output: what does the program display?
```

---

## Example — Read It First

```python
numbers = [3, 7, 2, 9, 4]
result = 0

for num in numbers:
    if num > result:
        result = num

print(result)
```

**Think through it step by step:**
```
result = 0
Iteration 1: num=3, 3 > 0 → result=3
Iteration 2: num=7, 7 > 3 → result=7
Iteration 3: num=2, 2 > 7 → no change
Iteration 4: num=9, 9 > 7 → result=9
Iteration 5: num=4, 4 > 9 → no change
print(9)
```

**Output:** `9`

---

## Example — Code with Functions

```python
def double(x):
    return x * 2

def apply_all(lst):
    result = []
    for item in lst:
        result.append(double(item))
    return result

nums = [1, 2, 3]
print(apply_all(nums))
```

**Output:** `[2, 4, 6]`

---

## Tips

- **Trace on paper**—write down the variable values for each iteration.
- **Read function names**—a good name explains what a function does.
- **Look for `return`**—it gives you the function's result.
