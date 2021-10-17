import sys

# BOJ 11568
# 이 문제는 전형적인 LIS 문제였다.
# 주어진 N의 범위는 최대 1000까지여서 직관적인 풀이인 O(N^2)로 가능해보였고 통과했다.
# 그런데 풀고나서 알고리즘 분류를 보니 LIS(NlogN)이라고 적혀있었다.
# 이럴거면 N 범위를 조금 더 크게 만들었어야 하지 않나 싶었다.

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
LIS = [1]*N
for i in range(N):
    for j in range(i):
        if cards[j] < cards[i] and LIS[i] < LIS[j] + 1:
            LIS[i] = LIS[j] + 1
print(max(LIS))