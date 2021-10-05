import sys

# BOJ 1941
# 이 문제는 정말.. 많은걸 배우게 된 문제다.
# 우선 BFS나 DFS 특성상 한 번 방문했던 노드는 다시는 거치지 않는 특성 때문에, 특정 길이를 만족하는
# 모든 가짓수를 파악하기 힘들다. 따라서 조합을 통해 길이가 7인 경우를 모두 탐색해봐야 하는데,
# 이를 위해 여기선 좌표 공간을 정수 하나로 표현하는 특이한 방식이 도입된다.
# 총 5x5의 행렬에서 각 좌표공간을 0~24로 채운 뒤에 //5와 %5를 활용해 x, y 좌표를 구할 수 있다.
# 따라서 0~24까지의 25개 좌표에 대하여 7개를 뽑는 조합을 고려하고, 해당 조합에서
# 서로가 이어지는 지의 여부를 파악하면 되는 문제였다.
# 그리고 조합을 위한 백트래킹 과정 중에 변수를 겹치게 선언하여 문제 원인을 찾는 데에 시간을 꽤나 할애했었다.
# 다음부턴 신중하게 변수명을 정해야겠다는 생각을 하게 되었다.

def able(current):
    check = {x: False for x in current}
    sX, sY = current[0] // 5, current[0] % 5
    visited = [[False] * 5 for _ in range(5)]
    stack = [(sX, sY)]
    while stack:
        x, y = stack.pop()
        visited[x][y] = True
        num = pos2Idx[x][y]
        if num in check:
            check[num] = True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if -1 < nx < 5 and -1 < ny < 5 and pos2Idx[nx][ny] in check and not check[pos2Idx[nx][ny]]:
                stack.append((nx, ny))
    if False not in check.values():
        return True
    else:
        return False

def solve(start, nY, n, current):
    global answer
    if nY > 3:
        return
    if n == 7:
        if able(current):
            answer += 1
        return
    for i in range(start, 25):
        x, y = i//5, i%5
        if girls[x][y] == 'Y':
            solve(i+1, nY+1, n+1, current + [i])
        else:
            solve(i+1, nY, n+1, current + [i])


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

girls = [list(sys.stdin.readline().rstrip()) for _ in range(5)]
pos2Idx = [[-1]*5 for _ in range(5)]
idx = 0
answer = 0
for i in range(5):
    for j in range(5):
        pos2Idx[i][j] = idx
        idx += 1
solve(0, 0, 0, [])
print(answer)