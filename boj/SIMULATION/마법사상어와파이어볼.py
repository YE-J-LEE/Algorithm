import sys

# BOJ 20056
# 마법사 상어 시리즈.. 이번 시뮬레이션은 꽤 어려웠다. 각각의 파이어볼들이 질량, 속도, 방향을 고유하게 가지고 있어서
# 파이어볼이 이동하면 이동한 곳에 그 정보들을 기록했어야 했다. 때문에 불가피하게 매 반복문마다 새롭게 파이어볼 내용을 담은 배열을 재선언해줬는데
# 아무래도 이것 때문에 시간이 좀 걸리는 것 같다. 물론 Python으로 1.3초 가량에 통과는 됐지만 더 빠른 방법을 모색해봐야 겠다.

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, sys.stdin.readline().split())
matrix = [[0]*N for _ in range(N)]
fireBalls = []
for _ in range(M):
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    fireBalls.append((r-1, c-1, m, s, d))
    matrix[r-1][c-1] += 1
for _ in range(K):
    current = [[[] for _ in range(N)] for _ in range(N)]
    while fireBalls:
        r, c, m, s, d = fireBalls.pop()
        matrix[r][c] -= 1
        nr, nc = -1, -1
        deltaR = dx[d]*s
        deltaC = dy[d]*s
        if deltaR < 0:
            deltaR = (-deltaR)%N
            nr = r - deltaR if r - deltaR > -1 else r - deltaR + N
        else:
            nr = (r + deltaR)%N
        if deltaC < 0:
            deltaC = (-deltaC)%N
            nc = c - deltaC if c - deltaC > -1 else c - deltaC + N
        else:
            nc = (c + deltaC)%N
        matrix[nr][nc] += 1
        current[nr][nc].append((m, s, d))
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                m, s, d = current[i][j][0]
                fireBalls.append((i, j, m, s, d))
            elif matrix[i][j] >= 2:
                m, s, odd, even = 0, 0, 0, 0
                for subM, subS, d in current[i][j]:
                    m += subM
                    s += subS
                    if d%2 == 0:
                        even += 1
                    else:
                        odd += 1
                m //= 5
                if m:
                    s //= matrix[i][j]
                    if odd == matrix[i][j] or even == matrix[i][j]:
                        for d in [0, 2, 4, 6]:
                            fireBalls.append((i, j, m, s, d))
                    else:
                        for d in [1, 3, 5, 7]:
                            fireBalls.append((i, j, m, s, d))
                    matrix[i][j] = 4
                else:
                    matrix[i][j] = 0
answer = 0
for _, _, m, _, _ in fireBalls:
    answer += m
print(answer)