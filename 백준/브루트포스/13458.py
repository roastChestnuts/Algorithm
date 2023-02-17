n = int(input())
a = list(map(int,input().split()))
b, c = map(int, input().split())
answer = n

for num in a:
    if num - b > 0:
        if num - b > c:
            answer += (num-b)//c
            if (num-b)%c > 0:
                answer += 1
        else:
            answer += 1
            
print(answer)      