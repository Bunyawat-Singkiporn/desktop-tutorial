def add_book(books, title):
    books.append(title)

def count_books(books):
    return len(books)

def show_books(books):
    for title in books:
        print(title)

books = []
n = int(input("How many books? "))
for i in range(n):
    add_book(books, input("Title: "))

print("=== Library ===")
show_books(books)
print(f"Total books: {count_books(books)}")
