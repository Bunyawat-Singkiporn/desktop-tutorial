# 📚 if/else — Q5: คะแนนรวมผ่านเกณฑ์ไหม
**Difficulty:** 🟢 Easy
---
## Task
วิชาหนึ่งเก็บคะแนน 2 ส่วน คือคะแนนเก็บกับคะแนนสอบ
จะผ่านวิชานี้ได้ต้องได้ **คะแนนรวม** ตั้งแต่ 100 คะแนนขึ้นไป
เขียนโปรแกรมรับคะแนนทั้งสองส่วน แล้วบอกผล
**Rules:**
- คะแนนรวม `>= 100` → `Qualified`
- น้อยกว่านั้น → `Not Qualified`
---
## Input
2 บรรทัด — คะแนนเก็บ และคะแนนสอบ
## Output
2 บรรทัด — คะแนนรวม และผลการตัดสิน
---
## Example
**Input:**
```text
45
62
```

**Output:**

```text
Total  : 107
Result : Qualified
```
---
## 💡 Hint
รวมคะแนนเก็บไว้ในตัวแปรก่อน แล้วค่อยเอาตัวแปรนั้นไปเทียบกับเกณฑ์
---
## Starter Code
```python
work_score = int(input())
exam_score = int(input())

# Write your code here
```
