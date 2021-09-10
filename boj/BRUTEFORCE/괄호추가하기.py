import sys

# DP로 풀어내고 싶었지만 풀지 못한 문제다..
# 앞에서부터 계산되고 숫자들은 0부터 9까지이기에 앞에서의 최댓값에서 계속해서 최댓값을 만들어나가면
# 최종적으로 최댓값을 반환할 것만 같았다.
# 하지만 중간에 음수 * 음수인 경우가 최적의 해인 반례가 존재했다.
# 그래서 최소를 만들어내는 DP도 따로 만들어서 최소와 최대의 DP를 병행해 구하고자 했지만 실패하고..
# 결국 N의 최대가 19까지라 완전탐색을 통해 풀어냈다,
# 그렇다고 해서 순탄하게 풀어낼 순 없었고 괄호가 중첩되지 않는다는 조건하에 겨우 풀어낼 수 있었다.
# 재귀를 통한 완전탐색이라고 해서 그렇게 쉽진 않다는 것을 다시 한 번 깨달았다.

def bruteforce(i, result):
    global answer, M
    if i == M-1:
        answer = max(answer, result)
        return
    normal = eval(str(result) + op[i] + num[i+1])
    bruteforce(i+1, normal)
    if i+2 < M:
        pre = str(eval(num[i+1] + op[i+1] + num[i+2]))
        special = eval(str(result) + op[i] + pre)
        bruteforce(i+2, special)

N = int(sys.stdin.readline())
M = (N+1)//2
num, op = [], []
for c in sys.stdin.readline().rstrip():
    if c in '+-*':
        op.append(c)
    else:
        num.append(c)
answer = -float('inf')
bruteforce(0, int(num[0]))
print(answer)