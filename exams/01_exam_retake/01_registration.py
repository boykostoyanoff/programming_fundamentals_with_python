username = input()

command = input()

while not command == "Registration":
    command = command.split(' ')
    action = command[0]

    if action == "Letters":
        if command[1] == "Lower":
            username = username.lower()
            print(username)
        elif command[1] == "Upper":
            username = username.upper()
            print(username)

    elif action == "Reverse":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index <= end_index < len(username):
            temp_string = username[start_index:end_index + 1]
            temp_string_reversed = ''
            for i in range(-1, -len(temp_string) - 1, -1):
                temp_string_reversed += temp_string[i]

            print(temp_string_reversed)

    elif action == "Substring":
        substring = command[1]
        if substring in username:
            username = username.replace(substring, '')
            print(username)
        else:
            print(f"The username {username} doesn't contain {substring}.")

    elif action == "Replace":
        ch = command[1]
        username = username.replace(ch, '-')
        print(username)

    elif action == "IsValid":
        ch = command[1]
        if ch in username:
            print(f"Valid username.")
        else:
            print(f"{ch} must be contained in your username.")


    command = input()
