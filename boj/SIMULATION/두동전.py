import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    while queue:
        x1, y1, x2, y2 = queue.popleft()
        if visited[x1][y1][x2][y2] > 9:
            return -1
        for i in range(4):
            cnt = 0
            nx1, ny1 = x1 + dx[i], y1 + dy[i]
            nx2, ny2 = x2 + dx[i], y2 + dy[i]
            if -1 < nx1 < N and -1 < ny1 < M:
                if matrix[nx1][ny1] == '#':
                    nx1, ny1 = x1, y1
            else:
                cnt += 1
            if -1 < nx2 < N and -1 < ny2 < M:
                if matrix[nx2][ny2] == '#':
                    nx2, ny2 = x2, y2
            else:
                cnt += 1
            if cnt == 1:
                return visited[x1][y1][x2][y2] + 1
            elif cnt == 0 and visited[nx1][ny1][nx2][ny2] == -1:
                visited[nx1][ny1][nx2][ny2] = visited[x1][y1][x2][y2] + 1
                queue.append((nx1, ny1, nx2, ny2))
    return -1


N, M = map(int, sys.stdin.readline().split())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
position = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'o':
            position.append((i, j))
x1, y1 = position[0]
x2, y2 = position[1]
queue = deque([(x1, y1, x2, y2)])
visited = [[[[-1]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
visited[x1][y1][x2][y2] = 0
print(bfs())