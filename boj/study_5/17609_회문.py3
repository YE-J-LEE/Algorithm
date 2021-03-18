import sys

def palindrome(s, l):
    mid = l // 2 - 1
    i = 0
    j = l - 1
    while i <= mid:
        if s[i]!=s[j]:
            return False, i, j
        i += 1
        j -= 1
    return True, 1, 1

T = int(sys.stdin.readline())
for _ in range(T):
    s = sys.stdin.readline().rstrip()
    l = len(s)
    pal, i, j = palindrome(s, l)
    if pal:
        print(0)
    else:
        check1, i1, j1 = palindrome(s[:i]+s[i+1:], l-1)
        check2, i2, j2 = palindrome(s[:j]+s[j+1:], l-1)
        if not check2 and not check1:
            print(2)
        else:
            print(1)