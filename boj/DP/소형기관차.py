import sys

N = int(sys.stdin.readline())
train = [0] + list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
for i in range(1, N+1):
    train[i] += train[i-1]
    
# N * logN 욕심이 나지만 이진탐색을 하기 위한 오름 / 내림차순 같은 규칙이 없다
# 이럴때 최소 및 최대인 경우 DP로 방향을 빠르게 틀자
# DP로 틀어도 답이 잘 안 보이면 DP[N][K]같이 세워두고 차근 차근 쌓아가는 것을 이미지화 하자
DP = [[0]*3 for _ in range(N+1)]
DP[M][0] = train[M]
for i in range(M+1, N+1):
    DP[i][0] = max(DP[i-1][0], train[i]-train[i-M])
    DP[i][1] = DP[i-1][1]
    DP[i][2] = DP[i-1][2]
    if i >= 2*M:
        DP[i][1] = max(DP[i][1], DP[i-M][0] + train[i]-train[i-M])
    if i >= 3*M:
        DP[i][2] = max(DP[i][2], DP[i-M][1] + train[i]-train[i-M])
print(DP[N][2])
