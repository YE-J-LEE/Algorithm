import sys

# BOJ 15989
# 전형적인 숫자 맞추기 DP 문제이다
# 특이하게 1+1+2 1+2+1의 경우 모두 한 가지로 치기에
# 숫자들을 써놓고 겹치는 부분에 대한 처리를 따로 할 수 있도록 해야 한다.

T = int(sys.stdin.readline())
DP = [[0]*4 for _ in range(10001)]
for i in range(1, 4):
    for j in range(1, i+1):
        DP[i][j] = 1

for i in range(4, 10001):
    for j in range(1, 4):
        DP[i][j] += sum(DP[i-j][:j+1])

for _ in range(T):
    n = int(sys.stdin.readline())
    print(sum(DP[n]))
