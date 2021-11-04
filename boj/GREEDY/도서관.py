import sys

# BOJ 1461
# 아 역시 그리디 문제 정말 너무 어렵다.
# 처음엔 책 하나를 위해 앞으로 나아간 후 해당 책과 가장 가까운 애들을 하나로 뭉쳐 거리를 덮어쓰는 느낌으로 가려고 했다.
# 거리를 덮어쓰는 전략은 맞았다. 하지만 양수와 음수를 따로 구분해줘야 그것이 그리디하며 동시에 최적화가 된다는 것을 알게 되었다.

N, M = map(int, sys.stdin.readline().split())
books = list(map(int, sys.stdin.readline().split()))
positive, negative = [], []
for book in books:
    if book > 0:
        positive.append(book)
    else:
        negative.append(book)
dist = []
positive.sort(reverse=True)
negative.sort()
for i in range(0, len(positive), M):
    dist.append(positive[i])
for i in range(0, len(negative), M):
    dist.append(-negative[i])
print(sum(dist)*2-max(dist))