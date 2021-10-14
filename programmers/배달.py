import heapq

# 프로그래머스 배달
# 이 문제는 전형적인 다익스트라 문제였다.
# 조건문을 통해 불필요한 검사를 제거했고 min heap을 이용해 구현했다.

def solution(N, road, K):
    answer = 0
    graph = {x: {} for x in range(1, N+1)}
    for src, dst, cost in road:
        if dst in graph[src]:
            if graph[src][dst] > cost:
                graph[src][dst] = cost
                graph[dst][src] = cost
        else:
            graph[src][dst] = cost
            graph[dst][src] = cost
    time = [1e9]*(N+1)
    time[1] = 0
    heap = []
    heapq.heappush(heap, (1, 0))
    while heap:
        x, t = heapq.heappop(heap)
        if t > time[x]:
            continue
        for nx, cost in graph[x].items():
            addedTime = t + cost
            if addedTime < time[nx]:
                time[nx] = addedTime
                heapq.heappush(heap, (nx, addedTime))
    for i in range(1, N+1):
        if time[i] <= K:
            answer += 1

    return answer