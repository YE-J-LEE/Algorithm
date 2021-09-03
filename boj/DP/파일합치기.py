import sys

# 이 문제는 단 하나의 조건인 소설을 '연속적'으로 합한다에서 연쇄행렬곱셉을 DP로 풀어내는 문제와 같아졌다고 봐도 된다.
# 연쇄행렬곱을 DP로 풀어낼 때에는 행렬의 i 부터 j 사이 어딘가 k를 두고
# 왼쪽과 오른쪽 연산횟수를 이용해 diagonal식으로 DP행렬을 채워나가는 방식인데, diagonal이 안하다보면 어떻게 구현해야하는지
# 까먹게 된다. 그래서 이 문제를 해결할 때 diagonal DP 코드를 참고해가며 풀어냈다...
# 그런데 문제에서의 여러 테스트케이스의 갯수인 T가 존재하기에... Python으로 제출했더니 시간초과가 났다..
# 딱 하나 K=500일때만 보면 O(K^3)으로 125000000여서 시간초과가 난 것 같다..
# Pypy로 어찌저찌 통과는 했지만 Python으로도 푼 사람이 있어서 코드를 보니 변수명에 knuth라는 의미심장한 단어가 있었다.
# 바로 구글링을 통해 크누스 최적화라는 개념에 대해 알게 되었고, 이 개념을 공부한 뒤에 다음 공부시간에 있을 연쇄행렬곱에
# 이 크누스 최적화 개념을 가미해 O(K^2)으로 만드는 시도를 해볼 것이다.

T = int(sys.stdin.readline())
for _ in range(T):
    K = int(sys.stdin.readline())
    fictions = [0] + list(map(int, sys.stdin.readline().split()))
    for i in range(1, K+1):
        fictions[i] += fictions[i-1]
    DP = [[0]*(K+1) for _ in range(K+1)]
    for diagonal in range(K):
        for i in range(1, K-diagonal+1):
            j = i + diagonal
            if i == j:
                continue
            DP[i][j] = 1e9
            for k in range(i, j):
                DP[i][j] = min(DP[i][j], DP[i][k] + DP[k+1][j] + fictions[j]-fictions[i-1])
    print(DP[1][K])

