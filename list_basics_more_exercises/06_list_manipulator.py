numbers = [int(n) for n in input().split(' ')]

while True:
    command = input()
    if command == "end":
        break

    command = command.split()
    action = command[0]

    if action == "exchange":
        idx = int(command[1])
        if idx == len(numbers) - 1:
            pass
        elif not (0 <= idx < len(numbers)):
            print("Invalid index")
        else:
            left = numbers[:idx + 1]
            right = numbers[idx + 1:]
            numbers = list(right + left)
    elif action == "max":
        max_number = ''
        action_type = command[1]
        sorted_numbers = list()
        if action_type == "even":
            sorted_numbers = [n for n in numbers if n % 2 == 0]
        elif action_type == "odd":
            sorted_numbers = [n for n in numbers if not (n % 2 == 0)]
        if not sorted_numbers:
            print("No matches")
        else:
            max_number = max(sorted_numbers)
            max_number_index = 0
            for i in range(len(numbers)):
                if numbers[i] == max_number:
                    max_number_index = i
            print(max_number_index)
    elif action == "min":
        max_number = ''
        action_type = command[1]
        sorted_numbers = list()
        if action_type == "even":
            sorted_numbers = [n for n in numbers if n % 2 == 0]
        elif action_type == "odd":
            sorted_numbers = [n for n in numbers if not (n % 2 == 0)]
        if not sorted_numbers:
            print("No matches")
        else:
            max_number = min(sorted_numbers)
            max_number_index = 0
            for i in range(len(numbers)):
                if numbers[i] == max_number:
                    max_number_index = i
            print(max_number_index)
    elif action == "first":
        count_ = int(command[1])
        sorted_numbers = list()
        if command[2] == "even":
            sorted_numbers = [n for n in numbers if n % 2 == 0]
        elif command[2] == "odd":
            sorted_numbers = [n for n in numbers if not (n % 2 == 0)]

        if count_ >= len(numbers):
            print("Invalid count")
        else:
            if count_ > len(sorted_numbers):
                count_ = len(sorted_numbers)
            print(sorted_numbers[:count_])
    elif action == "last":
        count_ = int(command[1])
        sorted_numbers = list()
        if command[2] == "even":
            sorted_numbers = [n for n in numbers if n % 2 == 0]
        elif command[2] == "odd":
            sorted_numbers = [n for n in numbers if not (n % 2 == 0)]

        if count_ > len(numbers):
            print("Invalid count")
        else:
            if count_ > len(sorted_numbers):
                count_ = len(sorted_numbers)
            print(sorted_numbers[-count_:])


print(numbers)