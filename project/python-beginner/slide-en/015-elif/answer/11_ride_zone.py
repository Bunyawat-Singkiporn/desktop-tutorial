height = int(input())

if height >= 150:
    zone = "Thrill Zone"
elif height >= 120:
    zone = "Adventure Zone"
elif height >= 90:
    zone = "Family Zone"
else:
    zone = "Kids Zone"

print(f"Height : {height}")
print(f"Zone   : {zone}")
