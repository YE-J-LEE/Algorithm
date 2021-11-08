import sys
from collections import deque

# BOJ 12886
# 뭔가 찝찝하게 풀었다. 방문 체크용 배열을 만들기엔 크기가 너무 컸다. 그래서 set을 활용해 만들어 시간이 걸리긴 해도 통과는 했다.
# 그래도 조금 걸려 다른이들의 풀이를 참고하니 세 그룹의 총합은 항상 같다는 논리를 활용해 2차원 방문배열만 만든 것을 확인할 수 있었다.
# 이를 통해 문제의 조건을 꼼꼼하게 파악하여 활용할 수 있어야 겠다는 생각을 하게 되었다.

visited = set()
A, B, C = map(int, sys.stdin.readline().split())
queue = deque([(A, B, C)])
visited.add((A, B, C))
answer = 0
while queue:
    x, y, z = queue.popleft()
    if x == y and y == z:
        answer = 1
        break
    if x != y:
        if x > y:
            nx = x - y
            ny = 2*y
        else:
            ny = y - x
            nx = 2*x
        if (nx, ny, z) not in visited:
            visited.add((nx, ny, z))
            queue.append((nx, ny, z))
    if y != z:
        if z > y:
            nz = z - y
            ny = 2*y
        else:
            ny = y - z
            nz = 2*z
        if (x, ny, nz) not in visited:
            visited.add((x, ny, nz))
            queue.append((x, ny, nz))
    if x != z:
        if x > z:
            nx = x - z
            nz = 2*z
        else:
            nz = z - x
            nx = 2*x
        if (nx, y, nz) not in visited:
            visited.add((nx, y, nz))
            queue.append((nx, y, nz))
print(answer)
