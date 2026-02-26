person = {"name" : "Lara", "age": 15, "height" : 5.4, "gender" : "girl" }

print(person["name"])
person["country"] = "England"
print(person)
person["age"] = "14"
print(person)
del person["age"]
print(person)

for key in person:
    print(key + "-" + str(person[key]))

for key,value in person.items():
    print(key,value)

print(person.keys())
print(person.values())