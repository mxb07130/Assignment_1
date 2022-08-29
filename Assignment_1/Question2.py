dog={"name","color","breed","legs","age"}
student={"first_name":"manoj","last_name":"kumar","gender":"female","age":"30","martial status":"thrice","skills":["java","c","python"],"country":"usa","city":"kansas","address":"1004"}
#length
print(len(student))
#values of skills
print(student["skills"])
#modify
student["skills"].append("c sharp")
print(student["skills"])
#keys
print(student.keys())
#values
print(student.values())


