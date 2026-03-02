import math

times = [int(t) for t in input().split(' ')]
left_time = 0
right_time = 0

for i in range(len(times) // 2):
    time_to_add = times[i]
    if time_to_add == 0:
        left_time *= 0.8
    else:
        left_time += time_to_add

for i in range(-1, -len(times) // 2, -1):
    time_to_add = times[i]
    if time_to_add == 0:
        right_time *= 0.8
    else:
        right_time += time_to_add


winner = "left"
time = 0
if left_time <= right_time:
    time = left_time
else:
    time = right_time
    winner = "right"
print(f"The winner is {winner} with total time: {time:.1f}")
