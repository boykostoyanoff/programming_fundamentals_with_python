from itertools import count

board = [[line for line in input().split(' ')] for i in range(3)]
winner = "Draw!"
lines = [line for line in board]
for cow in range(3):
    line = list()
    for rol in range(3):
        line.append(board[rol][cow])
    lines.append(line)

left_diagonal = list()
right_diagonal = list()
for i in range(3):
    left_diagonal.append(board[i][i])
    right_diagonal.append(board[i][-1 - i])
lines.append(left_diagonal)
lines.append(right_diagonal)

for line in lines:
    if line.count('1') == 3:
        winner = "First player won"
        break
    if line.count('2') == 3:
        winner = "Second player won"
        break
print(winner)