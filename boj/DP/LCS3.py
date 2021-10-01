import sys

# BOJ 1958
# 3개의 문자열에 대한 LCS를 구하는 문제라 3차원 DP 배열이 필요했다.
# 그런데 3차원이기 때문에 점화식을 구하기 위해 종이에 써내려가는 것이 어려웠다.
# 3차원을 2차원인 종이에 표현하려니... 머리도 복잡해져 어려움이 있었지만 상상력을 총동원해 점화식을 구해냈다..

S1 = 'X' + sys.stdin.readline().rstrip()
S2 = 'X' + sys.stdin.readline().rstrip()
S3 = 'X' + sys.stdin.readline().rstrip()
L1 = len(S1)
L2 = len(S2)
L3 = len(S3)
DP = [[[0]*L3 for _ in range(L2)] for _ in range(L1)]
for i in range(1, L1):
    for j in range(1, L2):
        for k in range(1, L3):
            if S1[i] == S2[j] == S3[k]:
                DP[i][j][k] = DP[i-1][j-1][k-1] + 1
            else:
                DP[i][j][k] = max(DP[i-1][j][k], DP[i][j-1][k], DP[i][j][k-1])
print(DP[L1-1][L2-1][L3-1])