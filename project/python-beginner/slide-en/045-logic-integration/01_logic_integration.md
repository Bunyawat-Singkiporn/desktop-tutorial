♪ Logic Integration ♫

---

♪ Algoritmic thinking

Before writing code, ask yourself:
```
1. Input คืออะไร?
2. ต้องการ Output แบบไหน?
3. ขั้นตอนจากอินพุตไปเอาต์พุตคืออะไร?
4. ต้องใช้ tools อะไร?
```---

#### Choose the tool right

▪ The situation
•----------------------
▪ Keep multiple values, add negatives
▪ Double key-value
• constant
▪ Expert
□ Repeat by number
• Repeat until conditions end
▪ Repeat code

---

## Example Problem solved.

== sync, corrected by elderman ==

```
Input:  ชื่อ 5 คน
Output: ชื่อที่ขึ้นต้นด้วย A

ขั้นตอน:
1. สร้าง list ว่าง
2. รับชื่อ 5 ครั้งด้วย loop
3. loop ผ่าน list
4. if ชื่อขึ้นต้นด้วย "A" → print
```

```python
names = []
for i in range(5):
    name = input(f"Enter name {i+1}: ")
    names.append(name)

for name in names:
    if name.startswith("A"):
        print(name)
```---

♪ Main

- Fix the problem step by step.
- Test output every step.
- Share the function when the code is complicated.
