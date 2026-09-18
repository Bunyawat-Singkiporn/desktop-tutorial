# 1) รู้จัก `dict`

## เป้าหมาย
เข้าใจ dict ก่อนเอาไปใช้กับนก

---

## แนวคิด — จาก list สู่ dict

**แบบ list** — ต้องจำว่าช่องไหนคืออะไร

```python
player = ["Mint", 120, 3, 45]
print(player[2])        # 3 ... แต่ 3 คืออะไร? ชีวิต? เลเวล? 🤔
```

**แบบ dict** — อ่านแล้วรู้เลย

```python
player = {
    "name": "Mint",
    "score": 120,
    "lives": 3,
    "level": 45,
}
print(player["lives"])      # 3 ← ชัดเจนว่าคือชีวิต ✅
```

---

## คำสั่งพื้นฐาน

```python
player["score"] = 200               # แก้ค่าเดิม
player["coins"] = 50                # เพิ่มคีย์ใหม่
print(len(player))                  # 5 คีย์
print("coins" in player)            # True
```

| โค้ด | ทำอะไร |
|------|--------|
| `d["key"]` | อ่านค่า |
| `d["key"] = v` | เขียนค่า (ถ้าไม่มีคีย์ = สร้างใหม่) |
| `"key" in d` | มีคีย์นี้ไหม |
| `len(d)` | มีกี่คีย์ |

> ⚠️ `player["hp"]` ทั้งที่ไม่มีคีย์ `hp` → `KeyError` พังทันที
> เช็กก่อนด้วย `if "hp" in player:` ถ้าไม่แน่ใจ

---

## แนวคิด — วนดูทุกคีย์

```python
for key in player:
    print(key, "=", player[key])
```

```text
name = Mint
score = 200
lives = 3
level = 45
coins = 50
```

---

## 📝 สร้างไฟล์ `dict_test.py` แล้วลองเล่น

```python
player = {
    "name": "Mint",
    "score": 120,
    "lives": 3,
}

print("ชื่อ:", player["name"])
print("คะแนน:", player["score"])

player["score"] = player["score"] + 50
player["coins"] = 10

print("--- ข้อมูลทั้งหมด ---")
for key in player:
    print(key, "=", player[key])
```

---

> รันดู — คะแนนต้องเป็น 170 และมีคีย์ `coins` เพิ่มมา ✅
> ลองเพิ่ม `player["level"] = 5` แล้วรันใหม่
