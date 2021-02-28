import sys
N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
start = 1
last = max(tree)

answer = 0

while start<=last:
    mid = (start+last)//2
    R = sum(filter(lambda x: x > 0,map(lambda y: y-mid, tree)))
    if R >= M:
        answer = mid
        start = mid+1
    else:
        last = mid-1
print(answer)