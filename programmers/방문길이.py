# 프로그래머스 방문 길이
# 이 문제는 주의할 점이 꽤 있다.
# 좌표평면이기에 기존에 행렬의 행과 열 인덱스를 적용하기엔 사실 x, y가 서로 뒤바뀐다. 하지만 이 문제에선 그저 길이만을 구하길 원하기 때문에
# 그냥 넘어갈 수 있다. 하지만 두 번째로 주의할 점은 바로 '지나간' 길이라는 점이다.
# 어떠한 방향으로 해당 길을 지났다면 그 반대 방향으로 지날 경우도 지나간 것에 포함되므로 매번 처음 방문하는 길이라면 방문 체크로
# 반대 방향으로 지나갈 경우도 체크를 해줘야 통과할 수 있다.

def solution(dirs):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    directions = {'U': 0, 'R': 1, 'D': 2, 'L': 3}
    answer = 0
    matrix = [[-1] * 11 for _ in range(11)]
    visited = [[[False] * 4 for _ in range(11)] for _ in range(11)]
    x, y = 5, 5
    for direct in dirs:
        d = directions[direct]
        nx = x + dx[d]
        ny = y + dy[d]
        if -1 < nx < 11 and -1 < ny < 11:
            if not visited[nx][ny][d]:
                answer += 1
                apposite = (d + 2) % 4
                visited[x][y][apposite] = True
                visited[nx][ny][d] = True
            x, y = nx, ny

    return answer