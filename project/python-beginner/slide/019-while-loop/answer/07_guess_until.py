secret = 7
guess = int(input())
while guess != secret:
    print("Wrong")
    guess = int(input())
print("Correct!")
