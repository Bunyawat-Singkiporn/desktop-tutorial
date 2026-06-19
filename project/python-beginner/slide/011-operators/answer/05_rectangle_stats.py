# โจทย์: รับความกว้างและความสูง แล้วคำนวณพื้นที่ เส้นรอบวง และเส้นทแยงมุม

# รับข้อมูล
width = int(input())
height = int(input())

# คำนวณค่าต่างๆ
area = width * height                          # พื้นที่
perimeter = (width + height) * 2              # เส้นรอบวง
diagonal = (width**2 + height**2) ** 0.5     # เส้นทแยงมุม √(w²+h²)

# แสดงผล
print(f"Width : {width}")
print(f"Height: {height}")
print(f"Area  : {area}")
print(f"Perim : {perimeter}")
print(f"Diag  : {diagonal:.2f}")
