numbers = [int(n) for n in input().split(', ')]
beggars = int(input())
result = [0 for _ in range(beggars)]

i = 0

for j in range(len(numbers)):
    result[i] += numbers[j]
    i += 1
    if i == beggars:
        i = 0
print(result)