import sys

n = int(sys.stdin.readline())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, sys.stdin.readline().split())))
for i in range(n):
    for j in range(i+1):
        if i-1 < 0:
            continue

        if j==0:
            triangle[i][j] += triangle[i-1][j]
        elif i==j:
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
print(max(triangle[-1]))