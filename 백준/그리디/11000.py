import heapq
import sys
input = sys.stdin.readline

n = int(input())
lec_list = []
for i in range(n):
    lec_list.append(list(map(int, input().split())))

lec_list.sort()
end_time = []
heapq.heappush(end_time, lec_list[0][1])

count = 1

for i in range(1, n):
    if lec_list[i][0] < end_time[0]:
        count+=1
    else:
        heapq.heappop(end_time)
    heapq.heappush(end_time, lec_list[i][1])
    
print(count)    