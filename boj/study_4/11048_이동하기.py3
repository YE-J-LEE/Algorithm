import sys
sys.setrecursionlimit(100000)
N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
DP = [[-1]*M for _ in range(N)]

def solve(i, j):
    if i==N-1 and j==M-1:
        return maze[i][j]

    if DP[i][j] != -1:
        return DP[i][j]

    DP[i][j] = -1
    np = [(i+1, j), (i, j+1), (i+1, j+1)]
    for nx, ny in filter(lambda x: -1<x[0]<N and -1<x[1]<M, np):
        DP[i][j] = max(DP[i][j], solve(nx, ny)+maze[i][j])

    return DP[i][j]

print(solve(0, 0))