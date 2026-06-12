## เป้าหมาย

รับการกดปุ่มจากผู้เล่น

---

## KEYDOWN

ตรวจว่ามีการกดปุ่ม

```python
if event.type == pygame.KEYDOWN:
```

---

## ตรวจเลข 1

```python
if event.key == pygame.K_1:
```

---

## เปลี่ยนข้อความ

```python
message = "You Pressed 1"
```

---

## วิเคราะห์

Input

```text
กดเลข 1
```

↓

Process

```python
if event.key == pygame.K_1
```

↓

Output

```text
You Pressed 1
```

---

## โค้ดที่เพิ่ม

```python
if event.type == pygame.KEYDOWN:

    if event.key == pygame.K_1:
        message = "You Pressed 1"
```
