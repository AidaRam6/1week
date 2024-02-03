from movies import movies 

def f():
    sum=0
    for i in movies:
        sum+=i["imdb"]
    average=sum/len(movies)
    print(average)
f()