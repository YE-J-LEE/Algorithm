import sys

# BOJ 2841
# 문제에서 손가락의 최소한의 움직임이라고 하는데..
# 사실 문제에서 최소한으로 움직이도록 하는 규칙을 알려줬다. 그래서 오히려 무슨 말인지 알아듣기 힘들었다.

N, P = map(int, sys.stdin.readline().split())
answer = 0
guitar = [[] for _ in range(7)]
for _ in range(N):
    n, p = map(int, sys.stdin.readline().split())
    if guitar[n]:
        if p > guitar[n][-1]:
            guitar[n].append(p)
            answer += 1
        elif p < guitar[n][-1]:
            while guitar[n] and p < guitar[n][-1]:
                answer += 1
                guitar[n].pop()
            if guitar[n]:
                if guitar[n][-1] != p:
                    guitar[n].append(p)
                    answer += 1
            else:
                guitar[n].append(p)
                answer += 1
    else:
        guitar[n].append(p)
        answer += 1
print(answer)














