import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

W, H = map(int, sys.stdin.readline().split())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
visited = [[[-1]*4 for _ in range(W)] for _ in range(H)]
C = []
for i in range(H):
    for j in range(W):
        if matrix[i][j] == 'C':
            C.append((i, j))
sX, sY = C[0]
eX, eY = C[1]
queue = deque()
for i in range(4):
    queue.append((sX, sY, i))
    visited[sX][sY][i] = 0
answer = 1e9
aa = []
while queue:
    x, y, d = queue.popleft()
    if x == eX and y == eY:
        answer = min(answer, visited[x][y][d])
        continue
    left = 3 if d == 0 else d - 1
    right = (d+1)%4
    nx, ny = x + dx[d], y + dy[d]
    if -1 < nx < H and -1 < ny < W and matrix[nx][ny] != '*':
        if visited[nx][ny][d] == -1:
            visited[nx][ny][d] = visited[x][y][d]
            queue.append((nx, ny, d))
        elif visited[nx][ny][d] > visited[x][y][d]:
            visited[nx][ny][d] = visited[x][y][d]
            queue.append((nx, ny, d))

    if matrix[x][y] == 'C':
        continue
    lx, ly = x + dx[left], y + dy[left]
    rx, ry = x + dx[right], y + dy[right]
    if -1 < lx < H and -1 < ly < W and matrix[lx][ly] != '*':
        if visited[lx][ly][left] == -1:
            visited[lx][ly][left] = visited[x][y][d] + 1
            queue.append((lx, ly, left))
        elif visited[lx][ly][left] > visited[x][y][d] + 1:
            visited[lx][ly][left] = visited[x][y][d] + 1
            queue.append((lx, ly, left))
    if -1 < rx < H and -1 < ry < W and matrix[rx][ry] != '*':
        if visited[rx][ry][right] == -1:
            visited[rx][ry][right] = visited[x][y][d] + 1
            queue.append((rx, ry, right))
        elif visited[rx][ry][right] > visited[x][y][d] + 1:
            visited[rx][ry][right] = visited[x][y][d] + 1
            queue.append((rx, ry, right))

print(answer)