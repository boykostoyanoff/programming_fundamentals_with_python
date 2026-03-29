def loading_bar(num: int):
    bar = ['.']
    if num == 100:
        bar = "100% Complete!" + "\n" + "[%%%%%%%%%%]"
    else:
        bar = f"{num}% [{(num // 10) * '%'}{(10 - (num // 10)) * '.'}]" + '\n' + "Still loading..."
    return bar
number = int(input())
print(loading_bar(number))