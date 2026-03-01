fires = input().split('#')
water = int(input())
cells = list()

for fire in fires:
    fire = fire.split(' = ')
    type_of_fire = fire[0]
    fire_range = int(fire[1])

    if (not (type_of_fire == "High" and 81 <= fire_range <= 125)
            and not (type_of_fire == "Medium" and 51 <= fire_range <= 80)
            and not (type_of_fire == "Low" and 1 <= fire_range <= 50)):
        continue
    if water >= fire_range:
        cells.append(fire_range)
        water -= fire_range

total_fire = sum(cells)
effort = total_fire * 0.25
print("Cells:")
for cell in cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")