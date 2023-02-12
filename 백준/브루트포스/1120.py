a, b = input().split()

a_len = len(a)
b_len = len(b)

diff = b_len - a_len
answer = 50

for i in range(diff + 1):
  count = 0
  for j in range(i, i + a_len):
    if b[j] != a[j - i]:
      count += 1

  answer = min(answer, count)

print(answer)