def add_name(names, name):
    names.append(name)

def show_names(names):
    for name in names:
        print(name)

names = []
n = int(input("How many campers? "))
for i in range(n):
    add_name(names, input("Name: "))

print("=== Camp List ===")
show_names(names)
