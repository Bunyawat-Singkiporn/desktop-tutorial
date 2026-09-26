n = int(input())
data = {}
for i in range(n):
    name = input()
    score = int(input())
    data[name] = score

best_name = ""
best_score = -1
for name, score in data.items():
    if score > best_score:
        best_score = score
        best_name = name
print(f"Top: {best_name} {best_score}")
