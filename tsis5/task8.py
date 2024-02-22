import re
a = input()

pattern = r'[A-Z]'

result = re.split(pattern, a)
print(result)