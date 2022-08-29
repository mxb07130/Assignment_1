import statistics;

ages=[19,22,19,24,20,25,26,24,25,24];

#sorting the list and showing min and max values
sortedlist = ages.sort();
print(ages);
print(min(ages));
print(max(ages));

#adding min and max values to list

minvalue=min(ages);
maxvalue=max(ages);
ages.append(minvalue);
ages.append(maxvalue);
print(ages);

#mediana

median=statistics.median(ages);
print(median);

#average

length=len(ages);
a=0;
for i in ages:
    a+=i;
print(a/length)

#range

ranges=maxvalue-minvalue
print(ranges)




