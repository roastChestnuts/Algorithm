import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())
ans=0

while n!= 0:
    n -= 1
    line = 2**n
    line_sq = line**2 #한변의 제곱 = 나뉘어진 공간의 크기
    if r <  line and c < line: #1사분면
        ans += line_sq * 0 #한 변의 길이니까 제곱
    if r <  line and c >= line: #2사분면
        ans += line_sq * 1
        c -= line
    if r >=  line and c < line: #3사분면
        ans += line_sq * 2
        r -= line
    if r >=  line and c >= line: #4사분면
        ans += line_sq * 3
        r -= line
        c -= line
print(ans)        

