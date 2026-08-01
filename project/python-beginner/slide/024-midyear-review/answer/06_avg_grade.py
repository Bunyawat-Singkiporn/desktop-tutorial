s1 = int(input())
s2 = int(input())
s3 = int(input())
avg = (s1 + s2 + s3) / 3
print(f"{avg:.1f}")
if avg >= 80:
    print("A")
elif avg >= 60:
    print("B")
else:
    print("C")
