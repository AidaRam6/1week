import re 

a=input()

pattern = r'[a-z]_[a-z]'

result = re.search(pattern,a)

if result:
    print("Yes")
else :
    print("No")
