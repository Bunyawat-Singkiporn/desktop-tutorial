days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for day in days:
    if day == "Sat" or day == "Sun":
        continue
    print(f"Work: {day}")
