import sys

# BOJ 18405
# 이 문제는 일반적인 BFS와 비슷하게 queue를 통해 탐색이 진행된다.
# 하지만 매 시간마다 우선순위가 빠른 바이러스부터 다시 감염이 시작되기 때문에
# 이 부분에 대해서 정렬로 q를 매번 갱신해주면 된다.

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, K = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
S, X, Y = map(int, sys.stdin.readline().split())
q = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] > 0:
            q.append((matrix[i][j], i, j))
q.sort(key=lambda x: x[0])
t = 0
while t < S and q:
    temp = []
    for virus, x, y in q:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < N and -1 < ny < N and matrix[nx][ny] == 0:
                matrix[nx][ny] = virus
                temp.append((virus, nx, ny))
    q = sorted(temp)
    t += 1
print(matrix[X-1][Y-1])