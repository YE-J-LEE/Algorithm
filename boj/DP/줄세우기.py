import sys

# BOJ 7570
# 2631번 줄세우기 문제와 비교해봐야한다. 저 문제는 심지어 LIS 잘 파악해서 맞았었다.
# 근데 이번 문제는 최근에 푼 문제들에 영향을 받아서 현재 인덱스와 정렬 후이 인덱스 차를 가지고 너무 많이 고민했다.
# 왜냐하면 서로간 비정렬 상태가 상대적이고 위의 방식으로 규칙을 찾기가 너무 어려웠다.
# 그리고 LIS로 풀리지 않을 것 같다고 무심코 생각해 지나쳐버렸다.
# 하지만 LIS로 접근했어도 틀렸을 것 같긴 하다. 왜냐하면 이번 LIS는 +1 씩 늘어나야한 길이가 늘어나는 형태였기 때문이다.

N = int(sys.stdin.readline())
children = list(map(int, sys.stdin.readline().split()))
DP = [0]*(N+1)
for child in children:
    DP[child] = DP[child-1] + 1
print(N-max(DP))