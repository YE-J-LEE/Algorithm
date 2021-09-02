import sys

# LIS 문제의 응용 버전이다.
# 처음엔 DP 설정을 자기 자신 위치까지 제일 긴 길이를 저장해놨었는데 이렇게 해버리니 자기 자신이 포함되지 않는 상태에서의 길이까지 걸어두어서
# 그 뒤로의 감소하는 (LIS의 역) 부분의 시작 위치가 잘못 설정되었다. 그래서 자기 자신까지 포함해서 가장 긴 길이를 담도록 수정하고
# 더해줘서 성공할 수 있었다.

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
LIS = [1]*N
LIS2 = [1]*N
for i in range(N):
    for j in range(i):
        if A[j] < A[i] and LIS[j] + 1 > LIS[i]:
            LIS[i] = LIS[j] + 1
rA = A[::-1]
for i in range(N):
    for j in range(i):
        if rA[j] < rA[i] and LIS2[j] + 1 > LIS2[i]:
            LIS2[i] = LIS2[j] + 1
for i in range(N):
    LIS[i] += LIS2[N-i-1]
print(max(LIS)-1)