exam = int(input())
portfolio = int(input())

if exam >= 70 and portfolio >= 50:
    result = "Offer"
elif exam >= 90 or portfolio >= 80:
    result = "Waitlist"
else:
    result = "Reject"

print("========================")
print("        CLUB")
print("========================")
print(f"Exam      : {exam}")
print(f"Portfolio : {portfolio}")
print(f"Result    : {result}")
print("========================")
