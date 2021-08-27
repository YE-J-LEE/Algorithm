# 이 문제는 너무 아름다운 문제다.
# 가끔 파이썬으로 PS풀이를 하면서 느끼는건데, 워낙에나 느린 언어라 항상 최적의 풀이를 찾을 수 있도록 오히려 도움이 된다.
# 이 문제같은 경우 나름의 팰린드롬 규칙을 이용해 O(N^2) 시간 정도로 풀어내려 했지만 끼워 넣는 수들이 아무 곳에나 넣을 수 있기에
# 하드 코딩을 진행했던 나의 풀이는 막혔었다.
# 그래서 힌트를 보았더니 알고리즘 분류가 DP였고, N <= 5000이기에 대략 N^2으로 푸는 것은 들어맞았고 늘상 생각하던 대로
# 앞에서부터 하나씩 늘리며 이전의 최적해로 현재의 최적해를 찾아낼 수 있는가를 따졌지만 점점 더 미로 속으로 빠져들어갔다.
# 재귀로 눈을 돌렸지만 역시 보이지 않았고 다른 이들의 풀이를 찾아보게 되었다.
# 대부분의 풀이는 C++로 진행된 코드들이었다. 제일 먼저 찾은 방식이 재귀 형식이었고 팰린드롬의 성질을 통해 양쪽에서 가운데로 수렴하는 형태의
# 재귀 풀이였다. 보자마자 바로 아차 싶었고 그대로 파이썬으로 풀어냈다.
# 하지만 메모리 초과가 났다. 128MB의 빠듯한 메모리였고 5000*5000자리의 DP배열이 있다지만 재귀를 통해 함수 스택 메모리가 추가적으로
# 잡아먹어서 메모리 초과가 나는 것 같았다. 실제 파이썬 재귀 제한을 10**8까지 올려도 최악의 경우인 N = 5000일때 돌아가지 않았다.
# 따라서 파이썬으로는 수렴형 재귀 DP로 풀지 못 한다는 결론을 내렸고, 그럼에도 불구하고 파이썬으로 푼 사람들이 있기에 다른 풀이를 찾게 되었다.
# 그게 바로 두 번째 풀이인 LCS 풀이이다.
# 보고 경악을 금치 못했다. 팰린드롬과 LCS가 이러한 관계였다니 충격이었다.
# 그리고 이내 새로운 지식을 얻었다는 사실에 기뻤고, 바로 LCS를 통해 구현했다.
# 하지만 시간초과. 파이썬의 경우 대략 1초당 2000만의 복잡도를 해결한다는 가정하에 코딩을 하는데,
# 문제에서 2초를 주었고, 5000*5000짜리 배열 만드는 데에 2500만, 그리고 그 DP에 값을 채우는 데에 2500만 총 5000만 복잡도라
# 시간초과가 난 것 같다. 사실 C++ 입장에선 1초에 대략 1억 정도가 수행 가능하기에 무심코 지나쳤을 사실이다.
# 하지만 정말 크리티컬하지 않고 그나마 일반적인 풀이로 접근한다는 면에서 이 LCS 풀이가 현재 나의 실력으로 최적인 풀이라고 생각했고
# PyPy로 제출해 맞았다.

# 수렴형 재귀 풀이
# import sys
# sys.setrecursionlimit(10**8)
#
# def solve(left, right):
#     if left > right:
#         return 0
#     if DP[left][right] != -1:
#         return DP[left][right]
#     if A[left] == A[right]:
#         DP[left][right] = solve(left+1, right-1)
#         return DP[left][right]
#     else:
#         DP[left][right] = min(solve(left+1, right)+1, solve(left, right-1)+1)
#         return DP[left][right]
#
# N = int(sys.stdin.readline())
# A = list(map(int, sys.stdin.readline().split()))
# DP = {x: {} for x in range(N)}
# for i in range(N):
#     for j in range(i, N):
#         DP[i][j] = -1
# print(solve(0, N-1))

# LCS 풀이
import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
DP = [[0]*(N+1) for _ in range(N+1)]
paddedA = [0] + A
reversedA = [0]
while A:
    reversedA.append(A.pop())
for i in range(1, N+1):
    for j in range(1, N+1):
        if reversedA[i] != paddedA[j]:
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])
        else:
            DP[i][j] = DP[i-1][j-1]+1
print(N-DP[N][N])