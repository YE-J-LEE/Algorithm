import sys
from itertools import combinations_with_replacement

# BOJ 15666
# 완전탐색으로 풀려다 틀려버리고 파이썬 라이브러리 함수를 통해 풀어냈는데..
# 문제 분류를 보니 백트래킹이었다. 적당한 시점에서 브레이크를 걸었어야 했던 것 같다..

N, M = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))
visited = set()
for comb in combinations_with_replacement(arr, M):
    if comb not in visited:
        visited.add(comb)
        print(*list(comb))



