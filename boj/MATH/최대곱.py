import sys

# BOJ 1500
# 프로그래머스에서 비슷한 문제를 보았다. 그때는 각 수들의 제곱의 합이 최대가 되도록 설계하는 것이었는데
# 이 문제에선 그냥 곱의 합이 최대가 되도록 하면 됐었다. 그렇다 해도 각 수들이 전부 커야 최대가 되기 때문에
# 골고루 분배해준 뒤 부족한 만큼 +1씩 해주면 된다.

S, K = map(int, sys.stdin.readline().split())
nums = [S//K]*K
R = S%K
for i in range(R):
    nums[i] += 1
answer = 1
for num in nums:
    answer *= num
print(answer)



