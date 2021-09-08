import sys, heapq

# ACM craft 문제와 같은 우선순위를 고려한 위상정렬 문제이다.
# 차수 배열을 선정하고 차수가 0인 친구들만 heap에서 뽑아 다음 차수를 줄여주는데,
# 이때 heap에서 뽑는 기준을 가장 먼저 끝나는 작업을 기준으로 뽑는다.
# 왜냐하면 작업은 동시에 진행될 것이고 먼저 끝나는 작업에 대해서 그 끝나는 시간은 중요치 않기 때문이다.
# 제일 먼저 끝나면 어차피 끝나도 다음 차수를 0으로 만드는 친구가 끝날때까지 기다려야 한다.

N = int(sys.stdin.readline())
time = [0]*(N+1)
answer = [0]*(N+1)
indegree = [0]*(N+1)
nbuilding = {x: [] for x in range(1, N+1)}
heap = []
for i in range(1, N+1):
    info = list(map(int, sys.stdin.readline().split()))
    time[i] = info[0]
    M = len(info)
    if M == 2:
        heapq.heappush(heap, (info[0], i))
        answer[i] = info[0]
    else:
        for j in range(1, len(info)-1):
            nbuilding[info[j]].append(i)
            indegree[i] += 1
while heap:
    t, x = heapq.heappop(heap)
    for nx in nbuilding[x]:
        indegree[nx] -= 1
        if indegree[nx] == 0:
            heapq.heappush(heap, (t+time[nx], nx))
            answer[nx] = t+time[nx]
for i in range(1, N+1):
    print(answer[i])
