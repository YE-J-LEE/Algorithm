import sys
from collections import deque
from itertools import permutations

# BOJ 16985
# 아 완전 탐색 문제였다. 3차원 배열인데 각 층을 회전시킬 수 있으면 각 층들을 어떤 순서로 쌓는지도 자유다.
# 다행히 5x5x5 행렬이지만... 그렇다할지라도 Python에겐 버겁다. 최악의 케이스인 모든 층이 1인 경우가 테스트케이스에 있길래
# 돌려봤는데 4초는 거뜬히 넘어버린다. 그리고 알고리즘 분류도 브루트포스이기에.. 그냥 Pypy로 제출해 통과해버렸다.

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def BFS(m):
    visited = [[[-1]*5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = 0
    queue = deque([(0, 0, 0)])
    while queue:
        x, y, z = queue.popleft()
        if x == 4 and y == 4 and z == 4:
            return visited[x][y][z]
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if -1 < nx < 5 and -1 < ny < 5 and -1 < nz < 5 and m[nx][ny][nz] and visited[nx][ny][nz] == -1:
                visited[nx][ny][nz] = visited[x][y][z] + 1
                queue.append((nx, ny, nz))
    return float('inf')

def solve(f, i, maze):
    global answer
    if i == 5:
        if maze[0][0][0] and maze[4][4][4]:
            answer = min(answer, BFS(maze))
        return
    for pick in floors[f[i]]:
        solve(f, i+1, maze + [pick])

floors = []
answer = float('inf')
for _ in range(5):
    floor = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
    floors.append([floor])
for k in range(5):
    for _ in range(3):
        rotated = []
        for j in range(5):
            row = []
            for i in range(4, -1, -1):
                row.append(floors[k][-1][i][j])
            rotated.append(row)
        floors[k].append(rotated)
for p in permutations(range(5), 5):
    solve(list(p), 0, [])
if answer == float('inf'):
    print(-1)
else:
    print(answer)

