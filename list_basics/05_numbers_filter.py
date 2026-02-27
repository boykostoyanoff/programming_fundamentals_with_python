n = int(input())
numbers = list()
for i in range(n):
    numbers.append(int(input()))

action = input()

if action == "even":
    numbers = [n for n in numbers if n % 2 == 0]
elif action == "odd":
    numbers = [n for n in numbers if n % 2 == 1]
elif action == "negative":
    numbers = [n for n in numbers if n < 0]
elif action == "positive":
    numbers = [n for n in numbers if n >= 0]

print(numbers)