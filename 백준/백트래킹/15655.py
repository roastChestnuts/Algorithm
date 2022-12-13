n, m = map(int, input().split())
ans = []
array = list(map(int, input().split()))
array.sort()

def func(start):
  if len(ans) == m:
    print(*ans)
    return
  for i in range(start, n):
    ans.append(array[i])
    func(i+1)
    ans.pop()

func(0)    
  