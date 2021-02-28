import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
network = {x:set() for x in range(1, N+1)}

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    network[x].add(y)
    network[y].add(x)

visited = set()
stack = [1]

while stack:
    ndst = stack.pop()
    visited.add(ndst)
    for dst in network[ndst]-visited:
        stack.append(dst)
print(len(visited)-1)