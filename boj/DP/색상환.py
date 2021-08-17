import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
answer = 0

# pick first color
DP = [[0]*(K+1) for _ in range(N+1)]
DP[1][1] = 1
DP[2][1] = 1

for i in range(3, N):
    for j in range(1, K+1):
        DP[i][j] = DP[i-1][j] + DP[i-2][j-1]
answer += DP[N-1][K]

# don't pick first
DP = [[0]*(K+1) for _ in range(N+1)]
DP[1][0] = 1
DP[2][0] = 1
DP[2][1] = 1
for i in range(3, N+1):
    DP[i][0] = 1
    for j in range(1, K+1):
        DP[i][j] = DP[i-1][j] + DP[i-2][j-1]
answer += DP[N][K]
print(answer%1000000003)