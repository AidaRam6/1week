thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"]) #Ford
print(type(thisdict)) #<class 'dict'>

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)  #{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
print(len(thisdict)) #3

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict) #{'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}


thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)  #{'name': 'John', 'age': 36, 'country': 'Norway'}

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x) #Mustang

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
#dict_keys(['brand', 'model', 'year'])
#dict_keys(['brand', 'model', 'year', 'color'])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.values()
print(x) #dict_values(['Ford', 'Mustang', 1964])
x = thisdict.items()
print(x) #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

#add
thisdict.update({"year": 2020})
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

#remove
thisdict.pop("model") 
del thisdict["model"]
print(thisdict) #{'brand': 'Ford', 'year': 1964}
thisdict.popitem()
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang'}

thisdict.clear()
print(thisdict) #{}

#loop
for x in thisdict:
  print(x)
  
for x in thisdict.keys():
  print(x)

"""
brand
model
year
"""

for x in thisdict:
  print(thisdict[x])
  
"""
Ford
Mustang
1964
"""
for x, y in thisdict.items():
  print(x, y)
"""
brand Ford
model Mustang
year 1964
"""
#copy
mydict = thisdict.copy()
print(mydict)

mydict = dict(thisdict)
print(mydict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#nested
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
print(myfamily) #{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

#Ex1
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#Ex2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

#Ex3
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"]="red"

