def sum_numbers(a, b):
    result = a +b
    return result

def subtrack(s, c):
    result = s - c
    return result

def add_and_subtrack(a, b, c):
    result = subtrack(sum_numbers(a, b), c)
    return result

a = int(input())
b = int(input())
c = int(input())

print(add_and_subtrack(a, b, c))