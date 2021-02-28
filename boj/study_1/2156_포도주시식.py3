import sys

n = int(sys.stdin.readline())
grape = [0]
DP = [0]*(n+1)
for _ in range(n):
    grape.append(int(sys.stdin.readline()))
if n==1:
    print(grape[1])
elif n==2:
    print(grape[1]+grape[2])
elif n==3:
    print(sum(grape[1:4])-min(grape[1:4]))
elif n==4:
    print(sum(grape[1:5])-min(grape[2:4]))
else:
    DP[1] = grape[1]
    DP[2] = grape[1]+grape[2]
    DP[3] = sum(grape[1:4])-min(grape[1:4])
    DP[4] = sum(grape[1:5])-min(grape[2:4])
    for i in range(5, n+1):
        DP[i] = max(DP[i-4]+grape[i-1]+grape[i-2], DP[i-3]+grape[i-1]+grape[i], DP[i-2] + grape[i])
    print(DP[n])