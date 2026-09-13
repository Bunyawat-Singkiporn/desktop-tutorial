def ticket_price(age):
    if age < 12:
        return 80
    else:
        return 150

def print_ticket(name, age, price):
    print("=== Movie Ticket ===")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Price: {price} baht")
    print("Enjoy the movie!")

name = input()
age = int(input())
price = ticket_price(age)
print_ticket(name, age, price)
