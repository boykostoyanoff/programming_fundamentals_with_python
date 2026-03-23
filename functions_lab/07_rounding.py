
numbers = [float(n) for n in input().split(' ')]

result = lambda nums:[round(n) for n in nums]
print(result(numbers))