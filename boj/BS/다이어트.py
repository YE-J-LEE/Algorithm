import sys

# 아래는 내 사고 과정이다. 우선 보고나서 쌍곡선이 떠올라서 머릿속으로 그려보았는데, x(가능한 현재 몸무게 값)에 제한이 없어보였다.
# 자연수라해도 무한하게 뻗어나가며 존재할 것 같았지만.
# 좀 지나서 x에 max값이 존재할 수 있다는 것을 알게 되어, 바로 가능한 x의 max값이 50000이라는 것을 확인하고
# 인풋값이 G가 되기 위해 명확한 값이 하나라도 존재하기만 하면 되며, x보다 작은 정렬된 상태의 값들을 가지고 답을 확인하기 때문에
# 이분탐색을 통해 구현했다. 풀고나서 투포인터를 활용하는 방법이 있다는데 잘 떠오르지 않아서 이건 다른 사람의 풀이를 참고해보려고 한다.

# x^2 - px^2 = 100000
# x^2 = 100000 + px^2

# i = 2
# while True:
#     if i**2 - (i-1)**2 >= 100000:
#         print(i**2 - (i-1)**2)
#         print(i)
#         break
#     i += 1
G = int(sys.stdin.readline())
answer = []
x = 50000
while x > 1:
    start = 1
    end = x-1
    found = False
    while start <= end:
        mid = (start+end)//2
        result = x**2-mid**2
        if result > G:
            start = mid+1
        elif result == G:
            found = True
            break
        else:
            end = mid-1
    if found:
        answer.append(x)
    x -= 1
if answer:
    while answer:
        print(answer.pop())
else:
    print(-1)