def check_ticket(age):
    if age >= 13:
        print("You can watch")
    else:
        print("Sorry, too young")

age = int(input())
check_ticket(age)
