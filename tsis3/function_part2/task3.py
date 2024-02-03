from movies import movies
def category(category):
    for i in movies:
        if i["category"]==category:
            print(i["name"])
n=input()
category(n)