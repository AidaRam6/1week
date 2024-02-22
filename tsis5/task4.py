import re 

a=input()

pattern = r'[A-Z][a-z]+'

result = re.search(pattern,a)

if result:
    print("Yes")
else :
    print("No")
