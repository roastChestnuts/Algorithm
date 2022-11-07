import sys
input = sys.stdin.readline

n = int(input())
sum = 0

for i in range(n):
    check = 0
    sum=0
    ox = list(input().rstrip())
    for j in range(len(ox)):
        if(ox[j] == 'O'):
            check += 1
            sum += check
        else:
            check = 0
    print(sum)
    