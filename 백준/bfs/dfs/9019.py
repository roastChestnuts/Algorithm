from collections import deque 

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    q = deque()
    q.append([a, ''])
    visited = [True for _ in range(10000)]
    
    while q:
        tmp, reg = q.popleft()
        
        if tmp == b:
            print(reg)
            break
        #d
        d = tmp*2 % 10000
        #s
        if tmp==0:
            s = 9999
        else:
            s = tmp-1
        #l
        l = ((tmp%1000)*10) + (tmp//1000)
        #r
        r = (tmp//10) + ((tmp%10)*1000)
        
        if visited[d]:
            q.append([d, reg+'D'])
            visited[d] = False
            
        if visited[s]:
            q.append([s, reg+'S'])
            visited[s] = False    
            
        if visited[l]:
            q.append([l, reg+'L'])
            visited[l] = False    
            
        if visited[r]:
            q.append([r, reg+'R'])
            visited[r] = False    