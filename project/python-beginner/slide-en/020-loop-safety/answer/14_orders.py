while True:
    item = input()
    if item == "done":
        break
    if item == "cancel":
        continue
    print(f"Order: {item}")
print("End of orders")
