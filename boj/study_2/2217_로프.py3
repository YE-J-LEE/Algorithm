import sys

N = int(sys.stdin.readline())
rope = []
for _ in range(N):
    rope.append(int(sys.stdin.readline()))
rope.sort()
maxWeight = rope[-1]
for i in range(N-1):
    w = rope[i]*(N-i)
    maxWeight = w if w >= maxWeight else maxWeight
print(maxWeight)