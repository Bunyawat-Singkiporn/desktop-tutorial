present = int(input())
report = int(input())

if present >= 40 and report >= 40:
    result = "Pass"
else:
    result = "Fail"

print("========================")
print("       PROJECT")
print("========================")
print(f"Present : {present}")
print(f"Report  : {report}")
print(f"Result  : {result}")
print("========================")
