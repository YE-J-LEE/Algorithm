import sys

# BOJ 2624
# 굉장히 어려웠다. 비슷한 문제를 푼 적이 있었는데 이 문제는 조금 새롭게 접근해야 했다.
# 중복을 고려해서 뒤에서부터 내려오며 값을 갱신하는 것이 생각하기 어려웠던 문제다.

T = int(sys.stdin.readline())
k = int(sys.stdin.readline())
coins = []
for _ in range(k):
    p, n = map(int, sys.stdin.readline().split())
    coins.append((p, n))

DP = [0]*(T+1)
DP[0] = 1

for i in range(k):
    val, total = coins[i]
    for j in range(T, -1, -1):
        for cnt in range(1, total+1):
            if j - cnt*val < 0:
                break
            DP[j] += DP[j - cnt*val]
print(DP[T])


