def parking_fee(hours):
    if hours <= 1:
        return 0
    else:
        return (hours - 1) * 20

hours = int(input())
print(parking_fee(hours))
