import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    parent = {}
    for _ in range(N-1):
        A, B = map(int, sys.stdin.readline().split())
        parent[B] = A
    a, b = map(int, sys.stdin.readline().split())
    x, y = a, b
    depthA, depthB = 0, 0
    while a in parent:
        depthA += 1
        a = parent[a]
    while b in parent:
        depthB += 1
        b = parent[b]
    if depthA == depthB:
        while x != y:
            x = parent[x]
            y = parent[y]
        print(x)
    elif depthA > depthB:
        for _ in range(depthA - depthB):
            x = parent[x]
        while x != y:
            x = parent[x]
            y = parent[y]
        print(x)
    else:
        for _ in range(depthB - depthA):
            y = parent[y]
        while x != y:
            x = parent[x]
            y = parent[y]
        print(x)