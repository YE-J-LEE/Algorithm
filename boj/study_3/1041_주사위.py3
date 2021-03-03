import sys

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
three = min(a[3]+a[4]+a[5], a[1]+a[3]+a[5], a[1]+a[2]+a[5], a[2]+a[4]+a[5],
            a[0]+a[3]+a[4], a[0]+a[1]+a[3], a[0]+a[1]+a[2], a[0]+a[2]+a[4])
two = min(a[0]+a[2], a[2]+a[5], a[3]+a[5], a[0]+a[3], a[1]+a[2], a[2]+a[4], a[3]+a[4], a[1]+a[3]
          ,a[0]+a[1], a[1]+a[5], a[4]+a[5], a[0]+a[4])
one = min(a)

if N==1:
    print(sum(a)-max(a))
elif N==2:
    print(three*4 + two*4)
else:
    print((8*N-12)*two + three*4 + (5*N**2 -16*N+12)*one)