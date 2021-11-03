import sys

# BOJ 15657
# 내장 함수 함부로 쓰려다가 시간초과가 났다..
# 문제를 통한 재귀 백트래킹 구상을 조금 더 신중하게 고민해볼 필요가 있어 보인다.. 자꾸 놓친다..

def solve(i, j):
    global N, M
    if i == M:
        print(*result)
        return
    for k in range(j, N):
        result.append(numbers[k])
        solve(i+1, k)
        result.pop()

N, M = map(int, sys.stdin.readline().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))
result = []
solve(0, 0)


