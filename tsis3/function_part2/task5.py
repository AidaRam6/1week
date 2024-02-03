from movies import movies
def f(category):
    sum=0
    count=0
    for i in movies:
        if i["category"]==category:
            sum+=i["imdb"]
            count+=1
    average=sum/count
    print(average)
n=input("category:")
f(n)