import sys
from collections import deque
from itertools import permutations

# 이번 문제는 보자마자 예전에 쇼크를 받은 적이 있는 물통 문제가 생각났다.
# 상태값을 변환시키는 어떠한 행위들이 전부 가중치가 같은 경우 BFS를 통해 이미 최소 행위수로 도달했던
# 특정 상태값들을 저장해놓고 푸는, 정말 BFS의 본질을 이용한 문제였기에 아직도 기억에 남았다.
# 그래서 이 문제 역시 바로 BFS로 풀어냈다.
# 하지만 알고리즘 분류에 BFS가 없고 DP만 있었다.
# 그러고나서 문제를 다시 보니 재귀를 활용한 DP로도 충분히 풀어낼 수 있었다.
# 이를 통해 다시 열린 사고를 갖자며 다짐을 하는 계기가 되었다.

N = int(sys.stdin.readline())
SCV = list(map(int, sys.stdin.readline().split()))
maxHP = max(SCV)

if N == 1:
    print((SCV[0]-1)//9+1)
elif N == 2:
    visited = [[-1]*(maxHP+1) for _ in range(maxHP+1)]
    first, second = SCV
    visited[first][second] = 0
    queue = deque([(first, second)])
    while queue:
        x, y = queue.popleft()
        if x == 0 and y == 0:
            print(visited[x][y])
            break
        if x == 0:
            ny = 0 if y <= 9 else y-9
            if visited[0][ny] == -1:
                visited[0][ny] = visited[x][y] + 1
                queue.append((0, ny))
                continue
        if y == 0:
            nx = 0 if x <= 9 else x-9
            if visited[nx][0] == -1:
                visited[nx][0] = visited[x][y] + 1
                queue.append((nx, 0))
                continue
        nx1 = 0 if x <= 9 else x-9
        ny1 = 0 if y <= 3 else y-3
        if visited[nx1][ny1] == -1:
            visited[nx1][ny1] = visited[x][y] + 1
            queue.append((nx1, ny1))
        nx2 = 0 if x <= 3 else x-3
        ny2 = 0 if y <= 9 else y-9
        if visited[nx2][ny2] == -1:
            visited[nx2][ny2] = visited[x][y] + 1
            queue.append((nx2, ny2))
else:
    visited = [[[-1]*(maxHP+1) for _ in range(maxHP+1)] for _ in range(maxHP+1)]
    first, second, third = SCV
    visited[first][second][third] = 0
    queue = deque([(first, second, third)])
    while queue:
        x, y, z = queue.popleft()
        if x == 0 and y == 0 and z == 0:
            print(visited[x][y][z])
            break
        for p in permutations([1, 3, 9], 3):
            dx, dy, dz = p
            nx = 0 if x <= dx else x-dx
            ny = 0 if y <= dy else y-dy
            nz = 0 if z <= dz else z-dz
            if visited[nx][ny][nz] == -1:
                visited[nx][ny][nz] = visited[x][y][z] + 1
                queue.append((nx, ny, nz))

