# 🔥 Code Readability — Question 4: Full Refactor

**Difficulty:** 🔴 Hard

---

## Problem

The code below works, but it is very difficult to read. Refactor it into clean code by:
1. Giving variables meaningful names.
2. Splitting the code into functions.
3. Adding comments where needed.
4. Using f-strings.

```python
d={"a":85,"b":72,"c":90,"d":68}
t=0
for k in d:t+=d[k]
av=t/len(d)
best=""
bs=0
for k in d:
 if d[k]>bs:bs=d[k];best=k
print("avg:"+str(av)+"top:"+best+"("+str(bs)+")")
```

**Output:**
```
Average: 78.75
Top student: c (90)
```

---

## Starter Code

```python
# Refactored version
# Split the code into get_average() and get_top_student() functions
```
