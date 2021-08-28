import sys

# 이 문제를 통해 그래프 내에서 사이클을 찾는 데에 가장 효율적인 방법을 찾을 수 있었다.
# 우선 첫 번째로 생각해낸 접근 방법은 DFS였다. 아무래도 BFS 보다는 DFS로 깊이 우선적으로 뻗어나가는 것이 직관적인 방법이었기 때문이다.
# 또한 탐색을 해나가는 도중에 사이클이 생긴 것을 발견하고 트리가 아니라는 사실을 확인했다고 할지라도 계속해서 뻗어나가며 방문 체크를 해주고
# 다음 노드 탐색 차례에 이미 방문했으면 건너 뛰도록 설정했다.
# 시간 초과가 났지만 Pypy로는 통과할 수 있었다. 물론 중간에 틀려서 구글링을 통해 DFS로 사이클 찾는 코드들을 살펴보고
# 사이클의 발생 지점은 시작 노드뿐만이 아니라 중간 노드에서 발생할 수도 있기 때문에 기존 depth를 stack의 두번째 인자로 넣어주는 것이 아닌
# 이전 노드를 넣어주는 트릭을 통해 해결할 수 있었다,
# 하지만 Python으로는 시간 초과가 났기에, 나는 개선하는 것을 멈추지 않았다.
# 그리고 발견한 것이 사이클이 생기는 지점에서 break를 거는 것이었다.
# 처음 접근법을 구상했을 때 사이클 지점을 찾아도 계속 탐색하며 방문체크를 미리 해버리는 것이 낫지 않나라고 생각했었지만
# 다른 사람의 BFS풀이를 보고 깊이가 충분히 깊고 브랜치역시 너무나 많은 경우엔
# 전부 다 미리 탐색해 방문체크 해버리려는 나의 생각이 내가 만든 나만의 작은 스택에겐 큰 부담이었다는 것을 알게 되었다.
# 또한 머릿속으로 접근법을 구상할때 사이클 중간에 브레이크를 걸면 나머지 놀던 노드들에 대해 탐색을 다시 시작해야하기에 오히려 이 방법이 안 될 줄 알고 시도를 안했었다.
# 하지만 스택의 형편을 고려하여 사이클이 생길 때 브레이크를 걸어줘야 함이 올바른 방법이라는 것을 꺠우치고
# 브레이크를 걸자 Python에서의 시간초과가 해결되었다. 그리고 심지어 내가 참고했던 BFS풀이 방식보다 속도가 빨라서 뿌듯했다.
idx = 1
while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    graph = {x: [] for x in range(1, n+1)}
    for _ in range(m):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)
    cnt = 0
    visited = [False]*(n+1)
    for node in range(1, n+1):
        if not graph[node]:
            cnt += 1
            continue
        if visited[node]:
            continue
        stack = [(node, 0)]
        isTree = True
        while stack:
            x, px = stack.pop()
            visited[x] = True
            for nx in graph[x]:
                if visited[nx]:
                    if nx != px or nx == x:
                        isTree = False
                        break
                else:
                    stack.append((nx, x))
            if not isTree:
                break
        if isTree:
            cnt += 1
    if cnt == 1:
        print("Case {}: There is one tree.".format(idx))
    elif cnt > 1:
        print("Case {}: A forest of {} trees.".format(idx, cnt))
    else:
        print("Case {}: No trees.".format(idx))
    idx += 1


