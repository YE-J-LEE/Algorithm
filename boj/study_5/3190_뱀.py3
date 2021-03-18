import sys
from collections import deque

N = int(sys.stdin.readline())
board = [[0]*N for _ in range(N)]
snake = [[False]*N for _ in range(N)]
snake[0][0] = True
direction = deque()
trace = deque()
time = 1
go = "right"

K = int(sys.stdin.readline())
for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    board[x-1][y-1] = 1

L = int(sys.stdin.readline())
for _ in range(L):
    x, c = sys.stdin.readline().split()
    direction.append((int(x), c))
x, y = 0, 0
tx, ty = 0, 0
def head(di):
    global go
    if go == "left":
        if di=="L":
            go = "down"
        else:
            go = "up"
    elif go == "up":
        if di=="L":
            go = "left"
        else:
            go = "right"
    elif go == "right":
        if di=="L":
            go = "up"
        else:
            go = "down"
    else:
        if di=="L":
            go = "right"
        else:
            go = "left"
    return

def move():
    global tx, ty, time, x, y, N
    # if time == direction[0][0]:
    #     _, c = direction.popleft()
    #     head(c)
    #     return True
    #time += 1
    if go=="left":
        if -1<x<N and -1<y-1<N and not snake[x][y-1]:
            snake[x][y-1] = True
            trace.append((0, -1))
            if board[x][y-1]==0:
                nx, ny = trace.popleft()
                snake[tx][ty] = False
                tx += nx
                ty += ny
            else:
                board[x][y-1] = 0
            y -= 1
        else:
            return False
    elif go=="up":
        if -1<x-1<N and -1<y<N and not snake[x-1][y]:
            snake[x-1][y] = True
            trace.append((-1, 0))
            if board[x-1][y]==0:
                nx, ny = trace.popleft()
                snake[tx][ty] = False
                tx += nx
                ty += ny
            else:
                board[x - 1][y] = 0
            x -= 1
        else:
            return False
    elif go=="right":
        #print(type(x), type(y), type(N))
        if -1<x<N and -1<y+1<N and not snake[x][y+1]:
            snake[x][y+1] = True
            trace.append((0, 1))
            if board[x][y+1]==0:
                nx, ny = trace.popleft()
                snake[tx][ty] = False
                tx += nx
                ty += ny
            else:
                board[x][y + 1] = 0
            y += 1
        else:
            return False
    else:
        if -1<x+1<N and -1<y<N and not snake[x+1][y]:
            snake[x+1][y] = True
            trace.append((1, 0))
            if board[x+1][y]==0:
                nx, ny = trace.popleft()
                snake[tx][ty] = False
                tx += nx
                ty += ny
            else:
                board[x + 1][y] = 0
            x += 1
        else:
            return False
    return True

while move():
    #print(x, y, time, go)
    if direction and time == direction[0][0]:
        _, c = direction.popleft()
        head(c)
    time += 1

print(time)