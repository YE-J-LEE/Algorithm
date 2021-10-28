import sys
from collections import deque

# BOJ 11967
# 이 문제 접근을 잘못했다. 불이 켜진 곳으로만 이동할 수 있는데, 해당 시점에서의 인접한 불켜진 부분만 생각하고 다시 넘겨버렸다.
# 최대의 개념을 적용할때 현재 시점의 주변 부분만 확인해서 체크했기에... 물론 DP로 접근했지만 가짓수를 빼먹었다.
# 불을 켤 때마다 킨 곳의 주변이 내가 방문한 적이 있는 부분이면 갈 수 있다는 의미이기에 그 부분을 큐에 다시 넣어주는 방식은 처음 알게 된 방식이다.
# 처음에 BFS로 풀지 말아야 겠다는 생각을 한 이유도 지나온 지점을 다시 거슬러 가야 하기 때문이었는데.. 정말 새로운 문제 풀이 방법을 얻게 된 좋은 문제다.
# 이런 식으로 내가 가는 길에 따라서 새로운 길이 다시 생긴다는 개념, 그리고 새로운 길의 주변이 내가 방문했던 곳이라면 즉 내가 갈 수 있는 길이라면
# 다시 큐에 넣어주는 방식은 인접행렬 말고도 그래프에서 다익스트라의 경우도 응용해볼 수 있을 것 같단 생각이 들었다.

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())
getLight = [[[] for _ in range(N)] for _ in range(N)]
onOff = [[False]*N for _ in range(N)]
onOff[0][0] = True
visited = [[False]*N for _ in range(N)]
for _ in range(M):
    x, y, a, b = map(int, sys.stdin.readline().split())
    getLight[x-1][y-1].append((a-1, b-1))
answer = 1
queue = deque([(0, 0)])
visited[0][0] = True
while queue:
    x, y = queue.popleft()
    for w, z in getLight[x][y]:
        if not onOff[w][z]:
            onOff[w][z] = True
            answer += 1
            for i in range(4):
                nw, nz = w + dx[i], z + dy[i]
                if -1 < nw < N and -1 < nz < N and visited[nw][nz]:
                    queue.append((nw, nz))
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if -1 < nx < N and -1 < ny < N and not visited[nx][ny] and onOff[nx][ny]:
            visited[nx][ny] = True
            queue.append((nx, ny))
print(answer)
