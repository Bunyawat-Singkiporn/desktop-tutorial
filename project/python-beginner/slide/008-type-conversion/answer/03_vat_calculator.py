# โจทย์: รับราคา แล้วคำนวณราคาหลังบวก VAT 7%

# รับราคาเป็น float (รองรับทศนิยม)
price = float(input())

# คำนวณ VAT 7%
vat = price * 0.07

# คำนวณราคารวม
total = price + vat

# แสดงผล
print("Original:", price)
print("VAT (7%):", vat)
print("Total:", total)
