a, b, c = map(int, input().split())

def recur(a,b):
    if b == 1:
        return a%c
    temp = recur(a,b//2)
    if b%2 == 0:
        return (temp * temp) % c
    else:
        return (temp * temp * a) % c
ans = recur(a, b)    
print(ans)