# โจทย์: รับชื่อสินค้าและราคา แล้วแสดงป้ายสินค้าด้วย f-string

# รับข้อมูล
product_name = input()
price = float(input())

# แสดงด้วย f-string
# {price:.2f} แสดงทศนิยม 2 ตำแหน่งเสมอ
print(f"Product: {product_name}")
print(f"Price: {price:.2f} baht")
