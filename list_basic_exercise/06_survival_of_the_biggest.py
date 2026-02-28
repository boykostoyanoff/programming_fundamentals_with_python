numbers = [int(n) for n in input().split(' ')]
numbers_to_remove = int(input())
numbers_sort = sorted(numbers)

for i in range(numbers_to_remove):
    numbers.remove(numbers_sort[i])

print(', '.join([str(n) for n in numbers]))