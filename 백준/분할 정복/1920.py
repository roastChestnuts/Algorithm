############################################(집합 자료형으로 중복제거 후 탐색)
import sys
input = sys.stdin.readline

n = int(input())
n_list = set(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

for num in m_list:
    if num in n_list:
        print(1)
    else:
        print(0)

################################################(이분탐색)        

n = int(input())
n_list = sorted(list(map(int, input().split())))
m = int(input())
m_list = list(map(int, input().split()))

def div_search(st, ed, num):
    if st>ed:
        print(0)
        return
    mid = (st+ed)//2
    
    if num == n_list[mid]:
        print(1)
        return
    elif num > n_list[mid]:
        div_search(mid+1, ed, num)
    elif num < n_list[mid]:
        div_search(st, mid-1, num)

for num in m_list:
    div_search(0, n-1, num)
    
#둘의 시간차가 나는 이유는 탐색시간이 아닌 정렬여부에 따른 시간차이가 아닐까 생각
#탐색시간의 경우 이분탐색은 logn으로 압도적으로 빠르지만
#sorted의 경우 nlogn이니까 단순히 set으로 변경하여 탐색하는 경우 n의 시간복잡도에 탐색이 가능    
