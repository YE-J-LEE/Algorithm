# 이 문제는 BFS풀이와 플로이드와샬 2가지 풀이가 있다.
# 나에게 더 익숙하고 자주 쓰는 풀이인 BFS를 이용하여 pypy를 통해 풀어냈다. 6초가 걸렸다.
# 아무래도 입력으로 들어오는 테스트 케이스들에 대하여 BFS를 돌때마다 항상 set 자료구조를 통해 방문했던 노드들을 차집합 해주는 부분이
# 시간을 많이 잡아먹는 것 같았다.
# 그래서 비록 플로이드와샬 풀이가 O(N^3)=6400만 정도이지만 한 번 만들고나면
# 입력받는 테스트 케이스들에 대하여 전부 O(1)내로 출력할 수 있기에 플로이드 와샬로 풀자
# 6400만이라 2초라는 시간을 줘도 Python으로는 애초에 2초면 4000만이 최선이기에 pypy로 제출했고 0.7초가 나왔다.

# BFS풀이 6초
# import sys
# from collections import deque
#
# def check(G, src, dst):
#     queue = deque([(src)])
#     visited = {src}
#     while queue:
#         x = queue.popleft()
#         if x == dst:
#             return True
#         for nx in G[x]-visited:
#             visited.add(nx)
#             queue.append(nx)
#     return False
#
# n, k = map(int, sys.stdin.readline().split())
# graph = [set() for _ in range(n+1)]
# reversedGraph = [set() for _ in range(n+1)]
# for _ in range(k):
#     pre, post = map(int, sys.stdin.readline().split())
#     graph[pre].add(post)
#     reversedGraph[post].add(pre)
# s = int(sys.stdin.readline())
# for _ in range(s):
#     a, b = map(int, sys.stdin.readline().split())
#     if check(graph, a, b):
#         print(-1)
#     elif check(reversedGraph, a, b):
#         print(1)
#     else:
#         print(0)

# 플로이드와샬 풀이 0.7초
import sys

n, k = map(int, sys.stdin.readline().split())
floyd = [[0]*n for _ in range(n)]
for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    floyd[a-1][b-1] = 1
s = int(sys.stdin.readline())
for k in range(n):
    for i in range(n):
        for j in range(n):
            if floyd[i][k] and floyd[k][j]:
                floyd[i][j] = 1
for _ in range(s):
    a, b = map(int, sys.stdin.readline().split())
    if floyd[a-1][b-1]:
        print(-1)
    elif floyd[b-1][a-1]:
        print(1)
    else:
        print(0)







