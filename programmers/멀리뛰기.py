# 프로그래머스
# 이 문제는 전형적인 DP 문제였고 꽤 쉬운 편이었다.

def solution(n):
    answer = 0
    DP = [[0] * 3 for _ in range(n + 1)]
    DP[1][1] = 1
    DP[0][1] = 1
    mod = 1234567
    for i in range(2, n + 1):
        DP[i][1] = sum(DP[i - 1]) % mod
        DP[i][2] = sum(DP[i - 2]) % mod

    return sum(DP[n]) % mod