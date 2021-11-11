import sys

# BOJ 15683
# 완전탐색이 가미된 시뮬레이션 문제이다. 예전엔 이런 문제가 너무 복잡해 풀 엄두가 안 났었는데 이제는 가볍게 풀 수 있다.
# 적절한 해싱과 재귀를 활용한 완전탐색으로 풀어냈다.

def solve(i):
    global N, M, L, answer
    if i == L:
        result = 0
        for x in range(N):
            for y in range(M):
                if office[x][y] == 0:
                    result += 1
        answer = min(answer, result)
        return
    x, y, direction = cctv[i]
    for angle in eyeSight[direction]:
        flipFlop = []
        for d in angle:
            nx, ny = x, y
            while -1 < nx + dx[d] < N and -1 < ny + dy[d] < M and office[nx + dx[d]][ny + dy[d]] != 6:
                nx += dx[d]
                ny += dy[d]
                if office[nx][ny] == 0:
                    office[nx][ny] = -1
                    flipFlop.append((nx, ny))
        solve(i+1)
        for w, z in flipFlop:
            office[w][z] = 0

# up / right / down / left
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

eyeSight = {1: [[0], [1], [2], [3]], 2: [[0, 2], [1, 3]], 3: [[0, 1], [1, 2], [2, 3], [3, 0]],
            4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], 5: [[0, 1, 2, 3]]}
answer = 1e9

N, M = map(int, sys.stdin.readline().split())
office = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cctv = []
for i in range(N):
    for j in range(M):
        if 0 < office[i][j] < 6:
            cctv.append((i, j, office[i][j]))
L = len(cctv)
solve(0)
print(answer)