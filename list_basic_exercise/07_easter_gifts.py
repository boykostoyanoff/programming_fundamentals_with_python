gifts = input().split(' ')
command = input()

while not command == "No Money":
    command = command.split(' ')
    action = command[0]
    gift = command[1]

    if action == "OutOfStock":
        for i in range(len(gifts)):
            if gift == gifts[i]:
                gifts[i] = None
    elif action == "Required":
        idx = int(command[2])
        if 0 <= idx < len(gifts):
            gifts[idx] = gift
    elif action == "JustInCase":
        gifts[-1] = gift

    command = input()

print(' '.join(g for g in gifts if not g is None))