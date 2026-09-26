hp = int(input())
mana = int(input())

if hp < 20 or mana < 10:
    alert = "Danger"
else:
    alert = "Safe"

print("========================")
print("       STATUS")
print("========================")
print(f"HP     : {hp}")
print(f"Mana   : {mana}")
print(f"Alert  : {alert}")
print("========================")
