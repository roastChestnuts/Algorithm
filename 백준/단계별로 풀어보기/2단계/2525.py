h, m = map(int, input().split())
add = int(input())

plus_hour = add//60

if(add > 59):
    h += plus_hour
    m += add - (plus_hour * 60)
else:
    m += add
    
if(m > 59):
    h += m // 60
    m = m - (m//60)*60

if(h > 23):
    h = h-24
    
print(h, m)    