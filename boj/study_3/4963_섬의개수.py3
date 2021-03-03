import sys
from collections import deque

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w==0 and h==0:
        break
    matrix = []
    visited = []
    answer = 0
    for _ in range(h):
        matrix.append(list(map(int, sys.stdin.readline().split())))
        visited.append([False]*(w))
    for i in range(h):
        for j in range(w):
            if not matrix[i][j] or visited[i][j]:
                continue
            answer += 1
            visited[i][j] = True
            queue = deque([(i, j)])
            while queue:
                x, y = queue.popleft()
                for nx, ny in filter(lambda p:-1<p[0] and p[0]<h and -1<p[1] and p[1]<w ,[(x-1, y), (x-1, y+1), (x, y+1), (x+1, y+1), (x+1, y), (x+1, y-1), (x, y-1), (x-1, y-1)]):
                    if not matrix[nx][ny] or visited[nx][ny]:
                        continue
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    print(answer)