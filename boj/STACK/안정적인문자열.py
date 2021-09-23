import sys

# BOJ 4889
# 안정적으로 괄호가 닫히는 문자열 문제이다. 이는 스택 자료구조를 활용한 문제 중 가장 대표적인 문제이다.
# 여기선 안정적으로 괄호를 닫기 위해 괄호 모양을 반전시키는 최소 횟수를 구하라고 한다.
# 문자열의 길이는 최대 2000으로, 모든 가짓수는 2^2000번이라 너무 많다.
# 여태껏 괄호 닫기 문제에서 스택을 써왔으므로 스택을 통해 안정적으로 닫히는 애들은 미리 닫아주고 짝이 없어 길을 헤매는 친구들에
# 대해서만 따로 처리를 해주었다. 그런데 나의 이 접근법이 항상 최소의 결과값을 반환하는지 자신이 없었다.
# 하지만 운 좋게도 내 방식이 그대로 들어맞았다. 그렇지만 수식으로 증명할 수 없어서 맞고도 찝찝한 문제였다.

i = 1
while True:
    S = sys.stdin.readline().rstrip()
    if S[0] == '-':
        break
    stack = []
    answer = 0
    for c in S:
        if c == '{':
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                stack.append('{')
                answer += 1
    if stack:
        answer += len(stack)//2
    print("{}. {}".format(i, answer))
    i += 1





















