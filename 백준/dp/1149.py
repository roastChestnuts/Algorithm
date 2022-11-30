n = int(input())
red, blue, green = [], [], []

for i in range(n):
  r, g, b = map(int, input().split())
  red.append(r)
  green.append(g)
  blue.append(b)

for i in range(1, n):
  red[i] = min(green[i-1], blue[i-1]) + red[i]
  green[i] = min(red[i-1], blue[i-1]) + green[i]
  blue[i] = min(green[i-1], red[i-1]) + blue[i]

print(min(red[n-1], green[n-1], blue[n-1]))