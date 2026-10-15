count = 0
while True:
    menu = input()
    if menu == "end":
        break
    print(menu)
    count = count + 1
print(f"Count: {count}")
