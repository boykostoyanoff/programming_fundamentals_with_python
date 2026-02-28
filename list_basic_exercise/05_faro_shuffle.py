deck = input().split(' ')
shuffles = int(input())
middle = len(deck) // 2

for _ in range(shuffles):
    left_deck = deck[:middle]
    right_deck = deck[middle:]
    temp_deck = list()
    for i in range(middle):
        temp_deck.append(left_deck[i])
        temp_deck.append(right_deck[i])

    deck = temp_deck

print(deck)