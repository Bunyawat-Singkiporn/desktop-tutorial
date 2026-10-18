def add_saving(saved, amount):
    return saved + amount

def report(saved, goal):
    print(f"Saved: {saved}")
    need = goal - saved
    if need < 0:
        need = 0
    print(f"Need: {need}")
    if saved >= goal:
        print("Done")
    else:
        print("Keep going")

goal = int(input())
saved = 0
for i in range(3):
    amount = int(input())
    saved = add_saving(saved, amount)

report(saved, goal)
