import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solve(N, M):
    for i in range(N):
        for j in range(M):
            color = matrix[i][j]
            visited = [[False]*M for _ in range(N)]
            stack = [(i, j, 0)]

            # 시작지점으로 다시 가야하기 때문에 DFS로만 해야하는 경우
            while stack:
                x, y, depth = stack.pop()
                visited[x][y] = True
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if -1 < nx < N and -1 < ny < M and matrix[nx][ny] == color:
                        if not visited[nx][ny]:
                            stack.append((nx, ny, depth+1))
                        elif nx == i and ny == j and depth != 1:
                            return True
    return False

N, M = map(int, sys.stdin.readline().split())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
if solve(N, M):
    print("Yes")
else:
    print("No")
