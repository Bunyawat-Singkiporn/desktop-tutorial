is_member = int(input())
day = input()

if is_member == 1 and day == "weekday":
    offer = "Discount"
else:
    offer = "No Discount"

print(f"Member : {is_member}")
print(f"Offer  : {offer}")
