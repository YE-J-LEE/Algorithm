import sys
from collections import deque

n = int(sys.stdin.readline())
p1, p2 = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

people = {x: [] for x in range(1, n+1)}
visited = [False]*(n+1)
visited[p1] = True

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    people[x].append(y)
    people[y].append(x)

queue = deque([(p1, 0)])
flag = True
while queue:
    person, depth = queue.popleft()
    if person==p2:
        flag = False
        print(depth)
        break
    for dst in people[person]:
        if visited[dst]:
            continue
        visited[dst] = True
        queue.append((dst, depth+1))
if flag:
    print(-1)