import sys

# BOJ 9934
# 문제에선 중위순회 결과를 단서로 주고 완전 이진 트리인 점을 토대로 각 레벨을 반환하라고 한다.
# 이러한 순회 결과가 주어진 트리 문제의 경우 재귀를 활용한 풀이가 보편적이다.
# 하지만 완전 이진 트리인 점을 활용해 비교적 쉽게 인덱스를 활용하여 풀어보았다.

K = int(sys.stdin.readline())
N = 2**K-1
nodes = list(map(int, sys.stdin.readline().split()))
q = [(0, N-1)]
while q:
    temp = []
    level = []
    for start, end in q:
        mid = (start+end)//2
        level.append(nodes[mid])
        if start == mid:
            continue
        temp.append((start, mid-1))
        temp.append((mid+1, end))
    print(*level)
    q = temp

