a = {"A", "B", "C", "D"}
b = {"B", "C", "E"}
a.remove("D")
result = list(a & b)
result.sort()
print(result)
