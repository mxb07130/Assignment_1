it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#Find the length of the set it_companies
print("The length of set is:", len(it_companies))
#Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)
#Insert multiple IT companies at once to the set it_companies
multiple_ITcompanies= ["Tesla","Samsung", "Deloitte", "Meta"]
it_companies.update(multiple_ITcompanies)
print(it_companies)
#Remove one of the companies from the set it_companies
it_companies.remove("Samsung")
print(it_companies)
#Join A and B
C = A.union(B)
print(C)
#Find A intersection B
D = A.intersection(B)
print(D)
#Is A subset of B
E = A.issubset(B)
print(E)
#Are A and B disjoint sets
F = A.isdisjoint(B)
print(F)
#Join A with B and B with A
G = B.union(A)
print(C,G)
#What is the symmetric difference between A and B
H = A.symmetric_difference(B)
print(H)
#Delete the sets completely
del A,B
#Convert the ages to a set and compare the length of the list and the set
I= set(age)
print(len(I))