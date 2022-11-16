import sys
input = sys.stdin.readline

def find(start, end):
    if (start == end): return 0
    if (start+1 == end): return histogram[start]
    
    global ans
    mid = (start+end)//2
    left = mid #중앙에서 시작
    right = mid #중앙에서 시작
    width = 1 #밑변은 1부터 시작
    height = histogram[mid]
    ans = max(find(start, mid), find(mid, end)) #좌, 우측에서 존재하는 최대값 찾기
    
    while(right-left + 1 < end - start):
        left_height = min(height, histogram[left-1]) if left > start else -1
        right_height = min(height, histogram[right + 1]) if right < end-1 else -1
        
        if(left_height >= right_height):
            height = left_height
            left -= 1
        else:
            height = right_height
            right += 1
        width += 1
        ans = max(ans, width*height)
    return ans
n = int(input())
histogram = []
for i in range(n):
  histogram.append(int(input()))

print(find(0, n))