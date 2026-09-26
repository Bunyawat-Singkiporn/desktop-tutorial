def with_bonus(score):
    if score % 2 == 0:
        return score + 5
    else:
        return score + 3

print(with_bonus(10))
print(with_bonus(7))
