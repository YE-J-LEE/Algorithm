import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n, k = map(int, sys.stdin.readline().split())
    DP = [[[0]*2 for _ in range(k+1)] for _ in range(n)]
    DP[0][0][0] = 1
    DP[0][0][1] = 1
    for i in range(1, n):
        DP[i][0][0] = DP[i-1][0][0] + DP[i-1][0][1]
        DP[i][0][1] = DP[i-1][0][0]
        for j in range(1, k+1):
            DP[i][j][0] = DP[i-1][j][0] + DP[i-1][j][1]
            DP[i][j][1] = DP[i-1][j][0] + DP[i-1][j-1][1]
    print(sum(DP[n-1][k]))