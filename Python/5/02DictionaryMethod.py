myDict={
    "name":"Santosh Bhandari",
    "age": 21,
    "address": "Jhapa",
    "marks":[20,25,16,25]
}


emptDict={}
print(type(myDict))
print(type(emptDict))

# print(myDict.items())
# print(myDict.keys())
# print(myDict.values())
updateDict={
    'College':"Mechi Multiple Campus",
    "Level":"Bachelor",
    "Semester":"Fourth"
}
myDict.update(updateDict)
# print(myDict)
print(myDict.get("name"))
print(myDict.get("work"))