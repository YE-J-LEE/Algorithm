import sys

sentence = sys.stdin.readline().rstrip()
i = 0
real = ''
hidden = ['a', 'e', 'i', 'o', 'u']
while i < len(sentence):
    if sentence[i] not in hidden:
        real += sentence[i]
        i += 1
    else:
        real += sentence[i]
        i += 3
print(real)