import sys

# BOJ 16918
# 아아... 1초씩 늘려서 리얼 시뮬레이션을 돌리니 시간 초과가 났던 문제이다..
# 시간 초과가 자꾸 나기에.. 분명 C/C++ 사용자들은 쉽게 넘어갔겠지만..
# Python 사용자인 나는 또 다른 최적화 난관에 부딪혔다.
# 그래서 초별로, 홀수초냐 짝수초냐에 따라 매트릭스 상태를 관찰했고
# 짝수초는 디폴트, 그리고 홀수초에선 +2씩 시간을 늘려 기존의 것보다 시간을 절반 이상 가량 줄였더니 통과하게 되었다.

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

R, C, N = map(int, sys.stdin.readline().split())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
t = 1
q = []
# 1 : 초기 q에 넣고
# 2 : 전부 폭탄
# 3 : q 터치기
# 4 : 전부
if N == 1:
    for row in matrix:
        print(''.join(row))
elif N%2 == 0:
    for _ in range(R):
        print('O'*C)
else:
    t = 1
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 'O':
                q.append((i, j))
    matrix = [['O']*C for _ in range(R)]
    while True:
        for x, y in q:
            matrix[x][y] = '.'
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if -1 < nx < R and -1 < ny < C:
                    matrix[nx][ny] = '.'
        t += 2
        if t == N:
            for row in matrix:
                print(''.join(row))
            break
        q = []
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 'O':
                    q.append((i, j))
                else:
                    matrix[i][j] = 'O'
