## เป้าหมาย

สร้างเกมเดาเลข

---

## Secret Number

เลขลับ

```python
secret_number = 3
```

---

## Guess

เลขที่ผู้เล่นเดา

```python
guess = 1
```

---

## ถ้าเดาถูก

```python
if guess == secret_number:
```

ผลลัพธ์

```text
Correct!
```

---

## ถ้าเดาต่ำไป

```python
elif guess < secret_number:
```

ผลลัพธ์

```text
Too Low!
```

---

## ถ้าเดาสูงไป

```python
else:
```

ผลลัพธ์

```text
Too High!
```

---

## เพิ่มในเกม

```python
if event.key == pygame.K_1:
    guess = 1

elif event.key == pygame.K_2:
    guess = 2

elif event.key == pygame.K_3:
    guess = 3

elif event.key == pygame.K_4:
    guess = 4

elif event.key == pygame.K_5:
    guess = 5


if guess == secret_number:
    message = "Correct!"

elif guess < secret_number:
    message = "Too Low!"

else:
    message = "Too High!"
```