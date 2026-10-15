def add_name(names, name):
    names.append(name)
    return names

def show_names(names):
    for n in names:
        print(n)

names = []
names = add_name(names, "Ann")
names = add_name(names, "Ben")
show_names(names)
