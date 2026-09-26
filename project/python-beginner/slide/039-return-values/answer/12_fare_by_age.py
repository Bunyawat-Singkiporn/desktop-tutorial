def fare(age):
    if age < 6:
        return 0
    elif age < 18:
        return 20
    else:
        return 40

print(fare(4))
print(fare(10))
print(fare(30))
