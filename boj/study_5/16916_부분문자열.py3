import sys

S = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()
l1 = len(S)
l2 = len(P)

def pattern(p, table):
    j = 0
    for i in range(1, len(P)):
        while j>0 and p[i] != p[j]:
            j = table[j-1]
        if p[i] == p[j]:
            j += 1
            table[i] = j

table = [0]*l2
pattern(P, table)
j = 0
for i in range(l1):
    while j > 0 and S[i] != P[j]:
        j = table[j-1]
    if S[i]==P[j]:
        if j == l2-1:
            print(1)
            break
        j += 1
else:
    print(0)