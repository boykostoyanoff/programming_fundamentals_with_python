from faulthandler import cancel_dump_traceback_later

train_ticket_price = 150
clothes_max_price = 50
shoes_max_price = 35
accessories_max_price = 20.5

items = input()
budget = float(input())
bought_items = list()
items = items.split('|')
for item in items:
    item = item.split("->")
    item_type = item[0]
    item_price = float(item[1])

    if (not (item_type == "Clothes" and item_price <= clothes_max_price) and
     not (item_type == "Shoes" and item_price <= shoes_max_price) and
    not (item_type == "Accessories" and item_price <= accessories_max_price)):
        continue

    if budget >= item_price:
        budget -= item_price
        bought_items.append(item_price)

sold_items = [price * 1.4 for price in bought_items]
print(' '.join(f"{price:.2f}" for price in sold_items))

profit = sum(sold_items) - sum(bought_items)
print(f"Profit: {profit:.2f}")
budget += sum(sold_items)
if budget >= train_ticket_price:
    print(f"Hello, France!")
else:
    print("Not enough money.")