import sys

# BOJ 17299
# 이 문제는 밑 레벨에도 자주 등장했던, O(N) 시간 정도에 비교를 할 수 있는 스택을 활용한 문제이다.
# 기억을 더듬어가며 쉽게 풀 수 있었다.

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
FA = []
numCnt = {}
for num in A:
    if num in numCnt:
        numCnt[num] += 1
    else:
        numCnt[num] = 1
FA = [numCnt[num] for num in A]
answer = [-1]*N
stack = []
for i in range(N):
    while stack and stack[-1][0] < FA[i]:
        _, idx = stack.pop()
        answer[idx] = A[i]
    stack.append((FA[i], i))
print(*answer)


