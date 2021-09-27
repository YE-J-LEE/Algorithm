import sys
from itertools import combinations

# BOJ 15661
# 팀을 두 개로 나누고 문제에서 설명하는 바와 같이 각 팀의 점수를 매겨
# 두 팀 점수차의 최솟값을 구하는 문제이다.
# 조합을 통한 완전탐색으로 풀어냈다. 파이썬의 내장함수를 사용했지만
# Python으로 통과하진 못 했고 Pypy를 통해 성공한 후 조금 더 개선시켜서 3초 내로 완성할 수 있었다..

N = int(sys.stdin.readline())
team = set(range(1, N+1))
stat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 1e9
for i in range(1, N//2+1):
    for comb in combinations(range(1, N+1), i):
        start = set(comb)
        link = team - start
        statOfStart = 0
        statOfLink = 0
        for pair in combinations(link, 2):
            x, y = pair
            statOfLink += stat[x-1][y-1]
            statOfLink += stat[y-1][x-1]
        if i == 1:
            answer = min(answer, statOfLink)
            continue
        for pair in combinations(start, 2):
            x, y = pair
            statOfStart += stat[x-1][y-1]
            statOfStart += stat[y-1][x-1]
        answer = min(answer, abs(statOfStart-statOfLink))
print(answer)