def topping_cost(count):
    return count * 10

def final_price(base, count):
    return base + topping_cost(count)

base = int(input())
count = int(input())
print(final_price(base, count))
