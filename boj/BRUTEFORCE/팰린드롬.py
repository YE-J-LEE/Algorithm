import sys

# 이 문제는 출력해야하는 테스트케이스들에 맞추어서 그때그때마다 계산해서 출력할 경우 복잡도가 터져버린다.
# 테스트케이스가 100만개이고 수열의 크기는 2000이기에 최악의 경우 2000 * 100만이 되어버리기 때문이다.
# 따라서 테스트케이스들에 대하여 O(1)로 이미 그 테스트케이스들에 대한 정답들을 모두 사전에 알고 있어야 한다는 소리다.
# 그리고 수열의 크기 N의 최댓값은 2000이기에 충분히 O(N^2)짜리의 연산을 통해 답을 미리 구해놓을 수 있다.
# 그래서 수열 내 각각의 원소에 대해 발산하는 형식으로 팰린드롬을 찾아주었다. 그리고 발산하는 도중 양쪽값이 달라지면
# 그 이후로 뻗어나가도 팰린드롬일 수 없기 때문에 이때 브레이크를 걸어주었다.
# 결국 완전탐색 느낌으로 문제를 해결할 수 있었다.

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
palindrome = [['0']*N for _ in range(N)]
M = int(sys.stdin.readline())
for i in range(N):
    left, right = i, i
    while left >= 0 and right < N:
        if A[left] == A[right]:
            palindrome[left][right] = '1'
            left -= 1
            right += 1
        else:
            break
for i in range(N-1):
    left, right = i, i+1
    while left >= 0 and right < N:
        if A[left] == A[right]:
            palindrome[left][right] = '1'
            left -= 1
            right += 1
        else:
            break
for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    sys.stdout.write(palindrome[S-1][E-1] + '\n')
