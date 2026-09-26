temps = [30, 33, 24, 28, 35, 22, 31]
hot = 0
normal = 0
cool = 0
for temp in temps:
    if temp >= 32:
        hot = hot + 1
    elif temp < 25:
        cool = cool + 1
    else:
        normal = normal + 1
print("========================")
print("       WEATHER")
print("========================")
print(f"Hot    : {hot}")
print(f"Normal : {normal}")
print(f"Cool   : {cool}")
print("========================")
