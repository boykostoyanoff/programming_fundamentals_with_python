numbers = input().split(' ')
words = list(input())
message = ""
for number in numbers:
    index = 0
    for digit in number:
        index += int(digit)
    while index >= len(words):
        index -= len(words)
    message += words.pop(index)

print(message)
