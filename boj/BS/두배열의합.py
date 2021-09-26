import sys

# BOJ 2143
# 이 문제는 배열이 총 2개 있으며 각각의 배열에서의 부분합끼리의 합이 원하는 T값이 되는 경우의 수를 반환하는 문제였다.
# 처음엔 부분합이면서 또 연속적인 원소들의 합이므로 누적합으로 구할 수 있어 너무 쉬운게 아닌가 싶어서 DP로 풀어야 하는
# 범위인가 싶어 찾아봤더니 T의 값 범위가 음양 max로 +-10^9였다.
# 이는 메모이제이션을 위한 배열 생성 자체가 불가능하기에.. 우선 두 배열 각각 누적합을 구해주고
# 나올 수 있는 수들에 대해서 딕셔너리를 통해 각 수가 몇개씩 존재하는지 저장해뒀다.
# 그리고 한 쪽 배열에서 부분합 값을 가져오고 다른 배열은 정렬을 해둔 뒤에 이분 탐색을 통해 log시간 내에 찾을 수 있도록 하였다.

T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
A = [0] + list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = [0] + list(map(int, sys.stdin.readline().split()))
uniqueA, uniqueB = dict(), dict()
for i in range(1, n+1):
    A[i] += A[i-1]
for i in range(1, m+1):
    B[i] += B[i-1]
for i in range(1, n+1):
    own = A[i] - A[i-1]
    if own in uniqueA:
        uniqueA[own] += 1
    else:
        uniqueA[own] = 1
    for j in range(i+1, n+1):
        subSum = A[j] - A[i-1]
        if subSum in uniqueA:
            uniqueA[subSum] += 1
        else:
            uniqueA[subSum] = 1
for i in range(1, m+1):
    own = B[i] - B[i-1]
    if own in uniqueB:
        uniqueB[own] += 1
    else:
        uniqueB[own] = 1
    for j in range(i+1, m+1):
        subSum = B[j] - B[i-1]
        if subSum in uniqueB:
            uniqueB[subSum] += 1
        else:
            uniqueB[subSum] = 1
pair = sorted(uniqueB.keys())
N = len(pair)
answer = 0
for key in uniqueA.keys():
    target = T - key
    start = 0
    end = N - 1
    while start <= end:
        mid = (start+end)//2
        if pair[mid] > target:
            end = mid - 1
        elif pair[mid] < target:
            start = mid + 1
        else:
            answer += uniqueA[key] * uniqueB[pair[mid]]
            break
print(answer)

