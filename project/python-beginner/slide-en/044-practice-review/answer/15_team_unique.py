raw = ["C", "A", "B", "A"]
team = []
for name in raw:
    if name not in team:
        team.append(name)
team.sort()
print(team)
