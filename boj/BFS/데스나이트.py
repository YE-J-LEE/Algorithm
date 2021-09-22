import sys
from collections import deque

# BOJ 16948
# BFS의 기본형인 문제이다.
# 문제 내용부터 매우 기본적인 풀이로 해결하도록 안내되어 있으며
# 단지 평소 상하좌우 한칸씩과 다르게 dx, dy값이 변할뿐이다.

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

N = int(sys.stdin.readline())
r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
visited = [[-1]*N for _ in range(N)]
queue = deque([(r1, c1)])
visited[r1][c1] = 0
answer = -1
while queue:
    x, y = queue.popleft()
    if x == r2 and y == c2:
        answer = visited[x][y]
        break
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < nx < N and -1 < ny < N and visited[nx][ny] == -1:
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))
print(answer)














