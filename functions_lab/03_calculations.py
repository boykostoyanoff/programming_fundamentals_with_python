action = input()
first_number = int(input())
second_number = int(input())

def calculate(act: str, a: int, b: int):
    result = None
    if act == "multiply":
        result = a * b
    elif act == "divide":
        if not b == 0:
            result = a / b
    elif act == "add":
        result = a + b
    elif act == "subtract":
        result = a - b
    return int(result)

print(calculate(action ,first_number, second_number))