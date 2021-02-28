import sys
N = int(sys.stdin.readline())
numbers = [0]
for _ in range(N):
    numbers.append(float(sys.stdin.readline()))

if N==1:
    print(numbers[1])
else:
    DP = [0] * (N + 1)
    DP[1] = numbers[1]
    DP[2] = max(numbers[1], numbers[2], numbers[1]*numbers[2])
    for i in range(2, N+1):
        DP[i] = max(numbers[i], DP[i-1]*numbers[i])
    print('%.3f'%round(max(DP[1:]), 3))