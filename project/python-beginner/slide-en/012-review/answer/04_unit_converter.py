# โจทย์: รับระยะทางเป็นกิโลเมตร แล้วแปลงเป็นหน่วยต่างๆ

# รับระยะทาง
km = float(input())

# คำนวณการแปลงหน่วย
meters = km * 1000         # 1 km = 1,000 m
miles = km * 0.621         # 1 km = 0.621 miles
yards = km * 1093.61       # 1 km = 1,093.61 yards

# แสดงผล
print(f"Distance: {km} km")
print(f"= {meters:.0f} m")
print(f"= {miles:.2f} miles")
print(f"= {yards:.2f} yards")
