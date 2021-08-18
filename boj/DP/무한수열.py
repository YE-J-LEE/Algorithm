import sys
sys.setrecursionlimit(10**5)

def solve(i):
    global P, Q
    if i in A:
        return A[i]
    A[i] = solve(i//P) + solve(i//Q)
    return A[i]

N, P, Q = map(int, sys.stdin.readline().split())
A = {0: 1}
print(solve(N))