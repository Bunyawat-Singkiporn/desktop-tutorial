score = 50

def bonus():
    global score
    score += 10

def reset():
    global score
    score = 0

bonus()
reset()
print(score)
