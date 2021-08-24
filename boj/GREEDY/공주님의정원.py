import sys

# 문제에서부터 그리디한 냄새가 난다.
# 보통 순수 그리디인 경우 정렬을 이상적으로 했을 때 쉽게 풀리는 경향이 있어서 이번에도 최적의 정렬을 찾기 위해 시간을 허비했다.
# 하지만 그림을 그려 따라가보니 꽃이 피는 시간외에 추가적인 정렬이 필요없이 꽃을 갱신만 해주면 되었다.
# 추가적으로 이와같은 월 + 일 또는 시간 + 분 인 경우 zfill등을 활용해 string으로 바꾸면 부등호식이 한결 편해진다.
N = int(sys.stdin.readline())
flowers = []
for _ in range(N):
    m1, d1, m2, d2 = sys.stdin.readline().split()
    flowers.append((m1.zfill(2) + d1.zfill(2), m2.zfill(2) + d2.zfill(2)))
flowers.sort(key=lambda x: x[0])
cut = '0301'
postCut = '0000'
answer = 0
for s, e in flowers:
    if s <= cut and cut >= e:
        continue
    if s <= cut and cut <= e:
        if postCut == '0000':
            answer += 1
        postCut = max(e, postCut)
    else:
        cut, postCut = postCut, '0000'
        if s <= cut and cut <= e:
            answer += 1
            postCut = max(e, postCut)
    if postCut >= '1201':
        print(answer)
        break
else:
    print(0)




