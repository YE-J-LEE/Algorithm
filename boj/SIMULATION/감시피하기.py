import sys
from itertools import combinations

# BOJ 18428
# 이 문제는 조합과 시뮬레이션 문제이다. N이 6까지라 총 36개의 좌표에서 3개를 선택하는 경우가 7천이었나.. 계산해보니 그리 높지 않은 숫자였다.
# 그래서 재귀를 통해 하나씩 좌표를 방문배열로 체크해가며 조합을 만들기보단.. 내장함수로 미리 전부 구해놓고 하나씩 검사해봐도 될 것 같았다.
# 코드를 짜는데 시간이 많이 걸린것은 바로 T가 S를 찾기 위해 십자모양으로 탐색하는 부분이었다. 결국엔 하드코딩이 되긴 했다만..
# 하드코딩은 짜고 나서 보면 안 이쁘다. 그렇다고 한 번에 잡아서 다 묶고 if 문을 활용해 되는 애들만 쏙 체크한다거나... 오히려 머리가 아플것 같아서 그냥 이렇게 짰다.

def check(x, y):
    midX, midY = x, y
    while x-1 >-1:
        x -= 1
        if matrix[x][y] == 'O':
            break
        elif matrix[x][y] == 'S':
            return True
    x, y = midX, midY
    while x+1 < N:
        x += 1
        if matrix[x][y] == 'O':
            break
        elif matrix[x][y] == 'S':
            return True
    x, y = midX, midY
    while y + 1 < N:
        y += 1
        if matrix[x][y] == 'O':
            break
        elif matrix[x][y] == 'S':
            return True
    x, y = midX, midY
    while y - 1 > -1:
        y -= 1
        if matrix[x][y] == 'O':
            break
        elif matrix[x][y] == 'S':
            return True
    return False


N = int(sys.stdin.readline())
matrix = [sys.stdin.readline().split() for _ in range(N)]
idx = 0
teacher = []
blank = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'T':
            teacher.append((i, j))
        elif matrix[i][j] == 'X':
            blank.append(idx)
        idx += 1
answer = False
for comb in combinations(blank, 3):
    for pos in comb:
        x, y = pos//N, pos%N
        matrix[x][y] = 'O'
    for x, y in teacher:
        if check(x, y):
            break
    else:
        answer = True
        break
    for pos in comb:
        x, y = pos//N, pos%N
        matrix[x][y] = 'X'
if answer:
    print('YES')
else:
    print('NO')
