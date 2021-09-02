import sys

# 이 문제는 백트래킹의 힘을 체험할 수 있는 문제다.
# 우선 11개의 줄에서 각각 하나씩 뽑는데, 각 줄에서 최대 5개씩 유효능력치가 존재해 총 5^11 개의 가짓수가 존재한다.
# 계산해보았을 때 대략 4000만정도가 된다. 또한 여러 개의 테스트케이스가 존재한다고 문제에서 제시했기에, 최소 테스트 케이스가 10개라고 하면
# 총 4억번의 연산 횟수로 인해 이것은 C++로도 해결 못 할 문제가 되어버린다.
# 그래서 DP로 생각해 봤지만 반복되는 매커니즘에서 점화식을 구현할 수 없어서
# 백트래킹을 시도해 함수 호출 횟수, 그리고 최댓값을 찾기 위한 비교 횟수가 얼마나 되는지 체크해봤다.
# 그 결과, 함수 호출은 총 6930번 이루어졌고 최댓값 비교 횟수는 1824에 그쳤다.
# 브루트포스적으로 생각했을때 4000만 정도의 연산에서 6930번까지 줄어들어서 자신있게 백트래킹 풀이로 제출했고 성공할 수 있었다.

def backTracking(i, result):
    global answer
    if i == 11:
        answer = max(answer, result)
    for j in range(11):
        if not visited[j] and matrix[i][j] != 0:
            visited[j] = True
            backTracking(i+1, result + matrix[i][j])
            visited[j] = False

C = int(sys.stdin.readline())
for _ in range(C):
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(11)]
    visited = [False]*11
    answer = 0
    backTracking(0, 0)
    print(answer)