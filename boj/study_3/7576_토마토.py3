import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
tomato = []
done = []

for _ in range(N):
    tomato.append(list(map(int, sys.stdin.readline().split())))
    done.append([False]*M)
day = 0
flag = True
root = []
def check():
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 0 and not done[i][j]:
                queue = deque([(i, j)])
                done[i][j] = True
                ex = False
                while queue:
                    x, y = queue.popleft()
                    position = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
                    for nx, ny in filter(lambda z: -1 < z[0] and z[0] < N and -1 < z[1] and z[1] < M, position):
                        if tomato[nx][ny] == 1:
                            ex = True
                        if tomato[nx][ny] == 0 and not done[nx][ny]:
                            done[nx][ny] = True
                            queue.append((nx, ny))
                if not ex:
                    return False
            elif tomato[i][j] == 1:
                root.append((i, j, 0))
                done[i][j] = True
    return True

if not check():
    print(-1)
    flag = False

queue = deque(root)

while queue and flag:
    x, y, depth = queue.popleft()
    position = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
    for nx, ny in filter(lambda z: -1 < z[0] and z[0] < N and -1 < z[1] and z[1] < M, position):
        if tomato[nx][ny] == 0:
            tomato[nx][ny] = 1
            queue.append((nx, ny, depth+1))
    if not queue:
        day = depth
        break
if flag:
    print(day)