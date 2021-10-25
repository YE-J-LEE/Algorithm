# programmers weekly 12
# DP인가 싶었지만 적절한 break point를 가진 백트래킹으로 볼 수도 있고 전반적인 틀은 완전탐색인 문제였다.
# 이것으로 프로그래머스 위클리 챌린지가 끝났다고 하는데 조금 아쉽다..

answer = 0
N = -1
visited = []


def solve(i, stamina, dungeons):
    global answer, N, visited
    if i == N:
        answer = N
        return
    for j in range(N):
        if visited[j]:
            continue
        if stamina >= dungeons[j][0]:
            visited[j] = True
            solve(i + 1, stamina - dungeons[j][1], dungeons)
            visited[j] = False
        else:
            answer = max(answer, i)


def solution(k, dungeons):
    global answer, N, visited
    N = len(dungeons)
    visited = [False] * N
    solve(0, k, dungeons)
    return answer





