def data_types(text: str, num):
    result = None
    if text == "int":
        num = int(num)
        result = num * 2
    elif text == "real":
        num = float(num)
        num = 1.5 * num
        result = f"{num:.2f}"
    elif text == "string":
        result = f"${num}$"

    return result

txt = input()
number = input()

print(data_types(txt, number))