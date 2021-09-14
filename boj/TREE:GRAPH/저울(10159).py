import sys
from collections import deque

def check(G, src, dst):
    queue = deque([src])
    visited = {src}
    while queue:
        x = queue.popleft()
        if x == dst:
            return True
        for nx in G[x]-visited:
            visited.add(nx)
            queue.append(nx)
    return False

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = {x: set() for x in range(1, N+1)}
reversedGraph = {x: set() for x in range(1, N+1)}
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].add(b)
    reversedGraph[b].add(a)
for i in range(1, N+1):
    cnt = 0
    for j in range(1, N+1):
        if i == j:
            continue
        if not check(graph, i, j) and not check(reversedGraph, i, j):
            cnt += 1
    print(cnt)








