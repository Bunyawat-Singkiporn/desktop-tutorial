user = {"name": "Finn", "age": 16, "temp": 1, "city": "Nan"}
user.update({"age": 17, "city": "Lampang"})
del user["temp"]
for key, value in user.items():
    print(f"{key}: {value}")
