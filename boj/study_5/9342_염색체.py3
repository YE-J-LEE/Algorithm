import sys

T = int(sys.stdin.readline())
rule = ['A', 'B', 'C', 'D', 'E', 'F', '']
for _ in range(T):
    s = sys.stdin.readline().rstrip()
    i = 0
    stack = []
    for c in s:
        if stack:
            if stack[-1] == c:
                continue
        stack.append(c)
    short = ''.join(stack)
    if 'A' not in short:
        print('Good')
    else:
        start = short.index('A')
        if short[start:start+3] != 'AFC':
            print('Good')
        else:
            left = short[:start]
            right = short[start+3:]
            if left in rule and right in rule:
                print("Infected!")
            else:
                print('Good')