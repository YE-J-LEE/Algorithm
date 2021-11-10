import sys
from collections import deque

# BOJ 2251
# BFS 문제이다. 예전에 이 문제를 처음 만났을 때는 풀지 못 했지만 이제는 특정 상태를 저장한다는 개념이 잡혀있어서
# 풀 수 있었다. 이러한 특징을 잘 활용하면 다른 복잡한 문제도 새롭게 해석해 풀 수 있을 것 같다.

A, B, C = map(int, sys.stdin.readline().split())
visited = [[[False]*(C+1) for _ in range(B+1)] for _ in range(A+1)]
visited[0][0][C] = True
queue = deque([(0, 0, C)])
answer = set()
while queue:
    x, y, z = queue.popleft()
    if x == 0:
        answer.add(z)
    if x:
        if y < B:
            nx, ny = -1, -1
            if x + y > B:
                ny = B
                nx = x + y - B
            else:
                ny = x + y
                nx = 0
            if not visited[nx][ny][z]:
                visited[nx][ny][z] = True
                queue.append((nx, ny, z))
        if z < C:
            nx, nz = -1, -1
            if x + z > C:
                nz = C
                nx = x + z - C
            else:
                nz = x + z
                nx = 0
            if not visited[nx][y][nz]:
                visited[nx][y][nz] = True
                queue.append((nx, y, nz))
    if y:
        if x < A:
            nx, ny = -1, -1
            if x + y > A:
                nx = A
                ny = x + y - A
            else:
                nx = x + y
                ny = 0
            if not visited[nx][ny][z]:
                visited[nx][ny][z] = True
                queue.append((nx, ny, z))
        if z < C:
            ny, nz = -1, -1
            if y + z > C:
                nz = C
                ny = y + z - C
            else:
                nz = y + z
                ny = 0
            if not visited[x][ny][nz]:
                visited[x][ny][nz] = True
                queue.append((x, ny, nz))
    if z:
        if x < A:
            nx, nz = -1, -1
            if x + z > A:
                nx = A
                nz = x + z - A
            else:
                nx = x + z
                nz = 0
            if not visited[nx][y][nz]:
                visited[nx][y][nz] = True
                queue.append((nx, y, nz))
        if y < B:
            ny, nz = -1, -1
            if y + z > B:
                ny = B
                nz = y + z - B
            else:
                ny = y + z
                nz = 0
            if not visited[x][ny][nz]:
                visited[x][ny][nz] = True
                queue.append((x, ny, nz))
print(*sorted(list(answer)))