import sys

# BOJ 10800
# 이 문제는 크기와 공의 색깔을 동시에 고려해줘야 해서 누적합으로 구현하되 꽤나 복잡해 애를 먹었던 문제이다.
# 처음 보았을 때 최소나 최대의 언급이 없어 일단 DP의 가능성은 배제해두고 N이 20만에 달했기에 O(N)이나 O(NlogN)정도의 시간복잡도로
# 끝내야겠다는 생각을 했다. 이분탐색을 적용하기엔 사이즈에 따라 정렬을 해도 공의 색깔이라는 또 하나의 변수가 있어 아닌 것 같았고
# 누적합을 활용해보자는 생각을 시작으로 구현하게 되었다.
# 물론 통과는 했지만 4.8초나 걸리며 꽤나 오래 걸리면서 간시히 통과했다.
# 그래서 내 코드를 분석해보니 공의 사이즈가 전부 다 다를때, 이전 정보들을 담고 있는 배열을 복사해야 하기에 시간이 오래 걸린다는 것을 알게 되었다.
# 그렇다면 나보다 짧게 걸리는 사람들은 어떻게 푼 것인가 하고 찾아봤더니 for문을 도는 메인 i 이외에 j를 따로 선언하여
# 정말 딱 필요한 때마다 j를 2차적으로 이동시켜주는, 그러니까 for문 안에 조건문을 통한 while문을 넣어 i와 j를 통해 효율적으로
# 누적합을 구해나가면서 크가가 같아 막힐때 이전 정보를 어디론가 복사하는게 아닌 그냥 이미 들고 있던 것을 활용하는 방식이었다.
# 나의 약점이 그대로 드러나버린 문제였다. 분명 맞았지만 평소 투포인터와 같은 for문 안에 while문을 넣어 효율적이게 하는 그러한 방식을 피해
# 먹고 싶은 것만 먹어 편식하던 내가 적나라하게 드러나 다시 한 번 부족함을 깨닫게 되는 문제였다. 46line은 다른 사람의 메소드이며 나중에 다시 보기 위해 남겨두었다.

N = int(sys.stdin.readline())
balls = []
for i in range(N):
    color, size = map(int, sys.stdin.readline().split())
    balls.append([size, color-1, i])
balls.sort(key=lambda x: x[0])
tilNow = [0]*N
answer = [0]*N
tilNow[balls[0][1]] = balls[0][0]
preSum = 0
preSet = [0]*N
pureSize = [balls[i][0] for i in range(N)]

for i in range(1, N):
    if (pureSize[i-1] != pureSize[i]):
        temp = balls[i][0]
        balls[i][0] += balls[i-1][0]
        answer[balls[i][2]] = balls[i-1][0] - tilNow[balls[i][1]]
        preSet = tilNow[:]
        preSum = balls[i-1][0]
        tilNow[balls[i][1]] += temp
    else:
        temp = balls[i][0]
        balls[i][0] += balls[i - 1][0]
        answer[balls[i][2]] = preSum - preSet[balls[i][1]]
        tilNow[balls[i][1]] += temp

for result in answer:
    print(result)

# 참고해야할 코드
# for i in range(n):
#     while balls[j][0] < balls[i][0]:
#         prefix += balls[j][0]
#         color[balls[j][1]] += balls[j][0]
#         j += 1
#
#     answer[balls[i][2]] = prefix - color[balls[i][1]]


