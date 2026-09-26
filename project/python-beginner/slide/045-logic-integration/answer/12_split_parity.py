nums = [1, 2, 3, 4, 5]
evens = []
odds = []
for n in nums:
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)
print(evens)
print(odds)
