import re

a = input()

pattern = r'[A-Z]'

result = re.sub(pattern," ",a)
print(result)