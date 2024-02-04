value = [int(x) for x in input("input integers seperated by space: ").split()]
def histogram(value):
    for i in value:
        while(i > 0):
            print('*', end ='')
            i-=1
        print("")
histogram(value)