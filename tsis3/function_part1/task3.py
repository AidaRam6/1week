heads,legs=map(int,input().split())
def solve(x,y):
    chikens,rabits=0
    for i in range(x):
        if (i*2)+((x-i)*4)==y:
            chikens=i
            rabits=x-i
    return chikens,rabits
nc,nr=solve(heads,legs)
print("chikens:",nc)
print("rabits",nr)
            