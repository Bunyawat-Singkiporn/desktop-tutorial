def who_is_older(age1, age2):
    if age1 > age2:
        print("Friend 1 is older")
    elif age2 > age1:
        print("Friend 2 is older")
    else:
        print("Same age")

age1 = int(input())
age2 = int(input())
who_is_older(age1, age2)
