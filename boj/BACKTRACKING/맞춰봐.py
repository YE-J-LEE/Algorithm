import sys

# BOJ 1248
# 백트래킹 문제다. 그런데 내가 싫어하는 diagonal 방식이 가미되었다. 물론 그리 복잡하게 for문을 설계할 정도까진 아니었지만..
# 아마도 부분합을 계속해서 O(N)방식으로 더해서 시간이 더 걸린 것 같다만 통과하였다.

def solve(diagonal, arr):
    global N
    if diagonal == N:
        print(*arr)
        sys.exit()
    for num in range(-10, 11):
        for i in range(diagonal+1):
            j = diagonal-i
            result = sum(arr[i:i+j]) + num if diagonal != 0 else num
            subOp = ''
            if result > 0:
                subOp = '+'
            elif result < 0:
                subOp = '-'
            else:
                subOp = '0'
            if subOp != S[i][j]:
                break
        else:
            solve(diagonal+1, arr + [num])
N = int(sys.stdin.readline())
op = sys.stdin.readline().rstrip()
S = []
start, end = 0, N
for _ in range(N):
    S.append(list(op[start:end]))
    sub = end - start
    start = end
    end = start + sub - 1
solve(0, [])