import sys

# BOJ 13904
# 이 문제는 현재 레벨보다 밑 레벨에 있을 때 만나서 부딪힌 적이 있던 문제다.
# 각각의 일 혹은 과제에 기간이 정해져있고 어떤 식으로 진행해야 최대 이익을 얻을 수 있는 지에 관한 문제였다.
# 이 문제도 똑같았고, 우선적으로 가장 큰 이익을 얻는 순으로 정렬한 뒤에
# 해당 일의 마감 기한 내로, 앞쪽으로 일수를 당기며 최대한 진행할 수 있도록 조정해놓으면 풀 수 있는 문제다.

N = int(sys.stdin.readline())
assign = []
for _ in range(N):
    d, w = map(int, sys.stdin.readline().split())
    assign.append((d, w))
assign.sort(key=lambda x: -x[1])
score = [0]*1001
for d, w in assign:
    start = d
    while start > 0 and score[start] != 0:
        start -= 1
    if start:
        score[start] = w
print(sum(score))

