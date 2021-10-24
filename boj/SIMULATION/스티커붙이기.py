import sys
from collections import deque

# BOJ 18808
# 이 문제는 상반기 N사의 공채 마지막 문제와 비슷하다.
# 도형이 여러 개 주어지고 해당 도형에 대해 뒤집기를 제외한 회전이 가능하게 하여 빈 틀에 도형을 최대한 채워넣는 문제이다.
# 이 문제에서 주목해야할 점은 바로 '회전'이다. 90으로 나누어떨어지는 각도에 의한 회전들은 정수 범위 내에 해결이 가능하다.
# 상반기에 저 문제를 풀지 못 한 뒤로 과연 증분값을 회전한 것을 그대로 활용해도 될까 머릿속으로 고민만 해왔었다.
# 왜냐하면 고등학교 수학에서 배우던 좌표평면에서의 회전은 우리가 사용하는 행렬의 i, j 인덱스가 뒤바뀐 상태며 값또한 다르기 때문이다.
# 그래서 처음에 문제를 풀기 전에 행렬을 (i, j)로 print 해놓고 규칙을 찾아보았다.
# 미심쩍었지만 다행스럽게도 내 생각이 맞았고 문제를 통과할 수 있었다.

def check(row):
    global N, M, K, visited, answer
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                continue
            trace = []
            for x, y in row:
                X, Y = i+x, j+y
                if -1 < X < N and -1 < Y < M and not visited[X][Y]:
                    trace.append((X, Y))
                else:
                    break
            else:
                for x, y in trace:
                    visited[x][y] = True
                    answer += 1
                return True
    return False


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M, K = map(int, sys.stdin.readline().split())
stickers = []
# (a, b) -> (b, -a)
for _ in range(K):
    R, C = map(int, sys.stdin.readline().split())
    sticker = [[]]
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
    visited = [[False]*C for _ in range(R)]
    found = False
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 0 or found:
                continue
            visited[i][j] = True
            found = True
            X, Y = i, j
            queue = deque([(i, j)])
            while queue:
                x, y = queue.popleft()
                sticker[0].append((x-X, y-Y))
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if -1 < nx < R and -1 < ny < C and matrix[nx][ny] and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
            break
    stickers.append(sticker)
for i in range(K):
    for _ in range(3):
        rotate = []
        for a, b in stickers[i][-1]:
            rotate.append((b, -a))
        stickers[i].append(rotate)
visited = [[False]*M for _ in range(N)]
answer = 0
for k in range(K):
    for row in stickers[k]:
        if check(row):
            break
print(answer)





