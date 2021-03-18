import sys
from re import compile

T = int(sys.stdin.readline())
for _ in range(T):
    pattern = compile("(100+1+|01)+")
    if pattern.fullmatch(sys.stdin.readline().rstrip()):
        print("YES")
    else:
        print("NO")