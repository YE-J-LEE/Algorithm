import sys

# 오랜만에 만나는 슬라이딩 윈도우 문제
# 개인적으로 난이도 범위가 다양하게 난무하는 투포인터보다는 쉽게 풀 수 있어서 좋다.
N, d, k, c = map(int, sys.stdin.readline().split())
sushi = [int(sys.stdin.readline()) for _ in range(N)]
for i in range(k-1):
    sushi.append(sushi[i])
sortOfFish = {}
answer = 0
for i in range(k):
    if sushi[i] in sortOfFish:
        sortOfFish[sushi[i]] += 1
    else:
        sortOfFish[sushi[i]] = 1
if c in sortOfFish:
    answer = len(sortOfFish.keys())
else:
    answer = len(sortOfFish.keys()) + 1
# 0 1 2 3
# 0 1 2
for i in range(1, N):
    oldFish = sushi[i-1]
    sortOfFish[oldFish] -= 1
    if sortOfFish[oldFish] == 0:
        del sortOfFish[oldFish]
    newFish = sushi[i+k-1]
    if newFish in sortOfFish:
        sortOfFish[newFish] += 1
    else:
        sortOfFish[newFish] = 1
    if c in sortOfFish:
        answer = max(answer, len(sortOfFish.keys()))
    else:
        answer = max(answer, len(sortOfFish.keys())+1)
print(answer)