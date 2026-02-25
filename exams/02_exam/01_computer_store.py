total_price = 0
price_without_taxes = 0
taxes = 0
while True:
    command = input()
    if command == "special":
        taxes += price_without_taxes * 0.2
        total_price = (price_without_taxes + taxes) * 0.9
        break
    if command == "regular":
        taxes += price_without_taxes * 0.2
        total_price = price_without_taxes + taxes
        break

    sum_to_add = float(command)
    if sum_to_add <= 0:
        print("Invalid price!")
    else:
        price_without_taxes += sum_to_add

if total_price == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")