import sys

# BOJ 16564 히오스 프로게이머
# 이분 탐색 문제인데..
# 우선 정답을 추측해놓고 각각의 정답에 따라 답이 될 수 있는지 체크하는 문제였다.
# 이떄의 정답이 곧 정답으로 직결되는 문제라 난이도는 쉬워보일 수 있으나
# 첫 정답의 범위를 구할때 정답이 될 수 있는 최대값을 구하는 것이 까다로워서
# 이분탐색의 while문 안으로 들어갔을때 mid의 값이 유망한 값인지 체크해줘야 했다.
# 또한 일련의 숫자들에 대한 대소관계에서 모순을 찾아낼 수 있어야 해서 나도 솔직히
# 감으로 대소관계 규칙을 생각해내 귀납적으로 테스트해보고 도입해봤지 꽤 복잡한 문제였다.

N, K = map(int, sys.stdin.readline().split())
level = [int(sys.stdin.readline()) for _ in range(N)]
level.sort()
start = level[0]
end = level[N-1] + K
answer = -1
while start <= end:
    mid = (start+end)//2
    if mid > level[0] + K:
        end = mid - 1
        continue
    diff = mid - level[0]
    copyK = K
    copyK -= diff
    pre = mid
    i = 1
    stop = False
    while i < N:
        if level[i] >= pre:
            answer = mid
            start = mid + 1
            stop = True
            break
        diff = pre - level[i]
        if copyK >= diff:
            copyK -= diff
            i += 1
        else:
            end = mid - 1
            stop = True
            break
    if not stop:
        answer = mid
        start = mid + 1
print(answer)












