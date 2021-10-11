import sys

# BOJ 4883
# 이 문제는 행에 따라서 행 이상을 벗어나지 않으며 특정 노드에 도착하기 위한 이전의 경로가 이미 정해져 있다.
# 특정 노드에 다다르기 위해 바로 이전 행으로부터 오는 경로가 정해져 있으며 반복된단 말이다. 그렇기에 DP가 적용이 된다.
# 그래서 바로 DP로 풀어냈다. 그런데 초기 조건 설정에 애를 먹어 계속 틀렸었다. 왜 자꾸 -1이 나올까 했는데
# 내가 처음에 -1로 설정했기 때문이었다... 어.. 백신 이슈인가..ㅋ
# 다음부턴 DP 초기화 값들 설정과 for문 시작에 앞서 앞의 값들은 잘 세팅이 되었는지 잘 파악해야겠다.

k = 1
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    DP = [[-1]*3 for _ in range(N)]
    DP[0][0] = 1e9
    DP[0][1] = cost[0][1]
    DP[0][2] = cost[0][1] + cost[0][2]
    for i in range(1, N):
        DP[i][0] = min(DP[i-1][0], DP[i-1][1]) + cost[i][0]
        DP[i][1] = min(DP[i][0], DP[i-1][0], DP[i-1][1], DP[i-1][2]) + cost[i][1]
        DP[i][2] = min(DP[i][1], DP[i-1][1], DP[i-1][2]) + cost[i][2]
    print("{}. {}".format(k, DP[N-1][1]))
    k += 1

