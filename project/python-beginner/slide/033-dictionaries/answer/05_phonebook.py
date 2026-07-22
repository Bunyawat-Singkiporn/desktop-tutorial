phonebook = {
    "Alice": "081-111-1111",
    "Bob": "082-222-2222",
    "Charlie": "083-333-3333"
}

for i in range(3):
    name = input("Search: ")
    if name in phonebook:
        print("Phone:", phonebook[name])
    else:
        print("Not found:", name)
