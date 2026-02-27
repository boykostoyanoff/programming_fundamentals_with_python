numbers = int(input())
positive_number = list()
negative_number = list()

for i in range(numbers):
    number = int(input())
    if number < 0:
        negative_number.append(number)
    else:
        positive_number.append(number)

print(positive_number)
print(negative_number)
print(f"Count of positives: {len(positive_number)}")
print(f"Sum of negatives: {sum(negative_number)}")