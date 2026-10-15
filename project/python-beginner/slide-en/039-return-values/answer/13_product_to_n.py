def product(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(product(4))
print(product(5))
