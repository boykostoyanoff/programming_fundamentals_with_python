places = input()
destinations = list()
travel_points = 0
places_list = places.split('=')
places_list.extend(places.split('/'))

for p in places_list:
    if len(p) < 3:
        continue
    if not p.isalpha():
        continue
    if not p[0].isupper():
        continue
 
    destinations.append(p)
    travel_points += len(p)

print("Destinations: ", end='')
print(', '.join(destinations))
print(f"Travel Points: {travel_points}")