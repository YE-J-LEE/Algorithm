import sys
sys.setrecursionlimit(10**6)

# BOJ 2342
# 이 문제는 현재의 발 위치를 이동할때 미래에 합산된 값이 최소가 되게끔 이동하는 DP 문제이다.
# 이런 경우 나는 보통 재귀를 통해 구현한다.
# 다행스럽게도 N의 범위가 최대 10만이어서 재귀 제한을 넉넉하게 10^6정도로 걸어주고 풀어냈다.

def solve(i, left, right):
    if command[i] == 0:
        return 0
    if DP[i][left][right] != -1:
        return DP[i][left][right]
    if left == 0 and right == 0:
        DP[i][left][right] = min(solve(i+1, command[i], right), solve(i+1, left, command[i])) + 2
    elif right == command[i] or left == command[i]:
        DP[i][left][right] = solve(i+1, left, right) + 1
    elif left == 0:
        DP[i][left][right] = min(solve(i + 1, command[i], right) + 2,
                                 solve(i + 1, left, command[i]) + 4 if abs(right - command[i]) == 2 else solve(i + 1, left, command[i]) + 3)
    elif right == 0:
        DP[i][left][right] = min(solve(i + 1, left, command[i]) + 2,
                                 solve(i + 1, command[i], right) + 4 if abs(left - command[i]) == 2 else solve(i + 1, command[i], right) + 3)
    else:
        DP[i][left][right] = min(solve(i + 1, command[i], right) + 4 if abs(left - command[i]) == 2 else solve(i + 1, command[i], right) + 3,
                                 solve(i + 1, left, command[i]) + 4 if abs(right - command[i]) == 2 else solve(i + 1, left, command[i]) + 3)
    return DP[i][left][right]

command = list(map(int, sys.stdin.readline().split()))
N = len(command)
DP = [[[-1]*5 for _ in range(5)] for _ in range(N)]
print(solve(0, 0, 0))
