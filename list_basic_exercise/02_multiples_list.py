factor = int(input())
count = int(input())
numbers = list()
for i in range(1, count + 1, 1):
    numbers.append(i * factor)

print(numbers)