seats = ["A", "B", "C", "D"]
for row in range(1, 4):
    print(f"Row{row}:", end=" ")
    for seat in seats:
        print(seat, end=" ")
    print()
