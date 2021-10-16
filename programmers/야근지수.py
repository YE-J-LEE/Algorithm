import heapq

# 프로그래머스
# 이 문제는 제곱수의 합이라 제곱수에 힌트를 좀 얻었다.
# 제곱수는 수가 기하급수적으로 증가하기 때문에 매번 가장 큰 값을 작게 낮춰줘야 한다.
# 그래서 최대힙을 활용해 풀어냈다.

def solution(n, works):
    answer = 0
    maxH = []
    for work in works:
        heapq.heappush(maxH, -work)
    for _ in range(n):
        if not maxH:
            break
        x = heapq.heappop(maxH)
        if x+1 == 0:
            continue
        heapq.heappush(maxH, x+1)
    for time in maxH:
        answer += time**2
    return answer