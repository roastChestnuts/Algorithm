import sys

cost = int(sys.stdin.readline())
count = int(sys.stdin.readline())

sum = 0

for i in range(count):
    product, product_cnt = map(int, sys.stdin.readline().split())
    sum += product * product_cnt
if(sum == cost):
    print('Yes')
else:
    print('No')