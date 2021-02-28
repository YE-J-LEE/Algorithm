import sys

N, M = map(int, sys.stdin.readline().split())
friends = {x:{x} for x in range(1, N+1)}
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    friends[x].add(y)
    friends[y].add(x)
days = 0
result = []
while True:
    if all(map(lambda x: len(list(friends[x]))==N, friends.keys())):
        print(days)
        for r in result:
            print(r)
        break
    days += 1
    apply = set()
    for key in friends.keys():
        queue = friends[key]
        for person in queue:
            if person == key:
                continue
            for newFriend in friends[person]-queue:
                apply.add((key, newFriend))
    result.append(len(list(apply))//2)

    for a in apply:
        friends[a[0]].add(a[1])