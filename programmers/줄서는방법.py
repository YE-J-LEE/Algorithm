# 프로그래머스
# 이 문제는 내가 싫어하던 등수 매기기 문제였다..
# 하지만 등수를 매기기 위한 중간 경우 갯수들을 팩토리얼로 계산해낼 생각을 하지는 못했던 문제이다.
# 사전순으로 정렬된다고 할 때 팩토리얼을 활용하는 방법은 신선했다.

def solution(n, k):
    answer = []
    factorial = [1]*21
    for i in range(2, 21):
        factorial[i] = factorial[i-1] * i
    number = [x for x in range(1, n+1)]
    while n:
        idx = (k-1)//factorial[n-1]
        answer.append(number.pop(idx))
        k = k%factorial[n-1]
        n -= 1
    return answer