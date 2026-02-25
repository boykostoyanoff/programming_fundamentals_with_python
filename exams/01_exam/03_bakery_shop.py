command = input()
foods = dict()
sold_quantity = 0
while not command == "Complete":
    action, quantity, food = command.split()
    quantity = int(quantity)

    if action == "Receive":
        if food in foods.keys():
            foods[food] += quantity
        else:
            foods[food] = quantity

    elif action == "Sell":
        if food not in foods.keys():
            print(f"You do not have any {food}.")
        else:
            if quantity > foods[food]:
                print(f"There aren't enough {food}. You sold the last {foods[food]} of them.")
                sold_quantity += foods[food]
                foods[food] = 0
            else:
                print(f"You sold {quantity} {food}.")
                foods[food] -= quantity
                sold_quantity += quantity
            if foods[food] == 0:
                foods.pop(food)
    command = input()

for (k, v) in foods.items():
    print(f"{k}: {v}")
print(f"All sold: {sold_quantity} goods")