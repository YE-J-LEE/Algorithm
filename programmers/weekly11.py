from collections import deque

# 프로그래머스 위클리 11주차
# BFS 구현 문제였다. 가운데 구멍 둘레 길이는 경로로 쳐주지 않는 느낌의 문제는 예전에 백준 문제에서 존재했었다.
# 하지만 이 문제는 좌표공간에서 진행되었으며 때문에 행렬에 담기엔 칸에 대한 꼭짓점의 좌표에 대한 고려가 필요했다.
# 그리고 좌표끼리의 라인을 따라 이동하기 때문에 좌표간 변에 대해 고유한 길을 새롭게 내주어야 한다.
# 왜냐하면 편의를 위해 칸에 변의 갯수를 일일이 기록해나가고 나중에 탐색을 진행하게 되면 칸끼리는 또 맞닿아있기에
# 탐색하기가 어렵기 때문이다. 그래서 나는 칸 끼리 맞닿는 부분의 변을 고유하게 설정해서 길을 만들어주었다.

def makePath(x, y, d):
    if d == 0:
        return x+1, y, x+1, y+1
    elif d == 1:
        return x, y, x+1, y
    elif d == 2:
        return x, y, x, y+1
    else:
        return x, y+1, x+1, y+1

def solution(rectangle, characterX, characterY, itemX, itemY):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    matrix = [[0] * 52 for _ in range(52)]
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1, x2):
            for j in range(y1, y2):
                matrix[i][j] = 1
    visited = [[False] * 52 for _ in range(52)]
    queue = deque([(0, 0)])
    visited[0][0] = True
    p2idx = [[0] * 52 for _ in range(52)]
    num = 0
    for i in range(52):
        for j in range(52):
            p2idx[i][j] = num
            num += 1
    graph = {x: set() for x in range(52*52)}
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if -1 < nx < 52 and -1 < ny < 52:
                if matrix[nx][ny]:
                    w1, z1, w2, z2 = makePath(nx, ny, d)
                    src = p2idx[w1][z1]
                    dst = p2idx[w2][z2]
                    graph[src].add(dst)
                    graph[dst].add(src)
                elif not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    start = p2idx[characterX][characterY]
    end = p2idx[itemX][itemY]
    visited = {start}
    queue = deque([(start, 0)])
    while queue:
        x, l = queue.popleft()
        if x == end:
            return l
        for nx in graph[x]-visited:
            visited.add(nx)
            queue.append((nx, l+1))
