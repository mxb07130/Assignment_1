import math
it = int(input("no of:"))
lst=[]
lst1=[]
for i in range(it):
    lst.append(int(input()))
for b in lst:
    a=(math.floor((b/2.2046) * 100 ) )/ 100;
    lst1.append(a)
print(lst1)
