import sys, heapq

# BOJ 11779
# 이 문제를 풀기 전 구슬탈출이라는 복잡한 구현문제를 풀다가
# 계속 틀리고 길을 잃어 이 문제로 피난을 왔다...
# 이 문제의 경우 제목부터가 최소비용 구하기, 그래서 읽어보니 다익스트라를 활용한 문제였다.
# 한동안 DP류 문제만 풀다보니 다익스트라 구현법이 기억이 안났지만 원리를 되새기며
# 코드를 써내려가니 내 몸은 이미 기억하고 있었다는 걸 알았다.
# 추가로 경로까지 구해내야하는 문제여서 visited 배열에 경로도 갱신해줬다.

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = {x: {} for x in range(1, n+1)}
for _ in range(m):
    a, b, cost = map(int, sys.stdin.readline().split())
    if b in graph[a]:
        graph[a][b] = min(graph[a][b], cost)
    else:
        graph[a][b] = cost
src, dst = map(int, sys.stdin.readline().split())
heap = []
visited = [[float('inf'), []] for _ in range(n+1)]
visited[src][0] = 0
heapq.heappush(heap, (0, src, [src]))
while heap:
    d, x, path = heapq.heappop(heap)
    if d > visited[x][0]:
        continue
    for nx, cost in graph[x].items():
        dist = d + cost
        if visited[nx][0] > dist:
            npath = path + [nx]
            visited[nx][0] = dist
            visited[nx][1] = npath
            heapq.heappush(heap, (dist, nx, npath))
print(visited[dst][0])
print(len(visited[dst][1]))
print(*visited[dst][1])