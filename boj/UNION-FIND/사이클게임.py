import sys

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n)]
answer = 0
for idx in range(1, m+1):
    x, y = map(int, sys.stdin.readline().split())
    if answer:
        continue
    if find(x) != find(y):
        union(x, y)
    else:
        answer = idx
print(answer)