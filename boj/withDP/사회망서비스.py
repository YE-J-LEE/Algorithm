import sys
sys.setrecursionlimit(10**6)

# 이 문제는 우선 나에게 두 가지 약점을 일깨워줬다.
# 첫 번째는 트리에서 재귀를 활용하는 법이고 두 번째는 적절한 자료구조의 사용이다.
# 우선 최근까지 그래프에서 나의 탐색 방법을 보자면 대부분 BFS를 사용해 풀어왔다. 그래서인지
# 이 문제처럼 DFS로 쉽게 접근할 수 있는 문제들을 보면 풀이를 생각해내지 못 한다.
# 그리고 이 문제에서 메모리 초과가 계속 났는데, 나는 이게 DFS함수의 스택 메모리 초과라고 생각해서
# 재귀 함수 없이 구현을 대체 어떻게 하라는 건지 되게 많이 고민했었다.
# 하지만 자식 노드를 탐색한 후에 DP 값을 채워주는 순서는 이 순서 자체가 너무 훌륭하기에 stack이라는 리스트를 따로 선언해
# 진행할 수 없었다. 재귀함수만으로 구현한 이 순서를 지킬 수 없기 때문이다.
# 그래서 다른 사람의 풀이와 내 풀이를 비교하던 중, graph를 짜는 데에 그냥 리스트를 사용한 것을 볼 수 있었다.
# 나는 딕셔너리 자료구조를 통해 풀어냈었다. 바로 여기서 사소한 메모리 차이가 생겨난 것이다.
# 일반적으로 딕셔너리는 해시 테이블을 이용해 구현되기에 순수 리스트보다 빠른 대신 메모리를 더 잡아먹는다.
# 내가 우려했던 재귀 함수 스택 메모리 이외에 애초에 그래프를 담고 있던 자료구조 자체가 메모리를 많이 잡아먹던 것이었다.
# 앞으로는 그래프를 짤 때 노드들을 담을 자료구조 선택을 신중하게 해야겠다는 생각을 하게 되었다.

def dfs(parent):
    visited[parent] = True
    DP[parent][1] = 1
    for child in graph[parent]:
        if not visited[child]:
            dfs(child)
            DP[parent][0] += DP[child][1]
            DP[parent][1] += min(DP[child][1], DP[child][0])

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [False]*(N+1)
DP = [[0]*2 for _ in range(N+1)]
dfs(1)
print(min(DP[1]))









