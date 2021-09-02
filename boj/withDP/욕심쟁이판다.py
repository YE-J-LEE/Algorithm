import sys
sys.setrecursionlimit(10**5)

# n의 max는 500이고 전체 매트릭스 크기는 nxn이다.
# 또한 시작은 어느 지점에서 할지도 모르고 그저 숫자가 커지는대로 계속 이어나갈 때 가장 큰 길이를 구하는 것이다.
# 사고의 시작인 브루트포스적 관점으로 워스트하게 구할 경우 시작 지점을 전부 고려했을 때 25만, 그리고 거기서 모든 지점을 탐색할때 25만 * 25만 = 625억이다.
# 보통 이런 경우 메모이제이션을 통해 이미 검사한 값을 재사용하여 시간을 단축시켜야 한다.
# 하지만 쉬운 행렬에서의 DP문제의 경우, 최단거리를 물으며 시작지점이 정해져 있고 오른쪽 혹은 아래로만 이동하는 규칙이 정해져
# DP 점화식을 구현하기 쉽게 되어있다. 하지만 이 경우는 다르다. 현재 내가 있는 지점을 오기까지 위 혹은 왼쪽에서 올 수 있지만 바로 오른쪽에서도 올 수 있고
# 아래에서 치고 올라올 수 있다. 이는 일반적인 오른쪽, 아래로 움직이던 행렬 DP문제와 조금은 다르다.
# 이 문제와 비슷한 문제를 이전에 푼 적이 있어서 다행히도 풀 수 있었다.
# DP[i][j]를 (i, j) 지점에서 시작했을 때 나올 수 있는 최장 거리라고 정한다.
# 그리고 이 문제의 핵심 조건인 자신보다 큰 값으로만 이동할 수 있는 규칙 덕분에
# solve(ni, nj)의 값을 가져다가 그대로 쓸 수 있다. 왜냐하면 바로 저 규칙 덕분에 (i, j)와 절대 겹칠 일이 없기 때문이다.
# 이런식으로 메모이제이션을 수행하며 재귀적으로 발판을 밟아나가며 답을 구했고 성공할 수 있었다.

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solve(x, y):
    if DP[x][y] != -1:
        return DP[x][y]
    DP[x][y] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if -1 < nx < n and -1 < ny < n and matrix[nx][ny] > matrix[x][y]:
            DP[x][y] = max(DP[x][y], solve(nx, ny))
    DP[x][y] += 1
    return DP[x][y]

n = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
DP = [[-1]*n for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(n):
        if DP[i][j] == -1:
            DP[i][j] = solve(i, j)
        answer = max(answer, DP[i][j])
print(answer)