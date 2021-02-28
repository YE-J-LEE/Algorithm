import sys
N = int(sys.stdin.readline())
stairs = []
for _ in range(N):
    stairs.append(int(sys.stdin.readline()))
#stairs.reverse()

if N==1:
    print(stairs[0])
elif N==2:
    print(sum(stairs))
elif N==3:
    print(stairs[-1] + max(stairs[:2]))
elif N==4:
    print(stairs[0] + stairs[3] + max(stairs[1:3]))
else:
    DP = [0] * (N + 1)
    DP[1] = stairs[0]
    DP[2] = stairs[0] + stairs[1]
    DP[3] = stairs[2] + max(stairs[:2])
    DP[4] = stairs[0]+stairs[3]+max(stairs[1:3])
    for i in range(5, N+1):
        DP[i] = max(DP[i - 2] + stairs[i - 1], DP[i - 3] + stairs[i - 1] + stairs[i - 2])
        # else:
        #     DP[i] = max(DP[i-2]+stairs[i-1], DP[i-4]+stairs[i-2]+stairs[i-3], DP[i-3]+stairs[i-1]+stairs[i-2])
    print(DP[N])