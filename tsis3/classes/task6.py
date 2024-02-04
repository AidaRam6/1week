def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True
def filter_list(list):
    return list(filter(lambda x: isPrime(x), list))