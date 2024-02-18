def generator(n):
    for i in range(1,n+1):
        yield i**2
n = int(input("n:"))
m=generator(n)
for i in m:
    print(i)