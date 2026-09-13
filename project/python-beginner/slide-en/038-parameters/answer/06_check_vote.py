def check_vote(age):
    if age >= 18:
        print("You can vote")
    else:
        print("Too young to vote")

age = int(input())
check_vote(age)
