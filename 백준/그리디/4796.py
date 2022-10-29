import sys
input = sys.stdin.readline

count = 1
while True:
    l, p, v = map(int, input().split())
    if l+p+v == 0:
        break
    
    day = l*(v//p)
    if (v%p) > l:
      day += l
    else:
      day += (v%p)
    print(f'Case {count}: {day}')
    count +=1