import sys

# 이제는 기본이 되어버린 LCS 문제이다..
# 저번에 팰린드롬 만들기 문제에서 다시금 환기되었고 원래부터 LCS는 제대로 이해가 되지 않은 상태라
# 풀어놓지 않고 있었다. 이제는 내가 다룰 수 있는 알고리즘이라고 생각되어 문제를 풀었다.

S1 = 'O' + sys.stdin.readline().rstrip()
S2 = 'O' + sys.stdin.readline().rstrip()
N1 = len(S1)
N2 = len(S2)
DP = [[0]*N2 for _ in range(N1)]
for i in range(1, N1):
    for j in range(1, N2):
        if S1[i] == S2[j]:
            DP[i][j] = DP[i-1][j-1] + 1
        else:
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])
print(DP[N1-1][N2-1])

