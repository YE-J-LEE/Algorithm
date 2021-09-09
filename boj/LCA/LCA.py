import sys
from collections import deque

# 이 문제는 공통 조상을 찾는 문제이다.
# 저번 단계 문제들을 풀 때 푼 적이 있다.
# 그때 역시 지금처럼 상식적인 접근법으로 깊이를 맞춰주고 올라가기 시작하며 값이 같아질 때 리턴했다.
# 이 모든건 트리에서 각 노드당 부모는 1개일 수 밖에 없다는 조건 하에 성립된다.
# 이 문제에서 어려웠던 점은 바로 트리를 구성하는 일이었다.
# 입력으로 들어오는 두 노드 중 어느 노드가 부모인지 안 알려줬다.
# 애초에 문제에서 노드 범위 5만개로, 2차원 배열을 통해 양방향을 구현하려들면 5만*5만이다.
# 시간제한은 3초, 여기서 파이썬으로 문제를 푸는 사람들은 괴리에 빠진다.
# 과연 이게 될까. 아니 배열을 생성할때부터 시간초과가 나버릴까..
# 하지만 밑져야 본전으로.. 시도해봤어야 했다. 배열이 생성되지 않을까 두려워
# 효율적으로 풀고자 해서 풀었던 풀이가 되려 완전브루트포스하게 되었다.
# 이 아래 코드는 조금 유연하게 2차원 배열을 생성한 코드이다. 이를 통해 시간을 절반 줄일 수 있었다.
# 하지만 이 역시 pypy로 통과한 코드며 다른 문제 풀이를 찾던중 LCA 알고리즘 풀이들이 다양한 것으로 보이며
# LCA 역시 추후 공부해야할 목록에 추가해야겠다. 언뜻보았지만 세그먼트트리나 DP를 이용한 풀이들이 있는 것 같은데
# 아직 내 레벨보다 높은 수준이다..

N = int(sys.stdin.readline())
depth = [-1]*(N+1)
depth[1] = 0
parent = {}
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    edges[a].append(b)
    edges[b].append(a)
queue = deque([(1, 0)])
while queue:
    x, level = queue.popleft()
    for nx in edges[x]:
        if depth[nx] == -1:
            depth[nx] = level + 1
            parent[nx] = x
            queue.append((nx, depth[nx]))
M = int(sys.stdin.readline())
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if depth[a] > depth[b]:
        for _ in range(depth[a] - depth[b]):
            a = parent[a]
    elif depth[a] < depth[b]:
        for _ in range(depth[b] - depth[a]):
            b = parent[b]
    while a != b:
        a = parent[a]
        b = parent[b]
    print(a)

