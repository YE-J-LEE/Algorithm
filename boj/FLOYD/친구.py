import sys

# BOJ 1058
# 플로이드와샬로 풀어야 겠다는 생각은 했고 거쳐가는 친구가 단 한 명이어야 하는 경우가 존재했어야 했다.
# 처음엔 플로이드 식 자체만 봐서 직관적으로 아 저려면 한 명 통해 가는 건 전부 걸리겠군! 했다가 틀렸다.
# 하지만 잘 분석해서 보면 floyd[i][k] + floyd[k][j]에서의 i,k k,j가 직통으로 가는 경우가 아닌
# 여러 경우의 합산이며 길이 합이자 연결 수이다. 따라서 해당 값이 2 이하여야 답을 색출할 수 있다.

N = int(sys.stdin.readline())
floyd = []
for _ in range(N):
    row = []
    for c in sys.stdin.readline().rstrip():
        if c == 'Y':
            row.append(1)
        else:
            row.append(float('inf'))
    floyd.append(row)
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[k][j])
answer = 0
for row in floyd:
    result = 0
    for cnt in row:
        if 0 < cnt < 3:
            result += 1
    answer = max(answer, result)
print(answer)
