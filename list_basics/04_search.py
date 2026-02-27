n = int(input())
word = input()
words = list()

for i in range(n):
    words.append(input())

print(words)
words = [w for w in words if word in w]
print(words)