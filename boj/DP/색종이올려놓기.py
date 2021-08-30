import sys
sys.setrecursionlimit(10**6)

# 이 문제는 0-1 knapsack과 유사하게 종이들을 넓이 순으로 정렬 후 해당 시점에서 색종이를 선택할 떄와 안 할 떄의
# 최종 종이갯수를 비교하며 만들어나가면 된다.
# 이때 선택하건 안하건 그 이후들의 가로 세로 길이에 해당하는 결과값들은 DP 메모이제이션 해놓음으로써 값을 재사용할 수 있다.
# 그런데 이보다 더 빠른 풀이들이 보여 다른 사람들의 풀이를 검색해보았다
# 뭔가 처음 문제를 봤을때 맡았던 LIS로의 풀이가 존재했다!
# 나는 냄새는 맡았지만 정렬과 이후 비교 기준을 떠올리지 못해 재귀로 풀었지만
# 다른 사람의 풀이 해설을 보고 한 수 배우게 되었다.

def solve(row, col, i):
    global N
    if i == N:
        return 0
    r, c = paper[i]
    if DP[row][col] != -1:
        return DP[row][col]
    DP[col][row] = solve(row, col, i+1)
    if (row >= r and col >= c) or (row >= c and col >= r):
        DP[col][row] = max(solve(r, c, i+1)+1, DP[col][row])
    DP[row][col] = DP[col][row]
    return DP[row][col]

N = int(sys.stdin.readline())
paper = []
for _ in range(N):
    r, c = map(int, sys.stdin.readline().split())
    paper.append((r, c))
paper.sort(key=lambda x: -x[0]*x[1])
DP = [[-1]*1001 for _ in range(1001)]
print(solve(1000, 1000, 0))