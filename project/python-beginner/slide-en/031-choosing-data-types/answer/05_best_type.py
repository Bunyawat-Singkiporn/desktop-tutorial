books = ["Python Basics", "Data Science", "Web Dev"]
categories = ("Fiction", "Non-fiction", "Science")
isbns = {"ISBN-001", "ISBN-002", "ISBN-003"}

books.append("Machine Learning")

new_isbn = "ISBN-999"
if new_isbn not in isbns:
    isbns.add(new_isbn)
    print(f"{new_isbn} is new → added")
else:
    print(f"{new_isbn} already exists")

print("Books:", len(books))
print("Categories:", len(categories))
print("ISBNs:", len(isbns))
