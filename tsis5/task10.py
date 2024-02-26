import re

a = input()

x = re.sub(r'(?<!^)(?=[A-Z])',"_",a).lower()
print(x)