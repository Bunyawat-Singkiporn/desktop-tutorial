temps = [29, 31, 30, 33, 28]
total = 0
for t in temps:
    total = total + t
average = total / len(temps)
print(f"Total: {total}")
print(f"Average: {average:.1f}")
if average >= 30:
    print("Status: Hot Week")
else:
    print("Status: Cool Week")
