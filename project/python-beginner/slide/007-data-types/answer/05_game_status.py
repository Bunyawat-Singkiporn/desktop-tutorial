# โจทย์: แสดงสถานะเกมพร้อม type name ของแต่ละตัวแปร

# ข้อมูลตัวละครในเกม
player_name = "Hero"           # str
player_level = 5               # int
player_hp = 87.5               # float
is_boss_defeated = False       # bool

# แสดงผลพร้อม type name
# type(x).__name__ ให้แค่ชื่อ type เช่น 'int' (ไม่มี <class '...'>)
print("=== Game Status ===")
print(f"Player  : {player_name:<10} ({type(player_name).__name__})")
print(f"Level   : {player_level:<10} ({type(player_level).__name__})")
print(f"HP      : {player_hp:<10} ({type(player_hp).__name__})")
print(f"Boss    : {is_boss_defeated:<10} ({type(is_boss_defeated).__name__})")
