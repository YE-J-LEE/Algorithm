import sys

# BOJ 2931
# 해싱이 꽤나 요구되는 시뮬레이션 문제이다.
# 파이프의 모양이 제각각이고 연결될 수 있는 지의 여부와 어느 입구로 들어왔냐에 따라 다음 방향이 어디로 결정되는지에 대해 해싱해줘야 수월하다.
# 처음엔 출발과 도착지점이 될 수 있는 M과 Z에 대하여, 만약 해커가 없앤 파이프가 바로 해당 지점들 주변이라면 이 문제 어떻게 풀까 고민했지만
# 다행히도 문제에서 입력으로 주어질 때 출발 및 도착지점의 바로 주변 블럭은 살아있다는 것을 확인할 수 있어서 풀어낼 수 있었다.

# 0123
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def whereToStart(matrix, n, m):
    for i in range(n):
        for j in range(m):
            if matrix[i][j] in 'MZ':
                for d in range(4):
                    ni = i + dx[d]
                    nj = j + dy[d]
                    if -1 < ni < n and -1 < nj < m and matrix[ni][nj] in '|-+1234' and d in enter[matrix[ni][nj]]:
                        return i, j, d

R, C = map(int, sys.stdin.readline().split())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
enter = {'|': [0, 2], '-': [1, 3], '+':[0,1,2,3], '1': [0, 3], '2': [2, 3], '3': [1, 2], '4': [0, 1]}
whichOne = {'02': '|', '13': '-', '0123': '+', '12': '1', '01': '2', '03': '3', '23': '4'}
nDirection = {('1', 3): 2, ('1', 0): 1, ('2', 2): 1, ('2', 3): 0, ('3', 1): 0, ('3', 2): 3, ('4', 1): 2, ('4', 0): 3}
x, y, d = whereToStart(matrix, R, C)

while True:
    nx = x + dx[d]
    ny = y + dy[d]
    if matrix[nx][ny] == '.':
        ableDirection = ''
        for i in range(4):
            ax = nx + dx[i]
            ay = ny + dy[i]
            if -1 < ax < R and -1 < ay < C and matrix[ax][ay] in '|-+1234' and i in enter[matrix[ax][ay]]:
                ableDirection += str(i)
        print(nx+1, ny+1, whichOne[ableDirection])
        break
    else:
        x, y = nx, ny
        if matrix[x][y] not in '|-+':
            d = nDirection[(matrix[x][y], d)]




