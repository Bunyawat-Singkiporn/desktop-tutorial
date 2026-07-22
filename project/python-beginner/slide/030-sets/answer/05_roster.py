room_a = ["Alice", "Bob", "Charlie", "Diana"]
room_b = ["Bob", "Eve", "Charlie", "Frank"]

set_a = set(room_a)
set_b = set(room_b)

all_students = set_a | set_b
both_rooms = set_a & set_b
only_one = all_students - both_rooms

print("Total unique students:", len(all_students))
print("In both rooms:", both_rooms)
print("Only in one room:", only_one)
