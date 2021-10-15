import sys

# BOJ 21608
# 이 문제는 시뮬레이션과 정렬 문제이다.
# 정렬에 사용되는 비교 우선순위 변수가 총 4개이다. lambda의 튜플에 차례대로 넣어주면 금방 해결되지만
# 문제 설명에서 사용되는 단어가 여러번 중복되어 나타나서 다소 난해한 경향이 있었다.

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(sys.stdin.readline())
command = [list(map(int, sys.stdin.readline().split())) for _ in range(N**2)]
classRoom = [[0]*N for _ in range(N)]
preferStudent = dict()
# -like, -blank, i, j
for info in command:
    student = info[0]
    prefer = info[1:]
    preferStudent[student] = prefer
    seats = []
    for i in range(N):
        for j in range(N):
            if classRoom[i][j]:
                continue
            blank = 0
            like = 0
            for d in range(4):
                ni, nj = i + dx[d], j + dy[d]
                if -1 < ni < N and -1 < nj < N:
                    if classRoom[ni][nj] == 0:
                        blank += 1
                    elif classRoom[ni][nj] in prefer:
                        like += 1
            seats.append((like, blank, i, j))
    seats.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    _, _, x, y = seats[0]
    classRoom[x][y] = student
answer = 0
for i in range(N):
    for j in range(N):
        score = 0
        for d in range(4):
            ni, nj = i + dx[d], j + dy[d]
            if -1 < ni < N and -1 < nj < N and classRoom[ni][nj] in preferStudent[classRoom[i][j]]:
                score += 1
        if score:
            answer += 10**(score-1)
print(answer)

