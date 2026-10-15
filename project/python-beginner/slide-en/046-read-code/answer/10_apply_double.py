def double(x):
    return x * 2

def apply_all(lst):
    result = []
    for item in lst:
        result.append(double(item))
    return result

print(apply_all([1, 2, 3]))
