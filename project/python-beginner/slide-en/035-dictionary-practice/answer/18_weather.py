weather = {"Bangkok": 34, "Chiang Mai": 28, "Phuket": 31}

city = input()
if city in weather:
    print(f"{city}: {weather[city]} C")
else:
    print("No data")
