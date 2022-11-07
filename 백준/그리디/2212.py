n = int(input())
k = int(input())
sensor_list = list(map(int, input().split()))
sensor_list.sort()

sensor_dis = []

for i in range(n-1):
    sensor_dis.append(sensor_list[i+1] - sensor_list[i])
sensor_dis.sort()

for i in range(k-1):
  if len(sensor_dis) > 0:
    del(sensor_dis[-1])
print(sum(sensor_dis))    