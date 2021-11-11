import sys

# BOJ 21610
# 시뮬레이션 문제이다. 마법사 상어 시리즈로, 아무래도 백준 문제집들을 보았을 때 삼성역량테스트 문제의 변형인듯 싶다.
# 꽤나 자주 나오며 요즘 코딩테스트가 주로 구현쪽에 치우쳐졌기에 한 번 풀어봤다. 이런 류의 문제를 풀 때 시간이 꽤 걸리는 것 같다.
# 파이썬이다보니 어떻게 하면 메모리나 시간을 줄일지 고민을 하게 된다. 가끔 2000만이 넘어 터지는 경우가 있기 때문이다.
# 풀기는 하지만 푸는 데에 오래 걸려서 숙달을 시켜야 할 것 같다.

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
moveInfo = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
copyRain = [[0]*N for _ in range(N)]
preCloud = [[False] * N for _ in range(N)]
for d, s in moveInfo:
    nCloud = []
    while cloud:
        x, y = cloud.pop()
        nx, ny = -1, -1
        deltaX = dx[d-1]*s
        deltaY = dy[d-1]*s
        if deltaX < 0:
            deltaX = (-deltaX)%N
            nx = x - deltaX if x - deltaX > -1 else x - deltaX + N
        else:
            nx = (x+deltaX)%N
        if deltaY < 0:
            deltaY = (-deltaY)%N
            ny = y - deltaY if y - deltaY > -1 else y - deltaY + N
        else:
            ny = (y+deltaY)%N
        preCloud[nx][ny] = True
        nCloud.append((nx, ny))
        matrix[nx][ny] += 1
    for x, y in nCloud:
        cnt = 0
        for i in [1, 3, 5, 7]:
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < N and -1 < ny < N and matrix[nx][ny]:
                cnt += 1
        copyRain[x][y] = cnt
    for x, y in nCloud:
        matrix[x][y] += copyRain[x][y]
        copyRain[x][y] = 0
    for i in range(N):
        for j in range(N):
            if preCloud[i][j]:
                preCloud[i][j] = False
                continue
            if matrix[i][j] >= 2:
                matrix[i][j] -= 2
                cloud.append((i, j))
answer = 0
for row in matrix:
    answer += sum(row)
print(answer)