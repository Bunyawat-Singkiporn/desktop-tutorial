

**Difficulty:** 🔴 Challenge

---





---

## Input
## Output
---



**Input:**# 🔄 Type Conversion — ข้อ 13: บัตรเข้าชมพิพิธภัณฑ์## โจทย์พิพิธภัณฑ์พิมพ์บัตรเข้าชมจากชื่อและอายุ
รับชื่อ (ข้อความ) และอายุ (จำนวนเต็ม)
สร้างข้อความบัตรด้วยการต่อ string และแสดงชนิดของอายุหลังแปลงแล้ว2 บรรทัด — ชื่อ และอายุข้อความบัตร 2 บรรทัด และชนิดของอายุ 1 บรรทัด## ตัวอย่าง```text
Mina
11
```
**Output:**```text
Visitor: Mina
Age: 11
Age type: <class 'int'>
```
---

## Hint
---

## Starter Codeอายุต้องผ่าน `int(input())` ก่อน — แล้วค่อยพิมพ์ค่าและ `type()` ของมัน```python
name = input()
age = int(input())

# Write your code here
```
