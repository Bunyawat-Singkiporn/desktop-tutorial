total = int(input())
is_vip = int(input())

if total >= 500 or is_vip == 1:
    gift = 1
else:
    gift = 0

print("========================")
print("        PROMO")
print("========================")
print(f"Total : {total}")
print(f"Gift  : {gift}")
print("========================")
