import sys

# BOJ 14728
# 또 다시 만난 knapsack류 DP 문제였다. 바보 같이 매 수행단계마다 N번씩 고르고 있었다. 그러지 않고 i에 따라서만 선태 or 선택 안 함으로
# 어차피 갈릴텐데... 그리고 선택 안 하고 넘기는 경우의 DP[i][t] = solve(i+1, t) 이 코드도 생각하지 못 했다.. 이런 유형 문제
# 자주 만났었는데 다음번엔 꼭 실수하지 않도록 해야겠다.

def solve(i, t):
    global N
    if i == N:
        return 0
    if DP[i][t] != -1:
        return DP[i][t]
    DP[i][t] = solve(i+1, t)
    if lecture[i][0] <= t:
        DP[i][t] = max(DP[i][t], solve(i+1, t-lecture[i][0]) + lecture[i][1])
    return DP[i][t]

N, T = map(int, sys.stdin.readline().split())
DP = [[-1]*(T+1) for _ in range(N+1)]
lecture = []
for _ in range(N):
    K, S = map(int, sys.stdin.readline().split())
    lecture.append((K, S))
print(solve(0, T))