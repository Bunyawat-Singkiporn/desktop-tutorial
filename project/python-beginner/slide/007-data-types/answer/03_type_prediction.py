# โจทย์: ตรวจสอบ type ของค่า 4 แบบ (รวมทั้ง "42" กับ 42)

a = 42       # int
b = "42"     # str — เพราะอยู่ในเครื่องหมาย "..."
c = 42.0     # float — เพราะมีจุดทศนิยม
d = True     # bool

# แสดง type — สังเกต: a กับ b ดูเหมือนกัน แต่ type ต่างกัน!
print(type(a))   # <class 'int'>
print(type(b))   # <class 'str'>
print(type(c))   # <class 'float'>
print(type(d))   # <class 'bool'>
