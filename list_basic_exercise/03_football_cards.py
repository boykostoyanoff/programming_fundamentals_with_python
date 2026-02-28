team_a = [x for x in range(1, 12)]
team_b = [x for x in range(1, 12)]
cards = input().split()

while cards:
    card = cards.pop(0)
    card = card.split('-')
    team = card[0]
    number = int(card[1])

    if team == 'A':
        if number in team_a:
            team_a.remove(number)
    elif team == 'B':
        if number in team_b:
            team_b.remove(number)
    if len(team_a) < 7 or len(team_b) < 7:
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if len(team_a) < 7 or len(team_b) < 7:
    print("Game was terminated")