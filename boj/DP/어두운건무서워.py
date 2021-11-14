import sys

# BOJ 16507
# 누적합을 사용해도 파이썬 기준 4.3초가 되어야 통과한다. 이런 비슷한 문제를 비트마스킹으로 푼 사람도 있었던 것 같은데
# 시간이 날 때 비트마스킹 방법도 연구해봐야겠다.

R, C, Q = map(int, sys.stdin.readline().split())
matrix = [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(R)]
for i in range(R):
    for j in range(1, C+1):
        matrix[i][j] += matrix[i][j-1]
for _ in range(Q):
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
    N = (r2-r1+1)*(c2-c1+1)
    answer = 0
    for i in range(r1-1, r2):
        answer += matrix[i][c2] - matrix[i][c1-1]
    print(answer//N)


