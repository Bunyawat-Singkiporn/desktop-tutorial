warehouse = {"S01", "S02", "S03"}
incoming = {"S03", "S04"}
warehouse.add("S05")
warehouse.remove("S01")
all_codes = list(warehouse | incoming)
all_codes.sort()
both = list(warehouse & incoming)
both.sort()
print(all_codes)
print(both)
print(f"Total: {len(all_codes)}")
