# โจทย์: รับราคาสินค้าและเงินที่จ่าย แล้วคำนวณเงินทอน

# รับข้อมูล
price = int(input())
paid = int(input())

# คำนวณเงินทอน
change = paid - price

# แสดงผล
print("Price:", price)
print("Paid:", paid)
print("Change:", change)
