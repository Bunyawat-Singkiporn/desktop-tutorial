member = {"name": "Kate", "point": 40, "city": "Loei"}
member.update({"point": 55})
member["tier"] = "Silver"
print("====================")
for key, value in member.items():
    print(f"{key}: {value}")
print("====================")
