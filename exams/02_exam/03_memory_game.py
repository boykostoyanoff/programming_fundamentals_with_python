elements = input().split(' ')
command = input()
turns = 0

while (not command == "end") and len(elements) > 1:
    turns += 1
    command = command.split(' ')
    first = int(command[0])
    second = int(command[1])

    if (not 0 <= first < len(elements)) or (not 0 <= second < len(elements)) or first == second:
        element_to_add = f"-{turns}a"
        index_to_add = len(elements) // 2
        elements.insert(index_to_add, element_to_add)
        elements.insert(index_to_add, element_to_add)
        print("Invalid input! Adding additional elements to the board")
    else:
        if elements[first] == elements[second]:
            element_to_pop = elements[first]
            if first > second:
                first, second = second, first
            elements.pop(second)
            elements.pop(first)
            print(f"Congrats! You have found matching elements - {element_to_pop}!")
        else:
            print("Try again!")

    command = input()

if not elements:
    print(f"You have won in {turns} turns!")
else:
    print(f'Sorry you lose :(')
    print(' '.join(elements))