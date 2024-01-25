thislist = ["apple", "banana", "cherry"]
print(thislist) #['apple', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) #['apple', 'banana', 'cherry', 'orange']
print(thislist[2:]) #['cherry', 'orange', 'kiwi', 'melon', 'mango']

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) #['apple', 'blackcurrant', 'watermelon', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) #['apple', 'banana', 'watermelon', 'cherry']

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) #['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist) #['apple', 'cherry', 'banana', 'kiwi']

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) #['apple', 'banana']

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) #['apple', 'banana', 'mango']

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort(reverse = True)

print(thislist) #['pineapple', 'orange', 'mango', 'kiwi', 'banana']

thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.reverse()

print(thislist) #['cherry', 'Kiwi', 'Orange', 'banana']

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist) #['apple', 'banana', 'cherry']

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
list1.extend(list2)
print(list1) #['a', 'b', 'c', 1, 2, 3]

#Ex1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#EX2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#Ex3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#Ex4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

#Ex5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#Ex6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#Ex7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#Ex8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))


