def is_perfect_number(num: str):
    number = int(num)
    sum_digits = 0
    for n in range(1, number):
        if number % int(n) == 0:
            sum_digits += int(n)
            if sum_digits > number:
                return False
    if number == sum_digits:
        return True
    else:
        return False


number = input()
if is_perfect_number(number):
    print(f"We have a perfect number!")
else:
    print(f"It's not so perfect.")