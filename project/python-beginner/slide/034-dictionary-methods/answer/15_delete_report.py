room = {"name": "Lab", "code": "TMP", "seats": 24}
del room["code"]
for key, value in room.items():
    print(f"{key}: {value}")
print(f"Fields: {len(room)}")
