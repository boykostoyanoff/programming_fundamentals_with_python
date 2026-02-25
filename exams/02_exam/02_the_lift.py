waiting_people = int(input())
lift = [int(x) for x in input().split(' ')]

for i in range(len(lift)):
    while lift[i] < 4 and waiting_people > 0:
        lift[i] += 1
        waiting_people -= 1

if lift[-1] < 4:
    print("The lift has empty spots!")
elif waiting_people > 0:
    print(f"There isn't enough space! {waiting_people} people in a queue!")

print(' '.join(str(w) for w in lift))