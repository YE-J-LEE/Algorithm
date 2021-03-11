import sys

N, S, M = map(int, sys.stdin.readline().split())
V = [0] + list(map(int, sys.stdin.readline().split()))
DP = [[0]*(M+1) for _ in range(N+1)]

def solve(i, prv):
    if i==N:
        ret = 0
        if 0 <= prv + V[i] <= M:
            return max(prv + V[i], ret)

        if 0 <= prv - V[i] <= M:
            return max(prv - V[i], ret)
        return -1

    if DP[i][prv]:
        return DP[i][prv]

    DP[i][prv] = -1
    if 0 <= prv + V[i] <= M:
        DP[i][prv] = max(DP[i][prv], solve(i+1, prv + V[i]))

    if 0 <= prv - V[i] <= M:
        DP[i][prv] = max(DP[i][prv], solve(i+1, prv - V[i]))

    if DP[i][prv] == -1:
        return -1
    else:
        return DP[i][prv]

print(solve(1, S))