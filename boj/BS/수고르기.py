import sys

# 보자마자 바로 풀이가 생각나지 않아 고민하던중
# N의 범위를 통해 유추했고 바로 O(N*logN)으로 배열 원소당 하나씩 짝을 찾아주기 위해 이분탐색을 더했다
# 알고리즘 분류를 살펴보니 투포인터 내용이 나왔다. 저번에도 비슷하게 이분탐색으로 푼 무제가 투포인터로 분류된 것을 봤는데
# 이분탐색과 투포인터의 상관관계에 대해 따로 공부를 해봐야겠다.
# 이 문제의 경우 첫 시도는 틀렸는데, 그 이유는 answer변수를 처음에 1e9로 선언했다가 범위를 잘 살펴보니 이보다 더 큰 수가
# 나올수 있단 걸 알았고 바로 실제 무한대를 나타내는 float('inf')로 바꾸었다.

def solve():
    global N, M
    answer = float('inf')
    if M == 0:
        return 0
    for i in range(N-1):
        found = -1
        start = i
        end = N-1
        while start <= end:
            mid = (start+end)//2
            diff = A[mid]-A[i]
            if diff == M:
                return M
            elif diff > M:
                found = diff
                end = mid - 1
            else:
                start = mid + 1
        if found != -1:
            answer = min(answer, found)
    return answer

N, M = map(int, sys.stdin.readline().split())
A = [int(sys.stdin.readline()) for _ in range(N)]
A.sort()
print(solve())