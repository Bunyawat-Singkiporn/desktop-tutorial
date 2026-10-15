product = {"name": "Soap", "price": 25, "note": "old"}
product.update({"price": 28})
del product["note"]
print("====================")
for key, value in product.items():
    print(f"{key}: {value}")
print("====================")
