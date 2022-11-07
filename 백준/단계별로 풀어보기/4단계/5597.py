students = [True for i in range(31)]
students[0] = False

#students 길이 31 - 3 => 28
for i in range(len(students) - 3):
    n = int(input())
    students[n] = False

#0~31
for i in range(len(students)):
    if students[i] == True:
        print(i)