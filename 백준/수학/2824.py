n = int(input())
a = list(input().split())
m = int(input())
b = list(input().split())

A = eval('*'.join([str(num) for num in a]))
B = eval('*'.join([str(num) for num in b]))

def gcd(i, j):
    while j>0:
        i, j = j, i%j
    return i

answer = gcd(A, B)
print(str(answer)[-9:])