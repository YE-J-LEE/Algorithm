import sys
from collections import deque

# BOJ 14442
# 이 문제는 시간이 매우 까다로운 문제였다.
# 우선 시간 제한은 2초였지만 방문 여부 체크 배열을 만드는 데에만 해도 4000만 정도의 시간복잡도가 할애된다.
# 이후엔 BFS를 통해 탐색해야하며 4방향에 대해서 또 안에서 if 문이 and 연산과 함께 꽤 복잡하게 이루어져 탐색을 진행한다.
# 그래서인지 Python으로는 통과하기 힘들었고 Pypy를 통해 성공했다.

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M, K = map(int, sys.stdin.readline().split())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[[-1]*(K+1) for _ in range(M)] for _ in range(N)]
queue = deque([(0, 0, K)])
visited[0][0][K] = 1
answer = -1
while queue:
    x, y, k = queue.popleft()
    if x == N-1 and y == M-1:
        answer = visited[x][y][k]
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < nx < N and -1 < ny < M:
            if k and matrix[nx][ny] == '1' and visited[nx][ny][k-1] == -1:
                visited[nx][ny][k-1] = visited[x][y][k] + 1
                queue.append((nx, ny, k-1))
            elif matrix[nx][ny] == '0' and visited[nx][ny][k] == -1:
                visited[nx][ny][k] = visited[x][y][k] + 1
                queue.append((nx, ny, k))
print(answer)