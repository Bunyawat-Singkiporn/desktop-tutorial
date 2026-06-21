# โจทย์: รับสินค้าและราคาซ้ำๆ จนพิมพ์ "done" แล้วแสดงใบเสร็จ

items = []
prices = []

# รับสินค้าซ้ำจนกว่าจะพิมพ์ "done"
while True:
    name = input()
    if name == "done":
        break
    price = int(input())
    items.append(name)
    prices.append(price)

# แสดงใบเสร็จ
print("=== Receipt ===")
for i in range(len(items)):
    print(f"{items[i]}: {prices[i]} baht")
print("---")
print(f"Total: {sum(prices)} baht")
