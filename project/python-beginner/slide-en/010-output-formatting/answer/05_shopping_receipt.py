# โจทย์: รับข้อมูลลูกค้าและสินค้า แล้วแสดงใบเสร็จสวยงาม

# รับข้อมูล
customer_name = input()
item_name = input()
price = float(input())
quantity = int(input())

# คำนวณยอดรวม
total = price * quantity

# แสดงใบเสร็จด้วย f-string
print("==============================")
print("         TECH STORE")
print("==============================")
print(f"Customer : {customer_name}")
print(f"Item     : {item_name}")
print(f"Price    : {price:.2f} baht")
print(f"Quantity : {quantity}")
print("------------------------------")
print(f"Total    : {total:.2f} baht")
print("==============================")
print(f"Thank you, {customer_name}!")
