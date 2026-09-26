member = {"name": "Ivy", "point": 10, "level": 1}
member.update({"point": 25, "level": 2})
for key, value in member.items():
    print(f"{key}: {value}")
