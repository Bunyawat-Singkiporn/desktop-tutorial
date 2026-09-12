# 3) สรุปคะแนน + เหรียญ

## เป้าหมาย
แปลงคะแนนเป็นเหรียญ GOLD / SILVER / BRONZE

---

## แนวคิด — จัดอันดับด้วย `if / elif / else`

```python
if score == 30:
    medal = "GOLD"
elif score == 20:
    medal = "SILVER"
elif score == 10:
    medal = "BRONZE"
else:
    medal = "ไม่มีเหรียญ"
```

> ทำไมไม่ใช้ `>=` ล่ะ? ใช้ได้เหมือนกัน และ **ดีกว่า** ด้วย:

```python
if score >= 30:
    medal = "GOLD"
elif score >= 20:
    medal = "SILVER"
elif score >= 10:
    medal = "BRONZE"
else:
    medal = "ไม่มีเหรียญ"
```

| คะแนน | เช็ก `>= 30` | เช็ก `>= 20` | เช็ก `>= 10` | ได้ |
|-------|-------------|-------------|-------------|-----|
| 30 | ✅ หยุด | - | - | GOLD |
| 20 | ❌ | ✅ หยุด | - | SILVER |
| 10 | ❌ | ❌ | ✅ หยุด | BRONZE |
| 0 | ❌ | ❌ | ❌ | ไม่มีเหรียญ |

> **ลำดับสำคัญมาก!** ถ้าเอา `>= 10` ไว้บนสุด ทุกคนจะได้ BRONZE หมด
> เพราะ 30 ก็ `>= 10` เหมือนกัน แล้ว Python จะหยุดที่บรรทัดแรกที่จริง

---

## 📝 เพิ่มท้าย `score.py`

**แทนที่** บรรทัด `print("คะแนนรวม:", score)` ด้วย:

```python
if score >= 30:
    medal = "GOLD"
elif score >= 20:
    medal = "SILVER"
elif score >= 10:
    medal = "BRONZE"
else:
    medal = "ไม่มีเหรียญ"

print("-" * 30)
print(f"  คะแนนรวม : {score} / 30")
print(f"  ตอบถูก   : {correct} / 3 ด่าน")
print(f"  เหรียญ   : {medal}")
print("-" * 30)
```

---

> รันหลายๆ รอบ ให้ได้ครบทุกเหรียญ ✅
> ตอบถูกหมด = GOLD / ผิดหมด = ไม่มีเหรียญ
