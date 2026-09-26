labels = ["Syntax", "Runtime", "Logic"]
code = int(input())
if code >= 0 and code < len(labels):
    print(labels[code])
else:
    print("Unknown")
