favourites = []
favourites.append("mango")
favourites.append("apple")
favourites.append("cherry")
favourites.append("kiwi")
favourites.append("grape")

to_remove = favourites[2]
favourites.remove(to_remove)

favourites.sort()

print("Removed:", to_remove)
print(favourites)
