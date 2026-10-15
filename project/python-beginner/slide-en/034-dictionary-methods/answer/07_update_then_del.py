profile = {"name": "Dan", "temp": 0, "city": "Rayong"}
profile.update({"city": "Chonburi"})
del profile["temp"]
for key, value in profile.items():
    print(f"{key}: {value}")
