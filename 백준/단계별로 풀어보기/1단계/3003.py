import sys

count = [1, 1, 2, 2, 2, 8]
in_count = list(map(int, sys.stdin.readline().split()))
get = []

for i in range(len(count)):
    print(count[i] - in_count[i], end=' ')
