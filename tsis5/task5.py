import re 

a=input()

pattern = r'a.*b'

result = re.search(pattern,a)

if result:
    print("Yes")
else :
    print("No")
