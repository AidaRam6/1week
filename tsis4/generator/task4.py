
def squares(a,b):
    for i in range(a,b):
        yield pow(i,2)
a = int(input("a:"))
b = int(input("b:"))
m=squares(a,b)
for i in m:
    print(i)