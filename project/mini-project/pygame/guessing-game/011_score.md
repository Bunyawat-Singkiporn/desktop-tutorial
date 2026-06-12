## เป้าหมาย

เพิ่มคะแนน

---

## Variable

ใช้เก็บคะแนน

```python
score = 0
```

---

## เพิ่มคะแนน

```python
score += 1
```

---

## ตัวอย่าง

```python
score = 0

score += 1

score += 1
```

ผลลัพธ์

```text
2
```

---

## ใช้ในเกม

ถ้าตอบถูก

```python
if guess == secret_number:

    message = "Correct!"

    score += 1
```

---

## แสดงคะแนน

```python
score_text = font.render(
    f"Score: {score}",
    True,
    "blue"
)

screen.blit(
    score_text,
    (20, 20)
)
```