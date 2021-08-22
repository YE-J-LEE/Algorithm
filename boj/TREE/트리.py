import sys

# 관찰과 분할정복
def solve(preorder, inorder):
    global rootIdx
    if not inorder:
        return []
    currentRoot = preorder[rootIdx]
    standard = inorder.index(currentRoot)
    rootIdx += 1
    answer = solve(preorder, inorder[:standard])
    answer += solve(preorder, inorder[standard+1:])
    answer.append(currentRoot)
    return answer

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    preorder = list(map(int, sys.stdin.readline().split()))
    inorder = list(map(int, sys.stdin.readline().split()))
    rootIdx = 0
    print(*solve(preorder, inorder))
