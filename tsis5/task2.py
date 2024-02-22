import re 

a=input()

pattern = r'ab{2,3}'

result = re.search(pattern,a)

if result:
    print("Yes")
else :
    print("No")
