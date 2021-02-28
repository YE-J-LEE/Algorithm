import sys

N = int(sys.stdin.readline())
numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

# 1 1 2 3 4 5
# 1 5  6 7 8 12 8
# 5 2 2 2 2
sub = 0
for i in range(N-1, 0, -1):
    if numbers[i-1] >= numbers[i]:
        sub += numbers[i-1]-numbers[i]+1
        numbers[i-1] = numbers[i]-1

print(sub)