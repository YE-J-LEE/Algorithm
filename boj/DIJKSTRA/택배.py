import sys, heapq

# 다익스트라에 단순 최단 거리값 뿐만이 아니라 최단 경로도 구해야했던 문제다.
# 여태 거리만 구했지 경로를 구하는 문제는 풀어본 적이 없었다.
# 그리고 실제 다익스트라 문제도 그렇게 많이 풀어보질 않아서.. 어떻게 경로를 구할지 바로 떠오르진 않았다.
# 우선 내가 아는 다익스트라를 거리만 구했을 때 어떤 식이었는지 쭉 코드로 써내려 갔고,
# 다익스트라를 코딩하면서 아 이쯤에 경로를 저장하고 갱신해야겠다 생각이 들어서 추가했다.
# 그런데 솔직히 걱정이 좀 됐다. 왜냐하면 지나온 경로들을 저장하기 위해 기존의 (거리, 노드) 튜플값에
# 추가로 (거리, 노드, 지나온 경로)가 되어서 heap이 뚱뚱해져 시간 초과가 날까 겁났다.
# 하지만 다행히 총 노드 갯수 200 이하, 간선은 10000개 이하여서 그런지 잘 통과됐다.

n, m = map(int, sys.stdin.readline().split())
graph = {x: {} for x in range(n)}
for _ in range(m):
    x, y, time = map(int, sys.stdin.readline().split())
    x, y = x-1, y-1
    if y in graph[x]:
        graph[x][y] = min(graph[x][y], time)
        graph[y][x] = min(graph[y][x], time)
    else:
        graph[x][y] = time
        graph[y][x] = time
answer = []
for i in range(n):
    distance = [[1e9, []] for _ in range(n)]
    distance[i][0] = 0
    distance[i][1] = [i]
    heap = []
    heapq.heappush(heap, (0, i, [i]))
    while heap:
        cost, src, path = heapq.heappop(heap)
        if cost > distance[src][0]:
            continue
        for dst, dist in graph[src].items():
            newDist = cost + dist
            if distance[dst][0] > newDist:
                newPath = path + [dst]
                distance[dst][0] = newDist
                distance[dst][1] = newPath
                heapq.heappush(heap, (newDist, dst, newPath))
    row = []
    for i in range(n):
        if distance[i][0] == 0:
            row.append('-')
        else:
            row.append(distance[i][1][1]+1)
    answer.append(row)
for row in answer:
    print(*row)