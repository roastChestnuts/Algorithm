n = int(input())

answer = []
for i in range(n//2, n+1):
    temp = [n]
    temp.append(i)
    idx = 1
    while True:
        ns = temp[idx-1] - temp[idx]
        if ns < 0:
            break
        temp.append(ns)
        idx += 1
      
    if len(answer) < len(temp):
        answer = temp
print(len(answer))      
print(*answer)        