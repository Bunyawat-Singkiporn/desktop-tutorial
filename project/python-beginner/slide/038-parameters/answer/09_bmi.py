def health_card(weight, height):
    bmi = weight / (height ** 2)
    print("Health Card")
    print(f"Weight: {weight} kg")
    print(f"Height: {height} m")
    print(f"BMI: {bmi:.2f}")

weight = float(input())
height = float(input())
health_card(weight, height)
