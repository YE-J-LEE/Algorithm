import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 일반적인 시뮬레이션 문제이다. 보통 이런 시뮬레이션 문제들은 BFS로 푸는 형태가 많다.
# Python으로 제출했으나 시간 초과가 났고 Pypy로는 통과했다.
# 최근 채점 현황을 살펴보니 대부분 Python으로 시간 초과가 나서 Pypy로 가는 것을 보았다.
# 그리고 해당 Pypy에서의 걸린 시간들은 내가 제일 빠르긴 했다.
# 혹시나 해서 맞은 사람 중 전체를 조회하니 역시나.. 한 6명 정도가 Python으로 3~4초 가량 시간대에 성공한 것을 볼 수 있었다.
# 그 중 열람이 가능한 코드가 있어서 들어가 코드를 보았다.
# 여러번의 함수 호출, 그리고 zip이나 reversed, list 같은 내장 함수들을 섞어 써서 앞선 등수의 사람들 시간대인 3초보다는 늦은
# 4초에 성공한 것 같다. 그렇다면 내 코드는 왜 통과하지 못했는가.
# 살펴보니 조금 하드코딩된 부분이 있는 것을 확인했다. 일반적으로 2차원 행렬에서 네 방향 이동을 해 BFS의 queue에 넣는 방식을
# 구현할 때, 대개 dx와 dy를 선언해 4짜리의 for문으로 dx, dy의 배열을 각각 열람한 후 값을 더해 확인한다.
# 하지만 이 사람의 경우, 그 부분을 그냥 하드 코딩했다. 또한, 해당 좌표가 배열 인덱스를 벗어난 경우를 체크하는 if문의 시간조차
# 없애버리기 위해 0값으로 미리 2차원 행렬 주변에 패딩시켜놨다. 아마 이 좌표를 하드코딩하며 패딩값을 통해 if문 시간을 없애버린 것이
# 키포인트인 것 같다. 하지만 나는 일반적인 접근 방식을 선호하기 때문에 Pypy로 제출한 내 코드가 더 일반적인 접근 방식이라고 생각되어 그대로 두었다.
# 물론 하드코딩된 부분은 마음에 안 들지만 if문 시간을 없애버리기 위해 행렬 주위를 패딩시키는 기술은 기억해두는게 좋겠다.
def fireStorm(l):
    global N
    # l : 한 변의 길이
    if l == 1:
        return
    x1, y1 = 0, 0
    x2, y2 = l-1, l-1
    for _ in range((N//l)**2):
        nA = []
        for j in range(y1, y2+1):
            row = []
            for i in range(x2, x1-1, -1):
                row.append(A[i][j])
            nA.append(row)
        for i in range(l):
            for j in range(l):
                A[i+x1][j+y1] = nA[i][j]
        if y2 == N - 1:
            x1, y1 = x1+l, 0
            x2, y2 = x1+l-1, y1+l-1
        else:
            x1, y1 = x1, y1+l
            x2, y2 = x1+l-1, y1+l-1

N, Q = map(int, sys.stdin.readline().split())
N = 2**N
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
L = list(map(int, sys.stdin.readline().split()))
for k in range(Q):
    fireStorm(2**L[k])
    copyA = [row[:] for row in A]
    for i in range(N):
        for j in range(N):
            if A[i][j] == 0:
                continue
            cnt = 0
            for d in range(4):
                ni = i + dx[d]
                nj = j + dy[d]
                if -1 < ni < N and -1 < nj < N and A[ni][nj] != 0:
                    cnt += 1
            if cnt < 3:
                copyA[i][j] -= 1
    A = copyA

iceSum, maxIce = 0, 0
for row in A:
    iceSum += sum(row)
visited = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if A[i][j] == 0 or visited[i][j]:
            continue
        partialIce = 0
        queue = deque([(i, j)])
        visited[i][j] = True
        while queue:
            x, y = queue.popleft()
            partialIce += 1
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if -1 < nx < N and -1 < ny < N and not visited[nx][ny] and A[nx][ny] != 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
        maxIce = max(maxIce, partialIce)
print(iceSum)
print(maxIce)