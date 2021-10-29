import sys
from collections import deque

# BOJ 16988
# 조합을 통한 완전탐색 문제로, 2가지만 뽑으면 되기에 배열 좌표들을 인덱스화 하여 짝을 지어주어 해결했다.

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())
baduk2 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0
total = N*M
for first in range(total-1):
    x1, y1 = first // M, first % M
    if baduk2[x1][y1] != 0:
        continue
    for second in range(first+1, total):
        x2, y2 = second//M, second%M
        if baduk2[x2][y2] != 0:
            continue
        visited = [[False] * M for _ in range(N)]
        baduk2[x1][y1] = 1
        baduk2[x2][y2] = 1
        totalScore = 0
        for i in range(N):
            for j in range(M):
                if baduk2[i][j] != 2 or visited[i][j]:
                    continue
                visited[i][j] = True
                compact = True
                score = 0
                queue = deque([(i, j)])
                while queue:
                    x, y = queue.popleft()
                    score += 1
                    cnt = 0
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if -1 < nx < N and -1 < ny < M:
                            if baduk2[nx][ny] == 0:
                                cnt += 1
                            elif baduk2[nx][ny] == 2 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
                    if cnt:
                        compact = False
                if compact:
                    totalScore += score
        answer = max(answer, totalScore)
        baduk2[x1][y1] = 0
        baduk2[x2][y2] = 0
print(answer)








