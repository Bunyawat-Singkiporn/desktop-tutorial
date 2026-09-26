temps = [31, 28, 35, 30, 33]
hottest = temps[0]
for t in temps:
    if t > hottest:
        hottest = t
print(f"Hottest: {hottest}")
