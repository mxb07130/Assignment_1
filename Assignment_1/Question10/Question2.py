dog={}
#updated dog dictionary
dog={"name":"cherry","color":"red","breed":"pug","legs":"short","age":5}
#creating student dictionary
student={"first_name":"manoj","last_name":"kumar","gender":"male","age":23,"martial status":"single","skills":["java","c","python"],"country":"usa","city":"kansas","address":"1004"}
#length
print("Length:",len(student))
#values of skills
print("Skills:",student["skills"])
#modify
student["skills"].append("c sharp")
print("Modified Skills:",student["skills"])
#printing keys
print("Keys:",student.keys())
#printing values
print("Values:",student.values())


