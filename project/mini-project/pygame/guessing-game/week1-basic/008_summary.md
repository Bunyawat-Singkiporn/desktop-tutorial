# สรุป — Guessing Game Week 1

---

## เกมที่เราสร้าง

✅ หน้าต่างเกม
✅ แสดงข้อความ
✅ รับการกดปุ่ม 1-5
✅ ตรวจคำตอบ (Correct / Too Low / Too High)
✅ เก็บคะแนน

---

## Flowchart → โค้ด

```text
Flowchart ที่วาด              โค้ดที่เขียน
──────────────────────         ──────────────────────────────
▭ secret_number = 3      →     secret_number = 3
▭ score = 0              →     score = 0
▭ รอผู้เล่นกดปุ่ม        →     if event.type == KEYDOWN
◇ guess == secret?       →     if guess == secret_number:
▭ "Correct!" + score+=1  →     message = "Correct!" / score += 1
◇ guess < secret?        →     elif guess < secret_number:
▭ "Too Low!"             →     message = "Too Low!"
▭ "Too High!"            →     else: message = "Too High!"
```

---

## Python ที่ใช้ในเกมนี้

| Python (จาก Python-beginner) | ใช้ในเกม |
|------------------------------|---------|
| `variable = value` | `secret_number = 3`, `score = 0` |
| `if / elif / else` | ตรวจ guess |
| `==` `<` (operators) | เปรียบเทียบเลข |
| `+=` (operators) | `score += 1` |
| `f"Score: {score}"` (f-string) | แสดงคะแนน |

---

## ขั้นตอนที่เราทำ (วิธีสร้างเกมทุกครั้ง)

```text
1. วาด Flowchart ก่อน
2. สร้างหน้าต่าง (window)
3. แสดงข้อความ (text)
4. รับ Input (กดปุ่ม)
5. Process (if/elif/else)
6. Output (คะแนน, ข้อความ)
```

---

> ทุกเกมใหม่ → เริ่มด้วย Flowchart เสมอ
