def print_smallest_of_three_numbers(a, b, c):
    if a > b:
        a = b
    if a > c:
        a = c
    print(a)

a = int(input())
b = int(input())
c = int(input())

print_smallest_of_three_numbers(a, b, c)