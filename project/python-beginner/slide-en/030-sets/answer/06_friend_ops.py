a = {"Ann", "Ben", "Cara"}
b = {"Ben", "Dan", "Cara"}
both = list(a & b)
both.sort()
all_friends = list(a | b)
all_friends.sort()
print(both)
print(all_friends)
