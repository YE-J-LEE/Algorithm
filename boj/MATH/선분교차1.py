import sys

# BOJ 17386
# 오랜만에 만나는 직선 교차점 관련 문제다.
# 그런데 직선이라면 쉽게 풀리겠지만 '선분'이라는 제약때문에 두 점을 잇는 직선끼리 교차를 해도
# 허용되는 x, y 범위에 해당하는 교점인지 체크해줘야 한다.
# 이에 대한 방법으로 처음엔 정렬 후에 인덱스 기준 1, 2의 원소들로 비교를 했지만 해당 방식엔 오류가 있음을 알게 되었고
# 예외처리를 추가해주어 해결하였다.

x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
A, B = y2-y1, x1-x2
E = A*x1 + B*y1
C, D = y4-y3, x3-x4
F = C*x3 + D*y3
determinant = A*D - B*C
if determinant == 0:
    print(0)
else:
    if (max(x1, x2) < min(x3, x4)) or (max(x3, x4) < min(x1, x2)) or (max(y1, y2) < min(y3, y4)) or (max(y3, y4) < min(y1, y2)):
        print(0)
    else:
        x = (D*E - B*F)/determinant
        y = (A*F - E*C)/determinant
        xRange = [x1, x2, x3, x4]
        yRange = [y1, y2, y3, y4]
        xRange.sort()
        yRange.sort()
        if xRange[1] <= x <= xRange[2] and yRange[1] <= y <= yRange[2]:
            print(1)
        else:
            print(0)





