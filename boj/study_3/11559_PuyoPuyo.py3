import sys
from collections import deque

matrix = []
for _ in range(12):
    matrix.append(list(sys.stdin.readline().rstrip()))
answer = 0
def crash(m):
    global answer
    visited = [[False]*6 for _ in range(12)]
    crashed = False
    for i in range(11, -1, -1):
        for j in range(6):
            if m[i][j] != '.' and not visited[i][j]:
                color = m[i][j]
                remover = []
                count = 0
                visited[i][j] = True
                queue = deque([(i, j)])

                while queue:
                    x, y = queue.popleft()
                    count += 1
                    remover.append((x, y))
                    position = [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]
                    for nx, ny in filter(lambda z: -1<z[0] and z[0]<12 and -1<z[1] and z[1]<6, position):
                        if m[nx][ny]==color and not visited[nx][ny]:
                            visited[nx][ny] = True
                            queue.append((nx, ny))

                if count >= 4:
                    crashed = True
                    for x, y in remover:
                        m[x][y] = '.'
    if crashed:
        answer += 1
        return True
    else:
        return False

def down(m):
    for j in range(6):
        queue = deque()
        for i in range(11, -1, -1):
            if m[i][j] != '.':
                queue.append(m[i][j])
        for i in range(11, -1, -1):
            if queue:
                m[i][j] = queue.popleft()
            else:
                m[i][j] = '.'

while crash(matrix):
    down(matrix)

print(answer)