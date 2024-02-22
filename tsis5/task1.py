import re 

a=input()

pattern = r'ab*'

result = re.search(pattern,a)

if result:
    print("Yes")
else :
    print("No")
