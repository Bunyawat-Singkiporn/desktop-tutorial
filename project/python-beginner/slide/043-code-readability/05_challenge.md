# 🔥 Code Readability — Question 4: Full Refactor

**Difficulty:** 🔴 Hard

---

## โจทย์

โค้ดด้านล่างทำงานได้แต่แย่มาก — refactor ให้ clean โดย:
1. ตั้งชื่อตัวแปรให้สื่อความหมาย
2. แบ่งออกเป็น functions
3. เพิ่ม comment ที่จำเป็น
4. ใช้ f-string

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

**Output ที่ถูกต้อง:**
```
Average: 78.75
Top student: c (90)
```

---

## Starter Code

```python
# Refactored version
# แบ่งเป็น functions: get_average() และ get_top_student()
```
