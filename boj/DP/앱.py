import sys

# 기존에 냅색류의 문제들은 전부 재귀를 통해 구했고 top-down방식과는 또 다르게 백준의 리조트 문제처럼
# 밑에서부터 쌓아가되 완성된 최적해를 바로 return하는 방식으로 풀어왔다,
# 이 때문에 DP 2차원 배열을 형성할 수 있는 발상의 전환 방식을 생각해냈음에도 기존에 내가 해오던 방식으로는 접목이 안 돼서 해당 풀이로의
# 가지가 유망하지 않다고 판단했었다.
# 울며 겨자 먹기로 백트래킹을 트라이했고 보기 좋게 시간초과가 났다.
# 알고리즘 분류를 보니 냅색이다. 그래서 기존 내 방식 (재귀를 밑에서부터 쌓는)을 시도 했지만 이 역시 완벽하지 않은 코드였다.
# 직접 생각해낸 반례들이 틀린다는 것은 허점이 분명하다는 것.
# 그래서 bottom-up 방식으로 냅색 풀이를 해보았다.
# 훨씬 깔끔하며 점화식의 정의도 명확했다. DP[i][j] 는 i까지의 작업들중 j 의 코스트로 만들 수 있는 최대 바이트 양
# 냅색의 늪에 빠져 풀이들을 찾아보다 0-1 말고 fractional 냅색도 있다는 걸 알게 되었다. 다음엔 저 내용을 공부해봐야겠다.

N, M = map(int, sys.stdin.readline().split())
memory = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))
maxVal = sum(cost)
DP = [[0]*(maxVal+1) for _ in range(N)]
answer = float('inf')
for i in range(N):
    for j in range(maxVal+1):
        if cost[i] > j:
            DP[i][j] = DP[i-1][j]
        else:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-cost[i]] + memory[i])
        if DP[i][j] >= M:
            answer = min(answer, j)
print(answer)

