import sys

# 시간 순서가 연관되어 2가지 변수를 고려해야 하는 그리디는 항상 어렵다.
# 여기서 주목해야할 것은 1. 시간 순서로 앞에서부터 최대한 빼곡하게 스케쥴을 짠다. 2. 페이가 쎈 강연들부터 채운다.
# 우선 페이가 쎈 친구, 해당 날짜까지 그 친구가 제일 쎄다. 이말은 그 날짜 기한까지는 그 친구와 견줄 강연이 없기에 바로 그 날로 배치를 하는 것이다.
# 왜냐하면 그 날의 이전 날들에는 각각의 날짜에 대해 페이가 날고 기는 친구들이 즐비하기에, 앞에서부터 최대한 빼곡하게 채워야 하기 때문이다.
# 따라서 날짜의 역순으로 채워나가는 방식으로 진행한다.
n = int(sys.stdin.readline())
pay = []
N = 0
for _ in range(n):
    p, d = map(int, sys.stdin.readline().split())
    pay.append((p, d))
    N = max(N, d)
pay.sort(key=lambda x: -x[0])
lecture = [0]*(N+1)
answer = 0
for p, d in pay:
    for i in range(d, 0, -1):
        if lecture[i] == 0:
            lecture[i] = p
            answer += p
            break
print(answer)