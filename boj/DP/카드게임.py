import sys
sys.setrecursionlimit(10**5)

# BOJ 11062
# 이 문제는 상당히 고전했다.
# DP로 풀어야 되는건 느낌이 왔지만 점화식 구상이 너무 어려웠다.
# 근우와 명우 둘 다 최선의 픽을 하기 때문에 처음엔 현재 자신이 가장 많은 점수를 얻을 수 있는 방향으로 구상했었다.
# 하지만 계속 자신의 입장만 고려하기에, 현재가 i인 경우와 i+2인 경우를 생각하면 i+2일때 카드가 얼마나 남았는지를 알 수가 없어서
# 점화식이 성립이 안 됐다. 그래서 다른 사람의 접근 방법을 찾아보니 명우의 입장에선 상대방인 근우가 가장 적게 점수를 획득하는 방향으로
# 카드를 픽하면 된다는 사실을 깨닫게 되었다. 정말 신선한 접근법이었고 알고리즘 분류에 있던 게임이론,
# 이러한 접근 방식도 게임 이론에 포함된 듯 하다.
# 다음번에 비슷한 부류의 문제가 나오면, 구하고자 하는 값에선 최고의 점수를 얻기 위한 방향, 그리고 다른 한 쪽은 상대방이 최저의 점수를 얻기 위한
# 방향으로 픽하게 하여, i와 i+1만으로 점화식을 구현할 수 있도록 해야 겠다.

def solve(i, start, end):
    global N
    if i > N-1:
        return 0
    if DP[start][end] != -1:
        return DP[start][end]
    if i%2 == 0:
        DP[start][end] = max(cards[start] + solve(i+1, start+1, end), cards[end] + solve(i+1, start, end-1))
    else:
        DP[start][end] = min(solve(i+1, start+1, end), solve(i+1, start, end-1))
    return DP[start][end]

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    cards = list(map(int, sys.stdin.readline().split()))
    DP = [[-1]*N for _ in range(N)]
    print(solve(0, 0, N-1))
