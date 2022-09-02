
# tuple with names of sisters and brothers
sisters = ("Kavya", "Ramya", "lavanya", "Sirisha", "Sravanthi")
brothers = ("Manoj", "Narendra", "Sravan")
print(sisters)
print(brothers)

# joining brothers and sisters

siblings= sisters + brothers
print(siblings)

#count of siblings

count_siblings= len(siblings)
print(count_siblings)

#appending father and mother

mother = "Latha"
father= "Krishna_Mohan"

family_members = list(siblings)

family_members.append(father)
family_members.append(mother)
print(family_members)
