x = 10

def change():
    x = 99          # local x — คนละตัวกับ global x
    print("Inside:", x)

change()
print("Outside:", x)
# x ภายนอกไม่เปลี่ยนเพราะ x ใน change() เป็น local variable
