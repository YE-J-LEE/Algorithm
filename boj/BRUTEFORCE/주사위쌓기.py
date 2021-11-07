import sys

# BOJ 2116
# 전개도가 지정되어 있기 때문에 해싱을 사용해 쉽게 풀 수 있는 문제였다.
# 예전엔 주사위 문제가 나오면 너무 어렵게만 느껴졌지만 이젠 익숙하게 풀어낼 수 있을 것 같다.

N = int(sys.stdin.readline())
dice = []
initDice = list(map(int, sys.stdin.readline().split()))
for _ in range(N-1):
    dice.append(list(map(int, sys.stdin.readline().split())))
answer = 0
opposite = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
around = {0: [1, 2, 3, 4], 1: [0, 2, 4, 5], 2: [0, 1, 3, 5], 3: [0, 2, 4, 5]
          , 4: [0, 1, 3, 5], 5: [1, 2, 3, 4]}
for i in range(6):
    for j in around[i]:
        sub = initDice[i]
        down = initDice[j]
        for D in dice:
            maxVal = 0
            idx = -1
            for k in range(6):
                if D[k] == down:
                    idx = k
                    break
            for p in around[idx]:
                maxVal = max(maxVal, D[p])
            sub += maxVal
            down = D[opposite[idx]]
        answer = max(answer, sub)
print(answer)