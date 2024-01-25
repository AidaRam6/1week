a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b") #a is greater than b
  
a = 2
b = 330

print("A") if a > b else print("B") #B

a = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B") #=

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True") #Both conditions are True

if a > b or a > c:
  print("At least one of the conditions is True") #At least one of the conditions is True

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b") #a is NOT greater than b 
  
#Ex1
a = 50
b = 10
if a > b:
    print("Hello World")
#Ex2
a = 50
b = 10
if a != b:
    print("Hello World")
#Ex3
a = 50
b = 10
if a == b:
    print("Yes")
else:
    print("No")
#Ex4
a = 50
b = 10
if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")
d=3
#Ex5
if a == b and c == d:
  print("Hello")
  
#Ex6
if a == b or c == d:
  print("Hello")
#ex7
if 5 > 2:
    print("YES")

#Ex8
a = 2
b = 5
print("YES") if a == b else print("NO")

#Ex9
a = 2
b = 50
c = 2
if a == c or b == c:
    print("YES")