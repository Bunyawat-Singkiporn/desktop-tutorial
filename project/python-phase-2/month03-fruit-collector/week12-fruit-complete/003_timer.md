# 2) นับถอยหลัง

## เป้าหมาย
เกมมีเวลา 45 วินาที หมดเวลาแล้วจบ พร้อมแถบเวลาที่สั้นลงเรื่อยๆ

---

## แนวคิด — ทบทวนจาก Week 7

```python
TIME_LIMIT = 45

start_time = pygame.time.get_ticks()          # จำเวลาที่เริ่มเกม

# ในลูป
passed = (pygame.time.get_ticks() - start_time) / 1000
time_left = TIME_LIMIT - passed

if time_left <= 0:
    time_left = 0
    game_over = True
```

> เหมือน Quiz Arena เป๊ะ ต่างแค่จับเวลา **ทั้งเกม** ไม่ใช่ทีละข้อ
> **ทักษะที่ใช้ซ้ำได้ = ทักษะที่คุ้มค่าเรียน** ♻️

---

## แนวคิด — แถบเวลา

```python
ratio = time_left / TIME_LIMIT
if ratio < 0:
    ratio = 0

pygame.draw.rect(screen, (60, 75, 95), (20, 56, 760, 12), border_radius=6)
pygame.draw.rect(screen, bar_color, (20, 56, int(760 * ratio), 12), border_radius=6)
```

เปลี่ยนสีตอนใกล้หมดเพื่อเร่งความตื่นเต้น

```python
if time_left > 15:
    bar_color = (80, 200, 130)
elif time_left > 5:
    bar_color = (240, 200, 70)
else:
    bar_color = (235, 80, 80)
```

---

## ⚠️ กับดัก: ต้องหยุดเวลาตอนจบเกม

```python
if not game_over:
    passed = (pygame.time.get_ticks() - start_time) / 1000
    time_left = TIME_LIMIT - passed
```

> ถ้าไม่ครอบ เวลาจะเดินต่อในจอจบเกม แล้วตัวเลขจะติดลบเรื่อยๆ

---

## แนวคิด — จบเกมได้ 2 ทาง

```python
if lives <= 0:
    game_over = True
    end_reason = "ชีวิตหมด"
if time_left <= 0:
    game_over = True
    end_reason = "หมดเวลา"
```

> เก็บ **เหตุผล** ไว้ด้วย เพื่อบอกผู้เล่นตอนจบว่าแพ้เพราะอะไร
> เกมที่ไม่บอกเหตุผล ผู้เล่นจะรู้สึกว่าโดนโกง

---

## 📝 แก้ `fruit.py`

1. เพิ่ม `TIME_LIMIT = 45`, `start_time = pygame.time.get_ticks()`, `time_left = TIME_LIMIT`
2. คำนวณเวลาในลูป (ครอบด้วย `if not game_over:`)
3. วาดแถบเวลาและตัวเลขวินาที
4. เพิ่ม `end_reason`

---

> รันแล้วปล่อยทิ้งไว้ — พอครบ 45 วินาทีเกมต้องจบเอง ✅
