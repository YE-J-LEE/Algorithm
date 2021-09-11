import sys

# 일반적인 백트래킹으로 구현했지만
# Python으로 제출해서 시간초과가 났고 pypy로는 통과했지만
# 조금 더 타이트하게 풀면 최적화가 가능해보인다.

def backTracking(cnt, result):
    global N, answer
    if cnt == N:
        answer.add(result)
        return
    for i in range(N):
        if result:
            if not visited[i] and result[-1] != S[i]:
                visited[i] = True
                backTracking(cnt+1, result+S[i])
                visited[i] = False
        else:
            visited[i] = True
            backTracking(cnt+1, S[i])
            visited[i] = False

S = sys.stdin.readline().rstrip()
N = len(S)
answer = set()
visited = [False]*N
backTracking(0, '')
print(len(list(answer)))




















