import sys
from collections import deque

# 이 문제는 일반적인 시뮬레이션 문제이다.
# 원형으로 시계/반시계 방향 돌리는 행위가 있기 때문에 앞/뒤 원소 빼기/넣기 등이 O(1)시간으로 동작할 수 있는 deque를 통해 구현했다.
# 이 문제는 좀 특이하게 원형큐가 겹겹이 쌓여있는 구조이며 각 계층별로 인접하는 경우를 고려해야해서 인접한 부분을 찾는 데에
# 코드가 복잡해지는 것을 방지하고자 따로 인접 좌표들을 구하는 함수를 구현해주었다.

def getAdj(x, y):
    result = []
    global N, M
    if x == 0:
        result.append((x+1, y))
        if y == 0:
            result.append((x, y+1))
            result.append((x, M-1))
            return result
        elif y == M-1:
            result.append((x, y-1))
            result.append((x, 0))
            return result
        else:
            result.append((x, y+1))
            result.append((x, y-1))
            return result
    elif x == N-1:
        result.append((x-1, y))
        if y == 0:
            result.append((x, y+1))
            result.append((x, M-1))
            return result
        elif y == M-1:
            result.append((x, y-1))
            result.append((x, 0))
            return result
        else:
            result.append((x, y+1))
            result.append((x, y-1))
            return result
    else:
        result.append((x + 1, y))
        result.append((x - 1, y))
        if y == 0:
            result.append((x, y + 1))
            result.append((x, M - 1))
            return result
        elif y == M - 1:
            result.append((x, y - 1))
            result.append((x, 0))
            return result
        else:
            result.append((x, y + 1))
            result.append((x, y - 1))
            return result


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M, T = map(int, sys.stdin.readline().split())
matrix = [deque(map(int, sys.stdin.readline().split())) for _ in range(N)]
alive = N*M
for _ in range(T):
    x, d, k = map(int, sys.stdin.readline().split())
    for num in range(x, N+1, x):
        idx = num-1
        if d:
            for _ in range(k):
                temp = matrix[idx].popleft()
                matrix[idx].append(temp)
        else:
            for _ in range(k):
                temp = matrix[idx].pop()
                matrix[idx].appendleft(temp)
    wholeAdj = False
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                continue
            target = matrix[i][j]
            adj = False
            for ni, nj in getAdj(i, j):
                if matrix[ni][nj] == target:
                    adj = True
                    wholeAdj = True
                    break
            if not adj:
                continue
            matrix[i][j] = 0
            alive -= 1
            queue = deque([(i, j)])
            while queue:
                x, y = queue.popleft()
                for nx, ny in getAdj(x, y):
                    if matrix[nx][ny] == target:
                        matrix[nx][ny] = 0
                        alive -= 1
                        queue.append((nx, ny))
    if wholeAdj:
        continue
    sumRow = 0
    for row in matrix:
        sumRow += sum(row)
    average = sumRow/alive if alive != 0 else 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                continue
            if matrix[i][j] < average:
                matrix[i][j] += 1
            elif matrix[i][j] > average:
                matrix[i][j] -= 1
answer = 0
for row in matrix:
    answer += sum(row)
print(answer)











