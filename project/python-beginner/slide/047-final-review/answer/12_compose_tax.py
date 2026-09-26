def net(price):
    return price - 10

def label(n):
    return f"Net: {n}"

print(label(net(100)))
