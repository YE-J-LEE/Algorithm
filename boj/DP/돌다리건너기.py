import sys

command = sys.stdin.readline().rstrip()
devil = list(sys.stdin.readline().rstrip())
angel = list(sys.stdin.readline().rstrip())
N = len(command)
M = len(devil)
DP = [[[0]*2 for _ in range(N)] for _ in range(M)]

# 뒤로 갈수록 결과를 모두 합산하려고 하면 복잡해지는 문제
for i in range(M):
    for j in range(N):
        if devil[i] == command[j]:
            if j == 0:
                DP[i][j][0] = 1
            else:
                for k in range(i):
                    DP[i][j][0] += DP[k][j-1][1]
        if angel[i] == command[j]:
            if j == 0:
                DP[i][j][1] = 1
            else:
                for k in range(i):
                    DP[i][j][1] += DP[k][j-1][0]
answer = 0

# 마지막에 이렇게 0~M 결과값을 세줘도 늦지않고 간편하다
for i in range(M):
    answer += DP[i][N-1][0] + DP[i][N-1][1]
print(answer)
