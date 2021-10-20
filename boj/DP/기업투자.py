import sys

# BOJ 2662
# 이 문제 같은 경우 해당 시점에서 무엇을 골랐을 때 결국 이것이 최대의 결과로 이끄는지 파악해야하는 knapsack류 DP문제였다.
# 처음엔 각 기업에 투자하는 제한 금액이 있어서 백트래킹으로 해결할 수 있을까 싶었지만 안 됐다.
# 그래서 재귀 DP를 통해 구현은 했으나 최대 결과값을 알 수 있었지 결국 각 기업에 얼마씩 투자했는지의 기록은 저장해두기 어려웠다.
# 왜냐하면 내가 구현하는 knapsack류 문제들은 대부분 DP 방식인데 중간 중간 최적의 선택값을 저장하는 방식이 생각하기 꽤 복잡해서
# 다시 말해 디테일한 전 과정이 내 머릿속에 잘 그려지진 않는 상태였다. 그래서 나와 같이 재귀로 푼 사람들의 풀이를 참고하니
# 어떤 방식으로 중간 값들을 기록하는지 알 수 있었고 통과할 수 있었다.

def solve(j, limit):
    global answer, N, M, resultArr
    if j > M:
        return 0
    if DP[j][limit] != -1:
        return DP[j][limit]
    DP[j][limit] = solve(j+1, limit)
    for i in range(1, N+1):
        if i > limit:
            break
        ret = solve(j+1, limit-i) + matrix[i][j]
        if ret > DP[j][limit]:
            DP[j][limit] = ret
            trace[j][limit] = i
    return DP[j][limit]

N, M = map(int, sys.stdin.readline().split())
matrix = [[0]*(M+1)]
answer = 0
result = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))
DP = [[-1]*(N+1) for _ in range(M+1)]
trace = [[0]*(N+1) for _ in range(M+1)]
print(solve(1, N))
total = N
for j in range(1, M+1):
    result.append(trace[j][total])
    total -= trace[j][total]
print(*result)
