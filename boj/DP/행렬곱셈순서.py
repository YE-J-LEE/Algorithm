import sys

# 우선... 저번 파일합치기 문제에서도 보았던 연쇄행렬 DP 문제이다.
# 정확한 시간복잡도는 (n-1)*n*(n+1)/6이라고 하는데.. 문제에서 N=500인 경우 2000만을 좀 넘기는 값이 나온다
# 제한 시간이 1초, 그리고 내가 아는 한 Python으로는 1초에 대략 2000만의 연산이 가능한 걸로 알고 있다.
# 물론 저번에 knuth 최적화를 시도해보겠다고 했지만.. 증명과정을 보고 접목하려니., 아직 나의 레벨이 아닌 것 같은 느낌이었다.
# 그래서 Pypy로는 통과했지만 Python으로 제출했지만 시간초과가 났다.
# 조금 더 레벨을 키워서.. 언젠가 꼭 knuth 최적화를 적용시켜보이겠다.

N = int(sys.stdin.readline())
matrix = [[-1, -1]]
for _ in range(N):
    r, c = map(int, sys.stdin.readline().split())
    matrix.append([r, c])
DP = [[0]*(N+1) for _ in range(N+1)]
# 14 => 11 24 / 12 34 / 13 44
for diagonal in range(N):
    for i in range(1, N-diagonal+1):
        j = i + diagonal
        if i == j:
            continue
        DP[i][j] = 1e9
        for k in range(i, j):
            DP[i][j] = min(DP[i][j], DP[i][k] + DP[k+1][j] + matrix[i][0]*matrix[k][1]*matrix[j][1])
print(DP[1][N])