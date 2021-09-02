import sys, heapq

# 이번 문제는 위상절령에 우선순위큐가 가미된 문제이다.
# 각 빌딩별로 우선 작업이 되어야 하는 indegree의 갯수를 기록하고 해당 빌딩에 도달하기 까지 가장 오래걸렸던
# 빌딩 작업을 기준으로 해당 빌딩의 작업 완료 시간을 갱신시켜준다.
# indegree를 0으로 만드는 최후의 작업은 가장 오래걸렸던 작업이어야 하므로 최소힙 우선순위큐를 만들어서
# indegree를 깎는 작업을 진행하도록 구현한다.

T = int(sys.stdin.readline())
for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    time = list(map(int, sys.stdin.readline().split()))
    indegree = [0]*N
    nbuild = {x: [] for x in range(N)}
    for _ in range(K):
        px, nx = map(int, sys.stdin.readline().split())
        px, nx = px-1, nx-1
        nbuild[px].append(nx)
        indegree[nx] += 1
    W = int(sys.stdin.readline())-1
    answer = 0
    minH = []
    for i in range(N):
        if indegree[i] == 0:
            heapq.heappush(minH, (time[i], i))
    while minH:
        t, x = heapq.heappop(minH)
        if x == W:
            print(t)
            break
        for nx in nbuild[x]:
            indegree[nx] -= 1
            if indegree[nx] == 0:
                heapq.heappush(minH, (time[nx] + t, nx))


