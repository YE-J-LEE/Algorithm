import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    answer = N
    test = []

    for j in range(N):
        p, i = map(int, sys.stdin.readline().split())
        test.append((p, i))
    test.sort()
    I = test[0][1]

    for i in range(1, N):
        if test[i][1] > I:
            answer -= 1
        else:
            I = test[i][1]

    # 1 4
    # 2 5 -
    # 3 6 -
    # 4 2
    # 5 7 -
    # 6 1
    # 7 3 -


    print(answer)