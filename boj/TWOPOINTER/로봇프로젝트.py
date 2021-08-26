import sys

# 백준의 두용액이라는 문제와 거의 비슷한 투포인터 문제이다.
# 투포인터중 단 두 가지만 선택해야하는 조건으로 고정되어있고 그 합 역시 고정되어있는 경우
# 양쪽에서 가운데로 수렴하며 O(N)의 시간 내에 해결할 수 있다.

while True:
    try:
        x = int(sys.stdin.readline())*10000000
        n = int(sys.stdin.readline())
        lego = [int(sys.stdin.readline()) for _ in range(n)]
        lego.sort()
        left = 0
        right = n-1
        done = []
        while left < right:
            L = lego[left] + lego[right]
            if L == x:
                done.append(lego[left])
                done.append(lego[right])
                break
            elif L > x:
                right -= 1
            else:
                left += 1
        if done:
            print("yes {} {}".format(done[0], done[1]))
        else:
            print("danger")
    except:
        break