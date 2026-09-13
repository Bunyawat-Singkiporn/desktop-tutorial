def countdown():
    start = int(input("Start from: "))
    for i in range(start, 0, -1):
        print(i)
    print("Go!")

countdown()
