# โจทย์: รับข้อมูลสินค้าและแสดงใบเสร็จสมบูรณ์พร้อมส่วนลด

# รับข้อมูลทั้งหมด
customer_name = input()
item_name = input()
price = float(input())
qty = int(input())
discount_percent = int(input())

# คำนวณ
subtotal = price * qty
discount_amount = subtotal * (discount_percent / 100)
total = subtotal - discount_amount

# แสดงใบเสร็จ
print("================================")
print("          FASHION STORE")
print("================================")
print(f"Customer : {customer_name}")
print(f"Item     : {item_name}")
print(f"Price    : {price:.2f} baht")
print(f"Qty      : {qty}")
print("--------------------------------")
print(f"Subtotal : {subtotal:.2f} baht")
print(f"Discount : {discount_amount:.2f} baht ({discount_percent}%)")
print(f"Total    : {total:.2f} baht")
print("================================")
print(f"Thank you, {customer_name}! See you again.")
