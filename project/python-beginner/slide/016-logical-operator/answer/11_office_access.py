day_type = input()
has_badge = int(input())

if day_type == "workday" and has_badge == 1:
    access = "Access Granted"
else:
    access = "Access Denied"

print(f"Day    : {day_type}")
print(f"Access : {access}")
