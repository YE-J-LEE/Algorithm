import sys

N, M = map(int, sys.stdin.readline().split())
partialSum = [0] + list(map(int, sys.stdin.readline().split()))
answer = 0
# 기본은 누적합 개념이지만 모듈러의 분배법칙을 적용하는 문제
for i in range(1, N+1):
    partialSum[i] += partialSum[i-1]
for i in range(1, N+1):
    partialSum[i] %= M
R = {}
for i in range(1, N+1):
    remain = partialSum[i]
    if remain in R:
        R[remain] += 1
    else:
        R[remain] = 1
if 0 in R:
    answer += R[0]
for cnt in R.values():
    answer += cnt*(cnt-1)//2
print(answer)
