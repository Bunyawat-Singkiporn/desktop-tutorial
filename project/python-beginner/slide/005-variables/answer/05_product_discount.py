# โจทย์: คำนวณราคาสินค้าหลังหักส่วนลด

# ข้อมูลสินค้า
product_name = "Running Shoes"
original_price = 1500
discount_percent = 20

# คำนวณส่วนลด
discount_amount = original_price * discount_percent / 100
# ราคาสุดท้าย = ราคาเดิม - ส่วนลด
final_price = original_price - discount_amount

# แสดงผล
print("Product:", product_name)
print("Original Price:", original_price)
print("Discount:", str(discount_percent) + "%")
print("You save:", int(discount_amount))
print("Final Price:", int(final_price))
