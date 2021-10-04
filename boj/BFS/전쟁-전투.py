import sys
from collections import deque

# BOJ 1303
# 이 문제는 전형적인 BFS 문제로, 그저 퍼져나가면서 영역의 수를 구하면 된다.

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())
war = [list(sys.stdin.readline().rstrip()) for _ in range(M)]
me, enemy = 0, 0
visited = [[False]*N for _ in range(M)]
for i in range(M):
    for j in range(N):
        if visited[i][j]:
            continue
        visited[i][j] = True
        n = 1
        color = war[i][j]
        queue = deque([(i, j)])
        while queue:
            x, y = queue.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if -1 < nx < M and -1 < ny < N and not visited[nx][ny] and war[nx][ny] == color:
                    visited[nx][ny] = True
                    n += 1
                    queue.append((nx, ny))
        if color == 'W':
            me += n**2
        else:
            enemy += n**2
print(me, enemy)
