import sys

# 간단한 재귀의 완전탐색 문제이다

def solve(idx, eggs):
    global res
    if idx == N:
        cnt = 0
        for i in range(N):
            if eggs[i] <= 0:
                cnt +=1
        if cnt > res:
            res = cnt
        return

    if eggs[idx] > 0:
        flag = False
        for i in range(N):
            if eggs[i] > 0 and i != idx:
                flag = True
                tmp = eggs[:]
                tmp[i] -= w[idx]
                tmp[idx] -= w[i]
                solve(idx+1, tmp)
        if not flag:
            solve(idx+1, eggs)
    else:
        solve(idx+1, eggs)
N = int(sys.stdin.readline())
s = [0]*N
w = [0]*N
for i in range(N):
    s[i], w[i] = map(int, input().split())

res = 0
solve(0, s)
print(res)