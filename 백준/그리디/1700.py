import sys
input = sys.stdin.readline

n, k = map(int, input().split())
use_list = list(map(int, input().split())) #플러그 사용순서
pluged = []
count=0

for i in range(k):
    if use_list[i] in pluged:
        continue
    elif len(pluged) != n:        #조건문의 순서가 바꼈다고 왜 틀리다는 건지를 잘 모르겠다..
        pluged.append(use_list[i])
        continue

    else:
        farthest = 0
        temp = 0
        for plug in pluged:
          if plug not in use_list[i:]:
            temp = plug
            break
          elif use_list[i:].index(plug) > farthest:
            farthest = use_list[i:].index(plug)
            temp = plug
        pluged[pluged.index(temp)] = use_list[i]
        count+=1
print(count)        