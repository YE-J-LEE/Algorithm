import sys

# BOJ 2166
# 신발끈 공식 문제이다. 공식만 알면 쉽게 풀 수 있는 문제다.
# 다만 소수 둘째 자리에서 반올림하여 첫째 자리까지만 표기해야 한다는 점.

N = int(sys.stdin.readline())
X = []
Y = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    X.append(x)
    Y.append(y)
X.append(X[0])
Y.append(Y[0])
left, right = 0, 0
for i in range(N):
    left += X[i]*Y[i+1]
    right += Y[i]*X[i+1]
print(round(abs(left-right)/2, 1))



