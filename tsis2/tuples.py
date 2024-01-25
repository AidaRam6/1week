thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple) #('apple', 'banana', 'cherry', 'apple', 'cherry')

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple) #('apple', 'banana', 'cherry', 'orange')

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
"""
apple
banana
cherry
"""

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple) #('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

#Ex1
fruits = ("apple", "banana", "cherry")
print(fruits[0])

#Ex2
fruits = ("apple", "banana", "cherry")
print(len(fruits))

#Ex3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#Ex4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

