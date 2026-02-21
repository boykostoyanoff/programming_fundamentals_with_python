number = float(input())
result = ''

if number == 0:
    result = "zero"
elif number < 0:
    result = "negative"
elif number > 0:
    result = "positive"

if 0 < abs(number) < 1:
    result = f"small {result}"
elif abs(number) > 1000:
    result = f"large {result}"

print(result)