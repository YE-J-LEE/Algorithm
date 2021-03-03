import sys
import copy
from collections import deque

N = int(sys.stdin.readline())
matrix = []
visited = []
answer = 0
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))
    visited.append([False]*N)

for h in range(0, 101):
    m = copy.deepcopy(matrix)
    v = copy.deepcopy(visited)
    safe = 0
    for i in range(N):
        for j in range(N):
            if m[i][j] <= h or v[i][j]:
                continue
            v[i][j] = True
            safe += 1
            queue = deque([(i, j)])

            while queue:
                cx, cy = queue.popleft()
                position = [(cx-1, cy), (cx, cy+1), (cx+1, cy), (cx, cy-1)]
                for nx, ny in filter(lambda x: -1<x[0] and x[0]<N and -1<x[1] and x[1]<N, position):
                    if m[nx][ny] <= h or v[nx][ny]:
                        continue
                    v[nx][ny] = True
                    queue.append((nx, ny))
    if not safe:
        break
    if safe > answer:
        answer = safe
print(answer)