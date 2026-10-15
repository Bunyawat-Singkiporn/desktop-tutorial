def cart_info(prices):
    total = 0
    for p in prices:
        total += p
    return {"count": len(prices), "total": total}

print(cart_info([25, 40, 35]))
