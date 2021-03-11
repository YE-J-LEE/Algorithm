import sys

N = int(sys.stdin.readline())
DP = [0]*(N+1)
if N%2!=0:
    print(0)
elif N==2:
    print(3)
elif N==4:
    print(9+2)
else:
    DP[2] = 3
    DP[4] = 11
    for i in range(5, N+1):
        if i%2==0:
            DP[i] = DP[i-2]*3 + 2
            for j in range(4, i, 2):
                DP[i] += DP[i-j]*2

    print(DP[N])