import sys

# BOJ 6987
# 이 문제 처음엔 단순하게 생각해서 무승부의 갯수가 짝지어지는지, 그리고 승패 합이 같은지의 여부 등을 파악해 시도했었다.
# 물론 어딘가 놓친 부분이 있을 것 같다는 생각이 들었지만 당연하게도 틀려버렸다.
# 찾아보니 나올 수 있는 대진표에 맞추어서 각 대진에서의 왼쪽 승, 오른쪽 승, 무승부 여부를 체크했어야 했다.
# 총 15개의 대진이 있을 수 있는데 여기서 승패무 총 3가지씩 경우가 생기므로 3^15일 것이다.
# 그리고 너무 크므로 승패나 무승부를 줄일 수 있는 결과값이 남아있는지 확인해 나올 수 있는 경우들에서 백트래킹 개념으로 적절하게 브레이크를 걸어주면 된다
# 이런 식으로 승이나 패같은 남아있는 갯수를 하나씩 줄이며 백트래킹 하는 문제를 풀어본적이 있지만 출제된 문제의 내용이 달라
# 접근하는 데에 어려움을 겪었다. 이 문제를 통해 시야가 확장된 느낌이었다.

answer = 0

def solve(i, group):
    global N, answer
    if i == N:
        remain = 0
        for row in group:
            remain += sum(row)
        if remain:
            answer = 0
        else:
            answer = 1
        return
    a, b = able[i]
    if group[a][0] > 0 and group[b][2] > 0:
        group[a][0] -= 1
        group[b][2] -= 1
        solve(i+1, group)
        group[a][0] += 1
        group[b][2] += 1
    if group[a][2] > 0 and group[b][0] > 0:
        group[a][2] -= 1
        group[b][0] -= 1
        solve(i+1, group)
        group[a][2] += 1
        group[b][0] += 1
    if group[a][1] > 0 and group[b][1] > 0:
        group[a][1] -= 1
        group[b][1] -= 1
        solve(i+1, group)
        group[a][1] += 1
        group[b][1] += 1

result = []
able = []
for i in range(5):
    for j in range(i+1, 6):
        able.append((i, j))
N = len(able)
for _ in range(4):
    answer = 0
    info = list(map(int, sys.stdin.readline().split()))
    group = []
    for i in range(0, 18, 3):
        group.append(info[i:i+3])
    solve(0, group)
    result.append(answer)

print(*result)