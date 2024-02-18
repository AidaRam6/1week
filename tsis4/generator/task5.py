def gen(n):
    while n != -1:
        yield n
        n=n-1
n = int(input("n:"))
m = gen(n)
for i in m:
    print(i)