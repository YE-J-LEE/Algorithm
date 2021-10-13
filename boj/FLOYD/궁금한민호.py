import sys

# BOJ 1507
# 이 문제는 겉으로 생긴건 플로이드와샬이라 플로이드와샬 알고리즘으로 탐색해야겠다는 냄새는 맡을 수 있는 문제다.
# 하지만 어떻게 응용할지가 좀 어려운 문제였다.
# 이미 기록된 정보들이 최소 cost인 것은 알겠으나 floyd[i][k] + floyd[k][j] == floyd[i][j] 라는 조건문에서
# 총 3가지의 경로가 있는데 대체 어떤 경로를 지워야 할까? 가 어려웠다.
# 다른 사람의 풀이를 참고했을때 k를 거치는 경로를 살리고 i - j 경로를 삭제한 것을 볼 수 있다.
# 단편적으로만 생각했을때 이해가 잘 되지 않았다.
# 하지만 '확실하게' 지울 수 '있는' 것만 지운다는 생각으로 접근해보면 k를 거치는 경로를 지우는 것은 확실치 않아도
# i - j 경로를 지우는 것은 확실하기 때문에 이런식으로 하나씩 지운다면 나중엔 정말 필요한 것만 남게 될 것 이라는 걸 깨닫게 되었다.

def solve(floyd, off):
    for k in range(N):
        for i in range(N):
            if k == i:
                continue
            for j in range(N):
                if i == j or k == j:
                    continue
                if floyd[i][k] + floyd[k][j] == floyd[i][j]:
                    off[i][j] = True
                elif floyd[i][k] + floyd[k][j] < floyd[i][j]:
                    return False
    return True

N = int(sys.stdin.readline())
floyd = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0
off = [[False]*N for _ in range(N)]
if solve(floyd, off):
    for i in range(N):
        for j in range(i, N):
            if not off[i][j]:
                answer += floyd[i][j]
    print(answer)
else:
    print(-1)
