menu = {"rice": 40, "soup": 30, "tea": 20}
order = ["rice", "tea", "soup"]

def bill(menu, order):
    total = 0
    for item in order:
        total += menu[item]
    return total

print(bill(menu, order))
