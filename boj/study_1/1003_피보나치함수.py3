import sys
T = int(sys.stdin.readline())
answer = []
DP = []
cnt = []
def fibo(n):
    if n==0:
        answer[0] += 1
        return 0
    elif n==1:
        answer[1] += 1
        return 1
    elif DP[n] > -1:
        answer[0] += cnt[n][0]
        answer[1] += cnt[n][1]
        return DP[n]
    else:
        DP[n] = fibo(n-1) + fibo(n-2)
        cnt[n] = answer[:]
        return DP[n]
for _ in range(T):
    answer = [0,0]
    n = int(sys.stdin.readline())
    DP = [0,1] + [-1]*(n-1)
    cnt = [0]*(n+1)
    fibo(n)
    print(answer[0], answer[1])