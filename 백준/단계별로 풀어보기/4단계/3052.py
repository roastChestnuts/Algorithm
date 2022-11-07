import sys
input = sys.stdin.readline

lst = []
lstlst = []

for i in range(10):
    lst.append(int(input()) % 42)

for ls in lst:
    if ls not in lstlst:
        lstlst.append(ls)

print(len(lstlst))