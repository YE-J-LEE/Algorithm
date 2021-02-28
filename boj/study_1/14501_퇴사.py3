import sys

N = int(sys.stdin.readline())
goal = N+1

table = {}
profit = {}
stack = []

for i in range(1,N+1):
    T, P = map(int, sys.stdin.readline().split())
    if i+T <= goal:
        table[i] = [x for x in range(i + T, goal + 1)]
        profit[i] = P
        stack.append((i, P))
    else:
        table[i] = [x for x in range(i + 1, goal + 1)]
        profit[i] = 0

maxPro = 0

while stack:
    dst, pro = stack.pop()
    if dst == goal:
        if maxPro < pro:
            maxPro = pro
    else:
        for d in table[dst]:
            if d == goal:
                stack.append((goal, pro))
            else:
                stack.append((d, pro+profit[d]))


print(maxPro)