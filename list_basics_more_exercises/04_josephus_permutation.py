peoples = [int(p) for p in input().split(' ')]
k = int(input())
killed = list()

index_to_kill = 0

while peoples:
    index_to_kill += k - 1
    while index_to_kill >= len(peoples):
        index_to_kill -= len(peoples)
    killed.append(peoples.pop(index_to_kill))

print("[" + ','.join([str(k) for k in killed]) + ']')