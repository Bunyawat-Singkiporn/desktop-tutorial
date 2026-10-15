staff = ["Ann", "Ben"]
rooms = ("Hall", "Garden")
guests = ["Ed", "Ann", "Ed", "Ben"]
staff.append("Cara")
unique_guests = list(set(guests))
unique_guests.sort()
print(staff)
print(rooms[0])
print(unique_guests)
