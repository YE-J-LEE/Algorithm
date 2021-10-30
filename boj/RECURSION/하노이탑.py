import sys

# BOJ 1914
# 하노이탑.. 유명한 재귀 문제라는데 나는 왜 처음 접하는가... N이 충분히 낮은 경우에 한하여 시간복잡도가 O(2^N)인 재귀 알고리즘으로
# 구현될 수 있으며 함수 호출 횟수 자체가 정답에 카운트되는 방식이라 결국엔 등비수열의 합이다.
# 값은 DP로도 구할 수 있다. 장대 3개의 상태를 계속 저장해줘야 하나 싶어 쉽사리 해결 방안이 떠오르지 않았던 문제였다.

def solve(n, src, mid, dst):
    if n == 1:
        sys.stdout.write(str(src) + ' ' + str(dst) + '\n')
        return
    solve(n-1, src, dst, mid)
    sys.stdout.write(str(src) + ' ' + str(dst) + '\n')
    solve(n-1, mid, src, dst)

N = int(sys.stdin.readline())
print(2**N-1)
if N <= 20:
    solve(N, 1, 2, 3)









