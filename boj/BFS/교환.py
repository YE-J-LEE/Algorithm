import sys
from collections import deque

# BOJ 1039
# 풀이를 알고도 잘못된 생각으로 지레 겁을 먹어 무한 고민에 빠졌던 문제다.
# 처음 문제를 보고나서 생각난 풀이로 풀어나가기 전 시간 및 공간 복잡도를 생각해봤다.
# 매 단계마다 교환할 총 횟수는 최대가 21번이다. 그런데 이를 통해 BFS 가지를 쭉 뻗어나갈 생각을 해보니 20^10번인 것이다!
# 그래서 전부 다 다른 최악의 경우가 된다면 매 20씩 곱해진 수들이 쌓여갈 것이라 생각해버렸다.
# 그런데 하나 놓친 것이 있었다. 아무리 다 달라도 20번의 비교 연산 후에 결국엔 7! = 5040개의 수들만 큐에 쌓일 것이란 걸..

N, K = map(int, sys.stdin.readline().split())
maxVal = 1000000
visited = [[False]*(K+1) for _ in range(maxVal)]
S = str(N)
if len(S) == 1 or N in (10, 20, 30, 40, 50, 60, 70, 80, 90):
    print(-1)
elif N == maxVal:
    print(maxVal)
else:
    answer = 0
    queue = deque([(S, 0)])
    M = len(S)
    while queue:
        s, depth = queue.popleft()
        if depth == K:
            answer = max(answer, int(s))
            continue
        s = list(s)
        for i in range(M-1):
            for j in range(i+1, M):
                if i == 0 and s[j] == '0':
                    continue
                s[i], s[j] = s[j], s[i]
                changed = ''.join(s)
                if not visited[int(changed)][depth+1]:
                    visited[int(changed)][depth+1] = True
                    queue.append((changed, depth+1))
                s[i], s[j] = s[j], s[i]
    print(answer)
