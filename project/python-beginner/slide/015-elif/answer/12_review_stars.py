stars = int(input())

if stars == 5:
    review = "Excellent"
elif stars == 4:
    review = "Good"
elif stars == 3:
    review = "Average"
else:
    review = "Poor"

print(f"Stars  : {stars}")
print(f"Review : {review}")
