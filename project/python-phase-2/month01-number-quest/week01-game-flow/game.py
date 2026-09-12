# ============================================================
# Week 1 - Number Quest : CREATE HERO  (เฉลย)
# แนวคิด: Input -> Process -> Output
# รัน: python game.py
# ============================================================

# ---------- OUTPUT : หัวเกม ----------
print("=" * 30)
print("   NUMBER QUEST - CREATE HERO")
print("=" * 30)

# ---------- INPUT : ชื่อฮีโร่ ----------
name = input("ชื่อฮีโร่ของเธอ: ")
if name == "":
    name = "ผู้ไร้นาม"
print(f"ยินดีต้อนรับ {name}!")
print()

# ---------- INPUT : เลือกอาชีพ ----------
print("เลือกอาชีพ")
print("  1) นักดาบ   - ตี 10  เลือด 100")
print("  2) นักธนู   - ตี 8   เลือด 90")
print("  3) นักเวทย์ - ตี 12  เลือด 80")
job = int(input("พิมพ์เลข 1-3: "))

# ---------- PROCESS : ตัดสินใจตามอาชีพ ----------
if job == 1:
    job_name = "นักดาบ"
    attack = 10
    hp = 100
elif job == 2:
    job_name = "นักธนู"
    attack = 8
    hp = 90
else:
    job_name = "นักเวทย์"
    attack = 12
    hp = 80

# ---------- OUTPUT : การ์ดฮีโร่ ----------
print()
print("-" * 30)
print(f"  ฮีโร่: {name}")
print(f"  อาชีพ: {job_name}")
print(f"  พลังโจมตี: {attack}")
print(f"  พลังชีวิต: {hp}")
print("-" * 30)
print("การผจญภัยกำลังจะเริ่ม...")
