def clamp(score):
    if score < 0:
        return 0
    elif score > 100:
        return 100
    else:
        return score

print(clamp(-5))
print(clamp(40))
print(clamp(150))
