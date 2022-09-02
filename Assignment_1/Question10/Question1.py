import statistics
ages=[19,22,19,24,20,25,26,24,25,24]
#sorting the list and showing min and max values
sortedlist = ages.sort()
print("Sorted List: ",ages)
print("Minimum Value: ",min(ages))
print("Maximum Value: ",max(ages))
#adding min and max values to list
minvalue=min(ages)
maxvalue=max(ages)
ages.append(minvalue)
ages.append(maxvalue)
print("Modified List: ",ages)
#Finding median by importing statistics package
median=statistics.median(ages)
print("Median: ",median)
#Finding average using for loop
length=len(ages)
a=0
for i in ages:
    a+=i
print("Average: ",a/length)
#Range value
ranges=maxvalue-minvalue
print("Range: ",ranges)




