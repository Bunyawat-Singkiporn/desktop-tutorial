def create_player(name):
    return {"name": name, "hp": 100}

def take_damage(player, dmg):
    player["hp"] = player["hp"] - dmg
    if player["hp"] < 0:
        player["hp"] = 0

def is_alive(player):
    return player["hp"] > 0

def show_status(player):
    print("=== Player Status ===")
    print(f"Name: {player['name']}")
    print(f"HP: {player['hp']}")
    if is_alive(player):
        print("Status: Alive")
    else:
        print("Status: Dead")

name = input()
dmg = int(input())
player = create_player(name)
take_damage(player, dmg)
show_status(player)
