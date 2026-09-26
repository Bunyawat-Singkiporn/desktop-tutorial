def race_result(seconds):
    if seconds <= 60:
        return "Pass"
    else:
        return "Fail"

print(race_result(55))
print(race_result(72))
