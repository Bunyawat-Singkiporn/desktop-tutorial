weight = float(input())
height = float(input())

bmi = weight / (height ** 2)

if bmi >= 30:
    band = "Obese"
elif bmi >= 25:
    band = "Overweight"
elif bmi >= 18.5:
    band = "Normal"
else:
    band = "Underweight"

print(f"BMI  : {bmi:.1f}")
print(f"Band : {band}")
