numbers = input().split(', ')
numbers = [int(n) for n in numbers]
zero_count = numbers.count(0)
numbers = [n for n in numbers if not n == 0]
numbers.extend([0 for _ in range(zero_count)])
print(numbers)