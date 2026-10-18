def electric_bill(units):
    if units <= 50:
        return units * 3
    elif units <= 150:
        return units * 4
    else:
        return units * 5

units = int(input())
print(electric_bill(units))
