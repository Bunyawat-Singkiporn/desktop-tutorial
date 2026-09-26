def create_player(name):
    return {"name": name, "hp": 100}

def take_damage(player, dmg):
    player["hp"] = player["hp"] - dmg

def is_alive(player):
    if player["hp"] > 0:
        return True
    else:
        return False

def show_status(player):
    print(f"Name: {player['name']}")
    print(f"HP: {player['hp']}")

p = create_player("Hero")
take_damage(p, 40)
show_status(p)
print(is_alive(p))
