import re 

a=input()

pattern = r'[,\s.]'

result = re.sub(pattern,":",a)

print(result)