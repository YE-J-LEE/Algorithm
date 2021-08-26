import sys

# 알고리즘 문제들만 풀다 보니 문제에서 LIS 혹은 Stack 냄새가 나 구현 방식을 구상하고 있었다.
# 하지만 이내 '선분'이라는 단어의 언급과 과연 빌딩 사이 각도가 얼마나 되어야지 '보일'지 생각을 해보니
# 수학문제라는 것을 깨닫게 되었고 바로 함수식을 통해 구현하였다.

N = int(sys.stdin.readline())
buildings = list(map(int, sys.stdin.readline().split()))
# (x1, y1), (x2, y2)  y = ax + b
# a = (y2-y1)/(x2-x1)
# b = y1 - a*x1
answer = 0
for i in range(N):
    x1, y1 = i, buildings[i]
    result = 0
    for left in range(0, i):
        if left == i-1:
            result += 1
            continue
        x2, y2 = left, buildings[left]
        a = (y2-y1)/(x2-x1)
        b = y1 - a*x1
        for mid in range(left+1, i):
            if a*mid + b <= buildings[mid]:
                break
        else:
            result += 1
    for right in range(i+1, N):
        if right == i+1:
            result += 1
            continue
        x2, y2 = right, buildings[right]
        a = (y2-y1)/(x2-x1)
        b = y1 - a*x1
        for mid in range(i+1, right):
            if a*mid + b <= buildings[mid]:
                break
        else:
            result += 1
    answer = max(answer, result)
print(answer)