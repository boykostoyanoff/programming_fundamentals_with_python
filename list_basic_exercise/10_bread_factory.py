energy = 100
coins = 100
is_day_completed = True

events = input().split('|')

for event in events:
    event = event.split('-')
    if event[0] == 'rest':
        energy_gained = int(event[1])
        if energy + energy_gained > 100:
            energy_gained = 100 - energy
        energy += energy_gained
        print(f"You gained {energy_gained} energy.")
        print(f"Current energy: {energy}.")

    elif event[0] == 'order':
        energy_decreased = 30
        if energy >= energy_decreased:
            coins_earned = int(event[1])
            coins += coins_earned
            energy -= energy_decreased
            print(f"You earned {coins_earned} coins.")
        else:
            energy += 50
            print(f"You had to rest!")
    else:
        ingredient = event[0]
        coins_spend = int(event[1])
        if coins >= coins_spend:
            print(f"You bought {ingredient}.")
            coins -= coins_spend
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            is_day_completed = False
            break

if is_day_completed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")