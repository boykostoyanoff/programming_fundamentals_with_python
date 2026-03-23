number = input()


def get_sum_of_odd_and_even_digits(number):
    odd_sum = 0
    even_sum = 0
    for digit in number:
        num = int(digit)
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    result = f"Odd sum = {odd_sum}, Even sum = {even_sum}"
    return result


print(get_sum_of_odd_and_even_digits(number))