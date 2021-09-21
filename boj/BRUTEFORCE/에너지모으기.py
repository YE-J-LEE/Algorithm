import sys

# BOJ 16198
# 무심코 그리디하게 수들을 더했다가 틀렸다.
# 테스트 케이스들마저 그리디하게 골랐을 경우 맞는 답이어서 더욱 더 그럴듯해 바로 틀렸다.
# 0%에서 바로 틀리자마자 머릿속에서 순간 내가 왜 이걸 그리디하게 골랐지? 하며 바로 브루트포스로 모든 경우를 조사했다..

def bruteForce(w, result):
    global answer
    if len(w) == 2:
        answer = max(answer, result)
        return
    for i in range(1, len(w)-1):
        sw = w[:i] + w[i+1:]
        bruteForce(sw, result + w[i-1]*w[i+1])

N = int(sys.stdin.readline())
W = list(map(int, sys.stdin.readline().split()))
answer = 0
bruteForce(W, 0)
print(answer)

















