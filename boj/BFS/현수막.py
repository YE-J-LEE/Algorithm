import sys
from collections import deque

# BOJ 14716
# 이 문제는 BFS에서 상하좌우 이외에 추가적으로 대각선도 포함하여
# 총 8개 방향에 대해 탐색을 하면 되는 문제였다.

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

M, N = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
visited = [[False]*N for _ in range(M)]
answer = 0
for i in range(M):
    for j in range(N):
        if visited[i][j] or matrix[i][j] == 0:
            continue
        visited[i][j] = True
        queue = deque([(i, j)])
        answer += 1
        while queue:
            x, y = queue.popleft()
            for d in range(8):
                nx, ny = x + dx[d], y + dy[d]
                if -1 < nx < M and -1 < ny < N and not visited[nx][ny] and matrix[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
print(answer)
