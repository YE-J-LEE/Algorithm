import sys

T = int(sys.stdin.readline())

def check(x, mid):
    i = 1
    while True:
        z = i*(i+1)//2 + x
        if z > mid:
            return False, i
        elif z == mid:
            return True, i
        else:
            i += 1

for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    mid = (x+y)//2
    z = 0
    cc, i = check(x, mid)
    if cc:
        z = i*(i+1) + x
        if z < y:
            print(2*i+1)
        else:
            print(2*i)
    else:
        z = i*(i-1)+i+x
        if z < y:
            print(2*i)
        else:
            print(2*i-1)