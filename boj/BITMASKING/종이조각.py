import sys

# BOJ 14391
# 이 문제 같은 경우... 완전탐색을 그대로 시행하기엔 6^16으로 아무리 겹치지 않는 가짓수들로 추린다 하여도 크다..
# 그래서 행렬에서 활성화 시킨 부위들만 따로 DP에 저장하고 싶었다. 근데 처음엔 어떻게 여러 좌표들을 한 번에 저장할 수 있을지 알 수가 없었다.
# 그런데 분류를 보니 비트마스킹. 그리고 비트마스킹이란 단어를 보자마자 최근에 익힌 좌표의 인덱싱 기법이 생각났다.
# 그래서 비트마스킹과 DP를 활용해 완전탐색이지만 중복되는 부분을 계속 갱신해가며 코드를 짜서 시간이 오래걸리긴 했지만 통과했다.
# 그런데 나보다 빠른 시간 내에 푸는 사람들이 여럿 보여서 풀이를 찾아봤다.
# 찾아보니 비트마스킹을 사용하되, 매우 간단한 해법이 존재했다.... 해당 해법은 언제 한 번 본 적이 있는 방법이었다.
# 0과 1을 가로와 세로라고 정의한 뒤에 행렬을 훑을 때 오른쪽으로는 가로로 된 것만 읽고 아래쪽으로는 세로로 된 것만 읽어서 더해주면 되는 것이었다..
# 이 문제를 통해 다시 한 번 사고가 열리는 경험을 하게 되었다.

def solve(bitmask, cnt, result):
    global N, M, L, total
    if cnt == total:
        return

    for i in range(total):
        if bitmask[i] == '1':
            continue
        x, y = i//M, i%M
        for d in range(2):
            undo = []
            subResult = ''
            for l in range(L):
                nx, ny = x + dx[d]*l, y + dy[d]*l
                if -1 < nx < N and -1 < ny < M:
                    p = p2idx[nx][ny]
                    if bitmask[p] == '1':
                        break
                    else:
                        bitmask[p] = '1'
                        bit = int(''.join(bitmask), 2)
                        subResult += matrix[nx][ny]
                        undo.append((nx, ny))
                        if visited[bit] < result + int(subResult):
                            visited[bit] = result + int(subResult)
                            solve(bitmask, cnt+l+1, visited[bit])
                else:
                    break
            for w, z in undo:
                p = p2idx[w][z]
                bitmask[p] = '0'


N, M = map(int, sys.stdin.readline().split())
total = N*M
L = max(N, M)
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
dx = [0, 1]
dy = [1, 0]
num = 0
p2idx = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        p2idx[i][j] = num
        num += 1
bitmask = ['0']*total
visited = [-float('inf')]*(2**total)
solve(bitmask, 0, 0)
print(visited[2**total-1])