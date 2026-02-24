import re

places = input()

pattern = r"([=/])([A-Z]{1}[a-zA-z]{2,})\1"

destinations = list()

for mach in re.finditer(pattern, places):
    destinations.append(mach.group(2))

print("Destinations: ", end='')
print(', '.join(destinations))
travel_points = sum(len(d) for d in destinations)
print(f"Travel Points: {travel_points}")