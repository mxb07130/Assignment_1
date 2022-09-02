import math
# Taking the integer value as input
students = int(input("Enter the count of all the students: "))
list=[]
list1=[]
# Taking all inputs into list

for i in range(students):
   list.append(int(input()))

# coverting lbs into kgs by using math.floor 
for m in list:
    x=(math.floor((m/2.2046) * 100 ))/ 100;
    list1.append(x)
    
print("Weights in kg is:", list1)
