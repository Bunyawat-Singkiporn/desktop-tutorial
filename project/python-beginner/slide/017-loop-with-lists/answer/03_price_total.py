# โจทย์: รวมราคาสินค้าใน list แล้วแสดงยอดรวม

prices = [120, 350, 75, 200, 45]
total = 0

# พิมพ์แต่ละราคา และเพิ่มเข้า total
for price in prices:
    print(price)
    total = total + price

# แสดงยอดรวมหลังออกจาก loop
print("Total:", total)
