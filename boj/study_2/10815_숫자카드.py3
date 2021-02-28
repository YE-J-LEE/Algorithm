import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
M = int(sys.stdin.readline())

def BS(target):
    start = 0
    last = N-1
    while start<=last:
        mid = (start+last)//2
        if numbers[mid] < target:
            start = mid+1
        elif numbers[mid] > target:
            last = mid-1
        else:
            return 1
    return 0
targets = list(map(int, sys.stdin.readline().split()))
for num in targets[:-1]:
    print(BS(num), '', end='')
print(BS(targets[-1]))