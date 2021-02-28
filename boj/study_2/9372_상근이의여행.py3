import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    for _ in range(M):
        x, y = map(int, sys.stdin.readline().split())
    print(N-1)