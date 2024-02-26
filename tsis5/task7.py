import re

a = input()

x = re.sub(r"(?:^|_)([a-z])",lambda match: match.group(1).upper(),a)

print(x)