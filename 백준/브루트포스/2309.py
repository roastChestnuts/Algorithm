#시간 복잡도 : O(n^2)
import sys
input = sys.stdin.readline

people = [int(input()) for _ in range(9)]
rm1 = 0
rm2 = 0

for i in range(8):
    for j in range(i+1, 9):
        if sum(people) - people[i] - people[j] == 100:
            rm1 = people[i]
            rm2 = people[j]
            break
people.remove(rm1)          
people.remove(rm2)
people.sort()

for person in people:
  print(person)