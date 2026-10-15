hours = int(input())

if hours <= 1:
    charged = 0
else:
    charged = hours - 1

fee = charged * 20

print("========================")
print("       PARKING")
print("========================")
print(f"Hours Parked : {hours}")
print(f"Hours Charged: {charged}")
print(f"Fee          : {fee}")
print("========================")
