import sys

# BOJ 14621
# 최소신장트리 문제로, 조금 특별한 부분은 '유효'한 경로를 추려내야 한다는 점이다.
# 이 점을 제외하면 나머지는 그냥 union-find를 통한 크루스칼 알고리즘으로 풀어내면 된다.

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

N, M = map(int, sys.stdin.readline().split())
parent = [i for i in range(N+1)]
gender = sys.stdin.readline().rstrip().split()
edges = []
for _ in range(M):
    u, v, d = map(int, sys.stdin.readline().split())
    if gender[u-1] != gender[v-1]:
        edges.append((u, v, d))
edges.sort(key=lambda x: x[2])
answer = 0
cnt = 0
for u, v, d in edges:
    if find(u) != find(v):
        union(u, v)
        cnt += 1
        answer += d
        if cnt == N-1:
            break
if cnt == N-1:
    print(answer)
else:
    print(-1)










