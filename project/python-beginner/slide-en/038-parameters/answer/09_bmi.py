def show_bmi(weight, height):
    bmi = weight / (height ** 2)
    print(f"BMI: {bmi:.2f}")

weight = float(input())
height = float(input())
show_bmi(weight, height)
