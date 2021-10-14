from math import gcd

# 프로그래머스 위클리 챌린지 10주차
# 요즘 코딩테스트에 ide사용이 불가능한 상태로 프로그래머스상으로만 해결해야하는 경우가 종종 있어서 프로그래머스로 풀어봤다
# 확실히 에러가 발생했을 경우 어느 라인에서 발생하는지 확인하기 어려웠다..
# 이 문제의 경우는 각 직선별로 정수로 집을 수 있는 교점만을 선별해야 하는 브루트포스느낌의 문제였다.
# 하지만 문제를 끝까지 읽지 않는 나란 사람은... x축과 y축이 서로 평행하거나 두 직선이 서로 평행한 경우에 대해서
# 0 division 방지를 위해 하드코딩해버렸다... 문제를 틀리고 나서 다시 보니 두 직선이 서로 평행한 케이스를 놓쳐서 런타임 에러가 났었다.
# 그리고 교점 구하는 판별식도 힌트로 주어진 상태였고.. 역시 문제를 끝까지 읽자..

def cross(a1, b1, c1, a2, b2, c2):
    if a1*b2 - b1*a2 == 0:
        return False, -1, -1
    if a1 == 0 and a2 == 0:
        return False, -1, -1
    elif a1 == 0:
        if -c1 % b1 != 0:
            return False, -1, -1
        y = -c1 // b1
        B = -c2 - b2 * y
        if B % a2 != 0:
            return False, -1, -1
        return True, B // a2, y
    elif a2 == 0:
        if -c2 % b2 != 0:
            return False, -1, -1
        y = -c2 // b2
        B = -c1 - b1 * y
        if B % a1 != 0:
            return False, -1, -1
        return True, B // a1, y
    if b1 == 0 and b2 == 0:
        return False, -1, -1
    elif b1 == 0:
        if -c1%a1 != 0:
            return False, -1, -1
        x = -c1//a1
        B = -a2*x-c2
        if B%b2 != 0:
            return False, -1, -1
        return True, x, B//b2
    elif b2 == 0:
        if -c2%a2 != 0:
            return False, -1, -1
        x = -c2//a2
        B = -a1*x-c1
        if B%b1 != 0:
            return False, -1, -1
        return True, x, B//b1

    pa1, pa2 = abs(a1), abs(a2)
    lcm = pa1 * pa2 // gcd(pa1, pa2)
    mul1 = lcm // pa1
    mul2 = lcm // pa2
    a1, b1, c1 = a1 * mul1, b1 * mul1, c1 * mul1
    a2, b2, c2 = a2 * mul2, b2 * mul2, c2 * mul2
    if a1 == a2:
        a2, b2, c2 = -a2, -b2, -c2
    B = b1 + b2
    C = -(c1 + c2)
    if C % B != 0:
        return False, -1, -1
    y = C // B
    K = -b1 * y - c1
    if K % a1 != 0:
        return False, -1, -1
    x = K // a1
    return True, x, y


def solution(line):
    crossPoint = []
    N = len(line)
    for i in range(N - 1):
        a1, b1, c1 = line[i]
        for j in range(i + 1, N):
            a2, b2, c2 = line[j]
            check, x, y = cross(a1, b1, c1, a2, b2, c2)
            if check:
                crossPoint.append([x, y])
    minX = min(crossPoint, key=lambda x: x[0])[0]
    maxX = max(crossPoint, key=lambda x: x[0])[0]
    minY = min(crossPoint, key=lambda x: x[1])[1]
    maxY = max(crossPoint, key=lambda x: x[1])[1]
    leftUp = [minX, maxY]
    N = maxY-minY+1
    M = maxX-minX+1
    # -4, 4  0, 4 -4, 1
    deltaX = -minX
    deltaY = -maxY
    result = [['.']*M for _ in range(N)]
    for x, y in crossPoint:
        if x == -4 and y == 1:
            print(y+deltaY,x+deltaX)
        result[-(y+deltaY)][x+deltaX] = '*'
    answer = [''.join(row) for row in result]

    return answer