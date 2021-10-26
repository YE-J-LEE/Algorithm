import sys

# BOJ 11780
# 이 문제는 문제 이름부터가 플로이드2다. Vertex의 개수 n은 최대가 100이라 n^3까지 수용 가능. 그리고 출력 형태에서도
# 플로이드로 풀어달라고 애원하고 있다. 바로 플로이드로 풀었다. 문제 제목인 플로이드2답게 최소비용 이외에 추가적으로
# 요구되는 출력값으로는 경로가 있었다. 이에 대해선 최소비용값이 갱신될 때마다 경로 역시 갱신해주는 방식으로 해결했다.

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
floyd = [[float('inf')]*n for _ in range(n)]
path = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    path[a-1][b-1] = [a, b]
    floyd[a-1][b-1] = min(floyd[a-1][b-1], c)
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if floyd[i][j] > floyd[i][k] + floyd[k][j]:
                floyd[i][j] = floyd[i][k] + floyd[k][j]
                path[i][j] = path[i][k][:-1] + path[k][j]
for i in range(n):
    for j in range(n):
        if floyd[i][j] == float('inf'):
            sys.stdout.write("0 ")
        else:
            sys.stdout.write(str(floyd[i][j]) + ' ')
    sys.stdout.write('\n')
for i in range(n):
    for j in range(n):
        l = len(path[i][j])
        if l == 0:
            sys.stdout.write("0")
        else:
            sys.stdout.write(str(l) + " ")
            for k in range(l):
                sys.stdout.write(str(path[i][j][k]) + ' ')
        sys.stdout.write('\n')