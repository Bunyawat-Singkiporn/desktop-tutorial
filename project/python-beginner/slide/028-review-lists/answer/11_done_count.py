status = ["Done", "Todo", "Done", "Todo", "Done"]
count = 0
for s in status:
    if s == "Done":
        count += 1
print(f"Done: {count}")
