secret = 25
while True:
    guess = int(input())
    if guess == secret:
        print("Correct!")
        break
    elif guess < secret:
        print("Too low")
        continue
    else:
        print("Too high")
        continue
