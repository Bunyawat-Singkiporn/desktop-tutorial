# โจทย์: แปลงอุณหภูมิจากเซลเซียสเป็นฟาเรนไฮต์
# สูตร: F = C × 9/5 + 32

# รับอุณหภูมิเป็น float (รองรับทศนิยม)
celsius = float(input())

# แปลงโดยใช้สูตร
fahrenheit = celsius * 9 / 5 + 32

# แสดงผล
print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)
