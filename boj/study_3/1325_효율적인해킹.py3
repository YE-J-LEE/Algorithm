import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
computers = {x:[] for x in range(1, N+1)}
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    computers[B].append(A)

answer = []
maxNum = 0
for i in range(1, N+1):
    if not computers[i]:
        continue
    queue = deque([i])
    visited = [False]*(N+1)
    visited[i] = True
    result = 1
    while queue:
        current = queue.popleft()
        for dst in computers[current]:
            if visited[dst]:
                continue
            visited[dst] = True
            result += 1
            queue.append(dst)
    if maxNum == result:
        answer.append(i)
    elif maxNum < result:
        answer = [i]
        maxNum = result

print(*answer)