def add_book(books, title):
    books.append(title)
    return books

def count_books(books):
    return len(books)

def show_books(books):
    for b in books:
        print(b)

books = []
books = add_book(books, "Python")
books = add_book(books, "Math")
print(count_books(books))
show_books(books)
