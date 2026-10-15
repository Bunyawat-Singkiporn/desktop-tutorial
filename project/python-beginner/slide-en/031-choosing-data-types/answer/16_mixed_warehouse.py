stock = ["Rice", "Oil"]
location = ("Zone", "A")
raw_codes = [101, 102, 101, 103]
stock.append("Salt")
stock.sort()
codes = list(set(raw_codes))
codes.sort()
print(stock)
print(location[-1])
print(codes)
