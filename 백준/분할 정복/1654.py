import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan_list = []
for i in range(k):
    lan_list.append(int(input()))
start = 1
end = max(lan_list)

while start <= end:
    mid = (start+end)//2
    count = 0
    for i in lan_list:
        count += i//mid
    if count < n:
        end = mid-1
    else:
        start = mid+1
print(end)        