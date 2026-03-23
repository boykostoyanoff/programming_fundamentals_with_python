def get_product_price(prod: str):
    price = 0.0
    if prod == "coffee":
        price = 1.50
    elif prod == "water":
        price = 1.00
    elif prod == "coke":
        price = 1.40
    elif prod == "snacks":
        price = 2.00

    return price

product_name = input()
quantity = int(input())
total_price = quantity * get_product_price(product_name)
print(f"{total_price:.2f}")