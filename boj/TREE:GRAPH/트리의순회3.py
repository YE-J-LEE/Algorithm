import sys
sys.setrecursionlimit(10**5)

# 효율적이지 못한 코드다.
# 최대한 시간을 줄이기 위해 노력했는데 현재 나의 레벨에서 이 수준이 최선이었다.
# 트리의 순회에 대해서 더 깊이있게 공부해야할듯 싶다.

def solve(inS, inE, postS, postE):
    if inS > inE or postS > postE:
        return
    root = postorder[postE]
    answer.append(root)
    # 0 1 2 3 4 5
    rootIdx = -1
    for i in range(inS, inE+1):
        if inorder[i] == root:
            rootIdx = i
            break
    if rootIdx == -1:
        return
    left = rootIdx-inS
    right = inE-rootIdx
    solve(inS, inS + left-1, postS, postS + left-1)
    solve(rootIdx+1, rootIdx + right, postS + left, postS + left + right - 1)

n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))
answer = []
solve(0, n-1, 0, n-1)
print(*answer)