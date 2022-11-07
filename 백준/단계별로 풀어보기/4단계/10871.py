import sys
input = sys.stdin.readline

N, X = map(int,input().split())

num_list = map(int, input().split())

for num in num_list:
    if(num < X):
        print(num, end=' ') 