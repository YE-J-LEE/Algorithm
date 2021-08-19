import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
mid = N//2
angle = [[False]*N for _ in range(N)]
for i in range(1, mid+1):
    angle[mid+i][mid+i] = True
    angle[mid+i][mid-i] = True
    angle[mid-i][mid+i] = True
    angle[mid-(i-1)][mid-i] = True
x, y, d = mid, mid, 3
answer = 0
while not(x==0 and y==0):
    current = d
    left = 3 if d == 0 else d-1
    right = (d+1)%4
    nx, ny = x+dx[d], y+dy[d]
    total = matrix[nx][ny]
    if angle[nx][ny]:
        d = left
    spread = [(x+dx[left], y+dy[left], 1), (x+dx[right], y+dy[right], 1)
        , (x+dx[left]+dx[current], y+dy[left]+dy[current], 7)
        , (x+dx[right]+dx[current], y+dy[right]+dy[current], 7)
        , (x + dx[left]*2 + dx[current], y + dy[left]*2 + dy[current], 2)
        , (x + dx[right]*2 + dx[current], y + dy[right]*2 + dy[current], 2)
        , (x + dx[left] + dx[current]*2, y + dy[left] + dy[current]*2, 10)
        , (x + dx[right] + dx[current]*2, y + dy[right] + dy[current]*2, 10)
        , (x+dx[current]*3, y+dy[current]*3, 5)]
    for cx, cy, percent in spread:
        amount = total*percent//100
        matrix[nx][ny] -= amount
        if -1 < cx < N and -1 < cy < N:
            matrix[cx][cy] += amount
        else:
            answer += amount
    alphaX, alphaY = x+dx[current]*2, y+dy[current]*2
    if -1 < alphaX < N and -1 < alphaY < N:
        matrix[alphaX][alphaY] += matrix[nx][ny]
        matrix[nx][ny] = 0
    else:
        answer += matrix[nx][ny]
        matrix[nx][ny] = 0
    x, y = nx, ny

print(answer)