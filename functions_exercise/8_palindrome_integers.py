numbers = [n for n in input().split(', ')]


def is_palindrome(num):
    if len(num) == 1:
        return True
    mid = len(num) // 2
    left = num[:mid]
    right = num[len(num) - mid:]
    right = right[::-1]
    return left == right


for num in numbers:
    print(is_palindrome(num))
