import sys

# BOJ 167562
# 최소한의 비용으로 모든 사람과 친구가 되어야 하므로,
# 사이클이 생기지 않는 한에서 그리디하게 union-find를 통해 최소 신장 트리를 만들어 풀었다.

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

N, M, k = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
parent = [i for i in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    union(a, b)
A = [(A[i], i+1) for i in range(N)]
A.sort()
able = 0
money = 0
for cost, person in A:
    if cost + money <= k:
        if find(0) != find(person):
            money += cost
            union(0, person)
            M += 1
            if M == N:
                able = money
                break
    else:
        break
if able:
    print(able)
else:
    print("Oh no")


