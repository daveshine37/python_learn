person = {"name": "dave", "age": 25, "city": "曲靖"}

print(person["name"])
print(person["city"])
print(person["age"])

person["age"] = 26
person["job"] = "转行学编程"

print(person)

for key,value in person.items():
    print(key,"=",value)