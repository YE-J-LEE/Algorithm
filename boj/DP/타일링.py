import sys

# BOJ 1793
# 타일링 문제로, 그림을 그려 풀면 쉬운 DP 문제이다.
# 다만 n = 0 일 때 아무것도 채울 수 없는 방법 역시 1가지 경우의 수로 보는 것 때문에
# 틀렸었다. 하지만 0! = 1이라는 식으로 이해할 수 있게 된 문제였다.

DP = [0]*251
DP[0] = 1
DP[1] = 1
DP[2] = 3
for i in range(3, 251):
    DP[i] = DP[i-1] + DP[i-2]*2
while True:
    try:
        n = int(sys.stdin.readline())
        print(DP[n])
    except:
        break
