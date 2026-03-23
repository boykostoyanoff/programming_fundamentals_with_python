def get_chars_between_two_chars(ch1: chr, ch2: chr):
    result = ""
    for i in range(ord(ch1) + 1, ord(ch2)):
        result += chr(i) + ' '

    return result

ch1 = input()
ch2 = input()

print(get_chars_between_two_chars(ch1, ch2))