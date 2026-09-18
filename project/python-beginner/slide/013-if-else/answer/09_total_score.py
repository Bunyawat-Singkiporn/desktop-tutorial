work_score = int(input())
exam_score = int(input())

total = work_score + exam_score

if total >= 100:
    result = "Qualified"
else:
    result = "Not Qualified"

print(f"Total  : {total}")
print(f"Result : {result}")
