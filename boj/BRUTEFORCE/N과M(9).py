import sys
from itertools import permutations

# BOJ 15663
# 순열을 이용한 문제로, 내장함수를 통해 쉽게 구할 수 있다.
# 현재 solve.ac의 class4를 달성시키기 위해 푸는 중이라 문제 난이도가 많이 하락한 경향이 있다.

N, M = map(int, sys.stdin.readline().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))
visited = set()
for p in permutations(numbers, M):
    if p not in visited:
        visited.add(p)
        print(*p)



