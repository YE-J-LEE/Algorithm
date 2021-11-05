import sys
from collections import deque
sys.setrecursionlimit(10**7)

# BOJ 15681
# 프로그래머스에서 이와 비슷한 로직이 포함된 문제를 푼적이 있다. 그때는 크기가 작은 트리라 stack을 활용한 DFS로 이동 경로를 거꾸로
# 올라가며 +1씩 해주었는데, 이번엔 범위가 커서 통하지 않았다. 그러다 밑을 보니 문제에 대한 힌트가 나와있길래 재귀를 활용해 더해주면 쉽게
# 풀리는 것을 확인하였다. 그래서 코드를 해당 로직을 참고하여 작성한 후 통과하였다. 앞으로 서브트리 갯수 세는 것은 이 방법을 이용해야겠다

def solve(cur):
    subTree[cur] = 1
    for nx in child[cur]:
        solve(nx)
        subTree[cur] += subTree[nx]

N, R, Q = map(int, sys.stdin.readline().split())
tree = [set() for _ in range(N+1)]
child = [[] for _ in range(N+1)]
for _ in range(N-1):
    U, V = map(int, sys.stdin.readline().split())
    tree[U].add(V)
    tree[V].add(U)
query = [int(sys.stdin.readline()) for _ in range(Q)]
stack = [(R, [R])]
visited = {R}
subTree = [0]*(N+1)
queue = deque([R])
while queue:
    x = queue.popleft()
    for nx in tree[x]-visited:
        child[x].append(nx)
        queue.append(nx)
        visited.add(nx)
solve(R)
for q in query:
    print(subTree[q])
