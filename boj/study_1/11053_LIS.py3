import sys

n = int(sys.stdin.readline())
DP = [1]*n
numbers = list(map(int, sys.stdin.readline().split()))
for i in range(1, n):
    for j in range(0, i):
        if numbers[j] < numbers[i]:
            DP[i] = max(DP[i], DP[j]+1)
print(max(DP))