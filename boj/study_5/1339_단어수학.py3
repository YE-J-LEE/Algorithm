import sys

N = int(sys.stdin.readline())
dic = {}
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    mul = 0
    for i in range(len(word)-1, -1, -1):
        if word[i] in dic:
            dic[word[i]] += 10**mul
        else:
            dic[word[i]] = 10 ** mul
        mul += 1
num = 9
answer = 0

for key in sorted(dic.keys(), key=lambda x: dic[x], reverse=True):
    answer += dic[key]*num
    num -= 1
print(answer)