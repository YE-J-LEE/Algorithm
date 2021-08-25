import sys
sys.setrecursionlimit(10**5)

# 선택하지 않거나, 선탣하거나 0-1의 문제가 아닌 여러 가지 선택지 중에 무얼 택하느냐의 문제다.
# 그리고 각각의 선택지에 따라 다른 영향을 미친다.
# 이 경우 리조트 문제와 상당히 비슷한 양상을 보이는데, 한 가지 다른 점은 이 문제의 경우 총 가짓수를 구하는 문제이다.
# 따라서 리조트의 경우엔 solve함수의 reuturn값으로 가격을 반환하게끔 짰지만, 여기선 return 값에 0과 1이 존재한다.
# 이 문제에서 눈 여겨 볼 테크닉은 바로 결석 변수에 대한 0처리이다.
# 연속 결석의 연속 여부를 0처리를 통해 시원하게 해결하는 모습을 볼 수 있다.
# 리조트같은 문제를 안 푼지 오래 되었고 요 근래 0-1 knapsack류의 문제만 풀어와서인지 풀이 방법이 잘 생각나지 않았다.

def solve(day, late, absent):
    global N

    if late >= 2:
        return 0
    if absent >= 3:
        return 0
    if day == N:
        return 1
    if DP[day][late][absent] != -1:
        return DP[day][late][absent]

    DP[day][late][absent] = solve(day+1, late, 0) + solve(day+1, late+1, 0) + solve(day+1, late, absent+1)
    return DP[day][late][absent]

N = int(sys.stdin.readline())
DP = [[[-1]*4 for _ in range(3)] for _ in range(N+1)]
print(solve(0, 0, 0)%1000000)