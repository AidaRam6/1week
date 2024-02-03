lis=list(int,input().split())
count =0
for i in range (len(lis)):    
    if lis[i]%2==0:
        count+=1
for i in range (len(lis)):
    if count<3:
        print(lis[i])    