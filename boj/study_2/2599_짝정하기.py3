import sys
from itertools import permutations

N = int(sys.stdin.readline())
girls = [0]*3
boys = [0]*3
result = []
flag = True
for i in range(3):
    boys[i], girls[i] = map(int, sys.stdin.readline().split())
for p in permutations(range(3), 3):
    g = girls[:]
    b = boys[:]
    result = []
    for i in p:
        for j in range(3):
            if i==j:
                continue
            sub = min(b[i], g[j])
            b[i] -= sub
            g[j] -= sub
            result.append([i, j, sub])
    if not sum(b+g):
        flag = False
        result.sort(key=lambda x: (x[0], x[1]))
        print(1)
        for i in range(0, 6, 2):
            print(result[i][2], result[i + 1][2])
        break


if flag:
    print(0)