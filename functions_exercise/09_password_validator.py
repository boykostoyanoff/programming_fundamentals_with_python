password = input()

def is_valid_password_message(word: str):
    message = list()
    if len(word) < 6 or len(word) > 10:
        message.append("Password must be between 6 and 10 characters")
    for ch in word:
        if not (ch.isdigit() or ch.isalpha()):
            message.append("Password must consist only of letters and digits")
            break
    digit_count = 0
    for ch in word:
        if ch.isdigit():
            digit_count += 1
    if digit_count < 2:
        message.append("Password must have at least 2 digits")
    if len(message) == 0:
        message.append("Password is valid")

    return message

print('\n'.join(is_valid_password_message(password)))


