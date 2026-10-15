tasks = ["Sweep", "Mop", "Dust", "Wipe"]
for i in range(len(tasks)):
    if i % 2 == 0:
        status = "Done"
    else:
        status = "Todo"
    print(f"{i} {tasks[i]} {status}")
