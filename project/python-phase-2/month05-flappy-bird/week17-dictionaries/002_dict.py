# Week 17 - เช็คพอยต์ 1 : รู้จัก dict
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
