numbers = [int(n) for n in input().split(' ')]

print(list(filter((lambda n: n % 2 == 0), numbers)))