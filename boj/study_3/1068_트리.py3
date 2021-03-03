import sys
from collections import deque

N = int(sys.stdin.readline())
Tree = {x: [] for x in range(-1, 50)}
visited = [False]*50
parents = list(map(int, sys.stdin.readline().split()))
rid = int(sys.stdin.readline())
root = []

for i in range(N):
    parent = parents[i]
    Tree[parent].append(i)
    if parent == -1:
        root.append(i)
answer = 0
for r in root:
    if r==rid:
        continue
    queue = deque([r])
    visited[r] = True

    while queue:
        p = queue.popleft()

        if Tree[p]:
            for np in Tree[p]:
                if visited[np]:
                    continue
                if np==rid:
                    if len(Tree[p])==1:
                        answer += 1
                    continue
                visited[np] = True
                queue.append(np)
        else:
            answer += 1

print(answer)