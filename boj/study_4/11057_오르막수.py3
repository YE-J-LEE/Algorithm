import sys

N = int(sys.stdin.readline())
DP = [[0]*(10) for _ in range(N+1)]
if N==1:
    print(10)
else:
    for k in range(10):
        DP[1][k] = 1
    for i in range(2, N+1):
        for j in range(10):
            if j==0:
                DP[i][j] += DP[i-1][0]
            else:
                DP[i][j] += sum(DP[i-1][:j+1])
    print(sum(DP[N])%10007)