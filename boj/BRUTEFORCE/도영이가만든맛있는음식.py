import sys
from itertools import combinations

# BOJ 2961
# 조합을 통한 완전탐색 문제이다.
# 완전탐색을 해도 대략 5000개? 정도의 가짓수가 나오기 때문에 쉽게 풀 수 있었다.
# 알고리즘 분류에 비트마스킹이 있던데, 몸이 좀 괜찮아지면 비트마스킹 풀이도 공부해봐야겠다.

answer = 1e9

N = int(sys.stdin.readline())
S, B = [], []
for _ in range(N):
    s, b = map(int, sys.stdin.readline().split())
    S.append(s)
    B.append(b)
for i in range(1, N+1):
    for comb in combinations(range(N), i):
        mulOf = 1
        sumOf = 0
        for idx in comb:
            mulOf *= S[idx]
            sumOf += B[idx]
        answer = min(answer, abs(mulOf-sumOf))
print(answer)
















