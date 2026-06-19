# 📐 Python Syntax — กฎการเขียนโค้ด

---

## Syntax คืออะไร?

**Syntax** คือ **กฎการเขียน** ของภาษา Python

เหมือนภาษาไทยที่มีกฎ:
- ประโยคต้องมีประธาน + กริยา
- วรรณยุกต์ต้องถูกต้อง

Python ก็มีกฎเช่นกัน — เขียนผิดกฎ → **Error!**

---

## กฎที่ 1: ตัวพิมพ์เล็ก / ใหญ่สำคัญมาก

Python **แยกตัวพิมพ์เล็กและใหญ่** (Case Sensitive)

| ❌ ผิด | ✅ ถูก | Error ที่ได้ |
|--------|--------|------------|
| `Print("Hello")` | `print("Hello")` | `NameError` |
| `PRINT("Hello")` | `print("Hello")` | `NameError` |

> **คำสั่งทั้งหมดใน Python ใช้ตัวพิมพ์เล็กเสมอ**

---

## กฎที่ 2: เครื่องหมายต้องครบคู่

| ทุก... | ต้องมี... | ตัวอย่างผิด | ตัวอย่างถูก |
|--------|----------|------------|------------|
| `(` | `)` ปิด | `print("Hi"` | `print("Hi")` |
| `"` เปิด | `"` ปิด | `print("Hi)` | `print("Hi")` |

---

## กฎที่ 3: Indentation (การย่อหน้า)

โค้ดปกติ **ไม่ต้องมี space นำหน้า**:

```python
print("Line 1")    ← ถูกต้อง
print("Line 2")    ← ถูกต้อง
```

```python
print("Line 1")    ← ถูกต้อง
  print("Line 2")  ← ผิด! IndentationError
```

> Indentation จะมีความหมายพิเศษเมื่อเรียน `if` และ `for`

---

## ตัวอย่าง Error จริงๆ

```python
Print("Hello")
```
```
NameError: name 'Print' is not defined
```
> สาเหตุ: `P` ตัวใหญ่ — Python ไม่รู้จัก `Print`

---

```python
print("Hello"
```
```
SyntaxError: '(' was never closed
```
> สาเหตุ: ขาด `)` ปิดวงเล็บ

---

```python
  print("Hello")
```
```
IndentationError: unexpected indent
```
> สาเหตุ: มี space นำหน้าโดยไม่จำเป็น

---

## สรุปกฎ 3 ข้อ

| # | กฎ | จำว่า |
|---|----|----|
| 1 | ตัวพิมพ์เล็กเสมอ | `print` ไม่ใช่ `Print` |
| 2 | เครื่องหมายครบคู่ | `(` มี `)`, `"` มี `"` |
| 3 | ไม่มี space นำหน้า | เริ่มต้นบรรทัดแรกสุด |
