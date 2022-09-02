import math
stu = int(input("Enter the count of all the students: "))
wt=[]
wt1=[]
for i in range(stu):
   wt.append(int(input()))
for m in wt:
    x=(math.floor((m/2.2046) * 100 ) )/ 100;
    wt1.append(x)
print("Weights in kg is:", wt1)
