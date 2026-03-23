def round_numbers_with_round(nums: list):
    nums_round = [round(n) for n in nums]
    return nums_round
numbers = [float(n) for n in input().split(' ')]
print(round_numbers_with_round(numbers))