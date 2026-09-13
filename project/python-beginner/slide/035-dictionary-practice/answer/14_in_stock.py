stock = {"pen": 10, "book": 5, "eraser": 20}

item = input()
if item in stock:
    print("In stock")
else:
    print("Sold out")
