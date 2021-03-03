import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    stock = list(map(int, sys.stdin.readline().split()))

    price = 0
    maxNum = stock[-1]

    for i in range(N-1, -1, -1):
        if stock[i] <= maxNum:
            price += maxNum-stock[i]
        else:
            maxNum = stock[i]


    print(price)