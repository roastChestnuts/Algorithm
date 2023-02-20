n, s = map(int, input().split())
array = list(map(int, input().split()))
part_ls = [] #부분수열
rst = 0

def func(start):
  global rst
  if sum(part_ls) == s and len(part_ls) > 0:
    rst += 1
  for i in range(start, n):
    part_ls.append(array[i])
    func(i+1)
    part_ls.pop()

func(0)
print(rst)
    