# 프로그래머스
# 이 문제는 처음엔 어떻게 풀어야할지 막막했다.
# DP로 담자니 숫자들의 합이 max가 1억이다.
# 그래서 다시 생각해보니 중간값을 활용한 문제였다.

def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    if s%n == 0:
        answer = [s//n]*n
    else:
        answer = [s//n]*n
        r = s%n
        i = 0
        while r:
            answer[i] += 1
            i = (i+1)%n
            r -= 1
    return sorted(answer)