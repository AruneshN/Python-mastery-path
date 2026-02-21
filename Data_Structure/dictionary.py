"""
Topic : Dictionary

desc:
1) values are duplicate , key is not allowed duplicate
2) values accesed by keys
3) ordered
"""
#dictionary

employess={
    "name":"arunesh",
    "age":22,
    "role":"Devops"
}
#Access items
print(employess["age"])
print(employess.get("name"))

#get keys
key=employess.keys()
print(key)

#get vales
print(employess.values())


#get items
''' items return the dictionary as tuple as list'''

print(employess.items())


#change values

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"]=2000

print(thisdict["year"])

#add items
thisdict["price"]=125000

print(thisdict)
thisdict.update({"colour":"red"})

#remove 
thisdict.pop("model")

print(thisdict)


#copy
mydict=thisdict.copy()

print(mydict)


#nested dictionary

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}


print(myfamily["child2"]["name"])